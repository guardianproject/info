---
id: 254
title: Code You Can Trust
date: 2010-05-09T00:06:46-04:00
author: n8fr8
layout: page
guid: http://guardianproject.info/?page_id=254
image: http://guardianproject.info/wp-content/uploads/2013/07/tumblr_lthb6agZVE1qlts9lo1_1280.jpg
---
The Guardian Project is about more than just apps. All of our code is open-source in order to move the collective ball forward in mobile security efforts. In addition we are building developer-focused libraries, tools and source code for you to add security-oriented features and capabilities to your own apps.

# **Connect**

  * [Guardian Project GitHub](https://github.com/guardianproject/): All of source code is hosted here, and mostly licensed under the GNU Public License v3.
  * IRC &#8211; Come hang out on IRC at #guardianproject on [freenode](http://freenode.net/irc_servers.shtml) [<a title="#GuardianProject on Freenode" href="irc://irc.freenode.net/guardianproject.net" target="_blank">Direct</a>] or [OFTC](http://www.oftc.net/oftc/) [<a title="#GuardianProject on OFTC" href="irc://irc.oftc.net/guardianproject.net" target="_blank">Direct</a>].
  * [Guardian-Dev Discussion List](https://lists.mayfirst.org/mailman/listinfo/guardian-dev): Guardian Project Developer Email List
  * Join our Developer Square Community Site: <https://talk.developersquare.net>

#<img class="alignnone" src="https://raw.githubusercontent.com/DevSqNet/DevSq/master/img/devsq_logo_sm.png" alt="" width="430" height="54" /> 

Developer Square is our new public community site for sharing, discussing, connect and learning. The main DevSq.net page offers an index of the content and resources we are promoting and sharing, while the &#8220;Talk&#8221; site (<https://talk.developersquare.net>) is a full fledged community discussion site focused on open-source, mobile app development.

# **Tools**

**CipherKit:** We have 3 tools designed for Android app developers to make apps that are able to ensure better encryption and anonymity:

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/sqlcipher"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2010/05/skitch.png" alt="" width="72" height="72" /><strong>SQLCipher: Encrypted Database</strong></a></span>  
SQLCipher is an SQLite extension that provides transparent 256-bit AES encryption of database files. It mirrors the standard android.database API. Pages are encrypted before being written to disk and are decrypted when read back.<span style="font-size: 15px; clear: left;"><br /> <a title="SQLCipher-for-Android" href="https://github.com/sqlcipher/android-database-sqlcipher" target="_blank">SQLCipher Source Code</a></span>

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/iocipher"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2010/05/skitch1.png" alt="" width="72" height="72" /><strong>IOCipher: Encrypted Virtual Disk</strong></a></span>  
IOCipher is a virtual encrypted disk for apps without requiring the device to be rooted. It uses a clone of the standard java.io API for working with files. Just password handling & opening the virtual disk are what stand between developers and fully encrypted file storage. It is based on [libsqlfs](https://github.com/guardianproject/libsqlfs "libsqlfs") and SQLCipher.  
[IOCipher Source Code](https://github.com/guardianproject/IOCipher)

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/netcipher"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2010/05/skitch2.png" alt="" width="72" height="72" /></a><a href="/code/netcipher/"><strong>NetCipher: Encrypted Network Data & Tor Integration</strong></a></span>  
NetCipher is improving network security. It provides a strong TLS/SSL verifier to help mitigate weaknesses in the certificate authority system. It eases the implementation of supporting SOCKS and HTTP proxies into applications and also supports onion routing for anonymity and traffic surveillance circumvention.  
[NetCipher Source Code](https://github.com/guardianproject/netcipher)

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/netcipher"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2016/01/round-button-hazard-150x150.png" alt="" width="72" height="72" /></a><a href="/tag/panic/"><strong>PanicKit: customizable, system-wide, app-specific panic buttons</strong></a></span>  
PanicKit is a collection of tools for letting panic trigger and panic receiver apps safely and easily connect to each other. The trigger apps are the part that the user will actual engage when in a panic situation. The receiver apps receive the trigger signal from the trigger apps when the user has initiated the panic response. The connections between trigger and receiver can be strictly enforced based on packageName and APK signing key.  
[PanicKit Source Code](https://github.com/guardianproject/panickit)

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/netcipher"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2010/05/trustedintents-150x150.png" alt="" width="72" height="72" /></a><a href="https://github.com/guardianproject/trustedintents"><strong>TrustedIntents: flexible trusted interactions between Android apps</strong></a></span>  
TrustedIntents is a library for flexible trusted interactions between Android apps. It is modeled after Android&#8217;s signature protection level for permissions. The key difference is that the framework allows the trusted signature to be set, rather than requiring to match the current app&#8217;s signature.  
[TrustedIntents Source Code](https://github.com/guardianproject/trustedintents)

[**libsqlfs**](https://github.com/guardianproject/libsqlfs)  
libsqlfs provides a complete virtual disk on top of a SQLite or SQLCipher database. The virtual disk is encrypted and contained in a single file, which can be easily moved around, copied, shared, etc. It is a standard FUSE filesytem that can work on Android, GNU/Linux, and hopefully soon Mac OS X.  
[libsqlfs GitHub code.](https://github.com/guardianproject/libsqlfs)

# **Not Maintained**

Here are some apps/libraries that we have made in the past, but are not longer maintained. For anyone interested in taking up maintenance, we will gladly help them with the process of taking the project over from us.

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/lildebi"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2010/05/lildebi.png" alt="" width="72" height="72" /></a><a href="https://guardianproject.info/code/lildebi/"><strong>Lil&#8217; Debi: Mobile Debian Installer</strong></a></span>  
Debian is an [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") composed of [open source](https://en.wikipedia.org/wiki/Free_and_open_source_software "Free and open source software") software packages mostly carrying the [GNU General Public License.](https://en.wikipedia.org/wiki/GNU_General_Public_License "GNU General Public License") Debian is one of the most popular [Linux distributions.](https://en.wikipedia.org/wiki/Linux_distribution "Linux distribution") Lil&#8217; Debi is a small version of it for phones. It builds the whole Debian chroot on a device entirely using debootstrap.  
<a href="https://github.com/guardianproject/lildebi" target="_blank">Lil&#8217; Debi GitHub code.</a>

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/gnupg"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2013/05/icon.png" alt="" width="72" height="72" /></a><a href="https://guardianproject.info/code/gnupg/"><strong>GnuPG: OpenPGP Encryption</strong></a></span>  
Gnu Privacy Guard (GnuPG) brings the OpenPGP encryption standard to Android. GnuPG combines hashing, compression, and public-key cryptography for keeping emails and files private, and for verifying that emails and files are from who you think they are. It includes an Android API and an app for keychain management.  
<a title="GnuPG Encryption" href="https://play.google.com/store/apps/details?id=info.guardianproject.gpg" target="_blank">Google Play</a> | <a title="GnuPrivacyGuard APK" href="https://guardianproject.info/builds/GnuPrivacyGuard/" target="_blank">Direct Download (.apk)</a>| [View source code](https://github.com/guardianproject/gnupg-for-android)

<span style="font-size: 15px; font-weight: bold; clear: left;"><a href="/code/ffmpeg"><img class="alignleft size-full wp-image-1018" style="margin-left: 3px; margin-right: 3px;" title="icon" src="https://guardianproject.info/wp-content/uploads/2010/05/skitch4.png" alt="" width="72" height="72" /></a><a href="https://guardianproject.info/code/ffmpeg/"><strong>ffmpeg: Media Privacy Framework</strong></a></span>  
fmpeg is a popular, widespread framework for transcoding and filtering digital videos. It’s being extended to provide a full framework for audio and image redaction, metadata management, and encryption of sensitive parts of the media. The framework is wrapped in a Java API.  
[ffmpeg source code.](https://github.com/guardianproject/android-ffmpeg)

&nbsp;