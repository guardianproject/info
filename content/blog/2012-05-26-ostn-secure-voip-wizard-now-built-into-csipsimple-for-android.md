---
id: 2281
title: '<!--:en-->OSTN secure VoIP wizard now built into CSipSimple for Android<!--:-->'
date: 2012-05-26T21:14:52-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=2281
permalink: /2012/05/26/ostn-secure-voip-wizard-now-built-into-csipsimple-for-android/
categories:
  - News
tags:
  - ostel
  - ostn
  - sip
  - voip
  - zrtp
---
<!--:en-->If you saw our last post about how to 

[setup your own secure voice-over-IP server instance](https://guardianproject.info/2012/05/17/build-your-own-open-secure-telephony-network-some-assembly-required/), then this news is for you.

If you are an Android user looking for the [best open-source VoIP app](http://code.google.com/p/csipsimple/), and really need one that can support [secure communications](https://OSTel.co), then this post is ALSO for you.

[CSipSimple](http://code.google.com/p/csipsimple/), the previously mentioned “best VoIP app”, now includes a wizard for setting up an account configuration for any server which complies with our [Open Secure Telephony Network specification](https://guardianproject.info/wiki/OSTN_Compliance_Specification). In short, this means it uses TLS or SSL to secure the SIP signaling traffic, and supports proxying of the RTP media streams for the actual voice or video calls, without in any way interfering with the ZRTP encryption passing through it.

There are currently two OSTN compliant public services, [OSTel](https://OSTel.co) and [PillowTalk](https://intimi.ca:4242/), but we hope and expect there to be many more, both public and private, and are very happy that this secure by default wizard configuration is now included in the core CSipSimple project. In addition, by having this support in a multiple purpose client (as opposed to a single OStel-only app), you can simultaneously use multiple VoIP accounts. For example, you might setup a second account with Callcentric, that is less secure, but that would allow you to make calls over the standard telephone system.

Below are screenshots of CSipSimple account setup running on an Android 4 ICS 7″ Tablet.

First, select “Add account”, scroll down to Generic wizards, and select OSTN.

[<img class="alignnone  wp-image-2282" title="Screenshot_2012-05-26-20-46-05" src="https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-46-05.png" alt="" width="614" height="360" srcset="https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-46-05.png 1024w, https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-46-05-300x175.png 300w" sizes="(max-width: 614px) 100vw, 614px" />](https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-46-05.png)

Then enter your username, password, and the OSTN compliant server you wish to connect to.

[<img class="alignnone  wp-image-2283" title="Screenshot_2012-05-26-20-53-56" src="https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-53-56.png" alt="" width="614" height="360" srcset="https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-53-56.png 1024w, https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-53-56-300x175.png 300w" sizes="(max-width: 614px) 100vw, 614px" />](https://guardianproject.info/wp-content/uploads/2012/05/Screenshot_2012-05-26-20-53-56.png)

Once you hit “Save”, the account should be configured, attempt to register, and be ready to make calls.

Learn more about the CSipSimple project: <http://code.google.com/p/csipsimple/>

Download the latest [CSipSimple nightly trunk here.](http://nightlies.csipsimple.com/trunk/)

Many thanks to the brilliant Ooze and R3gis for their continued support.<!--:-->

<!--:pt-->

<!--:-->

<!--:es-->

<!--:-->