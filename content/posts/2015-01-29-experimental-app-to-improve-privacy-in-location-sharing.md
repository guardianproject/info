---
id: 12831
title: Experimental app to improve privacy in location sharing
date: 2015-01-29T07:36:58-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12831
permalink: /2015/01/29/experimental-app-to-improve-privacy-in-location-sharing/
spacious_page_layout:
  - default_layout
categories:
  - News
tags:
  - android
  - anonymity
  - geo
  - geouri
  - location
  - metadata
  - panic
  - preview
  - privacy
  - prototype
---
[<img src="https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web-300x300.png" alt="ic_launcher-web" width="300" height="300" class="alignright size-medium wp-image-12835" srcset="https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web-300x300.png 300w, https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web-270x270.png 270w, https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web-230x230.png 230w, https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web.png 512w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2015/01/ic_launcher-web.png)As part of the T2 Panic effort, I&#8217;ve recently been diving deep into the issues of sharing location. It is unfortunately looking really bad, with many services, including Google, frequently sharing location as plain text over the network. I&#8217;ve started to write up some of the issues [on this blog](/tag/panic).

As part of this, I&#8217;ve put together an experimental Android app that aims to act as a privacy filter for all ways of sharing location. Mostly, that means it accepts all sorts of URLs from location services, and tries to parse the location from the URL, then rewrites it into a <a href="http://geouri.org" target="_blank"><code>geo:</code> URI</a>, which is the standard way to share location in Android (and hopefully soon all others). As of ChatSecure v14.1.0, these `geo:` URLs are also clickable.

Many URLs are not parsable, like `http://goo.gl/maps/Cji0V`. LocationPrivacy then goes online and to try to fetch the location. This should happen over Tor, but it does not yet. You have been warned! Otherwise, it changes the URL to `HTTPS` on services that support it.

You can get LocationPrivacy from all the usual channels, including on FDroid in the Guardian Project repo:  
<a href="https://f-droid.org" target="_blank">https://f-droid.org</a>  
<a href="https://guardianproject.info/fdroid" target="_blank">https://guardianproject.info/fdroid</a>

Or from Google Play:  
<a href="https://play.google.com/store/apps/details?id=info.guardianproject.locationprivacy" target="_blank">https://play.google.com/store/apps/details?id=info.guardianproject.locationprivacy</a>

Source code:  
<a href="https://github.com/guardianproject/LocationPrivacy" target="_blank">https://github.com/guardianproject/LocationPrivacy</a>

Report issues here:  
<a href="https://dev.guardianproject.info/projects/panic/issues" target="_blank">https://dev.guardianproject.info/projects/panic/issues</a>

Please do not rely on this app for strong privacy, it is still very much a new, beta app.