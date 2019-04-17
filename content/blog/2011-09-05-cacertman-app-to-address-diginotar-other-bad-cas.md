---
id: 1249
title: 'CACertMan app to address DigiNotar & other bad CA’s'
date: 2011-09-05T03:29:00-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=1249
permalink: /2011/09/05/cacertman-app-to-address-diginotar-other-bad-cas/
force_ssl:
  - "1"
categories:
  - Development
tags:
  - cacerts
  - certificate authority
  - comodo
  - diginotar
  - ssl
---
As I expect many of you are aware, there was a major compromise to a Dutch Certificate Authority named “DigiNotar” recently, where they allowed SSL certs for domains like \*.google.com, \*.torproject.org and even \*.cia.gov as well as \*.*.com to be issued.

It was brought up to the contribs of CyanogenMOD that they should probably remove the DigiNotar CA cert from the built-in Android OS keystore (located at /system/etc/security/cacerts.bks). Since they have 500k+ users, and can be more nimble than other ROM/device distributors, it was seen as a way to quickly address the problem, at least within their community. It turns out that it wasn’t as easy to convince them to do this (even though Mozilla, Google Chrome, IE, etc already had). You can read the thread, but it is still an open issue:  
h<ttp://code.google.com/p/cyanogenmod/issues/detail?id=4260>{.vt-p}

In the meantime, I decided to do something proactive about this, and took two approaches:

1) Create our own curated cacerts.bks file which rooted users could install using ‘adb’ from their desktop and/or the ‘Root Explorer’ app available in the market and elsewhere. Our version of the CACert file removes DigiNotar, as well as CNNIC, a Chinese gov’t-managed cert authority who we have reason not to trust. Our goal is to continue to audit, update and distribute our own cacerts file for users who trust us.

Install info: <https://raw.github.com/guardianproject/cacert/master/INSTALLATION>{.vt-p}

Guardian’s CACert: <https://github.com/downloads/guardianproject/cacert/cacerts.bks>{.vt-p}

[  
](https://guardianproject.info/wp-content/uploads/2011/09/device-2011-09-04-232720.png){.vt-p} 2) We also wanted to create an app that let the user decided which certs they wanted available, and which they didn’t. Beyond this one CA problem, there are potentially many more, and every handset manufacturer or carrier can also place their own CA certs into the system. We need an app to address today’s and future CA threats.

[<img class="alignleft size-medium wp-image-1254" style="margin: 6px;" title="device-2011-09-04-232720" src="https://guardianproject.info/wp-content/uploads/2011/09/device-2011-09-04-232720-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2011/09/device-2011-09-04-232720-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2011/09/device-2011-09-04-232720.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](https://guardianproject.info/wp-content/uploads/2011/09/device-2011-09-04-232720.png){.vt-p}I have been hacking away on a solution to address this, and an initial test release is available for you. ‘CACertMan’ is a simple app that loads up the system cacert store, allows you to back it up, search for certs, delete them, and then save it back to the system. You can always restore from your initial backup, as well. In the future we may allow for a cert to just be disabled, but for now it is delete and/or restore.

Here is the first alpha build for testing. This does require root, as well as a device that has the ‘grep’ command on it. This is basically CyanogenMOD, but most likely any other custom ROM. If the ‘save’ doesn’t work, then you will need to use ‘RootExplorer’ to make you /system partition read-write.

Download CACertMan v0.0.1-Alpha: <https://github.com/guardianproject/cacert/CACertMan-0.0.1-alpha.apk/qr_code>{.vt-p}

You can find the source project here: <https://github.com/guardianproject/cacert>{.vt-p}

Once we get confirmation that the app works for most people, we’ll place it in the market, and on or site for wider distribution.

Through these two approaches, we hope to mitigate the threats facing Android users who might encounter man-in-the-middle attacks enabled through the DigiNotar exploit. While many of you are presumably in “free” countries, we do know that may of our users of Orbot, Gibberbot and other software are not, and we hope this message can reach them.