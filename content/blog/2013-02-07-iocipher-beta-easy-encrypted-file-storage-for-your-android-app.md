---
id: 3056
title: 'IOCipher beta: easy encrypted file storage for your Android app'
date: 2013-02-07T14:45:28-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=3056
permalink: /2013/02/07/iocipher-beta-easy-encrypted-file-storage-for-your-android-app/
bigimg: [{src: "http://guardianproject.info/wp-content/uploads/2013/02/288491653_a9b6251477.jpg",}]
categories:
  - Development
  - New Release
tags:
  - android
  - beta
  - encryption
  - iocipher
  - open-source
  - privacy
  - psst
  - secure storage
---
At long last, we are proud to announce the [first beta release of IOCipher](https://guardianproject.info/code/iocipher/), an easy framework for providing virtual encrypted disks for Android apps.

  * does not require root or any special permissions at all
  * the API is a drop-in replacement for the standard java.io.File API, so if you have ever worked with files in Java, you already know how to use IOCipher
  * works easiest in an app that stores all files in IOCipher, but using standard java.io with IOCipher is possible
  * supports android-7 v2.1 and above
  * licensed under the LGPL v3+

You can download it here:

<https://guardianproject.info/code/iocipher/>

Adding IOCipher to our InformaCam and NoteCipher apps is already in the  
works. There is already one app in the Play Store built with IOCipher: <a title="Gryphn Secure Messaging in the Play Store" href="https://play.google.com/store/apps/details?id=com.Gryphn.mms&hl=en" target="_blank">Gryphn Secure Messaging</a>

We’ve recently done some heavy testing and bug fixing and this is ready for beta status. That means for many applications, it should be stable with reasonable performance. But its not done yet, and there are some known edge cases documented in our bug tracker which we aim to address in the next beta release:

<https://dev.guardianproject.info/projects/iocipher/issues>

Some additional notes on usage:

  * single thread/sequential access is the preferred way of using IOCipher
  * multi-threaded access possible, but potentially unstable under very high load
  * VFS now has beginTransaction and completeTransaction to optimize performance
  * parts of java.io not currently supported: vectored I/O, memory-mapped files

 

_featured photo [“Safe” from Pong on Flickr](http://www.flickr.com/photos/pong/288491653/)_