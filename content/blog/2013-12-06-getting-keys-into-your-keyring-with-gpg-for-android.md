---
id: 12148
title: Getting keys into your keyring with Gnu Privacy Guard for Android
date: 2013-12-06T15:11:53-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12148
permalink: /2013/12/06/getting-keys-into-your-keyring-with-gpg-for-android/
image: http://guardianproject.info/wp-content/uploads/2013/12/0x9F0FE587374BBE81-qr.png
categories:
  - HowTo
tags:
  - android
  - encryption
  - gnupg
  - gpg
  - howto
  - identity
  - open-source
  - openpgp
  - pgp
  - privacy
  - psst
  - security
---
Now that you can have a full <a href="https://www.gnupg.org" target="_blank"><em>GnuPG</em></a> on your Android device with <a href="https://play.google.com/store/apps/details?id=info.guardianproject.gpg" target="_blank"><em>Gnu Privacy Guard</em></a> for Android, the next step is getting keys you need onto your device and included in _Gnu Privacy Guard_. We have tried to make it as easy as possible without compromising privacy, and have implemented a few approaches, while working on others. There are a few ways to get this done right now.

_Gnu Privacy Guard_ registered itself with Android as a handler of all the standard <a href="https://www.rfc-editor.org/rfc/rfc3156.txt" title="RFC3156: MIME Security with OpenPGP" target="_blank">OpenPGP MIME types</a> (`application/pgp-keys`, `application/pgp-encrypted`, `application/pgp-signature`), as well as all of the OpenPGP and GnuPG file extensions (`.pkr` `.skr` `.key` `.sig` `.asc` `.gpg` `.bin`). This means that users just have to share a file to _Gnu Privacy Guard_ using any of the standard Android methods, these files can be launched from an email attachment, opened from the SD card using a file browser, clicked in the Downloads view, etc.

So if you want to quickly send your whole public keyring from your laptop to your mobile device, you can just grab the database file directly from _GnuPG_ and copy it to your SD card. Here is how:

  1. plug your device into your laptop via USB so you can copy files to the SD card
  2. find your _GnuPG_ home folder (on GNU/Linux and Mac OS X, it will be in `~/.gnupg/pubring.gpg`, on Windows it is `%APPDATA%\gnupg`)
  3. In your _GnuPG_ home folder, copy **pubring.gpg** to your device’s SD card
  4. unmount and unplug your device
  5. on your device, open your favorite file manager app (<a href="https://play.google.com/store/apps/details?id=org.openintents.filemanager" target="_blank"><em>OI File Manager</em></a>, _Astro_, etc)
  6. go to the SD card
  7. long-click on **pubring.gpg** and share it to _Gnu Privacy Guard_
  8. click OK on the Import Keys dialog

After that, _Gnu Privacy Guard_ will do the rest. Give is some time to sync to the Contacts database, then you’ll see all of your keys from your desktop are now in your People app and are listed in _Gnu Privacy Guard_ itself. You can now encrypt files to any of those keys, or verify files signed by any of those keys. Here are a couple screenshots to illustrate key points in the process, using _OI File Manager_:

<p align="center">
  <div id="attachment_12155" style="width: 209px" class="wp-caption alignleft">
    <a href="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-0.png"><img aria-describedby="caption-attachment-12155" src="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-0-199x300.png" alt="send your public keyring file" width="199" height="300" class="size-medium wp-image-12155" srcset="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-0-199x300.png 199w, https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-0.png 319w" sizes="(max-width: 199px) 100vw, 199px" /></a>
    
    <p id="caption-attachment-12155" class="wp-caption-text">
      1. send your public keyring file
    </p>
  </div>
</p>

<div id="attachment_12156" style="width: 209px" class="wp-caption alignright">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-1.png"><img aria-describedby="caption-attachment-12156" src="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-1-199x300.png" alt="choose Gnu Privacy Guard to send the file to" width="199" height="300" class="size-medium wp-image-12156" srcset="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-1-199x300.png 199w, https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-1.png 319w" sizes="(max-width: 199px) 100vw, 199px" /></a>
  
  <p id="caption-attachment-12156" class="wp-caption-text">
    2. choose <em>Gnu Privacy Guard</em> to send the file to
  </p>
</div>

<div id="attachment_12157" style="width: 209px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-2.png"><img aria-describedby="caption-attachment-12157" src="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-2-199x300.png" alt="click OK to import the key file" width="199" height="300" class="size-medium wp-image-12157" srcset="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-2-199x300.png 199w, https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-2.png 319w" sizes="(max-width: 199px) 100vw, 199px" /></a>
  
  <p id="caption-attachment-12157" class="wp-caption-text">
    3. click OK to import the key file
  </p>
</div>

