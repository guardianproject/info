---
id: 13148
title: First Reproducible Builds Summit
date: 2015-12-09T05:02:48-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13148
permalink: /2015/12/09/first-reproducible-builds-summit/
categories:
  - News
  - Research
tags:
  - android
  - bazaar
  - F-Droid
  - fdroid
  - F-Droid
  - fdroid
  - reproducible build
---
I was just in Athens for the “[Reproducible Builds Summit](https://reproducible-builds.org/events/athens2015/)“, an <a href="https://aspirationtech.org/" target="_blank">Aspiration</a>-run meeting focused on the issues of getting all software builds to be reproducible. This means that anyone starting with the same source code can build the _exact_ same binary, bit-for-bit. At first glance, it sounds like this horrible, arcane detail, which it is really. But it provides tons on real benefits that can save lots of time. And in terms of programming, it can actually be quite fun, like doing a puzzle or sudoku, since there is a very clear point where you have “won”.

Here are some examples of real benefits:

  * makes it easy to ensure no malware was inserted into software during the build process (e.g. the <a href="https://en.wikipedia.org/wiki/XcodeGhost" target="_blank">XCodeGhost</a> malware we just saw)
  * provides a QA tool to make sure that changes in the source code of a project produce only the expected results
  * allows F-Droid to use the developer’s APK signature while still verifying that apps build from 100% free software
  * make it possible to optimize and profile build processes while guaranteeing the results are exactly the same
  * for large projects, it can greatly speed up the build process (think rebuilding Gmail)

Represented there was: <a href="http://https//www.debian.org" target="_blank">Debian</a>, Google, <a href="https://www.freebsd.org/" target="_blank">FreeBSD</a>, <a href="https://getfedora.org/" target="_blank">Fedora</a>, <a href="https://f-droid.org" target="_blank">F-Droid</a>,  
<a href="http://brew.sh/" target="_blank">Homebrew</a>, <a href="https://www.macports.org/" target="_blank">MacPorts</a>, <a href="https://www.netbsd.org/" target="_blank">NetBSD</a>, <a href="https://www.archlinux.org/" target="_blank">Arch Linux</a>, <a href="https://www.coreboot.org/" target="_blank">Coreboot</a>, <a href="https://openwrt.org/" target="_blank">OpenWRT</a>, and a bunch of other  
projects like an automotive Linux distro called <a href="https://wiki.baserock.org/" target="_blank">Baserock</a>, the <a href="https://www.gnu.org/software/guix/" target="_blank">Guix</a> package manager, a Linux distro called <a href="https://nixos.org/" target="_blank">NixOS</a>, <a href="https://www.haskell.org/" target="_blank">Haskell</a> hackers, etc.

The organizers are already planning a second meeting, probably in April in Western Europe, and are looking to get more projects involved. Lots of people were talking about how it would be great to get some Android ROM developers involved. So if you are a contributor to CyanogenMod, Copperhead, <a href="https://omnirom.org/" target="_blank">OmniROM</a>, <a href="http://www.replicant.us/" target="_blank">Replicant</a>, Blackphone, etc. and would be interested in attending, please let us know!