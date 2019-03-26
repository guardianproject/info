---
id: 12490
title: 'Our first deterministic build: Lil&#8217; Debi 0.4.7'
date: 2014-06-09T16:41:34-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12490
permalink: /2014/06/09/our-first-deterministic-build-lil-debi-0-4-7/
categories:
  - News
tags:
  - android
  - bazaar
  - deterministic build
  - reproducible build
  - security
---
[<img src="https://guardianproject.info/wp-content/uploads/2014/06/determinism.gif" alt="determinism" width="206" height="138" class="alignright size-thumbnail wp-image-12493" />](http://abyss.uoregon.edu/~js/ast123/lectures/lec05.html)

We just released Lil&#8217; Debi 0.4.7 into the <a href="https://play.google.com/store/apps/details?id=info.guardianproject.lildebi" target="_blank">Play Store</a> and <a href="https://f-droid.org/repository/browse/?fdid=info.guardianproject.lildebi" target="_blank">f-droid.org</a>. It is not really different than the 0.4.6 release except in has a new, important property: the APK contents can be reproduced on other machines to the extent that the APK signature can be swapped between the official build and builds that other people have made from source, and this will still be installable. This is known as a &#8220;deterministic build&#8221; or &#8220;reproducible build&#8221;: the build process is deterministic, meaning it runs the same way each time, and that results in an APK that is reproducible by others using only the source code. There are some limitations to this, like it has to be built using similar versions of the OpenJDK 1.7 and other build tools, for example. But this process should work on any recent version of Debian or Ubuntu. Please try the process yourself, and let us know if you can verify or not:

  * <a href="https://github.com/guardianproject/lildebi/wiki/Deterministic-Builds" target="_blank">https://github.com/guardianproject/lildebi/wiki/Deterministic-Builds</a>

The ultimate goal here is to make a process that reproduces the APK exactly, bit-for-bit, so that the anyone who runs the process will end up with an APK that has the exact same hash sum. As far as I can tell, the only thing that needs to be fixed in Lil&#8217; Debi&#8217;s process is the timestamps in the ZIP format that is the APK container.

There are a number of other parallel efforts. The Tor Project has written a lot about <a href="https://blog.torproject.org/category/tags/deterministic-builds" target="_blank">their process for reproducible builds for the Tor Browser Bundle</a>. Debian has made some progress in <a href="https://wiki.debian.org/ReproducibleBuilds" target="_blank">fixing the package builders to make the process deterministic</a>.