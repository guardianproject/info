---
id: 1321
title: SQLCipher for Android v1 FINAL!
date: 2011-11-29T18:17:47-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=1321
permalink: /2011/11/29/sqlcipher-for-android-v1-final/
bigimg: [{src: "http://guardianproject.info/wp-content/uploads/2011/11/logo-sqlcipher-android.png",}]
categories:
  - Development
  - New Release
  - News
---
 

Team GP along with the good folks at [Zetetic](http://zetetic.net/), are happy to announce that we have reached _**FINAL**_ on our first release (“v1” 0.0.6 build) of [SQLCipher for Android](https://guardianproject.info/code/sqlcipher/). This means we consider this a production release, ready for shipping with your apps to provide for reliable, open-source, secure application data encryption.



If you need a refresher, here is what the cross-platform, open-source [SQLCipher](http://sqlcipher.net/) provides:

> SQLCipher is an [SQLite](http://sqlite.org/) extension that provides transparent 256-bit AES encryption of database files. Pages are encrypted before being written to disk and are decrypted when read back. Due to the small footprint and great performance it’s ideal for protecting embedded application databases and is well suited for mobile development.
> 
>   * Blazing fast performance with as little as 5-15% overhead for encryption on many operations
>   * 100% of data in the database file is encrypted
>   * Uses good security practices (CBC mode, key derivation)
>   * Zero-configuration and application level cryptography
>   * Broad platform support: works with C/C++, Obj-C, QT, Win32/.NET, Java, Python, Ruby, etc on Windows, Linux, iPhone/iOS…
>   * Algorithms provided by the peer reviewed [OpenSSL](http://openssl.org/) crypto library.

In addition to our work porting the core codebase, the work done on Android also provides near exact API compatibility with the default [Android Database API](http://developer.android.com/reference/android/database/package-summary.html). This means that developers can drop in SQLCipher, and add data encryption to their application, with very little changes to their existing codebase.

Finally, while full disk encryption is offered newer Android devices from Motorola, and those running Android 3.x Honeycomb or 4.x Ice Cream Sandwich, that only provides encryption of the entire internal or external storage, which must be unlocked and decrypted when the device is booted. The SQLCipher model ensures only a limited amount of data from your app is accessible at anytime, and allows the user or the app to lock itself down, whether or not the device itself is locked or encryption.

> **Download the Software Development Kit here for integration with your Android apps: <https://github.com/downloads/guardianproject/android-database-sqlcipher/SQLCipherForAndroid-SDK-0.0.6-FINAL.zip>**

You can see all the [closed issues addressed](https://github.com/guardianproject/android-database-sqlcipher/issues?sort=updated&direction=desc&state=closed&page=1) in this release.

If you want to build from source, you will need the Android NDK, as well as the SDK. Pull the repo, and run ‘make all’ with the included [SQLCipher Makefile](https://github.com/guardianproject/android-database-sqlcipher/blob/master/Makefile).

Our partners at [Zetetic](http://zetetic.net/) have published a [step-by-step application integration tutorial](http://sqlcipher.net/sqlcipher-for-android/).[  
](http://sqlcipher.net/sqlcipher-for-android/) [<img class="alignnone size-medium wp-image-1345" title="eclipse-class-libraries" src="https://guardianproject.info/wp-content/uploads/2011/11/eclipse-class-libraries-300x214.png" alt="" width="300" height="214" srcset="https://guardianproject.info/wp-content/uploads/2011/11/eclipse-class-libraries-300x214.png 300w, https://guardianproject.info/wp-content/uploads/2011/11/eclipse-class-libraries.png 754w" sizes="(max-width: 300px) 100vw, 300px" />](http://sqlcipher.net/sqlcipher-for-android/)[  
](http://sqlcipher.net/sqlcipher-for-android/) 

You can also get started by working with our [sample ‘NoteCipher’ project available on Github](https://github.com/guardianproject/notepadbot).

If you happen to encounter them, [please report any unexpected behaviours](https://github.com/guardianproject/android-database-sqlcipher/issues/new), bugs, typos or other abnormalities, as soon as you can. We know there are still some [outstanding issues](https://github.com/guardianproject/android-database-sqlcipher/issues?sort=updated&direction=desc&state=open) faced in some cases, but we did not consider them blockers.

SQLCipher for Android Home: <https://guardianproject.info/code/sqlcipher/>