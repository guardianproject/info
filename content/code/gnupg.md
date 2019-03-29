---
id: 2873
title: 'GnuPG: OpenPGP Encryption'
date: 2012-10-04T00:42:29-04:00
author: mark
layout: page
guid: https://guardianproject.info/?page_id=2873
has_been_saved:
  - "1"
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "405"
discourse_permalink:
  - https://talk.developersquare.net/t/gnupg-openpgp-encryption/285
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":285,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1551701545"
wpdc_sync_post_comments:
  - "0"
menu:
  main:
    parent: code
---
This project is **UNMAINTAINED**, we recommend [OpenKeychain](https://www.openkeychain.org/) instead. The core porting work has all be included upstream in the official <a href="https://gnupg.org" target="_blank">GnuPG</a> source repositories. The Android app needs a new maintainer. This could be you! Email us at <a href="&#109;&#x61;&#105;&#x6c;t&#x6f;:&#x73;u&#x70;p&#x6f;r&#x74;&#64;&#103;&#x75;&#97;&#x72;&#100;&#x69;a&#x6e;p&#x72;o&#x6a;e&#x63;t&#x2e;i&#110;&#x66;&#111;" target="_blank">s&#117;&#x70;&#x70;o&#114;&#x74;&#x40;g&#117;&#x61;&#x72;d&#105;&#x61;&#x6e;p&#114;&#x6f;&#x6a;e&#99;&#x74;&#x2e;i&#110;&#x66;&#x6f;</a>

[<img src="https://guardianproject.info/wp-content/uploads/2013/05/icon-150x150.png" alt="GnuPG for Android" width="150" height="150" class="alignleft size-thumbnail wp-image-3680" srcset="https://guardianproject.info/wp-content/uploads/2013/05/icon-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2013/05/icon-300x300.png 300w, https://guardianproject.info/wp-content/uploads/2013/05/icon.png 512w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2013/05/icon.png)Gnu Privacy Guard (GnuPG) for Android brings the widespread standard in OpenPGP encryption to Android. GnuPG provides solid encryption for keeping emails and files private, and for verifying that emails and files are who you think they are. GnuPG is built-in to basically every GNU/Linux distro, in <a href="https://gpgtools.org/" target="_blank">GPGTools</a> for Mac OS X and Apple Mail, a <a href="http://gpg4win.org/" target="_blank">GPG4Win</a> for Windows and Outlook, <a href="https://www.enigmail.net/" target="_blank">Enigmail</a> for Thunderbird, etc. We are working to bring GnuPG to Android to make it the cornerstone of Android encryption like it is elsewhere.

We are actively working on an API so that developers can easily embed this into any app to give it state of the art security features. We’re also building a graphical user interface for easy key management. You can <a href="https://dev.guardianproject.info/projects/gpgandroid/wiki/API_Sketch" target="_blank">follow our progress on our wiki</a>.

### Command Line Usage

If you want to use the command line, the easiest way to get started with GPG is to install Android Terminal Emulator. GPG will automatically configure Android Terminal Emulator as long as you have the &#8220;_Allow PATH extensions_&#8221; settings enabled. Get the <a href="https://play.google.com/store/apps/details?id=jackpal.androidterm" target="_blank">Android Terminal Emulator</a>.

### Source

  * full source: <a href="https://github.com/guardianproject/gnupg-for-android" target="_blank">https://github.com/guardianproject/gnupg-for-android</a>