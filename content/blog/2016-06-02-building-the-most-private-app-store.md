---
id: 13332
title: Building the most private app store
date: 2016-06-02T11:08:52-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13332
permalink: /2016/06/02/building-the-most-private-app-store/
categories:
  - News
tags:
  - android
  - anonymity
  - bazaar
  - debian
  - encryption
  - F-Droid
  - fdroid
  - identity
  - mobile
  - open-source
  - privacy
  - reproducible build
  - security
  - tor
---
_App stores can work well without any tracking at all_

[<img src="https://guardianproject.info/wp-content/uploads/2016/06/whichdoor-150x150.jpg" alt="whichdoor" width="150" height="150" class="alignright size-thumbnail wp-image-13337" />](https://guardianproject.info/wp-content/uploads/2016/06/whichdoor.jpg)

Attackers are increasingly seeing app stores as a prime <a href="https://guardianproject.info/2015/02/24/phishing-for-developers/" target="_blank">attack</a> vector, whether it is aimed at the masses like [XCodeGhost](http://researchcenter.paloaltonetworks.com/2015/09/more-details-on-the-xcodeghost-malware-and-affected-ios-apps/) or very targeted like in FBI vs Apple. When we install software from an app store, we are placing a lot of trust in a lot of different parties involved in getting the source code from the original developer delivered to our device in a useful form. Most people are entirely unaware of how much trust they are putting into this system, which they are entrusting with their personal data. Even for people who do understand the technical details involved, figuring out whether the people and the system itself is trustworthy is difficult to do.

We are building an app store that requires the bare minimum of trust: only the software developers themselves and the code they produce. We consider the app store operators and servers a threat. Building an ecosystem that enables automated, effective auditing lets the computers verify to make trust decisions easier. Effective external auditing requires an ecosystem that cannot deliver targeted content to just the auditing system, while feeding users something else (aka “binary transparency”).

**Most app stores track as much as possible**

The vast majority of apps stores track their users actions in detail. Some is necessary when using the business model of the app store operator taking a percentage of sales, but none of the tracking is inherent to running an app store. For example, payment verification can be handled in the app itself like shareware. A software delivery system that tracks its users makes it simple to hide malware delivery since it can target any auditing system. Most app stores know a lot about their users:

  * account name
  * identity
  * payment methods
  * everything you search for in the app store
  * everything you look at in the app store
  * everything you download, install, uninstall
  * which apps you actually run
  * where you are, based on IP, declared preference, etc.
  * your preferred language
  * and more…

Apps stores need to know very little in order to function: how to give you the files you request. That means indexes, descriptions, icons, apps, and install/delete requests (for “push” install/delete). Given that information, the client can do everything needed to provide a full app store user experience. For this work, we chose to build upon <a href="https://f-droid.org" target="_blank">F-Droid</a>, a community-run Android app store that distributes verified Free Software. The community has had an interest in privacy all along, and has always worked to avoid tracking. The security architecture is based on models proven by <a href="https://wiki.debian.org/SecureApt" target="_blank">Debian</a>, <a href="https://github.com/theupdateframework/tuf/blob/develop/docs/tuf-spec.txt" target="_blank">The Update Framework</a> , and others:

  * HTTPS connections by default
  * pinned TLS certificate built into the client app
  * updates verified based on the signature on the app itself
  * file integrity protected by signed metadata
  * signed metadata includes hashes of the app and its signing key
  * signed metadata generated on a separate machine, which can be fully offline
  * public key for verifying metadata signatures built into F-Droid client app
  * signed metadata includes timestamp and expiry

While the current setup is already a solid platform, we are implementing a number of improvements. The signed metadata will include list of official mirrors, then the client chooses mirrors based on availability and freshness based on local criteria like whether Tor is in use, closest on the internet, etc. We are also moving the standard HTTP “etag” cache check from the server to the client so it cannot be abused to track users.

In order to defend against an attacker that holds the signing keys for the app repository, there must be a trustworthy source of information to compare against. Reproducible builds means that anyone with the same source code will produce the exact same binary. When paired with an auditing system, it is easy to catch malware inserted in the build process, rather than the source code, like XCodeGhost. Reproducible builds also makes it possible to have all builds of a release binary have the exact same hash. Then any app repository can build apps only from source code, and have a source of verification data from any other app repository building the same app. Building software from source has become cheap enough that many companies like gitlab.com and Travis CI are offering free, automated build services in the cloud. Since the whole F-Droid toolset is free software and designed to be easy to setup, the barriers to setting up automatic auditing are quite low. People in separate areas of the world with different risk profiles can run verification servers to provide more trustworthy information.

Another key aspect of the F-Droid project is to provide the complete toolset needed to run an app store. This enables a more decentralized ecosystem. Therefore, one key goal is to lower the risks of running the services, so that more people can run their own app stores. If the app store does not track its users, then that removes the hassle of protecting personal data from any attacker. These services can be run without fear of responding to secret orders for personal information. It also means that the server setup is a lot simpler because it does not need dynamic content. The app store serve only needs to serve files (e.g. indexes, apps, etc.). The app repository is generated on a secure machine, or even a fully offline machine, and posted to the server. The main server is purely a mirror of the offline machine where the signed repository is generated. Mirrors just shuffle bits from place to place, they are no longer an attack vector.

Putting all these pieces together provides a system where users need only audit the source code in order to verify a trustworthy app delivery. The file pipeline provides redundantly secure data transmission, the apps can be reproducibly from source code, the app repositories can be automatically audited. Of course, this system relies not only on the power of cryptography, but also the power of transparency. Debian provides a great example of the power of transparency: Debian gives a thousand volunteers root access to every Debian install (by virtue of their ability to upload signed packages that get installed as root). Yet this system has been proven over the past 20+ years to provide solid security. Ultimately we hope that this will de-emphasize the signing key as the sole protection against abuse. If malware has a decent change of being spotted, it makes it much less likely to be used since malware authors either rigorously defend their exploits, or use well known exploits that are not difficult to automatically detect.

**Future Work**

One attack vector that is not well covered is malware that installable by everyone, that then uses data on the local device to target specific users. That would be a way to target individuals using an app store that does not track its users. We are starting to implement automated dynamic analysis of every app using tools like <a href="https://labs.mwrinfosecurity.com/tools/drozer" target="_blank">Drozer</a>.

We are also working towards making as many apps as possible build reproducibly. Some of our quick checks show that a large number of the apps in f-droid.org already will build reproducibly, given the right build environment. We are working on making the process of setting up that build environment as automated as possible.

The F-Droid “verification server” has been prototyped, and it will be further developed with the aim of making it dead simple to run in common cloud services.

We already have the infrastructure in place to do verified double-signing, where the developer first signs the release bulid, then once f-droid.org reproduces that build, it adds its signature. Then Android would enforce that both signatures need to be present in order for it to be a valid update.

As the full localization support is built out, the language that a user is using will not be reported to the server. While speaking Spanish in Spain does not provide much information, speaking Quechua in Uzbekistan can narrow it down to a single user. Instead of dividing the index metadata by language, it will instead be grouped by app. We will then group apps so that it is difficult to tell which app in the group is the one people are interested in. For example, if one very popular app is only grouped with apps that are rarely downloaded, then it is an easy assumption that someone getting info about that block of apps is most likely looking for that popular app.