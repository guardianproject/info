---
id: 11507
title: Jitsi, ostel.co and ISP censorship
date: 2013-07-22T15:33:44-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=11507
permalink: /2013/07/22/jitsi-ostel-co-and-isp-censorship/
bigimg: [{src: "/wp-content/uploads/2013/07/1347254257_genie.jpg",}]
categories:
  - Research
tags:
  - censorship
  - jitsi
  - ostel
  - ostn
  - sip
  - voip
---
Earlier last week n8fr8 suspected something changed on the ostel.co server, due to many users emailing support specifically about Jitsi connectivity to ostel.co. The common question was “why did it work a few weeks ago and now it doesn’t anymore?”

The tl;dr follows, skip to keyword CONCLUSION to hear only the punch line.

To support n8fr8’s hypothesis, there was a small change to the server but I wan’t convinced it effected anything since all my clients continued to work properly, including Jitsi. Obviously _something_ had changed but none of us knew what it was. After some testing we discovered the problem was related to insecure connections from Jitsi to UDP port 5060 on ostel.co. Secure connections (on TCP port 5061) continued to work as expected.

To make matters more confusing, I could register and make calls with two different clients (CSipSimple and Linphone) on the same network (my home ISP, Verizon FiOS) using an insecure connection to ostel.co on UDP port 5060.

At this point I was like WTF?

I went back to the server, diffed all the configs, checked server versions, connected with every client I could find that would run on any of my computers. The only change was a Kamailio upgrade from 4.0.1 to 4.0.2. A minor point release. The problem with Jitsi remained. What could the server be doing to this poor client?

I did a packet trace on the ostel.co server’s public network interface, filtered to dump packets only on UDP port 5060 that match my SIP username. I opened Jitsi and things got interesting. For the curious, here’s the utility and options I used. If you are new to operating a SIP network, ngrep is an excellent tool for debugging.

`ngrep -d eth0 -t -p -W byline foo port 5060`

I’ll include an excerpt (I’ve included only the relevant headers for this issue) of the initial request from Jitsi. IP addresses and usernames have been changed to protect the innocent.

`U 2013/07/19 22:17:34.920749 0.0.0.0:5060 -> 66.151.32.200:5060<br />
REGISTER sip:ostel.co SIP/2.0.<br />
CSeq: 1 REGISTER.<br />
From: "foo" <sip:&#x66;&#x6f;&#x6f;&#x40;&#x6f;&#x73;&#x74;&#x65;&#x6c;&#x2e;&#x63;&#x6f;>;tag=1eb3467e.<br />
To: "foo" <sip:&#x66;&#x6f;&#x6f;&#x40;&#x6f;&#x73;&#x74;&#x65;l.co>.<br />
Via: SIP/2.0/UDP 0.0.0.0:49152;branch=z9hG4bK-393535-2269e43afef0b312554eb419a8d0540e.<br />
User-Agent: Jitsi2.3.4752Linux.<br />
Contact: "foo" <sip:foo@0.0.0.0:49152;transport=udp;registering_acc=ostel_co>;expires=600.<br />
.`

#  
U 2013/07/19 22:17:34.921155 66.151.32.200:5060 -> 0.0.0.0:5060  
SIP/2.0 401 Unauthorized.  
CSeq: 1 REGISTER.  
From: “foo” <sip:fo&#x6f;@&#x6f;s&#x74;e&#x6c;.&#x63;o>;tag=1eb3467e.  
To: “foo” <sip:foo@&#x6f;&#x73;&#x74;&#x65;l.co>;tag=e01f0de2cdfebbeefc5ff0c8eabbb8b3.2f1f.  
Via: SIP/2.0/UDP 0.0.0.0:49152;branch=z9hG4bK-393535-2269e43afef0b312554eb419a8d0540e;rport=5060.  
WWW-Authenticate: Digest realm=”ostel.co”, nonce=”Uen0alHp8z4d6ePDl83RtMwARltAxzQu”, qop=”auth”.  
Server: kamailio (4.0.2 (x86_64/linux)).

If you read the response, you’ll see Kamailio sent 401 Unauthorized. This is normal for SIP authentication. A second client request should follow it, which should contain an Authorization header with an md5 and a nonce. When Kamailio receives this request, checks the auth database and sends a 200 OK response, the client is authenticated.

The SIP dialog looks good but Jitsi continues not to register. The dialog flow is cut off after the 401 Unauthorized response. It’s almost like something has blocked the response to the client.

Since I could register Linphone using the same account, I did the same trace for that client. Here’s the excerpt.

