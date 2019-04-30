---
id: 617
title: 'Firefox Mobile: Privacy Enhanced'
date: 2010-11-15T13:48:35-04:00
author: n8fr8
layout: page
guid: http://guardianproject.info/
spacious_page_layout:
  - default_layout
publish_to_discourse:
  - "1"
has_been_saved:
  - "1"
publish_post_category:
  - "5"
discourse_post_id:
  - "449"
discourse_permalink:
  - https://talk.developersquare.net/t/firefox-mobile-privacy-enhanced/323
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":323,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1552062211"
wpdc_sync_post_comments:
  - "0"
menu:
  main:
    parent: archive
aliases:
  - apps/firefoxprivacy
---
<!--:-->

<!--:en-->

### 

**Fall 2016: We no longer promote the user of Firefox with add-ons, as the solution can be insecure still and easily misconfigured.**

Please use our new [Orfox browser for Android](https://guardianproject.info/apps/orfox/), based on Tor Browser.

* * *

&nbsp;

<!--:de-->The latest releases of 

[Firefox on Android](http://www.mozilla.com/en-US/mobile/) are proving to be very usable, stable and an increasingly viable alternative to the built-in webkit browser. However, it unfortunately lacks the ability to manually configure proxy settings through any sort of standard user interface. This is a common problem for Android, which also lacks the ability to set browser or system-wide proxy settings. To solve this problem, we have created a very simple Firefox add-on [Proxy Mobile](https://addons.mozilla.org/en-US/firefox/?browse=featured) that exposes the Firefox browser&#8217;s proxy settings through a simple, graphical options menu.

[<img class="alignleft" src="https://guardianproject.info/wp-content/uploads/2010/11/proxymob-180x300.png" alt="proxymob" width="126" height="211" />](https://guardianproject.info/wp-content/uploads/2010/11/proxymob.png)

This means any user can easily set the HTTP and SOCKS proxy settings for Firefox, enabling access to web browsing on networks which require a proxy to access the web. This also means that users can connect Firefox to Orbot on Android devices and browse the web using the [Tor network ](https://torproject.org)or any other HTTP or SOCKS proxy.

### <span style="color: #aa0000;">Simply proxying through Tor is not the same as the full <a href="https://www.torproject.org/projects/torbrowser.html.en">TorBrowser feature set</a>, and does not provide any strong anonymity protections against directed attacks. </span>

&nbsp;

That said, there are many things you can do to configure Firefox for Android to be more privacy-preserving and secure.

First, you will need to get Firefox for Android:

  * **<a href="https://play.google.com/store/apps/details?id=org.mozilla.firefox" rel="nofollow">Install Firefox from the Google Play Store</a>**
  * or go to **<a href="http://firefox.com/m" rel="nofollow">firefox.com/m</a>** in your phone&#8217;s web browser.
  * or download the Firefox APK file **<a href="https://ftp.mozilla.org/pub/mozilla.org/mobile/releases/latest/android/multi/" rel="nofollow">directly from the Mozilla FTP server</a>**.

Then follow the 10 steps below to enhance your mobile web privacy!

  1. Use [Mobile Private Browsing](https://support.mozilla.org/en-US/kb/mobile-private-browsing-browse-web-without-saving-syncing-info) which &#8220;**allows you to browse the internet without saving any information about which sites and pages you&#8217;ve visited&#8221;.** Learn more in this [detailed article](https://support.mozilla.org/en-US/kb/mobile-private-browsing-browse-web-without-saving-syncing-info).
  2. Use the [Phony Add-on](https://addons.mozilla.org/en-US/android/addon/phony/?src=hp-dl-featured) to change your user-agent, to impersonate a different mobile device or browser. [INSTALL ADD-ON](https://addons.mozilla.org/en-US/android/addon/phony/?src=hp-dl-featured)
  3. Use the [Clean Quit Add-on](https://addons.mozilla.org/en-US/android/addon/cleanquit/) to ensure your browsing history, cookies and other data are deleted when you want them to be. [INSTALL ADD-ON](https://addons.mozilla.org/en-US/android/addon/cleanquit/)
  4. Use the [Self-Destructing Cookies Add-on](https://addons.mozilla.org/en-US/android/addon/self-destructing-cookies/) to only keep cookies around as long as you need them. [INSTALL ADD-ON](https://addons.mozilla.org/en-US/android/addon/self-destructing-cookies/)
  5. In Firefox Settings, set &#8220;Plugins&#8221; to &#8220;Disabled&#8221; under the Content section.
  6. Under &#8220;Privacy & Security&#8221;, set Cookies to &#8220;Enabled, excluding 3rd Party&#8221;
  7. Also under &#8220;Privacy & Security&#8221;, set Tracking to &#8220;Tell sites that I do not want to be tracked&#8221;.
  8. If you want the browser to remember your passwords, make sure to &#8220;Use master password&#8221; to secure them.
  9. Switch your search engine to [DuckDuckGo](https://addons.mozilla.org/en-us/firefox/addon/duckduckgo-for-firefox/) (a search engine that does not track) using their SSL mode search add-on. [INSTALL ADD-ON](https://addons.mozilla.org/en-us/firefox/addon/duckduckgo-for-firefox/)
 10. Obviously, if you haven&#8217;t done so, already, install ProxyMob to proxy your traffic through Tor, protecting it from logging, interception and targeting. [INSTALL ADD-ON](https://guardianproject.info/downloads/proxymob.xpi). It requires that Tor is already running, so make sure to get [Orbot: Tor for Android](/apps/orbot) and turn it on. ProxyMob will have all of the settings configured automagically. To test that it&#8217;s working, goto <a href="http://check.torproject.org/" target="_blank">check.torproject.org</a> and look for the congratulations message saying that it&#8217;s configured properly.

[<img class="alignleft" src="https://guardianproject.info/wp-content/uploads/2010/11/privatebrowsing-180x300.png" alt="privatebrowsing" width="126" height="210" />](https://guardianproject.info/wp-content/uploads/2010/11/privatebrowsing.png)  [<img class="alignleft" src="https://guardianproject.info/wp-content/uploads/2010/11/phony-180x300.png" alt="phony" width="126" height="210" />](https://guardianproject.info/wp-content/uploads/2010/11/phony.png) <img class="wp-image-11589 alignleft" src="https://guardianproject.info/wp-content/uploads/2010/11/selfdestructingcookies-180x300.png" alt="selfdestructingcookies" width="126" height="210" srcset="https://guardianproject.info/wp-content/uploads/2010/11/selfdestructingcookies-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/11/selfdestructingcookies-614x1024.png 614w, https://guardianproject.info/wp-content/uploads/2010/11/selfdestructingcookies.png 768w" sizes="(max-width: 126px) 100vw, 126px" />[<img class="alignleft" src="https://guardianproject.info/wp-content/uploads/2010/11/duckduckgo-180x300.png" alt="duckduckgo" width="126" height="210" />](https://guardianproject.info/wp-content/uploads/2010/11/duckduckgo.png)[<img class="alignleft" src="https://guardianproject.info/wp-content/uploads/2010/11/cleanquit-180x300.png" alt="cleanquit" width="126" height="210" />](https://guardianproject.info/wp-content/uploads/2010/11/cleanquit.png)

&nbsp;

### How to Contribute {.alignnone}

As with all of our work, this is open-source, and we encourage you to contribute to and improve upon what we&#8217;ve done via our Github project: <https://github.com/guardianproject/ProxyMob>

&nbsp;

&nbsp;

&nbsp;

&nbsp;