<div id="attachment_12158" style="width: 209px" class="wp-caption alignright">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-3.png"><img aria-describedby="caption-attachment-12158" src="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-3-199x300.png" alt="now you can see the imported keys in Gnu Privacy Guard" width="199" height="300" class="size-medium wp-image-12158" srcset="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-3-199x300.png 199w, https://guardianproject.info/wp-content/uploads/2013/12/GPGA-import-key-file-3.png 319w" sizes="(max-width: 199px) 100vw, 199px" /></a>
  
  <p id="caption-attachment-12158" class="wp-caption-text">
    4. now you can see the imported keys in <em>Gnu Privacy Guard</em>
  </p>
</div>

* * *

There are many ways to get the keyring files like **pubring.gpg** to your device: you can also share the keyring files via email, chat, or even services like _Dropbox_ or _Google Drive_. Then once the files are on your device, you can import them using the same procedure as above. But keep in mind that you are sending your whole collection of secure contacts to that service, which will have full access to read it. If you have any worries about leaking your keyring to anyone, then a good method is to copy it directly to the SD card.

<div id="attachment_12192" style="width: 209px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-search-keyserver.png"><img aria-describedby="caption-attachment-12192" src="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-search-keyserver-199x300.png" alt="search the keyserver for the author's key (I lost the key from 1998, so don't use that one...)" width="199" height="300" class="size-medium wp-image-12192" srcset="https://guardianproject.info/wp-content/uploads/2013/12/GPGA-search-keyserver-199x300.png 199w, https://guardianproject.info/wp-content/uploads/2013/12/GPGA-search-keyserver.png 319w" sizes="(max-width: 199px) 100vw, 199px" /></a>
  
  <p id="caption-attachment-12192" class="wp-caption-text">
    search the keyserver for the author’s key (the key from 1998 is lost, don’t use that one…)
  </p>
</div>

  
You can also search and download keys via the public pool of OpenPGP keyservers. If you already know someone’s keyid or fingerprint, you can search using that. Otherwise, you can search based on name or email address. But be careful! Downloading a key from a keyserver does not give you a key you can trust. Anyone can upload a key to the keyservers, and they can make that key have any name or email address. Downloading from the keyservers is a convenient way to download a key, but you must verify the key’s fingerprint with the person you are trying to find.

<div id="attachment_12184" style="width: 160px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/0x9F0FE587374BBE81-qr.png"><img aria-describedby="caption-attachment-12184" src="https://guardianproject.info/wp-content/uploads/2013/12/0x9F0FE587374BBE81-qr-150x150.png" alt="scan this QR Code to get the author's OpenPGP key" width="150" height="150" class="size-thumbnail wp-image-12184" srcset="https://guardianproject.info/wp-content/uploads/2013/12/0x9F0FE587374BBE81-qr-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2013/12/0x9F0FE587374BBE81-qr-300x300.png 300w, https://guardianproject.info/wp-content/uploads/2013/12/0x9F0FE587374BBE81-qr.png 330w" sizes="(max-width: 150px) 100vw, 150px" /></a>
  
  <p id="caption-attachment-12184" class="wp-caption-text">
    scan this QR Code to get the author’s OpenPGP key
  </p>
</div>In conjunction with the 

<a href="http://web.monkeysphere.info/" target="_blank">Monkeysphere</a> project, we developed a standard URI scheme for sending OpenPGP key fingerprints. For example, you can find my key ID here: [`openpgp4fpr:9F0FE587374BBE81`](openpgp4fpr:9F0FE587374BBE81). This provides a clickable way to get an OpenPGP key. On an Android device with _Gnu Privacy Guard_ installed, you can click on this link to download my key from the keyservers. This URI scheme also works well in QR Codes. Scan this QR Code on your device with an app like <a href="https://play.google.com/store/apps/details?id=com.google.zxing.client.android" title="Barcode Scanner in the Google Play Store" target="_blank"><em>Barcode Scanner</em></a>, and click **Open Browser**, and Gnu Privacy Guard will download my key to your device.

There are other ideas out there that we also want to support. For example, <a href="http://sufficientlysecure.org/index.php/openpgp-keychain/" target="_blank"><em>OpenPGP Keychain</em></a> includes a way to transmit the whole public key via <a href="https://en.wikipedia.org/wiki/Near_field_communication" title="Near Field Communication" target="_blank">NFC</a>. This allows people can swap keys directly from phone to phone without having internet access at all. But NFC is quite slow to transmit data so the devices need to be held together for a while until the whole key is received. NFC could be used to rapidly transmit an `openpgp4fpr:` URI, and then the whole public key would be fetched from a keyserver, but that then requires internet access and also leaks a bit of metadata to the internet. A better technique would be to transmit the entire public key over Bluetooth, using NFC to setup the Bluetooth session. We’re also looking at ways to do this via WiFi and <a href="https://en.wikipedia.org/wiki/Bonjour_(software)" target="_blank">Bonjour (mDNS)</a> local service advertisements.