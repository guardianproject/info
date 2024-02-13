---
id: 13552
title: 'Build Android apps with Debian: apt install android-sdk'
date: 2017-03-13T10:03:30-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13552
permalink: /2017/03/13/build-android-apps-with-debian-apt-install-android-sdk/
categories:
  - News
tags:
  - Android
  - bazaar
  - debian
  - howto
  - open source
  - reproducible builds
  - security
---
[<img src="https://guardianproject.info/wp-content/uploads/2015/04/debian-150x150.jpg" alt="" width="150" height="150" class="alignright size-thumbnail wp-image-12920" srcset="https://guardianproject.info/wp-content/uploads/2015/04/debian-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2015/04/debian-300x300.jpg 300w, https://guardianproject.info/wp-content/uploads/2015/04/debian-270x270.jpg 270w, https://guardianproject.info/wp-content/uploads/2015/04/debian-230x230.jpg 230w, https://guardianproject.info/wp-content/uploads/2015/04/debian.jpg 600w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2015/04/debian.jpg)  
In Debian stretch, the upcoming new release, it is now possible to build Android apps using only packages from Debian. This will provide all of the tools needed to build an Android app targeting the “platform” <tt>android-23</tt> using the SDK <tt>build-tools</tt> 24.0.0. Those two are the only versions of “platform” and “build-tools” currently in Debian, but it is possible to use the Google binaries by installing them into <tt>/usr/lib/android-sdk</tt>.  
<!--more-->

This doesn’t cover yet all of the libraries that are used in the app, like the Android Support libraries, or all of the other myriad libraries that are usually fetched from jCenter or Maven Central. One big question for us is whether and how libraries should be included in Debian. All the Java libraries in Debian can be used in an Android app, but including something like Android Support in Debian would be strange since they are only useful in an Android app, never for a Debian app.

**Building apps with these packages**

Here are the steps for building Android apps using Debian’s Android SDK on Stretch.

  1. `sudo apt install android-sdk android-sdk-platform-23`
  2. `export ANDROID_HOME=/usr/lib/android-sdk`
  3. In _build.gradle_, set _compileSdkVersion_ to 23 and _buildToolsVersion_ to 24.0.0
  4. run `gradle assembleDebug`

The Gradle Android Plugin is also packaged. Using the Debian package instead of the one from online Maven repositories requires a little configuration before running Gradle. In the _buildscript_ block:

  * add <tt>maven { url 'file:///usr/share/maven-repo' }</tt> to repositories
  * use <tt>compile 'com.android.tools.build:gradle:debian'</tt> to load the plugin

Currently there is only the target platform of API Level 23 packaged, so only apps targeted at _android-23_ can be built with only Debian packages. We will add more API platform packages via backports. Only _build-tools_ 24.0.0 is available, so in order to use the SDK, build scripts need to be modified. Beware that the Lint in this version of Gradle Android Plugin is still problematic, so running the :lint tasks might not work. They can be turned off with <tt>lintOptions.abortOnError</tt> in _build.gradle_. Google binaries can be combined with the Debian packages, for example to use a different version of the platform or build-tools.

**Why include the Android SDK in Debian?**

While Android developers could develop and ship apps right now using these Debian packages, this is not very flexible since only <tt>build-tools-24.0.0</tt> and <tt>android-23</tt> platform are available. Currently, we are not aiming to cover the most common use cases. Those are pretty well covered by Google’s binaries (except for the proprietary license on the Google binaries), and are probably the most work for the Debian Android Tools Team to cover. We are first working on use cases that are poorly covered by the Google binaries, for example, like where only specific parts of the whole SDK are used. Here are some we have in mind:

  * tools for security researchers, forensics, reverse engineering, etc. which can then be included in live CDs and distros like Kali Linux
  * a hardened APK signing server using _apksigner_ that uses a standard, audited, public configuration of all reproducibly built packages
  * Replicant is a 100% free software Android distribution, so of course <a href="http://blog.replicant.us/2017/02/replicant-6-0-development-updates/" target="_blank">they want to have a 100% free software SDK</a>
  * high security apps need a build environment that matches their level of security, the Debian Android Tools packages are <a href="https://reproducible-builds.org" target="_blank">reproducibly built</a> only from publicly available sources 
  * dead simple install with strong trust path with mirrors all over the world

In the long run, the <a href="https://wiki.debian.org/AndroidTools" target="_blank">Debian Android Tools Team</a> aims to cover more use cases well, and also building the Android NDK. This all will happen more quickly if we have more contributors! Android is the most popular mobile OS, and can be 100% free software like Debian. Debian and its derivatives are one of the most popular platforms for Android development.

Last but not least, we want feedback on how this should all work. For example, we need ideas for how to nicely integrate Debian’s Java libraries into the Android _gradle_ workflow. And ideally, the Android Support libraries would also be reproducibly built and packaged somewhere that enforces only free software.

For anyone interested in tools for working with Android apps and APKs, including for reverse engineering, inspection, auditing, etc. there are quite a few tools included now in Debian:

* `apt install android-sdk androguard apktool diffoscope dummydroid enjarify gplaycli libsmali-java libscout repo`