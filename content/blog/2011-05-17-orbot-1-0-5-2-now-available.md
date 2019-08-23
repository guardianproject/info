---
id: 1107
title: Orbot 1.0.5.2 now available
date: 2011-05-17T19:43:30-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=1107
permalink: /2011/05/17/orbot-1-0-5-2-now-available/
categories:
  - New Release
---
Our flagship app, [Orbot: Tor on Android](/apps/orbot), has been updated to version 1.0.5.2. It is available in the [Android Market](https://market.android.com/details?id=org.torproject.android&feature=search_result), or through direct download from the [Tor Project’s website](https://www.torproject.org/docs/android.html.en).

This release fixes a number of long standing bigs, includes the latest and greatest release of Tor itself, cleans up the user interface a bit, and adds some new advanced options (you can specify your exit node country!). It also fixes an issue with our “Tor Everything” capability, that allowed some Android system network traffic to leak and bypass the Tor routing. Finally, it provides for compatibility for [CyanogenMOD 7](https://code.google.com/p/cyanogenmod/issues/detail?id=1120), as well as Android Gingerbread and Honeycomb.

Enjoy and stay safe out there!

CHANGELOG

1.0.5.1/.2  
– small updates to layout of main screen to fit smaller screens  
– fixed preference setting of EntryNode torrc value

1.0.5  
– added exit node and “StrictExitNode” preference  
– fixed tor binary installation issue related to max resource size and compression  
– updated “start on boot” code to test for proper launch event  
– updated to Tor 0.2.2.25-alpha binary  
– moved back to single notification bar id to avoid double entries  
– cleaned up progress dialog and alert handling to avoid leaky windows  
– Merged __sporkbomb’s patch for how transproxy all works; now does “everything but Tor”  
– Added new toolbar notifications and alerts for displaying notifications and Tor messages  
– Removed unused Socks client code from android.net package  
– Updated wizard to show link to Gibberbot (formerly OTRchat) chat app  
– Bundled iptables 1.4.7 for ARM instead of relying on installed version  
– Fixed various issues related to iptables, transproxying for CyanogenMod7/Android 2.3.*  
– Changed how settings changed are processed through the control port (batched instead of one by one)  
– Stopped app by app flushing of iptables rules, in favor of complete flush of ‘nat’ and ‘filter’ type  
– removed useless log screen (logs can be viewed/retrieved using ‘alogcat’ 3rd party app)