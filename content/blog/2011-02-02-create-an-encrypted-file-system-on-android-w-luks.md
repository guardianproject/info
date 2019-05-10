---
id: 625
title: Create an encrypted file system on Android with LUKS
date: 2011-02-02T23:29:15-04:00
author: Derek
layout: post
guid: https://guardianproject.info/?p=625
permalink: /2011/02/02/create-an-encrypted-file-system-on-android-w-luks/
categories:
  - Development
  - HowTo
  - News
---
[LUKS](https://code.google.com/p/cryptsetup/) is the standard for Linux hard disk encryption. By providing a standard on-disk-format, it not only facilitates compatibility among distributions, but also provides secure management of multiple user passwords.

Building off the work from other [great](https://androidvoid.wordpress.com/2009/09/30/android-encryption-using-cryptsetup-and-luks/) [sources](http://forum.xda-developers.com/showthread.php?t=866131), the Guardian Project hack team decided to take a crack at porting LUKS to Android recently, with the goal of creating a proof of concept build process that can be easily adapted to future projects.

On our stock Guardian hardware (rooted NexusOne running [CyanogenMod](http://www.cyanogenmod.com/)) we were able to create a 50MB “secretagentman.mp3” file on the device sdcard to store our encrypted filesystem. We think the possibilities for enhanced privacy here are great: to the average phone snooper, this would appear as just another harmless media file on your device storage!

You can give it a shot by following the instructions over at the project [wiki](https://github.com/guardianproject/LUKS/wiki). Note that the build process requires setting up the [Android NDK](http://developer.android.com/sdk/ndk/index.html) on your machine, and the current setup process must be done through adb shell or terminal, requiring root permissions. Work on a GUI is just getting started.

As usual we encourage those wishing to get involved to check out our projects on [Git](https://github.com/guardianproject), [get in touch](https://guardianproject.info/contact/) with us, and join us on IRC at #guardianproject on [freenode](http://freenode.net/irc_servers.shtml).