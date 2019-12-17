---
title: 'IOCipher 64-bit builds'
author: Hans-Christoph Steiner
categories:
  - Development
  - News
tags:
  - android
  - iocipher
  - security
---

IOCipher v0.5 includes fulil 64-bit support and works with the latest
SQLCipher versions.  This means that the minimum supported SDK version
had to be bumped to _android-14_, which is still older than what
Google Play Services and Android Support libraries require.

One important thing to note is that newer SQLCipher versions require
an upgrade procedure since they changed how the data is encrypted.
Since IOCipher does use a SQLCipher database, and IOCipher virtual
disks will have to be upgraded.  That can be done by directly using the
[SQLCipher migration method](https://www.zetetic.net/sqlcipher/sqlcipher-api/#cipher_migrate)
on your IOCipher database files before opening them again.  It should
be possible to stick with SQLCipher
[v3.5.9 to avoid this](https://github.com/sqlcipher/android-database-sqlcipher/issues/446),
but this has not been tested.
