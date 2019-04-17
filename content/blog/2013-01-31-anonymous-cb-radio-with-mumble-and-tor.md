---
id: 3184
title: 'Mumble and the Bandwidth – Anonymous CB radio with Mumble and Tor'
date: 2013-01-31T02:05:50-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=3184
permalink: /2013/01/31/anonymous-cb-radio-with-mumble-and-tor/
force_ssl:
  - "1"
categories:
  - Research
tags:
  - anonymity
  - ostn
  - push-to-talk
  - tor
  - voice
  - voip
---
[<img class="aligncenter size-full wp-image-3186" alt="mumble and the bandwidth" src="https://guardianproject.info/wp-content/uploads/2013/01/mumble-and-the-bandwidth.jpg" width="800" height="478" srcset="https://guardianproject.info/wp-content/uploads/2013/01/mumble-and-the-bandwidth.jpg 800w, https://guardianproject.info/wp-content/uploads/2013/01/mumble-and-the-bandwidth-300x179.jpg 300w" sizes="(max-width: 800px) 100vw, 800px" />](https://guardianproject.info/wp-content/uploads/2013/01/mumble-and-the-bandwidth.jpg)

The journey towards anonymous and secure voice communication is a long one. There’s lots of roadblocks to get your voice from point A to point B over the Internet if you need to prevent eavesdropping or censorship. There is the limited bandwidth of mobile data connections. There is the high latency of the TCP protocol. [To achieve anonymity via Tor](https://www.torproject.org/about/overview.html.en#whyweneedtor), there’s even more latency added to each packet.

[Mumble](http://mumble.sourceforge.net/) is a non-standard protocol that was originally designed for realtime voice chat for video games. If you’ve ever played Halo or World of Warcraft, this should sound familiar. If not, think of it as a conference call you don’t have to ring. You simply connect to a Mumble server over the Internet and your voice will transmit to everyone else.

Mumble clients are available for [Android](https://play.google.com/store/apps/details?id=com.morlunk.mumbleclient&feature=nav_result#?t=W251bGwsMSwxLDMsImNvbS5tb3JsdW5rLm11bWJsZWNsaWVudCJd) and [iOS](https://itunes.apple.com/us/app/mumble/id443472808?ls=1&mt=8), as well as a cross-platform desktop client. The server software is also cross-platform. Guardian Project is focusing on the Android client named [Plumble](https://play.google.com/store/apps/details?id=com.morlunk.mumbleclient&feature=nav_result#?t=W251bGwsMSwxLDMsImNvbS5tb3JsdW5rLm11bWJsZWNsaWVudCJd) and the official server [backported to Debian stable](http://packages.debian.org/search?keywords=mumble&searchon=names&section=all&suite=squeeze-backports).

A cool feature of Mumble is a [Push To Talk](https://en.wikipedia.org/wiki/Push-to-talk) (PTT) method to speak to the channel. Your voice is only transmitted when you press the PTT button in the user interface. Another lower level feature that’s important for our anonymity goal is TCP support. For any application to run over Tor, it must use the TCP protocol. This rules out most VoIP clients, since they use UDP. Here is a case where Mumble’s non-standard protocol works to our advantage.

When Tor is running and your Mumble client is configured to use TCP, connecting to your local SOCKS5 proxy offered by Tor allows you to join a Mumble server anonymously. The big problem is as suspected, latency. The traffic passing through the Tor network must make [an indeterminate number of proxy hops](https://www.torproject.org/about/overview.html.en#thesolution) to be anonymized successfully. Each hop adds more and more latency. This makes a typical syncronous voice call impossible since there’s no way to determine when one person has stopped talking and when the other can respond without interrupting.

Latency in human speech transmision has deep psychological impact on a conversation. A [Japanese research project called SpeechJammer](https://sites.google.com/site/qurihara/top-english/speechjammer) exploited this part of our senses by inventing a “shut up gun.” When pointed at a person it makes them immediately stop talking. Everyone who has used a cell phone knows the frustration of “echo” where you hear your own voice, slightly delayed. The delay is caused by the network latency of the cellular carrier.

Another similar example is a [VoIP](http://en.wikipedia.org/wiki/Voip) call on a congested network. The side effect of the latency is that one person accidently interrupts the other person because he thinks the other person has finished talking, when in reality the other person’s voice hasn’t yet arrived at the other end. Interruption ensues, no one is happy nor do they know anything new since the transmission was not understood. High latency makes [full-duplex communication ineffective](http://en.wikipedia.org/wiki/Full-duplex#Full-duplex).

The contemporary telephone you are acustomed to allows both sides to talk and listen simultaneously. This is called full-duplex. Early radio telephones like walkie talkies, CB radio or aviation radio are half-duplex systems, meaning that for any given transmission, only one side can talk while the other side listens. Running Mumble over Tor takes a full-duplex technology and effectively reduces it to half-duplex. Even though the protocol is full-duplex, when run through a high latency network like Tor, the transmit and receive channels are so far out of sync there is no point in allowng both sides to talk at once. Again, interruption ensues.

Then it hit me. Radio telephones have been around since the turn of the 20th century, when people figured out a reasonable way to do voice chat without the technology causing accidental interruptions in the conversation. In particular, the use of procedure words, or [prowords](http://en.wikipedia.org/wiki/Procedure_word), are essential for one speaker to acknowledge the transmission of the other (Roger), to signify that one party is finished speaking (Over), or indicate when one party has left the conversation (Out).

Here in the USA, some prowords evolved into a coloquial language, complete with [slang](https://en.wikipedia.org/wiki/List_of_CB_slang) thanks to the Citizen Band radio boom of the 1960s and the truck driving culture that used it to communicate while on the road. The 1977 film [Smokey and the Bandit](http://www.imdb.com/title/tt0076729/?ref_=sr_1) is more than just a touching love story with world class actors, it is an amazing dramatization of an information culture that resembled pre-Internet [BBS systems](http://en.wikipedia.org/wiki/Bulletin_board_system) and current day [Internet Relay Chat (IRC)](http://en.wikipedia.org/wiki/IRC) networks around the globe. The truck drivers portrayed in that movie have a mobile, decentralized information sharing network that is anonymous. The users have pseudonyms and a language of their own. Many of them have never met their CB radio friends IRL. They are invisible companions on the lonely road of the US of A.

  
 

Old ideas are worth bringing back if they have strong roots. CB and general purpose radio telephones have a long history, unlike the standard the standard of tody, VoIP. Perhaps these features are thought of as obsolete or not cutting-edge enough to model into a digital system. Regardless of the reason, if you are looking for a mobile and open source PTT solution to use on the Internet with anonymity and security, Mumble over Tor is currently the state of the art. All you have to do is throw in some prowords to keep the conversation flowing.

The Guardian Project is operating a private Mumble server during a testing phase, and we have plans to open this to the public as part of the [OSTN research effort](https://guardianproject.info/wiki/OSTN). When that happens, I will post application-specific tutorials to install and configure the Plumble client. I will also publish a cookbook to build a Mumble server.

Finally, an example transmission log with some prowords:

_Internet_: Guardian Project. I have a ping response from your server, over.  
_GP_: Roger Internet. Ping was sent, over.  
_Internet_: Guardian Project. Build anonymous PTT system with open source software, over.  
_GP_: Internet, build anonymous PTT system with open source software, wilco. Out.