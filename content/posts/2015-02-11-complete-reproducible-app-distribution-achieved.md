---
id: 12847
title: Complete, reproducible app distribution achieved!
date: 2015-02-11T14:51:22-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12847
permalink: /2015/02/11/complete-reproducible-app-distribution-achieved/
spacious_page_layout:
  - default_layout
image: http://guardianproject.info/wp-content/uploads/2015/02/checkeycheckey.png
categories:
  - News
tags:
  - android
  - bazaar
  - checkey
  - f-droid
  - f-droid.org
  - fdroid
  - lildebi
  - prototype
  - reproducible build
  - security
---
With <a href="https://f-droid.org" target="_blank">F-Droid</a>, we have been working towards getting a complete app distribution channel that is able to reproducibly build each Android app from source. while this may sound like a mundane detail, it does provide lots of tangible benefits. First, it means that anyone can verify that the app that they are using is 100% built from the source code, with nothing else added. That verifies that the app is indeed 100% free, open source software.

It also verifies that there have not been any malicious bits of code added into the app during the build process. As has been <a href="https://www.youtube.com/watch?v=5pAen7beYNc" target="_blank">demonstrated</a> in the <a href="http://events.ccc.de/congress/2014/Fahrplan/events/6240.html" target="_blank">31c3 Reproducible Builds talk</a>, just flipping a single bit is enough to create a usable exploit in an app.

The F-Droid project is leading the way with its system for publishing verified builds. We know have our first full example, building upon our previous work with making <a href="https://guardianproject.info/2014/06/09/our-first-deterministic-build-lil-debi-0-4-7/" target="_blank">Lil&#8217; Debi build reproducibly</a>. We started with our simple little utility app <a href="https://github.com/guardianproject/checkey" target="_blank">Checkey</a> since it has few moving parts (first get one working, then the rest).

<p style="float: left" >
  <a href="https://guardianproject.info/releases/Checkey-0.1.1.apk"><img src="https://guardianproject.info/wp-content/uploads/2015/02/ic_launcher-web.png" alt="Checkey" width="128" height="128" /></a>
</p>

<p style="float: left; text-align: center; line-height: 128px; font-size: 1000%" >
  =
</p>

<p style="float: left" >
  <a href="https://f-droid.org/repo/info.guardianproject.checkey_101.apk"><img src="https://guardianproject.info/wp-content/uploads/2015/02/ic_launcher-web.png" alt="Checkey" width="128" height="128" style="float: right" /></a>
</p>

<p style="clear: both;">
  <p>
    When you download Checkey from f-droid.org, you will get an APK that was signed using the official Guardian Project offline signing key that was built by f-droid.org. No, we did not give them a copy of our key, instead, the fdroid publish process now looks for the Binaries: tag in the build recipe. If it sees that, it downloads that APK, then builds the app from source, then checks to make sure that they match using a simple diff of the APK contents and by checking that the signature on the official APK also validates on the APK that f-droid.org built.
  </p>
  
  <p>
    Now that we have our little Checkey working, we can work towards getting all of our apps verifying in the same way, eliminating a whole field of exploits that we have to worry about. You can follow the progress of this work on the F-Droid wiki <a href="https://f-droid.org/wiki/page/Deterministic,_Reproducible_Builds" target="_blank">Reproducible Builds</a> page, and learn about a future application of it on the <a href="https://f-droid.org/wiki/page/Verification_Server" target="_blank">Verification Server</a> page.
  </p>
  
  <p>
    The next two apps that are in the reproducible pipeline are <a href="https://leap.se/" target="_blank">LEAP</a>&#8216;s <a href="https://gitlab.com/fdroid/fdroiddata/tree/master/metadata/se.leap.bitmaskclient.txt" target="_blank">Bitmask</a> and our <a href="https://gitlab.com/fdroid/fdroiddata/blob/master/metadata/info.guardianproject.locationprivacy.txt" target="_blank">LocationPrivacy</a>.
  </p>