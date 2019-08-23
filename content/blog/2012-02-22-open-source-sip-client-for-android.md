---
id: 1543
title: Open Source SIP Client for Android
date: 2012-02-22T16:12:25-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=1543
permalink: /2012/02/22/open-source-sip-client-for-android/
categories:
  - Development
tags:
  - ostn
  - voip
  - zrtp
---
The first step in the [Open Secure Telephony Network (OSTN)](https://guardianproject.info/tag/ostn/) is a client. We can’t make a phone call without a phone. In this case there are three primary goals and a number of optional features. The primary goal is an application which speaks the SIP protocol for signalling. It must also speak the ZRTP protocol for peer to peer encryption key exchange. Finally the client must have source code freely available with a license that allows free redistribution.

[<img class="size-full wp-image-1546 alignleft" style="border-width: 3px;border-color: black;border-style: solid;margin: 3px" src="https://guardianproject.info/wp-content/uploads/2012/02/csipzrtp.jpg" alt="" width="200" height="300" />](https://guardianproject.info/wp-content/uploads/2012/02/csipzrtp.jpg)As of today, the only client for Andriod that fufills this qualification is named [CSipSimple](https://code.google.com/p/csipsimple/). Also as of today, the ZRTP functionality is only available from a [nightly build](http://nightlies.csipsimple.com/trunk/) of the binary package. Your mobile handset will not allow you to install this package until you enable “Unknown sources” in the Applications settings of your phone. By default this option is disabled on all phones. To do this, open Settings from the application menu and select Applications. Check the “Unknown sources” box. Some handset vendors [disable this process](http://www.androidcentral.com/att-confirms-third-party-apps-coming-existing-phones) (referred to by the euphemism “sideloading”) though [there are workarounds](http://www.androidcentral.com/swm). Remember, don’t install the version from the market, since that does not support the ZRTP protocol. You must type in the URL for the nightly build in the handset’s browser and download the .apk. Once the package is installed, future updates may be installed through the CSipSimple application settings menu.

CSipSimple offers some nice features. It abstracts the dizzying array of configuration options required by any application that wishes to speak the SIP protocol with another. It also has some template configuration for external service providers, which I will get to in my [next post](http://lee.rockingtiger.com/posts/78).

CSipSimple. Do it!

Original post created at 2012-01-14 05:19:02 UTC [Permalink](http://lee.rockingtiger.com/posts/77)