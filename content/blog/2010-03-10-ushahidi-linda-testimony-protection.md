---
id: 215
title: 'Ushahidi-Linda: “Testimony” + “Protection”'
date: 2010-03-10T19:53:00-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=215
permalink: /2010/03/10/ushahidi-linda-testimony-protection/
categories:
  - Development
tags:
  - crisis mapping
  - prototype
  - ushahidi
---
Ushahidi-linda (“Testimony” + “Protection” – _disclaimer: we don’t speak Swahili so this was a shot in the dark!_)

This is a fork of the [Ushahidi on Android](https://github.com/ushahidi/Ushahidi_Android) app, done as a way to prototype the implementation of increased security, anonymity and privacy for users viewing and submitting reports through [Ushahidi](http://ushahidi.com).

[<img class="size-full wp-image-199 alignleft" title="ushahidi_android_splash" src="https://guardianproject.info/wp-content/uploads/2010/03/ushahidi_android_splash.png" alt="" width="224" height="336" srcset="https://guardianproject.info/wp-content/uploads/2010/03/ushahidi_android_splash.png 320w, https://guardianproject.info/wp-content/uploads/2010/03/ushahidi_android_splash-200x300.png 200w" sizes="(max-width: 224px) 100vw, 224px" />](https://guardianproject.info/wp-content/uploads/2010/03/ushahidi_android_splash.png)

Ushahidi is a platform that crowdsources crisis information, allowing anyone to submit crisis information through text messaging using a mobile phone, email or web form.

The network code for the Ushahidi app has been tied into [Orbot](/apps/orbot) (Tor on Android) using a SOCKS5 client. This does NOT require a rooted device to work – both it and Orbot can be run on stock, off the shelf Android devices on any mobile operator that offers at least a GPRS connection. This version of the app will ONLY work if Orbot is activated and connected to the Tor Network. Otherwise, network connections will fail.

We plan/hope to work with the Ushahidi team to integrate this functionality into the main branch of code, and offer a clear, easy way for users to activate/deactivate use of the anonymity/anti-surveillence features.

You can access the complete source code for Ushahidi-Linda on Android via our [Git repository](https://github.com/guardianproject/Ushahidi_Android) and also [download test builds](https://github.com/guardianproject/Ushahidi_Android/downloads) as they are available. **PLEASE NOTE: Until further notice and formal announcements, these builds should be considered ALPHA and are for testing, proof of concept use only.**

Specifically you can see how we have provided a new [SocksHTTPClient package](https://github.com/guardianproject/Ushahidi_Android/tree/master/src/info/guardianproject/net/) that proxies all GET and POST connections through SOCKS.

From here, the plan is to implement a security pin on startup, local data encryption for storage of data both in the database and on the sdcard, as well as quick “delete all” features.

_Learn more about the Tor Project and how network anonymity works at_ [_https://www.torproject.org_](https://www.torproject.org)