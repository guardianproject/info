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
Our flagship app, [Orbot: Tor on Android](/apps/orbot), has been updated to version 1.0.5.2. It is available in the [Android Market](https://market.android.com/details?id=org.torproject.android&feature=search_result), or through direct download from the [Tor Project&#8217;s website](https://www.torproject.org/docs/android.html.en).

This release fixes a number of long standing bigs, includes the latest and greatest release of Tor itself, cleans up the user interface a bit, and adds some new advanced options (you can specify your exit node country!). It also fixes an issue with our &#8220;Tor Everything&#8221; capability, that allowed some Android system network traffic to leak and bypass the Tor routing. Finally, it provides for compatibility for [CyanogenMOD 7](http://code.google.com/p/cyanogenmod/issues/detail?id=1120), as well as Android Gingerbread and Honeycomb.

Enjoy and stay safe out there!

CHANGELOG

1.0.5.1/.2  
&#8211; small updates to layout of main screen to fit smaller screens  
&#8211; fixed preference setting of EntryNode torrc value

1.0.5  
&#8211; added exit node and &#8220;StrictExitNode&#8221; preference  
&#8211; fixed tor binary installation issue related to max resource size and compression  
&#8211; updated &#8220;start on boot&#8221; code to test for proper launch event  
&#8211; updated to Tor 0.2.2.25-alpha binary  
&#8211; moved back to single notification bar id to avoid double entries  
&#8211; cleaned up progress dialog and alert handling to avoid leaky windows  
&#8211; Merged __sporkbomb&#8217;s patch for how transproxy all works; now does &#8220;everything but Tor&#8221;  
&#8211; Added new toolbar notifications and alerts for displaying notifications and Tor messages  
&#8211; Removed unused Socks client code from android.net package  
&#8211; Updated wizard to show link to Gibberbot (formerly OTRchat) chat app  
&#8211; Bundled iptables 1.4.7 for ARM instead of relying on installed version  
&#8211; Fixed various issues related to iptables, transproxying for CyanogenMod7/Android 2.3.*  
&#8211; Changed how settings changed are processed through the control port (batched instead of one by one)  
&#8211; Stopped app by app flushing of iptables rules, in favor of complete flush of &#8216;nat&#8217; and &#8216;filter&#8217; type  
&#8211; removed useless log screen (logs can be viewed/retrieved using &#8216;alogcat&#8217; 3rd party app)