---
id: 1205
title: "Lil' Debi: Mobile Debian Installer"
date: 2011-06-24T15:28:42-04:00
author: n8fr8
layout: page
guid: http://guardianproject.info/?page_id=1205
force_ssl:
  - "1"
menu:
  main:
    parent: code
---
Have an Android phone and want an easy Debian chroot running that you can trust? Install [Lil’ Debi](https://github.com/guardianproject/lildebi), and you can have a Debian install running with a single click of a button. It builds up a whole Debian chroot on your phone entirely using debootstrap. You choose the release, mirror, and size of the disk image, and away it goes. It could take up to an hour on a slow device, then its done. The entire package is built from source using publicly available, repeatable builds. It even includes `gpgv` and the Debian repository keys in the apk and verifies the packages it downloads in the first stage of debootstrap before installing them. It will also check and update a SHA1 checksum to make sure your debian.img file has not be tampered with.

Then it has a simple chroot manager that `fsck`s your disk, mounts and unmounts things, and starts/stops sshd if you have it installed. You can also then use ‘apt-get’ to install any package that is released for ARM processors. This includes things like a complete real shell, Tor, TraceRouteTCP, iwconfig/ipconfig, and other security and crypto tools.

The aim of Lil&#8217; Debi is to provide a transparent and tightly integrated Debian install on your Android device. It mounts all of your Android partitions in Debian space, so you see a fusion of both systems. Its even possible to have Lil&#8217; Debi launch the normal Debian `init` start-up scripts when it starts, so that all you need to do is `apt-get install` and any servers you install will just work.

The aim is to make it work with as few modifications to the Android system as possible. Currently, it only adds a `/bin` symlink, and a `/debian` mount directory. It does not touch `/system` at all.

## Download

  * <a href="https://play.google.com/store/apps/details?id=info.guardianproject.lildebi" target="_blank">Google Play Store</a> (free)
  * <a href="https://f-droid.org/repository/browse/?fdfilter=lildebi&#038;fdid=info.guardianproject.lildebi" target="_blank">F-Droid</a>
  * direct download: [LilDebi-release-0.4.5.apk](https://guardianproject.info/releases/LilDebi-release-0.4.5.apk) 
      * [detached gpg signature](https://guardianproject.info/releases/LilDebi-release-0.4.5.apk.asc)
      * MD5: 7bbee559ee4349dd6a937f0d0585f57d
      * SHA1: 352a6049e6ac931ee4a112f60b42688d7bf1eddb
  * [nightly test builds](https://guardianproject.info/builds/LilDebi/ "nightly test builds")

### Source

  * full source (except gpgv): <a href="https://github.com/guardianproject/lildebi" target="_blank">https://github.com/guardianproject/lildebi</a>
  * gpgv is built as part of <a href="https://github.com/guardianproject/gnupg-for-android" title="GnuPG-for Android source repo" target="_blank">GnuPG-for-Android</a>

Learn more (for now), from [our blog post](https://guardianproject.info/2011/06/18/easy-installer-for-debian-on-android/).

<img class="alignnone" src="https://guardianproject.info/wp-content/uploads/2011/06/LilDebiInstalling.png" alt="" width="288" height="480" /> 

## Reporting Bugs

Please report any bugs or issues that you have with this app! We want to hear from you, no need to worry about technical details or language skills. Help us improve this software by filing bug reports about any problem that you encounter. Feature requests and patches are also welcome!

  * [<img src="https://guardianproject.info/wp-content/uploads/2011/02/reportbug-150x150.jpg" alt="report bug" width="150" height="150" class="size-thumbnail wp-image-12362" srcset="https://guardianproject.info/wp-content/uploads/2011/02/reportbug-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug-100x100.jpg 100w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug-200x200.jpg 200w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug.jpg 225w" sizes="(max-width: 150px) 100vw, 150px" /> <strong style="font-size: 200%">Report a Bug or Issue</strong>](https://github.com/guardianproject/lildebi/issues/new)

  * <a href="https://github.com/guardianproject/lildebi/issues" title="Issue Tracker" target="_blank">List of all open issues</a>
  * <a href="https://github.com/guardianproject/lildebi/issues/new" title="New Issue Tracker" target="_blank">submit a new issue report</a>