---
id: 2041
title: Orbot Your Twitter!
date: 2012-05-02T17:19:27-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=2041
permalink: /2012/05/02/orbot-your-twitter/
categories:
  - App Reviews
  - HowTo
---
In some ways, Twitter is the perfect application to run over the [Tor network](https://torproject.org). It works with small bits of data, it is asynchronous, works naturally in a “store and forward” queue model, and in general, has a decent amount of [default security built-in](http://twitter.com/about/security) through HTTP/S support and OAuth. Compared to the problem-child of the open web, which often involves large websites, streaming video, flash embeds, and malicious javascript, Twitter is a nearly perfect candidate for use over a secure, anonymous (but sometimes high latency) network. Add to the fact that Twitter is often [blocked or monitored in many countries](http://en.wikipedia.org/wiki/List_of_websites_blocked_in_the_People's_Republic_of_China)who do not care for free speech and human rights, and it becomes almost a necessity that you use it with a service like Tor.

> **WARNING AND DISCLAIMER: Twitter for Android is proprietary, closed-source software. Details of the implementation of proxy support have not been publicly disclosed or audited by a third-party at this time. In particular, resolution of hostnames via DNS may not be properly routed through Tor (this is a common issue with proxied software). In addition, through other permissions that Twitter for Android may have you on your device, there may be a strong ability to correlate identity between your registered Google Account and your activities on Twitter.**

Until recently, in order to run [Twitter for Android](https://play.google.com/store/apps/details?id=com.twitter.android&hl=en) through Tor for Android, aka [Orbot](https://guardianproject.info/apps/orbot/), you would need to [root your device](http://shortfuse.org/?page_id=2), or deal with complex proxy settings. However, as of last week, Twitter became _one of the first and only major apps (aka 100M+ installs!)_ to [add direct proxy support into their app](http://twitter.com/#!/moxie/status/195622774348324864), in a very easy to find and activate way.

_**UPDATE June 13, 2012: After a recent audit, we now recommend turning off the “Sync Data” option through Twitter’s Settings menu, under your registered Twitter account. This will stop push notifications from being sent, which are currently not handled by Orbot/Tor.**_

  1. Install and activate Orbot, open Twitter, tap the gear icon on the home screen.
  2. Check the “proxy” box, enter ‘localhost’ and ‘8118’.
  3. Open your account settings, and disable the “Sync Data” option to stop push notifications which cannot be proxied through Orbot/Tor.

See the screenshots below for a full walkthrough, and please spread the word to those in need.

<div id='gallery-7' class='gallery galleryid-2041 gallery-columns-3 gallery-size-thumbnail'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-165201.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-165201-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2047" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2047'>
      Orbot and Twitter now work together easily, thanks to new simple proxy settings feature in Twitter for Android
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164620.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164620-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2042" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2042'>
      When you setup Orbot, your device does not need root or “superuser” access in order to work with Twitter, or with other apps like Gibberbot (Chat) or ORWeb (safe web access)
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164656.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164656-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2043" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2043'>
      Orbot by default provides an HTTP proxy server on “localhost” and port 8118
    </dd>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164743.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164743-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2044" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2044'>
      In the Twitter app account sign in screen, click the small gear icon to open proxy settings
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164753.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164753-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2045" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2045'>
      Enable the proxy, set Proxy Host to ‘localhost’ and Proxy Port to ‘8118’
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164807.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-164807-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2046" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2046'>
      You can also modify Proxy settings in the app via Menu->Settings
    </dd>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170011.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170011-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2054" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2054'>
      You can use the app just the same as before, but now through Tor!
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170043.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170043-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2055" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2055'>
      With searches, you may need to try a few times for them to go through
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170118.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2012/05/device-2012-05-02-170118-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-7-2056" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-7-2056'>
      #OrbotYourTwitter!
    </dd>
  </dl>
  
  <br style="clear: both" />
</div>

 

Learn more and install apps

  * Twitter for Android: [Google Play](https://play.google.com/store/apps/details?id=com.twitter.android&hl=en)
  * Orbot: Tor for Android: [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android&) or [direct download via TorProject.org](https://www.torproject.org/docs/android.html.en)
  * Learn more about [how Tor works](https://www.torproject.org/about/overview.html.en) or just watch the video below!