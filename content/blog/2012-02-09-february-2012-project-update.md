---
id: 1503
title: 'February 2012: Project Update'
date: 2012-02-09T17:19:06-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=1503
permalink: /2012/02/09/february-2012-project-update/
force_ssl:
  - "1"
categories:
  - News
---
Through coordination with the Tor Project, we released **Orbot** 1.0.7, which includes an embedded version of OpenSSL to assure we have the latest security enhancements for this critical cryptographic library. In addition, compatibility testing was done on Android 4.0 (Ice Cream Sandwich) and with the latest versions of Firefox Mobile. As always you can learn more and download Orbot in the Android Market and at <https://guardianproject.info/apps/orbot>



With the public awareness of internet censorship and surveillence growing thanks to SOPA, PIPA and CarrierIQ, not to mention the ongoing unrest in many regions if the world, we have seen a huge spike in interest and download of Orbot, Orweb and Gibberbot. Here are some notable links:  
<http://mobileactive.org/howtos/user-guide-to-orbot>  
<http://www.chinagfw.org/2012/01/orbot-tor.html>  
<http://geeknews.cz/orbot-svobodnejsi-brouzdani-pro-android/352/>  
<http://www.101hacker.com/2012/01/10-must-have-free-android-apps.html>

We pushed a small fix to **ObscuraCam** to solve a problem with saving processed images on many Samsung Galaxy devices, and a number of fixes in the native Android JPEG Redaction library which has been developed as part of the project.  
<https://github.com/guardianproject/securesmartcam/tree/obscurav1>

Along with our partners at WITNESS, we presented the entire **SecureSmartCam** project at the monthly New York Tech Meetup event, attended by hundreds of the city’s top developers, entrepreneurs and investors. Our goal was too raise awareness about visual privacy, show off our app, and highlight the fact that we are doing grant-funded, open-source human rights tech work in the middle of Silicon Alley. The project was well received with the demo going off without a hitch. The Economist also featured the SecureSmartCam project in print and online through a story focused on the future of protest video.

Economist blog and video: <http://www.economist.com/blogs/babbage/2012/01/technology-and-democracy>  
New York Tech Meetup full stream: <http://vimeo.com/34608516>

Formal management of the **SQLCipher for Android** project has been moved over to a joint effort between Zetetic, LLC and the Guardian Project, with the new online home being <http://github.com/sqlcipher> and the code packaging moving to a net.sqlcipher.* base. Zetetic is the creator of the original core SQLCipher project and they have been critical in our efforts to bring it to Android. We expect to release an update to SQLCipher 2 with support for Android ICS 4.x this month.

Our **Portable Shared Security Tokens (PSST)** research project made great headway in sorting through the many, many formats for storing cryptographic keys in open-source software, specifically messaging apps using the Off-the-Record private messaging protocol. One of the project goals is to enable synchronization of keys, included trusted or verified status, from desktop to mobile contexts. An initial set of code has been posted which enables transfer of key between Pidgin and Gibberbot. Learn more at <https://guardianproject.info/wiki/PSST>

**Open Secure Telephony Network (OSTN)** is another internal research effort to audit and promote reliable solutions for secure open-source, mobile voice communication. Our chief focus has been the determining which client apps and server soft switches properly support TLS, SRTP and ZRTP protocols for encrypting both SIP signaling and the actual RTP media streaming. We also surveyed the mobile telephony habits of over twenty activists and NGOs, and unsurprisingly found a great dependence on Skype. We plan to release the results of the survey publicly, along with some initial assessments and tutorials in February. Track our efforts at <https://guardianproject.info/wiki/OSTN>