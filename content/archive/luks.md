---
id: 665
title: 'LUKS: Disk Encryption'
date: 2011-02-19T09:05:06-04:00
author: n8fr8
layout: page
guid: http://guardianproject.info/
publish_post_category:
  - "5"
publish_to_discourse:
  - "0"
menu:
  main:
    parent: archive
aliases:
  - code/luks
---
If you are looking for the homepage for LUKS, you can find it here: [**https://gitlab.com/cryptsetup/cryptsetup/**](https://gitlab.com/cryptsetup/cryptsetup/)

We are not the creators or maintainers of LUKS. We simply got it working on Android a long, long time ago!

* * *

LUKS is the standard for Linux hard disk encryption. By providing a standard on-disk-format, it does not only facilitate compatibility among distributions, but also provides secure management of multiple user passwords. In contrast to existing solution, LUKS stores all setup necessary setup information in the partition header, enabling the user to transport or migrate his data seamlessly.

This project is the port of LUKS to Android. You can find more information on the current status here: <https://github.com/guardianproject/luks/wiki>

[<img class="alignnone size-full wp-image-966" title="luks-logo-cropped" src="https://guardianproject.info/wp-content/uploads/2011/02/luks-logo-cropped.png" alt="" width="330" height="112" srcset="https://guardianproject.info/wp-content/uploads/2011/02/luks-logo-cropped.png 330w, https://guardianproject.info/wp-content/uploads/2011/02/luks-logo-cropped-300x101.png 300w" sizes="(max-width: 330px) 100vw, 330px" />](https://guardianproject.info/wp-content/uploads/2011/02/luks-logo-cropped.png)

### Design

LUKS was designed according to TKS1, a template design developed in [TKS1](http://code.google.com/p/cryptsetup/wiki/TKS1) for secure key setup. LUKS closely reassembles the structure recommended in the TKS1 paper, but also adds meta data for cipher setup management and LUKS also supports for multiple keys/passphrases.

### <a name="Why_LUKS?"></a>Why LUKS?

  * compatiblity via standardization,
  * secure against low entropy attacks,
  * support for multiple keys,
  * effective passphrase revocation,
  * free

The original LUKS CryptSetup project is here: <http://code.google.com/p/cryptsetup/>