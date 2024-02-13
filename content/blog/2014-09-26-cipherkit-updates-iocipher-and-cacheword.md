---
id: 12615
title: 'CipherKit updates: IOCipher and CacheWord'
date: 2014-09-26T21:39:54-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12615
permalink: /2014/09/26/cipherkit-updates-iocipher-and-cacheword/
categories:
  - News
tags:
  - Android
  - bazaar
  - cacheword
  - cipherkit
  - encryption
  - iocipher
  - martusvmm
  - password management
  - security
---
We’ve been on a big kick recently, updating the newest members of our CipherKit family of frameworks: [IOCipher](/code/iocipher) and <a href="https://github.com/guardianproject/cacheword" target="_blank">CacheWord</a>. There also are is a little news about the original CipherKit framework: <a href="https://www.zetetic.net/sqlcipher/open-source" title="SQLCipher for Android" target="_blank">SQLCipher-for-Android</a>.

## IOCipher v0.2

[<img src="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg" alt="alberti cipher disk" width="150" height="150" class="alignright size-thumbnail wp-image-3079" srcset="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg 245w" sizes="(max-width: 150px) 100vw, 150px" />](/code/iocipher)IOCipher is a library for storing files in an encrypted virtual disk. It’s API is the exact same as `java.io` for working with files, and it does not need root access. That makes it the sibling of SQLCipher-for-Android, both are native Android APIs that wrap the SQLCipher database.

This round of work focused on making IOCipher more reliable and secure, and easy to integrate with CacheWord. It can now handle files up to 4GB in size, the same as FAT filesystems, and it has much improved performance, especially under concurrent load. There is now also an `unmount()` method to lock the database and wipe the key from memory. The central `VirtualFileSystem` class is now a singleton, since you can only have a single virtual disk open at a time. Lastly, the IOCipher release now includes binaries for `armeabi`, `armeabi-v7a`, and `x86`. IOCipher v0.2 was built against SQLCipher-for-Android v3.1.0, and that is the minimum recommended version to use.

Find downloads, example projects, test suites, and more on [the IOCipher page](/code/iocipher). Follow the development on the <a href="https://dev.guardianproject.info/projects/iocipher" target="_blank">IOCipher project page</a>.

## CacheWord v0.1

Once you are using SQLCipher and IOCipher, then you’ll definitely need to do some password management, and password caching too, since no one wants to type their password again every time they come to an app. That is where CacheWord comes in: it is a library for managing passwords, and it is designed easily feed directly into SQLCipher and IOCipher, or really anything that needs secure password caching.

Most of this update was about making CacheWord ready to deploy. That means fixing bugs and drastically simplifying it’s dependencies. CacheWord now can be used as a plain jar file or an Android Library Project, and it only depends on `android-support-v4.jar`.

Part of the process of simplifying CacheWord also involved stripping down the API to only want CacheWord should really handle. The standard API is all in the CacheWordHandler class. So that means that your app has to handle any Notification, and pass it to CacheWord if you want CacheWordService to run in the foreground.

CacheWord also now dynamically chooses how many iterations of the key derivation function based on the CPU type. That means that new, fast devices, the derived key will be a lot stronger, while on slow, old devices, it won’t take a minute to unlock your app.

Find downloads, example projects, and more on [the CacheWord page](/code/cacheword). Follow the development on the <a href="https://dev.guardianproject.info/projects/cacheword" target="_blank">CacheWord project page</a>.

## SQLCipher

[<img src="https://guardianproject.info/wp-content/uploads/2010/05/skitch.png" alt="SQLCipher" width="64" height="72" class="alignright size-full wp-image-3613" />](https://www.zetetic.net/sqlcipher/)The upcoming release of SQLCipher-for-Android also has been simplified. It will no longer depend on commons-codec.jar or guava-r09.jar (thanks to Jeff Campbell for submitting those commits!), remove ~8000 methods for those who fear running into the 65k method limit of the classes.dex file. We’ve been working on making the build process be reproducible, so that anyone can verify that the official releases are built only from the source in the git repo, and nothing else has been added. We’re also working on moving the password format conversion code out of CacheWord and into SQLCipher, where it belongs.