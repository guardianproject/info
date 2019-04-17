---
id: 2929
title: Voice over Tor?
date: 2012-12-10T11:00:03-04:00
author: patch
layout: post
guid: https://guardianproject.info/?p=2929
permalink: /2012/12/10/voice-over-tor/
image: http://guardianproject.info/wp-content/uploads/2012/12/onioncart.jpg
categories:
  - News
tags:
  - orbot
  - tor
  - voice
  - voip
---
[<img class=" wp-image-2968" title="onioncart" src="https://guardianproject.info/wp-content/uploads/2012/12/onioncart.jpg" alt="" width="100%" height="425" srcset="https://guardianproject.info/wp-content/uploads/2012/12/onioncart.jpg 700w, https://guardianproject.info/wp-content/uploads/2012/12/onioncart-300x182.jpg 300w" sizes="(max-width: 700px) 100vw, 700px" />](https://guardianproject.info/wp-content/uploads/2012/12/onioncart.jpg)

Voice calls over <a title="Tor Project" href="https://www.torproject.org/" target="_blank">Tor</a> are supposed to be impossible. It seems this may no longer be the case.

Without being able to do voice over IP (VOIP) conversations over the Tor network, people are prevented from being able to route  calls outside of censored networks. People ask us if there is any way they can route voice traffic through Tor to avoid blocks. To our surprise, we tested <a title="skype" href="http://skype.com/" target="_blank">Skype</a> and found that it can work acceptably over <a title="Orbot" href="https://guardianproject.info/apps/orbot/" target="_blank">Orbot</a>.

There are two main reasons that it has been held that VOIP will not practically work over the Tor network.

  1. A technical problem with the transport layer that Tor supports.
  2. The network is too slow for the latency demands of a real-time voice conversation.

However, it turns out Skype has some pretty robust signaling capabilities such that it works on a variety of network conditions. Also, in practice the latency is more usable then one would have thought. This is good news for the future of VOIP traffic over the Tor network, and not only over Skype.

# **Problem 1: Transport Protocol**

TCP is the most common transport protocol for the Internet. It guarantees reliable communication and is used for nearly everything you do in an Internet browser. UDP is a more relaxed protocol used for real-time communications because it reduces latency. The cost for this is that UDP is not reliable and will occasionally drop traffic. For this reason, it is useful for real-time applications that benefit from lower latency. While dropping packets is never ideal, in a real-time communications it usually doesn&#8217;t significant affect the quality and even then the time it would take to re-transmit lost packets with TCP might preclude the data being relevant to the stream anymore.

The problem here is that Tor only supports TCP for its transport layer. Meanwhile, VOIP applications use UDP. So they&#8217;re not supposed to work over Tor and one of the main difficulties for VOIP users to apply strong anonymity to real-time voice communication.

Even if you tunneled UDP traffic through Tor it would be encapsulated in TCP and lose any benefits that UDP provides for real-time traffic. The TCP mechanisms attempt to account for lost packets and hold delivery of future packets until a resend is complete.

If you&#8217;re interested in learning more about networking, I would highly recommend <a title="Computer Networks by Peterson and Davie" href="http://books.google.com/books/about/Computer_networks.html?id=eftSAAAAMAAJ" target="_blank">Computer Networks by Peterson and Davie.</a> Its takes a practical approach to teaching the technology and avoids strict adherence to the layered model of the Internet. Beyond that, any TCP/IP or Internet technology introductory resource will get you far!

**Solution: **Here either Tor needs to support UDP or you need a VOIP client that supports TCP. It had been suggested that Skype will fallback to use TCP connections in instances in which the user has UDP traffic blocked. This is not a very uncommon network policy for some Internal networks and reflects Skype&#8217;s effort to make their application work in many hostile network conditions (NATs, firewalls, ect.).

# **Problem 2: Latency**

Second, Tor relays and mixes its traffic across multiple nodes which greatly increases latency. People generally have pretty high performance expectations for latency over a two-way phone conversation. Adding even a couple of  milliseconds of lag between conversations can be very noticeable to the user. It causes jerks and jumps in the conversation, making it hard to communicate. For this reason, it is likely that widespread routing of voice traffic through Tor is unlikely. However, people already cope with quite a bit of latency using VOIP internationally, and there are very real security and censorship demands that would require VOIP over Tor. In many situations latency will be quite usable. Let&#8217;s see how it actually feels over Tor.

**Solution: **

The solution here is just accepting the latency. The latency is not ideal but in practice, it is still quite usable. As Tor network performance increases (and one-day supports UDP), real-time communications will begin to have better performance.

# **Skype over Tor**

For testing, I used two Nexus One phones running Gingerbread and the latest Skype binary from the Android App Store. Orbot will transparently route traffic through Tor if you use its transproxy features. The transproxy will drop UDP traffic since it can&#8217;t be routed through Tor. It is this feature that causes Skype to fallback to TCP and work over Tor.

First, I looked at normal Skype traffic leaving the phone. It uses some TCP connections to contact Microsoft servers and authenticate your account. Once you start a voice chat you will see lots of UDP traffic as expected. However, if you turn on Orbots transproxy you will see Skype being forced to start up a conversation using only TCP.

Here is a Wireshark screenshot of failed UDP connections to Microsoft servers. I did this by letting the UDP traffic through, logging it, and then dropping it before it left my test environment. So you can see the UDP connections going one way to a variety of IP addresses:

[<img class="aligncenter size-full wp-image-2976" title="croppedUDP" src="https://guardianproject.info/wp-content/uploads/2012/12/croppedUDP.png" alt="" width="100%" srcset="https://guardianproject.info/wp-content/uploads/2012/12/croppedUDP.png 988w, https://guardianproject.info/wp-content/uploads/2012/12/croppedUDP-300x128.png 300w" sizes="(max-width: 988px) 100vw, 988px" />](https://guardianproject.info/wp-content/uploads/2012/12/croppedUDP.png)

We set one of the phones to route through Tor by turning on the transproxy. Then logged into Skype on each phone and placed a call. Skype worked over Tor! We were having a conversation across two IPs from two different ISPs. The latency wasn&#8217;t great, but it was surprisingly usable. I&#8217;ve included two-packet captures. One should just look like Tor traffic and is a Skype conversation over Tor. The other is an actual log of the dropped UDP packets (I dropped them at an intermediary device rather than using the Transproxy to capture this). In the UDP log set you&#8217;ll see a bunch of UDP traffic originating form a single address (the phone) with no return traffic. They UDP traffic was being immediately dropped after the log.

It turns out you can have a workable VOIP chat over Tor if you use Skype. The findings are interesting because they are relevant to the general problem of trying to use real-time communication through the Tor network. It may also be useful for VERY specific and limited threat models that involve censorship bypass in which there is little risk in being caught.

Here&#8217;s to hoping for UDP over Tor in the future. Until then, Guardian Project is working on a design for high latency voice communications. The idea is that you could send quick voice messages with the click of a button similar to how you use an old hand-held radio. We&#8217;re toying with names like Push to Torlk and Onion Ringer. Stay tuned!

> Disclaimer: In my opinion, Skype is not a secure standard for VOIP communication. It uses non-standard closed source encryption and has likely become CALEA compliant upon [acquisition](http://www.forbes.com/sites/ericjackson/2012/07/22/its-terrifying-and-sickening-that-microsoft-can-now-listen-in-on-all-my-skype-calls/) by Microsoft. That means that they have infrastructure in place to intercept communications and relay that information to law enforcement agencies around the world. It is unwise to assume that other state and non-state actors would not also have means to access that data.