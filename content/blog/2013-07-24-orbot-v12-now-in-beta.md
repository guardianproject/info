---
id: 11519
title: Orbot v12 now in beta
date: 2013-07-24T12:32:45-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=11519
permalink: /2013/07/24/orbot-v12-now-in-beta/
bigimg: [{src: "https://guardianproject.info/wp-content/uploads/2013/07/mightyorbot.jpg",}]
categories:
  - App Reviews
  - News
tags:
  - anonymity
  - privacy
  - surveillance
  - tor
  - tor project
---
After much too long, we’ve got a new build of Orbot out, and it is… a stable beta! Nothing radically new here, just many small changes to continue to improve the experience of our hundreds of thousands of active users out in the world. There will likely be one or two more “beta” releases to iron out small issues in v12, but for now, this one is good to go.

[<img alt="mightyorbot" src="https://guardianproject.info/wp-content/uploads/2013/07/mightyorbot-225x300.jpg" width="225" height="300" />  
](https://guardianproject.info/wp-content/uploads/2013/07/mightyorbot.jpg) _a very might orbot_

The really exciting aspect of this release is that we have ironed out some integration points with other apps, like our own Gibberbot, and third-party apps like DuckDuckGo. These apps can now tell if Orbot is installed, running, and if not, request it to start up. Once Orbot is started, it will return to the calling app, and let them know they can proceed with routing their traffic over Tor. We hope that through use of our [OrbotHelper utility](https://github.com/guardianproject/OnionKit/blob/master/libonionkit/src/info/guardianproject/onionkit/ui/OrbotHelper.java) (part of the [OnionKit/NetCipher library](https://github.com/guardianproject/OnionKit)), many more apps will choose to provide their users with better anonymity and privacy of their network traffic.

<span style="font-size: 13px;">Since we haven’t done a release in awhile, and we have some new build </span><span style="font-size: 13px;">tools, I mostly want to make sure I have not done something terribly </span><span style="font-size: 13px;">wrong in the build process. Please confirm back if you are able to </span><span style="font-size: 13px;">successfully use this release. You can report issues <a href="https://dev.guardianproject.info/projects/orbot/issues/new">on our bug tracker</a>.</span>

We’ve switched versioning styles to a simpler major.minor.bugfix “semantic” model, so this is now Orbot 12.0.1.

Signed 12.0.1 beta release build is here:  
<https://rink.hockeyapp.net/apps/92ace552aa5344d1a802decb71525897/>

Direct APK is here: <https://guardianproject.info/releases/Orbot-release-12.0.1-beta-1.apk> ([gpg sig](https://guardianproject.info/releases/Orbot-release-12.0.1-beta-1.apk.asc))

We also have automated “nightly” debug builds from the development branch:  
<https://guardianproject.info/builds/Orbot/>

Updates in 12.0.1:

  * <span style="font-size: 13px;">updated to Tor 0.2.4.15-RC</span>
  * <span style="font-size: 13px;">flashy screen bug fixed</span>
  * <span style="font-size: 13px;">now shows traffic stats in notification area</span>
  * <span style="font-size: 13px;">better handling of preference settings changes</span>
  * <span style="font-size: 13px;">added superuser permission for Cyanogen</span>
  * better support for “start” Intent, integration with other apps

Tagged source is here:  
<https://gitweb.torproject.org/n8fr8/orbot.git/log/refs/tags/12.0.1>