---
id: 576
title: Proxy Settings Add-on for Firefox Mobile
date: 2010-11-08T03:43:24-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=576
permalink: /2010/11/08/proxy-settings-add-on-for-firefox-mobile/
bigimg: [{src: "https://guardianproject.info/wp-content/uploads/2010/11/fennecoptions.png",}]
categories:
  - Development
  - News
tags:
  - add-on
  - fennec
  - firefox
  - proxy
  - tor
---
The latest beta of [Firefox 4 on Android](http://www.mozilla.com/en-US/mobile/) is proving to be very usable, stable and an increasingly viable alternative to the built-in webkit browser. However, it is unfortunately lacking the ability to manually configure proxy settings through any sort of standard user interface. This is a common problem for Android, which also lacks the ability to set browser or system wide proxy settings. This has caused real issues for us with getting [Orbot](https://guardianproject.info/apps/orbot) (aka “Tor on Android”) to work for un-rooted Android devices, because for routing through Tor to work, you must be able to set the HTTP or SOCKS proxy settings. Why this [very basic feature](http://code.google.com/p/android/issues/detail?id=1273) keeps getting missed or ignored is a mystery to us.

To solve this problem, we at the Guardian Project have created a very simple [Firefox add-on](https://addons.mozilla.org/en-US/firefox/?browse=featured) which exposes the proxy settings through a simple, graphical options menu. This means any user can easily set the HTTP and SOCKS proxy settings for Firefox, enabling access to web browsing on networks which require a proxy to access the we. This also means, that users can connect Firefox to Orbot on Android 2.x devices and [browse the web using the Tor](https://torproject.org).

[<img class="size-full wp-image-579 alignnone" title="fennecoptions" src="https://guardianproject.info/wp-content/uploads/2010/11/fennecoptions.png" alt="" width="792" height="499" srcset="https://guardianproject.info/wp-content/uploads/2010/11/fennecoptions.png 792w, https://guardianproject.info/wp-content/uploads/2010/11/fennecoptions-300x189.png 300w" sizes="(max-width: 792px) 100vw, 792px" />](https://guardianproject.info/wp-content/uploads/2010/11/fennecoptions.png)

**However, it must be stressed that this not a full port of the [TorButton add-on](http://www.torproject.org/torbutton/index.html.en), and does not provide for strong anonymity.**

We are working on porting TorButton to Firefox mobile, so stay tuned for that release. In addition, while there are [many, many Proxy add-ons for Firefox](https://addons.mozilla.org/en-US/firefox/search/?q=proxy&cat=all&lver=any&pid=1&sort=&pp=20&lup=&advanced=) on the desktop, none have been ported to mobile. We hope this small release will encourage one or more of them to port those add-ons to a mobile version. For now though, if you are eager to play and really need to access the web via a proxy, you can find the “ProxyMob” add-on at the following URL. Just navigate to this address from your Firefox mobile browser, and it will handle the add-on installation process:

<http://tinyurl.com/proxymob>  
aka: <https://guardianproject.info/downloads/proxymob-addon-0.0.5.xpi> ([gpg sig](https://guardianproject.info/downloads/proxymob-addon-0.0.5.xpi.asc))

As with all of our work, this is open-source, and we encourage you to contribute to and improve upon what we’ve done via our Github project: <https://github.com/guardianproject/ProxyMob>