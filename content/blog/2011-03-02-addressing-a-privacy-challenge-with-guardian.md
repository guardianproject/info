---
id: 775
title: 'Addressing a “Privacy Challenge” with Guardian'
date: 2011-03-02T20:39:18-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=775
permalink: /2011/03/02/addressing-a-privacy-challenge-with-guardian/
categories:
  - Development
  - News
tags:
  - challenge
  - contest
  - privacy
---
Organized by the [ACLU](http://aclunc.org/), [Tor Project](http://torproject.org/), and [PrivacyByDesign.c](http://privacybydesign.ca/)a, the [“Develop for Privacy Challenge”](http://www.develop4privacy.org/) is an interesting new software development challenge that was announced last month. Developers (teams or individuals) have until May 31st to come up with apps which address this goal:

> Develop apps for smartphones or other mobile devices that educate users about mobile privacy and give them the ability to claim or demand greater control of their own personal information.

We don’t plan to compete in this contest ourselves, as we would rather support and encourage other developers to take a shot at it. Along those lines, we would really like to see developers use some of the [apps we have built](https://guardianproject.info/apps), and [code we have released](https://github.com/guardianproject), as part of their solutions. We have been putting together a large number of “lego” building blocks over the last year, just waiting for someone to come and put them together in a revolutionary way. Here is a breakdown of some of our more useful components:

[<img class="alignleft" style="margin-left: 3px; margin-right: 3px;" src="https://www.torproject.org/images/THS-4.png" alt="" width="162" height="111" />](https://www.torproject.org/images/THS-4.png)

[ORbot -More than just Circumvention](https://guardianproject.info/apps/orbot): beyond just being a great way to connect to Tor on Android, Orbot also supports [Tor Hidden Services](https://www.torproject.org/docs/hidden-services.html.en). This means you can run local servers on your Android device, and access them via a .onion hostname from any other device or computer on the Tor network. We have been looking at building all sorts of cool anonymous peer-to-peer apps using this capability, but haven’t found the time yet.

[ORlib – Privacy-powered HTTP and Sockets:](https://guardianproject.info/code/orlib/) This an Android Library for use by any application that wishes to route its network traffic through the Tor network. If your app uses this library, and Orbot is installed and activated on the device, it will automatically handle routing your connections, DNS requests and traffic through the Tor network. By building this into your device, it means your users do not need to have a rooted device in order to have their network traffic anonymized and otherwise protected from filtering and surveillence.

[ProxyMob](https://guardianproject.info/apps/proxymob-firefox-add-on/): We have the beginnings of a Firefox for Android add-on that allows user to control the proxy settings for their browser. However, this add-on needs to fully evolve into a mobile version of [TorButton](https://www.torproject.org/torbutton/). This alone would be a great project to tackle, discovering what unique challenges their are to anonymizing mobile web access, such as constant geolocation tracking!

[<img class="alignright" style="margin-left: 3px; margin-right: 3px;" src="https://github.com/guardianproject/SecureSmartCam/raw/master/doc/comps/Still/11_blur.jpg" alt="" width="173" height="288" />](https://github.com/guardianproject/SecureSmartCam/raw/master/doc/comps/Still/11_blur.jpg)

[SecureSmartCam](https://guardianproject.info/apps/securecam/): Visual privacy is an emerging area of research and development, specifically with the growing problem/benefit of cameras being everywhere, in our pockets, on our streets, at all times. We are partnering with [Witness.org](http://witness.org) to build camera software that is capable of protecting identities, securing sensitive metadata stored in photos, and empowering the documenter and subjects of photos, video and audio recordings to maintain more control of media that they have consented to be a part of. With all that in mind, we need some serious media hackers who are interested in thing liks OpenCV, GStreamer, EXIF and more to contribute to this project, and to come up with some new brilliant secure cam apps of their own.

We have a number of other ongoing projects that you can find on our [Github site](https://github.com/guardianproject), including encrypted SQL databases and file system tools, and our secure instant messaging app, [Gibberbot](https://guardianproject.info/apps/gibber). All in all, there is a quite a bit of work on which any interest in improving mobile privacy can build upon. We would be very happy to provide support via [email or IRC](https://guardianproject.info/contact/) to any dev interested in working with us, as well.

**Good luck, and [game on](http://www.develop4privacy.org/)!**

**<http://www.develop4privacy.org/>  
**