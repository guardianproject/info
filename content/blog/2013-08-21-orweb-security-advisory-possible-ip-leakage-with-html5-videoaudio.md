---
id: 11559
title: 'Orweb Security Advisory: Possible IP leakage with HTML5 video/audio'
date: 2013-08-21T16:15:36-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=11559
permalink: /2013/08/21/orweb-security-advisory-possible-ip-leakage-with-html5-videoaudio/
bigimg: [{src: "https://guardianproject.info/wp-content/uploads/2010/03/orweb.png",}]
categories:
  - Advisory
tags:
  - orbot
  - orweb
  - tor
---
The [Orweb browser app](/apps/orweb) is vulnerable to [leak the actual IP of the device](https://dev.guardianproject.info/issues/1754) it is on, if it loads a page with HTML5 video or audio tags on them, and those tags are set to auto-start or display a poster frame. On some versions of Android, the video and audio player start/load events happen without the user requesting anything, and the request to the URL for the media src or through image poster is made outside of the proxy settings.

The Android WebView component upon which Orweb is built, does not [pass on the proxy settings](https://github.com/guardianproject/OnionKit/blob/master/libonionkit/src/info/guardianproject/onionkit/web/WebkitProxy.java) for the web page to embedded media players it displays. Additionally, even though the [proper API calls are made](http://developer.android.com/reference/android/webkit/WebSettings.PluginState.html) to turn off all plugins, apparently HTML5 video and audio players not considered plugins, and there is no way to disable them at an API level.

We are currently working to determine which versions of Android these issues occur on. We have a fix implemented that filters all video and audio tag instances out of retrieved content, and on newer versions of Android, that requires a user gesture/tap before media players are loaded.

We expect to have a fix out in the next 24 to 48 hours. In the meantime, if you are using Orweb with the goal of strong anonymity, and not just circumvention or proxying, we advise you to avoid all sites that may include HTML5 video or audio content embedded in the pages, or to just stop using the app all together. Alternatively, you can use [Firefox for Android](https://www.mozilla.org/en-US/mobile/) with the [Proxy Mobile](https://guardianproject.info/apps/proxymob-firefox-add-on/) add-on (load this XPI within Firefox: https://guardianproject.info/releases/proxymob-latest.xpi)

_This does NOT affect users who use the root mode with transparent proxying, as that handles proxying the entire traffic of the entire device or a particular app._