---
id: 2338
title: Auditing Twitter With Orbot
date: 2012-06-13T20:31:57-04:00
author: patch
layout: post
guid: https://guardianproject.info/?p=2338
permalink: /2012/06/13/auditing-twitter-with-orbot/
image: http://guardianproject.info/wp-content/uploads/2012/06/twitterSYNC3.png
categories:
  - News
---
Twitter&#8217;s new Android application provides a proxy option that supports Orbot. It is a great way to access Twitter, particularly if Twitter is blocked. Check out the [Orbot Your Twitter](https://guardianproject.info/2012/05/02/orbot-your-twitter/) blog post! That post explains how to set up Orbot with Twitter, however, it came with an important disclaimer:

> **WARNING AND DISCLAIMER: Twitter for Android is proprietary, closed-source software. Details of the implementation of proxy support have not been publicly disclosed or audited by a third-party at this time. In particular, resolution of hostnames via DNS may not be properly routed through Tor (this is a common issue with proxied software). In addition, through other permissions that Twitter for Android may have you on your device, there may be a strong ability to correlate identity between your registered Google Account and your activities on Twitter.**

****I decided to take on the challenge of auditing Twitter+Orbot to gain more insight (and hopefully trust) into their new support for proxying. I logged some traffic on my Nexus One using the proxied Twitter application to see what was going on. To eliminate excess traffic I used Droidwall to permit only traffic from Orbot and Twitter. This still allows the Twitter application the option to leak data while blocking other traffic we don&#8217;t wish to see.  I began logging with Orbot off and attempted to update my Twitter application. So far so good, it was not able to retrieve any tweets. Once Orbot was running the application worked great, I ran some searches and made a test tweet. Looking at the traffic, my phone contacted 3 IP addresses:

  * 83.241.211.6
  * 199.58.86.196
  * 149.9.0.60

[Tor Metrics](https://metrics.torproject.org/) has a handy tool called [ExoneraTor](https://metrics.torproject.org/exonerator.html) that confirmed that these addressed were indeed relays in the Tor network at the time of 2012-06-13 12:00.  One slightly concerning thing is that Twitter notifications will still show up when Twitter is proxied but Orbot is off! I logged more traffic this time not using Droidwall and making sure to trigger Twitter notifications with Orbot on and off.

<p style="text-align: center;">
  <a href="https://guardianproject.info/wp-content/uploads/2012/06/twitterSYNC3.png"><img class="size-full wp-image-2345 aligncenter" style="margin-right: 5px; margin-left: 5px; border-style: initial; border-color: initial; border-image: initial; border-width: 0px;" title="twitterSYNC" src="https://guardianproject.info/wp-content/uploads/2012/06/twitterSYNC3.png" alt="" width="583" height="146" srcset="https://guardianproject.info/wp-content/uploads/2012/06/twitterSYNC3.png 583w, https://guardianproject.info/wp-content/uploads/2012/06/twitterSYNC3-300x75.png 300w" sizes="(max-width: 583px) 100vw, 583px" /></a>
</p>

The traffic in green is making some HTTP requests to a Google server, but its not a result of the Twitter App or triggered notifications. The traffic going to and from 173.194.76.188 represents the notifications. A WHOIS reveals this to be encrypted traffic to a Google IP and doesn&#8217;t indicate a user is using Twitter. This is a result of Google&#8217;s Push Notifications and can be easily disabled on an Android phone under &#8216;Accounts & sync&#8217;.

> **If you have  Google account set up with your phone, Google knows your IP address and your Twitter account through the Push Notifications. This should be turned OFF in either the Twitter application settings or &#8216;Accounts & sync&#8217; menu.**

******What does it mean for Twitter+Orbot users?**

  * **Stops Local Traffic Surveillance:** It means that someone looking at your phone traffic will not be able to tell if you are using or accessing Twitter. They will see you accessing the Tor network, receiving push notifications from Google (if enabled), and they will see all your other normal traffic.
  * **Stops Service Logging Surveillance:** Twitter will only see a Tor Exit Node IP address and not be able to log your real IP address. The Tor Exit Node will only see an HTTPS connection to Twitter, and not know where you are connecting from, nor what your Twitter account is.
  * **Defeats Network Filtering: **The Twitter app will be able to connect to the Twitter service through the Tor network, even if it is blocked by the network or country you are connecting from.

Unfortunately, this does **not** mean that what you publish to Twitter is automatically anonymous. For strong anonymity in tweeting, precautions beyond proxying should be taken, such setting up a new email address, using a new Android phone, etc, that go beyond what we can cover here. You can view [Global Voices Guide to Anonymous Blogging](http://advocacy.globalvoicesonline.org/projects/guide/) and the EFF&#8217;s [How to Blog Safely](https://www.eff.org/wp/blog-safely) for a more in depth discussion of this. In short, Twitter+Orbot defeats traffic surveillance and network filtering, but does not automatically provide strong anonymity. No DNS leaks were detected, but if one is trying to maintain a anonymous Twitter account  (i.e. an account not linked to your real identitity or other pseudonym) more precautions need to be taken. The traffic logs of both tests can be downloaded [here](https://guardianproject.info/wp-content/uploads/2012/06/twittertraffic.zip). 10.0.2.64 is the IP of the Nexus One running Twitter and Orbot.

<div id="attachment_2054" style="width: 298px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170011.png"><img aria-describedby="caption-attachment-2054" class=" wp-image-2054  " style="border-image: initial; border-width: 1px; border-color: black; border-style: solid; margin: 1px;" title="Tweet Freely!" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170011.png" alt="" width="288" height="480" srcset="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170011.png 480w, https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170011-180x300.png 180w" sizes="(max-width: 288px) 100vw, 288px" /></a>
  
  <p id="caption-attachment-2054" class="wp-caption-text">
    You can use the app just the same as before, but now through Tor!
  </p>
</div>