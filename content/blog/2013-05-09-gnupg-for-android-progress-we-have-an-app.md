---
id: 3664
title: 'GnuPG for Android progress: we have an command line app!'
date: 2013-05-09T10:48:52-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=3664
permalink: /2013/05/09/gnupg-for-android-progress-we-have-an-app/
categories:
  - Development
  - New Release
  - News
tags:
  - Android
  - encryption
  - gnupg
  - gpg
  - oi2
  - open-source
  - openpgp
  - pgp
  - preview
  - psst
---
[<img src="https://guardianproject.info/wp-content/uploads/2013/05/icon-150x150.png" alt="GnuPG for Android" width="150" height="150" class="alignleft size-thumbnail wp-image-3680" srcset="https://guardianproject.info/wp-content/uploads/2013/05/icon-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2013/05/icon-300x300.png 300w, https://guardianproject.info/wp-content/uploads/2013/05/icon.png 512w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2013/05/icon.png)  
This alpha release of our command-line developer tool brings GnuPG to Android for the first time!

GNU Privacy Guard Command-Line (gpgcli) gives you command line access to the entire <a href="http://gnupg.org" title="Gnu Privacy Guard home page" target="_blank">GnuPG</a> suite of encryption software. GPG is GNU’s tool for end-to-end secure communication and encrypted data storage. This trusted protocol is the free software alternative to PGP. GnuPG 2.1 is the new modularized version of GnuPG that now supports OpenPGP and S/MIME.

You can get it from the Play Store:  
<a href="https://play.google.com/store/apps/details?id=info.guardianproject.gpg" target="_blank">https://play.google.com/store/apps/details?id=info.guardianproject.gpg</a>

Or download the `.apk` from our nightly builds:  
<a href="https://guardianproject.info/builds/GnuPrivacyGuard/" target="_blank">https://guardianproject.info/builds/GnuPrivacyGuard/</a>

## Setup

Before using gpgcli, be sure to launch the app and let it finish its installation process. Once it has completed, then you’re ready to use it. The easiest way to get started with gpgcli is to install <a href="https://play.google.com/store/apps/details?id=jackpal.androidterm" title="download Android Terminal emulator from the Google Play Store"  target="_blank">Android Terminal Emulator</a>. gpgcli will automatically configure Android Terminal Emulator as long as you have the _Allow PATH extensions</em settings enabled. 

## Features

  * TRUSTED SECURITY: This technology already seamlessly integrates into Linux on Debian, Ubuntu, Fedora, Mac OSX (GPGtools), Windows (gpg4win)
  * PUBLIC KEY ENCRYPTION: Full interoperable replacement of the proprietary Pretty Good Privacy (PGP) standard that uses a serial combination of hashing, data compression, symmetric-key cryptography and finally public-key cryptography; each step uses one of several supported algorithms.
  * BROAD ALGORITHM LANDSCAPE: Supports 3DES, AES, Blowfish, CAST5, DSA, ElGamal, MD5, RSA, RIPDE-MD-160, SHA-1, TIGER, and Twofish.
  * VERIFIABLE INTEGRITY AND AUTHENTICITY: Digital signatures create a trusted trail of ownership.
  * CONFIRMED SECURITY: Italian Police, the FBI, and British police have been unable to crack its security and have resorted to demanding private keys. It’s been likened as “the closest you’re likely to get to military-grade encryption” by cryptographer Bruce Schneier.
  * HELP SYSTEM: A quick help tool is built in.
  * KEYSERVER SUPPORT: Integrated support for HKP and LDAP keyservers (keys.gnupg.net).
  * OPEN STANDARD COMPLIANT: Full OpenPGP implementation. Learn more about standards <a href="http://tools.ietf.org/html/rfc2440" target="_blank">RFC2440</a> & <a href="http://tools.ietf.org/html/rfc4880" target="_blank">RFC4880</a> </ul> 
    ## Please Report Bugs
    
    This is an early release of a big project, so there will inevitable be bugs. Help us improve this software by filing bug reports about any problem that you encounter. Feature requests are also welcome!
    
    <a href="https://dev.guardianproject.info/projects/gpgandroid/issues" target="_blank">https://dev.guardianproject.info/projects/gpgandroid/issues</a>
    
    ## Coming Soon
    
      * SECURITY FOR APPS: We have an API in the works so that developers can  
        easily embed this into any app to give it state of the art security features.
      * GUI: We’re building a graphical user interface for easy key management.
      * STAY UP TO DATE: Sign up for our low-traffic <a href="https://lists.mayfirst.org/mailman/listinfo/guardian-dev" title="subscribe to the guardian-dev mailing list" target="_blank">Guardian-Dev</a> mailing list to  
        be notified when the API and GUI are released:  
        <a href="https://lists.mayfirst.org/mailman/listinfo/guardian-dev" target="_blank">https://lists.mayfirst.org/mailman/listinfo/guardian-dev</a>
      * Find us in IRC, we want feedback! 
          * [#guardianproject on freenode](irc://irc.freenode.net/guardianproject)
          * [#guardianproject on oftc](irc://irc.oftc.net/guardianproject)
        
        .</li> </ul>