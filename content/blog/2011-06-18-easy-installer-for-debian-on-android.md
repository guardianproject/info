---
id: 1133
title: 'Lil’ Debi: Easy Installer for Debian on Android'
date: 2011-06-18T04:22:52-04:00
author: n8fr8
layout: post
guid: http://guardianproject.info/?p=1133
permalink: /2011/06/18/easy-installer-for-debian-on-android/
categories:
  - Development
  - News
---
Have an Android phone and want an easy Debian chroot running it?

Alpha test our new app, [Lil’ Debi](https://github.com/guardianproject/lildebi). It builds up a whole Debian chroot on your phone entirely using debootstrap. You choose the release, mirror, and size of the disk image, and away it goes. It could take up to an hour, then its done. Then it has a simple chroot manager that mounts and unmounts things, and starts/stops sshd if you have it installed. You can also then use ‘apt-get’ to install any package that is released for ARM processors. This includes things like GPG, Tor, TraceRouteTCP and other security and crypto tools.

[<img class="alignleft size-full wp-image-1137" style="margin-right: 6px;" title="LilDebiInstalling" src="https://guardianproject.info/wp-content/uploads/2011/06/LilDebiInstalling.png" alt="" width="288" height="480" srcset="https://guardianproject.info/wp-content/uploads/2011/06/LilDebiInstalling.png 480w, https://guardianproject.info/wp-content/uploads/2011/06/LilDebiInstalling-180x300.png 180w" sizes="(max-width: 288px) 100vw, 288px" />](https://guardianproject.info/wp-content/uploads/2011/06/LilDebiInstalling.png)

Project and source are here:  
[https://github.com/guardianproject/lildebi  
](https://github.com/guardianproject/lildebi) 

Have a look at our automatic build bot for the latest binary installer APK here: [https://guardianproject.info/builds/lildebi/](https://github.com/guardianproject/lildebi/LilDebi-debug-20110617.apk/qr_code)

Check the GitHub [wiki](https://github.com/guardianproject/lildebi/wiki) for tips on using it. If you don’t know what you need this for, then you probably should not install it (for now).