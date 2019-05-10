---
id: 12004
title: VoIP security architecture in brief
date: 2013-11-21T19:07:17-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=12004
permalink: /2013/11/21/voip-security-architecture-in-brief/
bigimg: [{src: "/wp-content/uploads/2013/11/relation.gif",}]
categories:
  - News
tags:
  - ostel
  - ostn
  - sip
  - tls
  - voip
  - zrtp
---
Voice over IP (VoIP) has been around for a long time. It’s ubiquitous in homes, data centers and carrier networks. Despite this ubiquity, security is rarely a priority. With the combination of a handful of important standard protocols, it is possible to make untappable end to end encryption for an established VoIP call.

TLS is the security protocol between the signaling endpoints of the session. It’s the same technology that exists for SSL web sites; ecommerce, secure webmail, Tor and many others use TLS for security. Unlike web sites, VoIP uses a different protocol called the Session Initiation Protocol (SIP) for signaling: actions like ringing an endpoint, answering a call and hanging up. This is the metadata of calls. SIP-TLS uses the standard Certificate Authorities for key agreement. This implies trust between the certificate issuer and the calling endpoints.

<div id="attachment_12006" style="width: 440px" class="wp-caption aligncenter">
  <a href="http://www.siptutorial.net/SIP/relation.htm"><img aria-describedby="caption-attachment-12006" src="https://guardianproject.info/wp-content/uploads/2013/11/relation.gif" alt="SIP Dialog" width="430" height="322" class="size-full wp-image-12006" /></a>
  
  <p id="caption-attachment-12006" class="wp-caption-text">
    An example of a SIP dialog
  </p>
</div>

To add a little complexity, the content of calls has only a small relationship to SIP. The key agreement protocol for P2P VoIP content is called ZRTP. In a true P2P system, all the key agreement and encryption of a call’s content happens in the endpoint applications. An important distinction between VoIP and other networked communications is that all devices are both client and server at once, so we have only “endpoints” rather than “clients” or “servers”. Once the endpoints agree on a shared secret, the ZRTP session ends and the SRTP session begins. When established, all audio and video content going over the network is encrypted. Only the two peer endpoints who established a session with ZRTP can decrypt the media stream. This is the part of the conversation that cannot be wiretapped nor can metadata of sessions in progress be spied on.

<div id="attachment_12008" style="width: 560px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2013/11/zrtp_overview.png"><img aria-describedby="caption-attachment-12008" src="https://guardianproject.info/wp-content/uploads/2013/11/zrtp_overview-902x1024.png" alt="ZRTP Overview" width="550" height="624" class="size-large wp-image-12008" srcset="https://guardianproject.info/wp-content/uploads/2013/11/zrtp_overview-902x1024.png 902w, https://guardianproject.info/wp-content/uploads/2013/11/zrtp_overview-264x300.png 264w, https://guardianproject.info/wp-content/uploads/2013/11/zrtp_overview.png 986w" sizes="(max-width: 550px) 100vw, 550px" /></a>
  
  <p id="caption-attachment-12008" class="wp-caption-text">
    An example ZRTP key exchange
  </p>
</div>

To step back a little, let’s review some acronyms. First there is [SIP](http://www.siptutorial.net/SIP/background.html) (Session Initialization Protocol). This protocol is encrypted with TLS. It contains the IP addresses of the endpoints who wish to communicate but it does not interact with the audio or video stream. 

Second, there is ZRTP. This protocol enters into the mix after a successful SIP dialog establishes a call session by locating the two endpoints. It transmits key agreement information over a unverified SRTP channel between the peers. The peers use their voices to speak a secret that verifies that the channel is secure between only the two peers.

Third, enter SRTP. Only after the ZRTP key exchange succeeds is the call content encrypted with the Secure Real Time Protocol. From this point forward, all audio and video is secure and uniquely keyed to each individual session.

This brief was inspired by the numerous discussions I’ve participated in online and offline during my ongoing operation of ostel.co, a secure VoIP service sponsored by The Guardian Project. I understand that VoIP is complex when compared to HTTP and the mainstream understanding of the securirty elements often omits the ZRTP/SRTP content, rather focusing on only the SIP-TLS signaling. While signaling is important, few calls would be useful without content.