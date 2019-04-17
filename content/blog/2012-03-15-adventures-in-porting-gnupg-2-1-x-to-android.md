---
id: 1628
title: 'Adventures in Porting: GnuPG 2.1.x to Android!'
date: 2012-03-15T13:00:30-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=1628
permalink: /2012/03/15/adventures-in-porting-gnupg-2-1-x-to-android/
categories:
  - Development
  - News
tags:
  - android
  - gnu privacy guard
  - gnupg
  - gpg
  - gpgme
  - java
  - jni
  - native
  - open-source
  - openpgp
  - porting
  - preview
  - prototype
---
PGP started with Phil Zimmerman&#8217;s Pretty Good Privacy, which is now turned into an open IETF standard known as OpenPGP. These days, the reference OpenPGP platform seems to be [GnuPG](http://gnupg.org/): its used by Debian and all its derivatives in the OS itself for verifying packages and more. It is also at the core of all Debian development work, allowing the very diffuse body of Debian, Ubuntu, etc developers to communicate and share work effectively while maintaining a high level of security. It is also used for email encryption in Thunderbird + Enigmail, Apple Mail + GPGMail, GNOME Evolution, KDE KMail, Microsoft Outlook + Gpg4win.

<div id="attachment_1651" style="width: 160px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2012/03/Encryption.jpg"><img aria-describedby="caption-attachment-1651" src="https://guardianproject.info/wp-content/uploads/2012/03/Encryption-150x150.jpg" alt="lots of one and zeros" width="150" height="150" class="size-thumbnail wp-image-1651" /></a>
  
  <p id="caption-attachment-1651" class="wp-caption-text">
    Yes, encryption means lots of ones and zeros that you can't read!
  </p>
</div>

After actively using GnuPG for a few years, I thought it would be a good idea and not too difficult to port it to Android. I dove in and started with the code from git since I was hoping to involve the GnuPG developers. I had recently seen that they were stopping development on the 1.4.x branch, so the 2.1.x branch seemed like the logical choice to give us a reasonably complete OpenPGP implementation. Now I am happy to say we have it working on Android, with a couple of loose ends to tie up in order to get everything working.

One thing I do have to say is that GnuPG has evolved into a large and elaborate project that not only covers OpenPGP, but also PGP/MIME and things that have nothing to do with PGP like AES symmetric encryption and S/MIME email cryptography. That means it know is made up of many moving parts. It uses many libraries: libassuan, libgpg-error, libksba, npth, openldap, pinentry, and more if you want. It is also made up of a handful of programs to handle different aspects: `gpg` is the command line interface, `gpg-agent` seems to be the central key handler and task broker, `dirmngr` manages connections with directories like OpenPGP keyservers, `pinentry` handles getting passphrases from the user, etc.

The complexity does not stop there for our purposes: we need a Java API so we can make an Android app. So next up we built the <a href="http://www.gnupg.org/related_software/gpgme/" target="_blank">GPGME</a> (Gnu Privacy Guard Made Easy) library to provide a C/C++ API which is then wrapped in <a href="https://github.com/smartrevolution/gnupg-for-java" target="_blank">gpgme-for-java</a>, a JNI library to make the GPGME functions available in Java. And just to heap on the layers, we are making a GUI on top of all that so that when you use it, you have no idea that all these little pieces that I have just described are even there at all. 

You can follow our progress on this work on our <a href="https://guardianproject.info/wiki/PSST" target="_blank">PSST wiki: https://guardianproject.info/wiki/PSST</a>

_(coming soon: sketching a mobile UI for OpenPGP, follow our notes here: <a href="https://guardianproject.info/wiki/GnuPrivacyGuard_for_Android" target="_blank">https://guardianproject.info/wiki/GnuPrivacyGuard_for_Android</a>)_