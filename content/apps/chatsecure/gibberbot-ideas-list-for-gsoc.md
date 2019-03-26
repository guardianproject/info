---
id: 3412
title: Gibberbot Ideas list for GSoC
date: 2013-03-29T14:50:39-04:00
author: n8fr8
layout: page
guid: https://guardianproject.info/?page_id=3412
---
Here are the list of ideas open for Gibberbot work through the Google Summer of Code program.

You can find the full Gibberbot project tracker here: <https://dev.guardianproject.info/projects/gibberbot/issues>

  1. **OTR based file sharing**: Using the symmetric key sharing feature of OTRv3, we want to implement a file sharing mechanism between clients that tunnels inside of OTR. This would allow file sharing of audio, photo, video and any other file, within any established OTR channel, both securing the content and obfuscating the traffic.
  2. **Tor based file sharing**: For Gibberbot clients with Tor, we want to add Tor Hidden Service based file sharing. Hidden Service support is available in Orbot already, and Gibberbot can take advantage of this.
  3. **User interface overhaul**: While we have kept Gibberbot fairly up to date, we need to move to a full swipe, card and &#8220;Roboto&#8221; style modern interface to keep up with the latest looks from Google&#8217;s and other apps. We really are hoping for some great innovation here that keeps are app clean and light, while also making the user want to show it off to others.
  4. **Voice Plugin**: Building off of CSipSimple and our Open Secure Telephony Network back-end, we want to add a seameless &#8220;Call&#8221; feature between Gibberbot clients that establishes a secure ZRTP encrypted voice conversation without having to dial any phone numbers.