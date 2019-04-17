---
id: 12514
title: Recent news on Orweb flaws
date: 2014-06-30T12:43:51-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=12514
permalink: /2014/06/30/recent-news-on-orweb-flaws/
categories:
  - privacy
  - Research
---
**August 2014: New browser development news here, including Orfox, our Firefox-based browser solution: <https://lists.mayfirst.org/pipermail/guardian-dev/2014-August/003717.html>**

 

On Saturday, a new post was relased by Xordern entitled [IP Leakage of Mobile Tor Browsers](http://xordern.net/ip-leakage-of-mobile-tor-browsers.html). As the title says, the post documents flaws in mobile browser apps, such as [Orweb](/apps/orweb) and [Onion Browser](https://mike.tig.as/onionbrowser/), both which automatically route communication traffic over Tor. While we appreciate the care the author has taken, he does make the mistake of using the term “security” to lump together the need for total anonymity up with the needs of anti-censorship, anti-surveillance, circumvention and local device privacy. We do understand the seriousness of this bug, but at the same time, it is not an issue encountered regularly in the wild.

Here are thoughts on the three specific issues covered:

1) HTML5 Multimedia: This is a [known issue](https://guardianproject.info/2013/08/21/orweb-security-advisory-possible-ip-leakage-with-html5-videoaudio/) which is not present on 100% of Android devices, but is definitely something to be concerned about, if you access sites with HTML5 media player content on them. To us, it is a bug in Android, and not in Orweb, since all of the appropriate APIs are called when the browser is configured to proxy. However, it is a problem, and our solution remains to either use transparent proxying feature of Orbot, or to use the Firefix Privacy configuration we provide here: <https://guardianproject.info/apps/firefoxprivacy>

2) Downloads leak: This is a new issue and one we are trying to reproduce on our end. If our proxied download indeed is not working, we will issue a fix shortly. Again, using Firefox configured in the manner we prescribe, the downloads would be proxied properly.

3) Unique Headers: The inclusion of a unique HTTP header issue in this list is confusing, because it has nothing to do with IP leakage. We have never claimed that a mobile browser can be 100% anonymous, and defending against full fingerprinting of browsers based on headers is something beyond what we are attempting to do at this point.

At this point, we still recommend [Orweb](/apps/orweb) for most people who want a very simple solution for a browser that is proxied through Tor. This will defeat mass traffic surveillance, network censorship, filtering by your mobile operator, work or school, and more. Orweb also keeps little data cached on the local system, and so protects against physical inspection and analysis of your device, to retrieve your browser history. HOWEVER if you do seem to visit sites that have HTML5 media players in the them, then we recommend you do not use Orweb, and again, that you use [Firefox with our Privacy-Enhanced Configuration](https://guardianproject.info/apps/firefoxprivacy).

If you are truly worried about IP leakage, then you MUST root your phone, and use Orbot’s Transparent Proxying feature. This provides the best defense against leaking of your real IP. Even further, if you require even more assurance than that, you should follow Mike Perry’s [Android Hardening Guide](https://blog.torproject.org/blog/mission-impossible-hardening-android-security-and-privacy), which uses AFWall firewall in combination with Orbot, to block traffic to apps, and even stops Google Play from updating apps without your permission.

Finally, the best news is that we are making great progress in a fully privacy-by-default version of Firefox, under the project named “Orfox”. This is being done in partnership with the Tor Project, as a [Google Summer of Code](http://www.google-melange.com/gsoc/proposal/public/google/gsoc2014/amoghbl1/5629499534213120) effort, along with the Orweb team. We aim to use as much of the same code that Tor Browser does to harden Firefox in our browser, and are getting close to an alpha release. If you are interested in a testing the first prototype build, which address the HTML5 and Download leak issues, you can find it here: [https://guardianproject.info/releases/FennecForTor\_GSoC\_prototype.apk](https://guardianproject.info/releases/FennecForTor_GSoC_prototype.apk) and track the project here: <https://github.com/guardianproject/orfox>

 

 

 

 