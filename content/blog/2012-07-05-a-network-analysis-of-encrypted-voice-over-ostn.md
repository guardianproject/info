---
id: 2464
title: A Network Analysis of Encrypted Voice over OSTN
date: 2012-07-05T14:23:50-04:00
author: patch
layout: post
guid: https://guardianproject.info/?p=2464
permalink: /2012/07/05/a-network-analysis-of-encrypted-voice-over-ostn/
bigimg: [{src: "http://guardianproject.info/wp-content/uploads/2012/06/zrtpswitch.png",}]
categories:
  - News
tags:
  - audit
  - encryption
  - ostel
  - ostn
  - voip
  - zrtp
---
**Introduction to OSTN**

The [OSTN](http://guardianproject.info/wiki/OSTN) network stands for Open Source Telephony Network. It is a federated network standard for supporting Internet calling with end-to-end encryption ala ZRTP. Its very similar to e-mail in that VOIP calls can be routed to addresses such as &#x75;&#x73;&#x65;&#x72;@doma&#x69;&#x6e;&#x2e;&#x74;ld. Its a simple concept, but I believe it to be ground breaking implementation! Never before have I seen such an accessible solution to encrypted VOIP calls. OSTN is platform independent, is a federated network, and it is an open standard such that it is widely adoptable. There are two main components that are required to use OSTN with encryption: a VOIP client that supports ZRTP for end-to-end encryption and user account with an OSTN provider.

  * OSTEL is the first working OSTN provider. Sign up for an account at [ostel.me](https://ostel.me/ "ostel.me").
  * CSipSimple is the recommended VOIP client for use with OSTN. It has a built in  profile for OSTN accounts and supports ZRTP. You must use the [nightly build](http://nightlies.csipsimple.com/trunk/)! This is the latest version and requires that you allow outside applications on Android by checking the Settings>Applications>’Unknown sources’ box. Information on setting it up for your Android device can be found on [our wiki](http://guardianproject.info/wiki/Ostel "our wiki").

While this post focuses on using OSTN with the recommended CSipSimple software, the concepts extend to all OSTN platforms. Check out [the project page](https://guardianproject.info/wiki/OSTN) for more info on alternative clients.

**Looking at Encrypted VOIP with Wireshark**

Traffic dumps of an OSTN call and a ZRTP encrypted OSTN call were logged and analyzed in Wireshark for comparison. This is how someone between you and your caller would see your VOIP traffic. I was looking for three things in this audit

  1. Confirm encryption was working in conjunction with what a user would logically expect
  2. Demonstrate how easy it is to capture and view non-encrypted VOIP
  3. Identify threats what types of security ZRTP provides

I can confirm that the encryption works as expected. The traffic logs of both phone calls can be found at the end of this post. First, here is a look at a normal non-encrypted phone call over OSTN with CSipSimple and secure call.

<div id="attachment_2466" style="width: 246px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2012/06/uncrypt.png"><img aria-describedby="caption-attachment-2466" class=" wp-image-2466" title="Non-secure VOIP" src="https://guardianproject.info/wp-content/uploads/2012/06/uncrypt.png" alt="" width="236" height="360" /></a>
  
  <p id="caption-attachment-2466" class="wp-caption-text">
    Cleartext phone calls are noted by absence of ZRTP overlay.
  </p>
</div>

<div id="attachment_2467" style="width: 246px" class="wp-caption alignright">
  <a href="https://guardianproject.info/wp-content/uploads/2012/06/ostncall-encrypted.png"><img aria-describedby="caption-attachment-2467" class=" wp-image-2467" title="Secure VOIP" src="https://guardianproject.info/wp-content/uploads/2012/06/ostncall-encrypted.png" alt="" width="236" height="360" /></a>
  
  <p id="caption-attachment-2467" class="wp-caption-text">
    ZRTP Enabled phone calls are indicated by lock icon
  </p>
</div>

 

 

 

 

 

 

 

 

 

 

 

 

It is quite clear to the user that ZTRP has been enabled by the lock icon that appears in both phones.  Traffic logging has also confirmed that when you see the lock icon, ZRTP has successfully been set up and is being used. So far, so good. Make sure you see the lock sign if you are expecting to be talking on a secure conversation.

CSipSimple uses **opportunistic** ZRTP encryption that is enabled by default for OSTN accounts with CSipSimple. This means that all calls will begin without encryption and then send ‘ZRTP Hello’ packets to let each host know that a ZRTP conversation can begin. From here ZRTP negotiates a secure connection and then transfers the conversation to encrypted voice. Here are two pictures from Wireshark showing the very beginning of a (ZRTP enabled) OSTN phone call and where the encryption actually switches on. The SRTP protocol indicates that you are using encrypted voice. ZRTP simply defines the negotiation process for SRTP. This is not a minor thing however, it is because of this that ZRTP can provide end-to-end encryption. End-to-end encryption prevents a third-party from eavesdropping and possibly passing information on to higher authorities.

<div id="attachment_2474" style="width: 709px" class="wp-caption alignnone">
  <a href="https://guardianproject.info/wp-content/uploads/2012/06/zrtpstart.png"><img aria-describedby="caption-attachment-2474" class="size-full wp-image-2474 " title="zrtpstart" src="https://guardianproject.info/wp-content/uploads/2012/06/zrtpstart.png" alt="" width="699" height="97" srcset="https://guardianproject.info/wp-content/uploads/2012/06/zrtpstart.png 699w, https://guardianproject.info/wp-content/uploads/2012/06/zrtpstart-300x41.png 300w" sizes="(max-width: 699px) 100vw, 699px" /></a>
  
  <p id="caption-attachment-2474" class="wp-caption-text">
    First UDP packets of an ZRTP enabled phone call. ZTRP Hello is sent out at the same time as the first RTP packet.
  </p>
</div>

<div id="attachment_2475" style="width: 709px" class="wp-caption alignnone">
  <a href="https://guardianproject.info/wp-content/uploads/2012/06/zrtpswitch.png"><img aria-describedby="caption-attachment-2475" class="size-full wp-image-2475 " title="zrtpswitch" src="https://guardianproject.info/wp-content/uploads/2012/06/zrtpswitch.png" alt="" width="699" height="82" srcset="https://guardianproject.info/wp-content/uploads/2012/06/zrtpswitch.png 699w, https://guardianproject.info/wp-content/uploads/2012/06/zrtpswitch-300x35.png 300w" sizes="(max-width: 699px) 100vw, 699px" /></a>
  
  <p id="caption-attachment-2475" class="wp-caption-text">
    Successful ZRTP hand-off. Connection switches from normal RTP to encrypted RTP here.
  </p>
</div>

The important part to notice here is that the hand-off is fast. Comparing the times of the first RTP packet to the first encrypted packet takes about 1.5 seconds. Multiple traffic logs confirmed that this is a consistent number. This means that if you immediately start talking during the start of an encrypted phone it is possible for some of your voice to be transmitted clear-text. I attempted to record this section by talking in the very beginning of a call and extracting voice. I wasn’t successful, but I wouldn’t discount that you will release some clear voice audio at the beginning of a conversation.

**What ZRTP Guarantees**

So, things look good with OSTN calls. ZRTP is enabled by default on all OSTN accounts with CSipSimple and it uses opportunistic encryption. Also, it is very easy for the user to tell that their call has been successfully encrypted. Great! What does this mean for the user? When correctly using ZRTP, a user can expect that their phone calls are fully **confidential**. No third party can intercept, listen, or mangle your phone call. This includes your OSTN provider of course.

**What ZRTP Doesn’t Guarantee**

ZRTP does not stop** censorship ** or provide **anonymity.  **This is something Orbot might be able to help with one day. Currently, the latency of the Tor network prevents real-time protocols from working. The current best solution would be to use a VPN provider to tunnel ZRTP traffic. However, now that VOIP is illegal in many countries it is not recommended that anyone trust this solution until a tested and verified method is published.

**Conclusion**

Using end-to-end voice encryption has never been this easy! This analysis confirmed that OSTN works quite well in practice. There are two things the user should do to ensure secure communication: make sure to read and confirm the verification dialog boxes and check to make sure your calls have the lock icon when you are counting on them to be encrypted. Just like that, you too can be a [cypherpunk](http://en.wikipedia.org/wiki/Cypherpunk) (or just someone with a reasonable expectation of privacy!). Like Phil Zimmerman, the creator of ZRTP,  has said: “[OSTN] lets you whisper in someone’s ear a thousand miles away” Check back for our upcoming post which will look in more detail at the threat model of an OSTN phone call.

You can download the traffic log of a encrypted and unencrypted OSTN call [here](https://guardianproject.info/wp-content/uploads/2012/07/ostnlogs.zip)