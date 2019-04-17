---
id: 2785
title: Sometimes the best solution is a library, not an app
date: 2012-08-27T12:30:15-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=2785
permalink: /2012/08/27/sometimes-the-best-solution-is-a-library-not-an-app/
categories:
  - Development
tags:
  - developer tools
  - encryption
  - ffmpeg
  - frameworks
  - gnupg
  - gpg
  - iocipher
  - libraries
  - libsqlfs
  - orbot
  - orlib
  - sqlcipher
  - tor
---
[<img src="https://guardianproject.info/wp-content/uploads/2012/08/framework_wheel-150x150.png" alt="" title="thinking about frameworks" width="150" height="150" class="alignleft size-thumbnail wp-image-2792" />](https://guardianproject.info/wp-content/uploads/2012/08/framework_wheel.png)Our general approach to software development starts with surveying existing solutions that are available and in use, to see if there is already enough of an ecosystem or whether we need to seed that. When there is already an adundance of tools and apps out there, we work to find the good ones, provide feedback and auditing, and then build apps and tools to fill in any gaps. For example, this was our approach in the Open Secure Telephony Network.

When there is not an ecosystem around a given problem, then we aim to make it as easy as possible for people writing software to address the issues. In this case, we focus on making developer tools. For example, most of the data on our phones is easily accessible to someone who has physical access to the device, be it the secret police or a thief. IOCipher and SQLCipher-for-Android both provide tools to easily encrypt data, using APIs that are very familiar to anyone doing Android development. We specifically aim to take complex technical challenges and bundle them up into packages that allow developers to add functionality in a matter of hours or days rather than weeks or months.

With the developer tools that Guardian Project is creating, the impact is not as overt as in other software development since they are largely invisible to the users if we have done our jobs right.

In order for our developer projects to have a good impact, there are many different aspects that need to be covered. After assessing the current available tools to determine the general approach, the technical approach is chosen. This will influence the development time, the efficiency, and ease of use. As soon as the project is developed to a basic usable state, it is time to get feedback from willing testers to validate the techical approach. After more development and feedback, next comes documentation and beta releases. Once the project gets to a point where the releases and documentation are good enough for most people to figure out what they need, then we start evangelizing the tool and lobby the developers of existing software to adopt the new tool. As part of that, we also offer meetups and workshops for people to see demos, discuss ideas with us, get started, and learn best practices.

**Some Current Projects**

We already have a couple well known developer tools out there, like SQLCipher-for-Android and Orlib. We have many more in development. Here&#8217;s a quick overview:

  * Orlib is an Android library to make it very easy to include Orbot/Tor support in any app. Any app that uses orlib can transparently route all traffic through the Tor network without requiring that the device be rooted. It is a well established project that mostly needs more documentation, developer support, and evangelizing.
  * SQLCipher is a custom version of the SQLite database that provides easy-to-use, flexible and robust encryption. Guardian Project created SQLCipher-for-Android, which mirrors the standard Android database API, so developers already know how to use it, and need only add support for handling the passwords.
  * libsqlfs provides a complete virtual disk on top of a SQLCipher database. The virtual disk is encrypted and contained in a single file, which can be easily moved around, copied, shared, etc. It is a standard FUSE filesytem that can work on Android, GNU/Linux, and Mac OS X. libsqlfs is a pre-existing tool that was abandoned by its authors and has been adopted by the Guardian Project.
  * IOCipher is a cousin to SQLCipher-for-Android: it provides virtual encrypted disks for Android apps without requiring the device to be rooted. It uses the standard Java API for working with files, so developers already know how to use it, and only need to handle the passwords and opening and closing the virtual disks. It is based on libsqlfs and SQLCipher.
  * Gnu Privacy Guard (GnuPG) for Android brings the widespread standard in OpenPGP encryption to Android. GnuPG provides solid encryption for keeping emails and files private, and for verifying that emails and files are who you think they are. GnuPG is built-in to basically every GNU/Linux distro, in GPGTools for Mac OS X and Apple Mail, a plugin for Outlook and Thunderbird, etc. We are working to bring GnuPG to Android to make it the cornerstone of Android encryption like it is elsewhere.
  * ffmpeg is a popular, widespread framework for transcoding and filtering digital videos. It has been essential to our apps ObscuraCam, InformaCam, and Murrow/StoryMaker. We want to now work to make it dead simple for developers to build their own apps on it. We are also extending it to provide a full framework for audio and image redaction, metadata management, and encryption of sensitive parts of the media. This will make it easy for media app developers to build in privacy to their own apps.
  * Portable Shared Security Tokens (PSST) is our project to tackle the issues of digital identity and crypto key management. This is perhaps the most vexing issue facing deployment of secure mobile devices today. Public-key cryptography (HTTPS/SSL, OTR chat, PGP email, etc.) is a proven, powerful way to validate digital identity while keeping the contents private. Their cryptographic keys essentially become their proof of identity, and as such that identity must be portable across computing contexts (mobile devices, desktop environments, etc.). An interoperable standard and associated developer libraries needs to be developed to make possible a portable and secure solution for establishing one&#8217;s identity.
  * Always Secure Messaging (&#8220;AweSoMe&#8221;) is a collaborative effort to build interoperable, open-source, secure messaging applications, that work from mobile to mobile, as well as mobile to web. In particular, the goal is to create an extremely usable and high quality experience, that simultaneously supports one-to-one and one-to-many (group) end-to-end secure messaging communications across multiple platforms.
  * Bazaar provides the last piece of this puzzle: easy, secure and private distribution of software. Debian GNU/Linux has proven that decentralized software stores can work well. Google Play and the Apple App Store both provide excellent examples for how to make it easy to find and distribute apps, but are often blocked or not available in many parts of the world. Bazaar combines all of these ideas to provide a decentralized, peer-to-peer app store that makes it easy to find and distribute apps.