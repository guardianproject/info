---
id: 49
title: 'Orbot: Initial Release (repost)'
date: 2010-02-10T20:26:23-04:00
author: n8fr8
layout: post
guid: http://guardianproject.info/?p=49
permalink: /2010/02/10/orbot-initial-release-repost/
image: http://guardianproject.info/wp-content/uploads/2010/02/apple-touch-icon-256-150x150.png
categories:
  - News
---
_This was originally posted in October 2009._

I’d like to make this post without much fanfare. Just looking to share information on the work I’ve been doing with the fantastically radical team over at the [Tor Project](http://torproject.org), as part of my work on the [Guardian Project](http://openideals.com/guardian). We have successfully ported the native C Tor app to Android and built an Android application bundle that installs, runs and provides the glue needed to make it useful to end users…. secure, anonymous access to the web via Tor on Android is now a reality. (_Update: Tor doesn’t magically encrypt all of your Internet activities, though. You should [understand what Tor does and does not do for you](https://www.torproject.org/download.html.en#Warning)._)

However, there is still much work to be done… read on!

1) **Tor 0.2.2.5-alpha release** contains all the necessary code for building the Tor binary exe using the Android C SDK. I utilized <a href="http://github.com/tmurakam/droid-wrapper" target="_blank">http://github.com/tmurakam/droid-wrapper</a> toolchain wrapper scripts to make life easier. This will produce the output Tor exe that can run on Android w/o needing root.

_Update: Thanks to [Jake](http://www.appelbaum.net/), you can now read the updated [Orbot BUILD doc](https://svn.torproject.org/svn/projects/android/trunk/Orbot/BUILD) for the step by step build how to._

[![](http://farm4.static.flickr.com/3510/3933276410_275a88c115_d.jpg)](http://www.flickr.com/photos/ioerror/3933276410/)  
_(thanks to [ioerror](http://www.flickr.com/photos/ioerror) for the pic)_

At this point, we are pretty convinced that the performance and efficiency of the C binary is quite significantly better than the Java-based ports of Tor running within Dalvik… this translate to a better experience for the user, with no noticeable increase in battery drain or lag on the rest of the device while Tor is running in the background.

2) **Orbot** – this is the new Android app which bundles the Tor binary, handles its proper installation on the device and then provides a gui for starting/stopping, view the log and torrc, etc. It also provides a built-in HTTP Proxy and is licensed under the [Tor license](https://www.torproject.org/eff/tor-legal-faq.html).

[<img src="http://farm3.static.flickr.com/2588/4034052788_cff2aaf55c_m.jpg" alt="home.jpg" width="161" height="240" />](http://www.flickr.com/photos/natty/4034052788/ "home.jpg by nathanialfreitas, on Flickr")[<img src="http://farm3.static.flickr.com/2503/4033299037_49517e87b7_m.jpg" alt="tor-on.jpg" width="161" height="240" />](http://www.flickr.com/photos/natty/4033299037/ "tor-on.jpg by nathanialfreitas, on Flickr")[<img src="http://farm3.static.flickr.com/2484/4034052826_e326c056fc_m.jpg" alt="log.jpg" width="161" height="240" />](http://www.flickr.com/photos/natty/4034052826/ "log.jpg by nathanialfreitas, on Flickr")  
__

_Just to be clear – we aren’t using the NDK or a shared library… we are actually extracting a binary and managing it via Runtime.getRuntime().exec() calls. This is 100% supported – who knew?! More info on how to do this [here](http://remotedroid.net/blog/2009/04/13/running-native-code-in-android/)  
_ 

The first code is up here… all is working, but def needs much polish:  
<a href="https://svn.torproject.org/svn/projects/android/trunk/Orbot/" target="_blank">https://svn.torproject.org/svn/projects/android/trunk/Orbot/</a>

This post is in part a call for developers to contribute to the continued development of Orbot, so we can get it to a 1.0 state. The other big task is to modify the open-source, privacy focused [Shadow browser](http://www.cl.cam.ac.uk/research/dtg/android/tor/), from the University of Cambridge DTG group, in order to make it work with our HTTP proxy. That would be a really great step forward, as right now, we have to ask users to set their global APN (read: <a href="https://svn.torproject.org/svn/projects/android/trunk/Orbot/INSTALL" target="_blank">https://svn.torproject.org/svn/projects/android/trunk/Orbot/INSTALL</a>)

Thanks for everyone’s help and support to get here. I’d like to keep pushing on to a public release via the App Market very soon. Let me know if you’d like to contribute in any way – code, screen designs, icons, testing….  ****

**Domo arigato, Mr. Orbot-o!**!