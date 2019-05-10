---
id: 13986
title: 'IOCipher is the antidote to “Man-in-the-Disk” attack'
date: 2018-08-17T16:56:00-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=13986
permalink: /2018/08/17/iocipher-is-the-antidote-to-man-in-the-disk-attack/
bigimg: [{src: "/wp-content/uploads/2018/08/Man-in-the-Disk-Crash-Phone.png",}]
categories:
  - Development
tags:
  - defcon2018
  - man-in-the-disk
  - security
  - vulnerability
---
Recently, at DEFCON 2018, researchers at Check Point [announced a new kind of attack](https://blog.checkpoint.com/2018/08/12/man-in-the-disk-a-new-attack-surface-for-android-apps/) made possible by the way many Android apps are implemented. In summary, developers use the shared external storage space in an unsafe manner, by not taking into consideration that other apps also have read and write access to the same space. A malicious app can modify data used by another app, as a vector for compromising that app, causing it to be compromised or crash.

While Google does provide <a href="https://developer.android.com/training/articles/security-tips" target="_blank" rel="noopener">guidelines</a> on safe external storage use, most developers ignore them. Here is what they say:

  * “Perform input validation when handling data from external storage”
  * “Do not store executables or class files on External Storage”
  * “External Storage files should be signed and cryptographically verified prior to dynamic loading”

This is most likely due to lack of time or knowledge…. and, that is where our [IOCipher encrypted virtual filesystem library for Android](https://guardianproject.info/code/iocipher/) comes in!

IOCipher provides a virtual encrypted disk for Android apps without requiring the device to be rooted. It uses a clone of the standard `java.io` API for working with files, so developers already know how to use it. Only password handling, and opening the virtual disk are what stand between the developer and working encrypted file storage. It is based on and <a href="http://sqlcipher.net/" target="_blank" rel="noopener">SQLCipher</a>, and designed to work with <a href="https://github.com/guardianproject/IOCipher" target="_blank" rel="noopener">CacheWord</a> for handling the keys and passwords.

Regarding the three guidelines from Google, by storing downloaded data into an IOCipher virtual volume, you both benefit from the use of external storage, while ensuring, thanks to cryptography, that your data or executable code has not been read or modified by another application. If a malicious application tries to access or modify the encrypted volume, it will be detected and not able to load, without causing a crash in the application.

You can find IOCipher on Github today (and likely get it implemented in your app today, as well!)

<https://github.com/guardianproject/IOCipher>

 