---
id: 12999
title: 'Orfox: Aspiring to bring Tor Browser to Android'
date: 2015-06-30T15:32:16-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=12999
permalink: /2015/06/30/orfox-aspiring-to-bring-tor-browser-to-android/
image: http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133152.png
categories:
  - News
  - privacy
  - Research
tags:
  - browser
  - pets2015
  - privacys
  - secure
  - tor
---
**Update 24 September, 2015: Orfox BETA is now on Google Play: <https://play.google.com/store/apps/details?id=info.guardianproject.orfox>**

* * *

 

In the summer of 2014 (<https://lists.mayfirst.org/pipermail/guardian-dev/2014-August/003717.html>{.external}), we announced that the results of work by Amogh Pradeep (<https://github.com/amoghbl1>{.external}), our 2014 Google Summer of Code student, has proven we could build Firefox for Android with some of the settings and configurations from the Tor Browser desktop software. We called this app Orfox, in homage to Orbot and our current Orweb browser. This was a good first step, but we were doing the build on Mozilla’s Firefox code repository, and then retrofitting pieces from Tor Browser’s code, which wasn’t the right way to do things, honestly.

This summer (2015!), with fantastic continued effort by Amogh, we have switched to building the Orfox mobile app directly from the Tor Browser code repository, successfully working through any mobile OS incompatibilities in the security hardening patches added by the Tor Browser team. We also had the additional task of reviewing the Android application code in Firefox, that is not part of Tor Browser, in order to modify and patch it to work inline with the [Tor Browser requirements and design document](https://www.torproject.org/projects/torbrowser/design/).

As of today, we have a stable alpha release ready for testing, and are rapidly moving towards a public beta in a few weeks. Our plan is to actively encourage users to move from Orweb to Orfox, and stop active development of Orweb, even removing to from the Google Play Store. If users really want to continue using a WebView-based solution and do not need all of the capabilities that Orfox/Tor Browser provides, they can use Lightning Browser (<https://github.com/anthonycr/Lightning-Browser>{.external}), a lightweight, open-source app that offers automatic Orbot (SOCKS) proxying on start-up.

Below you will find screenshots and our current set of [Orfox Frequently Asked Questions](https://dev.guardianproject.info/projects/orfox-private-browser/wiki/Orfox_vs_Tor_Browser_FAQ) from the [project wiki](https://dev.guardianproject.info/projects/orfox-private-browser/wiki).

You can access the current Orfox release by installing the [F-Droid app](https://f-droid.org/) and subscribing to our F-Droid Alpha Channel at by clicking on the following link on your phone: [https://dev.guardianproject.info/debug/info.guardianproject.orfox/fdroid/repo  
](https://dev.guardianproject.info/debug/info.guardianproject.orfox/fdroid/repo) 

 

<div id='gallery-11' class='gallery galleryid-12999 gallery-columns-3 gallery-size-medium'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133152.png'><img width="169" height="300" src="http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133152-169x300.png" class="attachment-medium size-medium" alt="" aria-describedby="gallery-11-13003" srcset="https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133152-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133152-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133152.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-11-13003'>
      Recognized as Tor Browser
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133103.png'><img width="169" height="300" src="http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133103-169x300.png" class="attachment-medium size-medium" alt="" aria-describedby="gallery-11-13005" srcset="https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133103-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133103-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133103.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-11-13005'>
      A match made by onions!
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133624.png'><img width="169" height="300" src="http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133624-169x300.png" class="attachment-medium size-medium" alt="" aria-describedby="gallery-11-13000" srcset="https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133624-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133624-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133624.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-11-13000'>
      Bookmark support!
    </dd>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133414.png'><img width="169" height="300" src="http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133414-169x300.png" class="attachment-medium size-medium" alt="" aria-describedby="gallery-11-13001" srcset="https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133414-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133414-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133414.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-11-13001'>
      Easy access to onion sites!
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133223.png'><img width="169" height="300" src="http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133223-169x300.png" class="attachment-medium size-medium" alt="" aria-describedby="gallery-11-13002" srcset="https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133223-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133223-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133223.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-11-13002'>
      Tabs!
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133130.png'><img width="169" height="300" src="http://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133130-169x300.png" class="attachment-medium size-medium" alt="" aria-describedby="gallery-11-13004" srcset="https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133130-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133130-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/06/device-2015-06-30-133130.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-11-13004'>
      Tor-relevant default sites
    </dd>
  </dl>
  
  <br style="clear: both" />
</div>

**Where can I find all the relevant Orfox project pieces?**

  * The Orfox project tracker roadmap is here: <https://dev.guardianproject.info/projects/orfox-private-browser/roadmap>{.external}
  * The Orfox branch of the Tor Browser repository is here: <http://github.com/guardianproject/tor-browser>{.external}
  * The Orfox build project is here: <https://github.com/guardianproject/orfoxfennec>{.external}
  * The primary Tor Browser repository is here: <https://gitweb.torproject.org/tor-browser.git/>{.external}
  * Automated debug builds of Orfox alpha are available via F-Droid here (install F-Droid on your phone, then copy/paste or open the link to add the repo): <https://dev.guardianproject.info/debug/info.guardianproject.orfox/fdroid/repo>{.external}

**How is Orfox different than Tor Browser for desktop?**

Orfox is built from the same source code as Tor Browser (which is built upon Firefox), but with a few minor modifications to the privacy enhancing features to make them compatible with Firefox for Android and the Android operating system. In as many ways as possible, we will adhere to the design goals of Tor Browser (<https://www.torproject.org/projects/torbrowser/design/>{.external}), by supporting as much of their actual code as possible, and extending their work into the additional AF-Droid appndroid components of Firefox for Android.

  * The Orfox code repository is at <https://github.com/guardianproject/tor-browser>{.external} and the Tor Browser repository is here:<https://gitweb.torproject.org/tor-browser.git/>{.external}. The Orfox repository is a fork of the Tor Browser repository with the necessary modification and Android-specific code as patches on top of the Tor Browser work. We will keep our repository in sync with updates and release of Tor Browser.

  * Orfox is built from the Tor Browser repo based on ESR38 (<https://dev.guardianproject.info/issues/5146>{.external}<https://dev.guardianproject.info/news/221>{.external}) and has only two modified patches that were not relevant or necessary for Android

  * Orfox does not currently include the mobile versions of HTTPS Everywhere, No Script and the Tor Browser Button, but these we will be added shortly, now that we have discovered how to properly support automatic installation of extensions on Android (<https://dev.guardianproject.info/issues/5360>{.external})

  * Orfox includes a “Request Mobile Site” option that allows you to change the user-agent from the standard Tor Browser agent to a modified Android specific one: “Mozilla/5.0 (Android; Mobile; rv:31.0) Gecko/20100101 Firefox/31.0”. (<https://dev.guardianproject.info/issues/5404>{.external}). This is useful for being able to see the mobile version of a website, but does reduce the amount your browser blends in with other browsers.

  * Orfox currently allows for users to bookmark sites, and may have additional data written to disk beyond what the core gecko browser component does. We are still auditing all disk write code, and determining how to appropriately disable or harden it. (<https://dev.guardianproject.info/issues/5437>{.external})

  * Orfox cannot yet be built deterministically, but based on work with the FDroid project, we are aiming for this to be possible in the next year (<https://blog.torproject.org/blog/deterministic-builds-part-one-cyberwar-and-global-compromise>{.external} [https://f-droid.org/wiki/page/Deterministic,\_Reproducible\_Builds](https://f-droid.org/wiki/page/Deterministic,_Reproducible_Builds){.external})

**How is Orfox different than Firefox for Android?**

Beyond the core Tor Browser components, Orfox also must ensure all Android-specific code is properly routed through the Tor proxy, and otherwise hardened to protect against data and privacy leaks.

  * Orfox adds patches at the Android Java code layer to enable proxying of all Java network HTTP communications through the local Orbot HTTP proxy (HTTP localhost:8118 for now, but moving to SOCKS). (<https://dev.guardianproject.info/issues/5235>{.external} <https://dev.guardianproject.info/issues/5317>{.external})

  * Orfox removes the Android permissions for Contacts, Camera, Microphone, Location and NFC (<https://dev.guardianproject.info/issues/3822>{.external}) since the capability of using these features are not in line with the spirit of Tor Browser

  * Orfox removes features like WebRTC and support for interaction with Chromecasts or Roku devices, since this type of communication is not compatibility with proxying communication through a TCP-based network like Tor (<https://dev.guardianproject.info/issues/5358>{.external} <https://dev.guardianproject.info/issues/5357>{.external})

**How is Orfox different than Orweb?**

  * Orweb is our current default browser for Orbot/Tor mobile users (<https://guardianproject.info/apps/orweb>{.external}) that has been downloaded over 2 million times. It is VERY VERY SIMPLE, as it only has one tab, no bookmark capability, and an extremely minimal user experience.

  * Orweb is built upon the bundled WebView (Webkit) browser component inside of the Android operating system. This has proven to be problematic because we cannot control the version of that component, and cannot upgrade it directly when bugs are found. In addition, Google has made it very difficult to effectively control the network proxy settings of all aspects of this component, making it difficult to guarantee that traffic will not leak on all devices and OS versions.

  * Orweb also only provides a very limited amount of capability of Tor Browser, primarily related to reducing browser fingerprinting, minimizing disk writes, and cookie and history management. It trys to mimic some of the settings of Tor Browser, but doesn’t actually use any of the actual code written for Tor Browser security hardening.

  * Orweb does have an advantage which is that it less than 2MB while Orfox is in the 25-30MB range. This is primarily because Orweb relies on many components built into Android, so it does not need to bundle them. Orfox contains the full stack of code necessary for a complete browser, and thus is more secure and dependable, but also larger. The Mozilla Mobile team is working on reducing the size of their binaries, and the Orfox team is focused on this, as well, since we are disabling some of the components that have contributed the browser bloat.