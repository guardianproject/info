---
title: 'libsqlfs: filesystem on top of SQLite/SQLCipher'
author: eighthave
date: 2011-10-27
menu:
  main:
    parent: archive
---

{{< source-code name="libsqlfs" skipjavadoc="true" >}}

libsqlfs provides a complete virtual disk on top of a SQLite or
SQLCipher database. The virtual disk is encrypted and contained in a
single file, which can be easily moved around, copied, shared,
etc. It is a standard FUSE filesytem that can work on Android,
GNU/Linux, and perhaps also macOS.