`U 2013/07/19 22:33:18.372770 0.0.0.0:42680 -> 66.151.32.200:5060<br />
REGISTER sip:ostel.co SIP/2.0.<br />
Via: SIP/2.0/UDP 0.0.0.0:49153;rport;branch=z9hG4bK359459505.<br />
From: <sip:f&#x6f;o&#x40;&#x6f;s&#x74;e&#x6c;&#x2e;c&#x6f;>;tag=142131416.<br />
To: <sip:fo&#x6f;@&#x6f;s&#x74;e&#x6c;.&#x63;o>.<br />
CSeq: 3 REGISTER.<br />
Contact: <sip:foo@0.0.0.0:49153;line=65da8bffcabe8c4>.<br />
User-Agent: LinphoneAndroid/2.1.2-1-g23b7fc0 (eXosip2/3.6.0).<br />
.`

#  
U 2013/07/19 22:33:18.373112 66.151.32.200:5060 -> 0.0.0.0:42680  
SIP/2.0 401 Unauthorized.  
Via: SIP/2.0/UDP 0.0.0.0:49153;rport=42680;branch=z9hG4bK359459505.  
From: <sip:&#x66;&#x6f;&#x6f;&#x40;&#x6f;&#x73;&#x74;&#x65;&#x6c;&#x2e;&#x63;&#x6f;>;tag=142131416.  
To: <sip:foo&#x40;&#x6f;&#x73;&#x74;el.c&#x6f;>;tag=e01f0de2cdfebbeefc5ff0c8eabbb8b3.4065.  
CSeq: 3 REGISTER.  
WWW-Authenticate: Digest realm=”ostel.co”, nonce=”Uen4GlHp9u4FwHNY/uE1iQQNCfGHJiob”, qop=”auth”.  
Server: kamailio (4.0.2 (x86_64/linux)).

This 401 Unauthorized response was received by the client and the follow up request with the Authorization header was sent with the correct digest. Linphone registered. I made a call. Everything worked fine. Indeed WTF?

I stared at these traces for a while to get a clue. Look again at the first line of the request from Jitsi. You’ll see a timestamp followed by two IP:port pairs. Notice the port on the first IP is 5060 and the port on the second IP is also 5060. This means that the **source port** used by Jitsi on my home network is UDP port 5060. In order for a response to come back to Jitsi, it must enter my network on the same port it exited. Now read the top line of the response from Kamailio. Indeed, the server sent the response to UDP port 5060.

Now look at the same flow for Linphone. There is a very different source port in that dialog. In this case, Kamailio sent the response to UDP port 42680 and Linphone received it. Also notice the IP address used by Kamailio as the destination of the response is the same one in the dialog from Jitsi.

The question remained, why can’t Jitsi get the same kind of SIP response on UDP port 5060? Why is Jitsi using a single source port for outgoing traffic anyway? That value can be dynamic. I configured Jitsi to use a different port for insecure SIP. It has an advanced configuration for SIP with the key “SIP client port”. I set this to 5062 (5061 is conventionally used for secure SIP traffic so I incremented by 2) and tried to register again.

SUCCESSSSSSSSSSSS!

To be thorough, I changed Jitsi’s SIP port again to a 5 digit number I randomly typed on my keyboard without looking.

SUCCESSSSSSSSSSSS!

So if Jitsi can register to Kamailio on any port other than UDP port 5060, WTF is going on? I had a suspicion. I tried one more test before I called it. I configured Jitsi to connect on TCP port 5060. It registered successfully. Now I know what’s going on. I have a sad 🙁

CONCLUSION

My ISP, Verizon FiOS, has a firewall running somewhere upstream (it could be on the router they provided, I haven’t checked yet) that blocks incoming UDP traffic to port 5060. This probably falls under their TOS section which forbids “running servers” since Verizon provides voice services for an additional fee on top of data service, despite both running over the same fiber connection to my house. It seems like Verizon doesn’t want their data-only customers to get in the way of that sweet cheddar delivery each month in exchange for “phone service”.

This sucks on two levels.

LEVEL 1

Why is my ISP censoring my incoming traffic when I have 5 mbps of incoming bandwidth? I assume the answer is “because they can.” \*desolate frowny face\*

LEVEL 2

Why doesn’t Jitsi use a dynamic source port for SIP requests? I assume the answer is “Jitsi is open source, why don’t I change this and send a patch upstream?”

Both levels are formidable challenges to overcome. Convincing Verizon to play nice on the Internet feels like a vanity project. I’m writing that off. To make a change to the SIP stack in Jitsi is well within the area of the GP team’s expertise, myself included but it’s not a trivial undertaking. Since this is a default configuration change there is probably a reason upstream devs made this choice so in addition to the programming work there’s the work to convince the developers this would be a change worth a new release.

Since this is specific to Jitsi, I’m going to follow up with the developers and see if I missed anything. Stay tuned for part two.

Thanks for listening. Stay safe!