---
id: 2196
title: IOCipher lives! encrypted virtual file system for Android
date: 2012-05-17T16:44:35-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=2196
permalink: /2012/05/17/iocipher-lives-encrypted-virtual-file-system-for-android/
categories:
  - Development
tags:
  - Android
  - encryption
  - open source
  - prototype
  - psst
  - security
---
Nathan and I just got the first complete test of IOCipher working in the IOCipherServer/SpotSync app. We created a filesystem sqlite.db file, then mounted it and got all the files via HTTP. In the test suite, I have lots of operations all running fine and encrypting! The core idea here is a java.io API replacement that transparently writes to an encrypted store. So for the most part, just change your import statements from:

<pre>java.io.*   --->   info.guardianproject.iocipher.*</pre>

Then in your code, make a `VirtualFileSystem` instance and mount it, and unmount it. That’s about it. Right now, you can have only a single filesystem per app, but you can unmount one and mount another. We hope to add support for multiple filesystems in the not-too-distant future.

Its ready for people to try, some kind of early alpha. Here’s the framework itself:  
<a href="https://github.com/guardianproject/IOCipher" target="_blank">https://github.com/guardianproject/IOCipher</a>

THe easiest way to get started right now is probably the test suite:  
<a href="https://github.com/guardianproject/IOCipherTests" title="IOCipherTests" target="_blank">https://github.com/guardianproject/IOCipherTests</a>

Our first app using it is here:  
<a href="https://github.com/guardianproject/IOCipherServer" target="_blank">https://github.com/guardianproject/IOCipherServer</a>

Comments, feedback, criticism, welcome and wanted!