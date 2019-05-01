---
id: 12912
title: Getting Android tools into Debian
date: 2015-04-30T11:13:26-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12912
permalink: /2015/04/30/getting-android-tools-into-debian/
categories:
  - News
tags:
  - android
  - bazaar
  - debian
  - gnu/linux
  - gradle
  - gsoc
  - java
  - linux
  - open-source
  - packaging
  - summer of code
---
[<img src="https://guardianproject.info/wp-content/uploads/2015/04/debian-150x150.jpg" alt="debian" width="150" height="150" class="alignright size-thumbnail wp-image-12920" srcset="https://guardianproject.info/wp-content/uploads/2015/04/debian-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2015/04/debian-300x300.jpg 300w, https://guardianproject.info/wp-content/uploads/2015/04/debian-270x270.jpg 270w, https://guardianproject.info/wp-content/uploads/2015/04/debian-230x230.jpg 230w, https://guardianproject.info/wp-content/uploads/2015/04/debian.jpg 600w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2015/04/debian.jpg)

[<img src="https://guardianproject.info/wp-content/uploads/2015/04/android-150x150.png" alt="android" width="150" height="150" class="alignright size-thumbnail wp-image-12919" srcset="https://guardianproject.info/wp-content/uploads/2015/04/android-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2015/04/android-270x270.png 270w, https://guardianproject.info/wp-content/uploads/2015/04/android-230x230.png 230w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2015/04/android.png)

As part of Debian’s project in Google <a href="https://wiki.debian.org/SummerOfCode2015" target="_blank">Summer of Code</a>, I’ll be working with two students, Kai-Chung Yan and Komal Sukhani, and another mentor from the <a href="https://wiki.debian.org/Teams/JavaPackaging" target="_blank">Debian Java Team</a> team, <a href="https://&#x71;a&#x2e;d&#x65;b&#x69;a&#x6e;.&#x6f;r&#x67;/dev&#x65;l&#x6f;p&#x65;r&#x2e;p&#x68;p&#x3f;l&#x6f;gin=&#x61;p&#x6f;@&#x67;a&#x6d;b&#x61;r&#x75;.&#x64;e" target="_blank">Markus Koschany</a>. We are going to be working on getting the Android SDK and tools into Debian, as part of the Debian <a href="https://wiki.debian.org/AndroidTools" target="_blank">Android Tools</a> team, building upon the existing work already included from the Java and <a href="https://wiki.debian.org/Teams/AndroidTools" target="_blank">Android Tools</a> teams. This project is in conjunction with the Java team since there is overlap between Android and Java tools, like `gradle`, `maven`, etc. Since this work is in Debian, all of the Debian-derivatives will automatically inherit this work. That includes: Ubuntu, Mint, Elementary, and many more.

The first question a lot of Android developers are probably asking is: why would we want to put the Android tools into Debian when there is already an official distribution from Google with it’s own update tools? It turns out there are many reasons, mostly centered around making things much easier to use, as well as addressing some key security concerns. For example:

  * automatic trustworthy downloads, no need to verify hash sums or think about HTTPS
  * eliminate need for insecure wrapper scripts, like `./gradlew`
  * easy install and update channel that all Debian users already know
  * trivial install for specific tools, like `adb`, `fastboot`, etc.
  * setting up a Debian/Ubuntu/etc box for Android development is easier when everything is included

[<img src="https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing-150x150.jpg" alt="320px-Trawling_Drawing" width="150" height="150" class="alignright size-thumbnail wp-image-12873" srcset="https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing-230x230.jpg 230w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing.jpg)

The most glaring issue from my point of view is the security issues in `gradle`. It will happily download and execute code without any kind of verification whatsoever. It inherits this terrible practice from maven, which has been shown to be an <a href="http://blog.ontoillogical.com/blog/2014/07/28/how-to-take-over-any-java-developer/" target="_blank">easy path to exploit anyone using it</a>. This is especially concerning considering that developers are more and more <a href="https://guardianproject.info/2015/02/24/phishing-for-developers/" target="_blank">being directly targeted</a>. At least it is more common for `gradle` configs to use HTTPS, but it is still quite easy mess up a config and force users to use HTTP instead. Fragile configs are really bad for security. Even if <a href="https://github.com/WhisperSystems/gradle-witness" target="_blank">gradle-witness</a> is used to pin the hash for the jars used in the project, `gradle-wrapper` might still downloading insecure code an executing it immediately, giving attackers potential full user access to that machine. That is because `gradle-wrapper` will download versions of `gradle` that it needs, and `gradle-witness` can not be used to pin the hash of the `gradle` files. And the repositories that `gradle` uses only provide methods to protect against network-based attacks. If the server that holds the jars is exploited, the attacker can replace the jars and the sum files at the same time. There is <a href="https://github.com/gradle/gradle/pull/448" target="_blank">a pull request open for <code>gradle</code></a> to allow pinning of the `gradle` executables themselves, which will help this situation.

On a different note, many people who are not developers at all want to use tools like `adb` and `fastboot` to access their Android device, or even root it. Having them in Debian means they are trivial for people to install, vastly easier than trying to figure out how to download and install the Android SDK. What lots of people end up doing instead is downloading random binaries from insecure internet forums and using those. For many devices, it is already possible to use only tools in Debian to root the device. As we get more of the Android tools packaged and updated in Debian, that will become the norm.

**Updates when you need them, built upon a stable base**

One common complaint about packages in Debian is that they are old and outdated. It is part of the core mission of Debian/stable to provide an operating system that changes as little as possible. That mission is contrary to what most developers need from their SDKs and sometimes even the development tools. But stability is also important for developers as well. For example, tools like `make`, used to build native code using the Android NDK (`ndk-build` is a `make` script) and even Android itself, has been around a long time and is used in so many projects. That is a tool that almost every developer wants to have very stable.

For the packages that developers need to have completely up-to-date, like the Android SDK itself, there are many options for distribution. Ubuntu Personal Package Archives (PPA) have proven easy and useful for exactly this kind of thing, and Debian is working on adding support for PPAs. Official repositories for <a href="http://backports.debian.org/" target="_blank">backports</a> are another avenue for timely updates.

**Help us figure this out**

We want lots of feedback on how to do this right! A great example is how to best support the various versions of `gradle`. It seems to me that `gradle` is starting to stabilize, and it is no longer necessary to track very specific releases of `gradle`. For example, `gradle` v2.2.1 will work well with projects that were setup with just about any v2.x version. And projects still using 1.x, they mostly seem to work using v1.12. So if this is the case, then this fits into a common pattern with build tools in Debian: 

  * GNU Compiler Collection is packaged as `gcc4.8`, `gcc4.7`, etc.
  * Apache Maven is packaged as `maven` and `maven2`
  * GNU automake is packaged as `automake1.14`, `automake1.13`, etc.

I’m currently thinking that the best solution for gradle is like Maven, with the package called `gradle` (v2.3) being the most up-to-date in conjunction with specific packages to support older versions, like `gradle1` (v1.12). But maybe it makes sense to do something like gcc, with a gcc meta-package to install the currently best supported version, then all versions packaged with name that includes that version, i.e. a gradle meta-package with `gradle1`, `gradle2`, `gradle3`, etc.

Other issues that we will have to grapple with include:

  * how to package various NDK versions?
  * How do we best work with the upstream Android team?
  * is packaging Android Studio feasible?

We also hope to provide an example that any other packaging systems can learn from and build upon. GNU/Linux distros like Arch and Fedora are the obvious ones, but also projects like Homebrew, MacPorts, and Cygwin could also use this work to include Android tools as packages in their system. Indeed, some of the work already included in Debian was derived from <a href="https://wiki.archlinux.org/index.php/Android#Android_SDK_core_components" target="_blank">some Arch packages</a>.