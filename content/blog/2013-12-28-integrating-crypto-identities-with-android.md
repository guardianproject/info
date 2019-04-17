---
id: 12206
title: Integrating Crypto Identities with Android
date: 2013-12-28T19:42:56-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12206
permalink: /2013/12/28/integrating-crypto-identities-with-android/
categories:
  - Research
tags:
  - android
  - encryption
  - gnupg
  - gpg
  - identity
  - openpgp
  - otr
  - pgp
  - psst
  - usability
---
[<img src="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg" alt="alberti cipher disk" width="50" height="50" class="alignleft size-thumbnail wp-image-3079" srcset="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg 245w" sizes="(max-width: 50px) 100vw, 50px" />](https://en.wikipedia.org/wiki/Alberti_cipher_disk)ver the past couple of years, Android has included a central database for managing information about people, it is known as the <a href="https://developer.android.com/reference/android/provider/ContactsContract.html" target="_blank"><code>ContactsContract</code></a> (that&#8217;s a mouthful). Android then provides the _People_ app and reusable interface chunks to choose contacts that work with all the information in the `ContactsContract` database. Any time that you are adding an account in the _Settings_ app, you are setting up this integration. You can see it with Google services, _Skype_, _Facebook_, and many more. This system has a lot of advantages, including: 

  * a unified user experience for finding and managing data about people
  * apps can launch common interface dialogs and screens for working with that database without having to write custom versions (launching `Activity`s via `Intent`s
  * streamlined methods for building custom UIs based on the contacts database

With our work porting <a href="https://www.gnupg.org/" target="_blank">GnuPG</a> to Android, we want <a href="https://guardianproject.info/code/gnupg/" target="_blank"><em>Gnu Privacy Guard</em></a> for Android to be fully integrated into the Android experience. _Gnu Privacy Guard_ registers itself as a handler for all OpenPGP file and data types in Android, so users can work with these files using standard Android methods like Share/Send buttons. Or users can start by finding the person to encrypt to in the _People_ app, then choosing the file. These flows make it intuitive to Android users, and means we have to write less code because it taps into existing Android systems. With the past release, v0.2, we laid the foundations for having the GnuPG keyring integrated into this contacts database. The next release, v0.3 will improve contacts integration a lot.

<div id="attachment_12225" style="width: 560px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/gpg-contacts-integration.png"><img aria-describedby="caption-attachment-12225" src="https://guardianproject.info/wp-content/uploads/2013/12/gpg-contacts-integration-1024x640.png" alt="All of these contacts come from the GnuPG keyring being synced to the ContactsContract.  Nathan&#039;s contact is made up of combined info from Gnu Privacy Guard and Google. To encrypt a file to the author, select Encrypt File to... on his contact page." width="550" height="343" class="size-large wp-image-12225" srcset="https://guardianproject.info/wp-content/uploads/2013/12/gpg-contacts-integration-1024x640.png 1024w, https://guardianproject.info/wp-content/uploads/2013/12/gpg-contacts-integration-300x187.png 300w" sizes="(max-width: 550px) 100vw, 550px" /></a>
  
  <p id="caption-attachment-12225" class="wp-caption-text">
    All of these contacts come from the GnuPG keyring being synced to the <code>ContactsContract</code>. Nathan&#8217;s contact is made up of combined info from <em>Gnu Privacy Guard</em> and Google. To encrypt a file to the author, select <strong>Encrypt file to&#8230;</strong> on his contact page.
  </p>
</div>

One of the concerns that has been voiced about integrating with the `ContactsContract` database is that all the data put there will be then uploaded to the other accounts, like the Google account of the phone, or other accounts. As far as we can tell, there is no automatic syncing of data between accounts in the `ContactsContract`, instead it is a system of individual, local databases. We have not confirmed this with a code audit whether there is any data leakage from `ContactsContract`, and would love to hear more information on that. There is a layer of matching rules for locally merging those local databases into a single, unified view of that data. A good example of this unified data view in action is the built-in _People_ app. It will show data from all of the local databases, and it will link profiles together in a single view based on programmatic rules that look at email addresses, names, etc. In any case, _Gnu Privacy Guard_ only syncs one way. It treats the GnuPG keyring as canonical and clones the GnuPG keyring contacts to the `ContactsContract` whenever a sync is run. The sync process never reads from the `ContactsContract`, and currently no data is ever imported from it. So at the very least, the ContactsContract should not serve as a point to inject data into the GnuPG keyring.

<div id="attachment_12211" style="width: 330px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2013/12/ContactsContract.png"><img aria-describedby="caption-attachment-12211" src="https://guardianproject.info/wp-content/uploads/2013/12/ContactsContract.png" alt="The ContactsContract builds up the complete view of all contacts based on RawContacts provided by each account type, which are in turn built up of standard data types like name, email, phone number, etc." width="320" height="189" class="size-full wp-image-12211" srcset="https://guardianproject.info/wp-content/uploads/2013/12/ContactsContract.png 320w, https://guardianproject.info/wp-content/uploads/2013/12/ContactsContract-300x177.png 300w" sizes="(max-width: 320px) 100vw, 320px" /></a>
  
  <p id="caption-attachment-12211" class="wp-caption-text">
    The <code>ContactsContract</code> builds up the complete view of all contacts based on <code>RawContacts</code> provided by each account type, which are in turn built up of standard data types like name, email, phone number, etc.
  </p>
</div>

One unexplored idea is for apps that need to use crypto to use only the standard Android contacts API to fetch crypto identity information like public keys and fingerprints. For example, PGP email app <a href="https://play.google.com/store/apps/details?id=com.fsck.k9" target="_blank"><em>K-9</em></a> could look up OpenPGP info at the same time it is looking in the contacts database for email addresses. It probably even makes sense for _K-9_ to offload even more to an OpenPGP provider, and have _K-9_ just query the PGP provider whether there is a signing key available, whether the receiver has a PGP key, etc.

It is also tempting to think about using a similar technique for storing other types of keys like OTR keys for secure chat. The hard part is that OTR has no method built-in to the key for verifying whether that key is trusted. OpenPGP has key signing and the Web-of-Trust, with all of its issues, but the OpenPGP security model is designed around untrusted methods of moving public key data around. Using the contacts database for moving around public key material for later verification will work equally well for OTR, OpenPGP, etc.

On a similar note, we are also working with Dominik Schürmann and the _K-9_ devs to create <a href="https://dev.guardianproject.info/projects/gpgandroid/wiki/API_Sketch" target="_blank">a common Android API for a generic OpenPGP provider</a>. This is similar to the contacts system in recent versions of Android in that there is a single, central contacts system that any app can tap into for managing data related to people.

We have decided to go with Dominik Schürmann&#8217;s approach of using an AIDL API to an Android Service. AIDL does have some downsides mostly around it being overcomplicated. But AIDL is the main Android method for inter-process communication with `Service`s, so we are stuck with it, more or less. The beautiful thing is that this arrangement will make it possible for apps to fully offload the crypto handling to the `Service`, including all the required GUI bits like passphrase prompting, progress dialog overlays, key selection, etc.

[<img src="https://guardianproject.info/wp-content/uploads/2013/12/public-key-encryption-cartoon-300x292.jpg" alt="contacts with keys" width="300" height="292" class="alignright size-medium wp-image-12212" srcset="https://guardianproject.info/wp-content/uploads/2013/12/public-key-encryption-cartoon-300x292.jpg 300w, https://guardianproject.info/wp-content/uploads/2013/12/public-key-encryption-cartoon.jpg 414w" sizes="(max-width: 300px) 100vw, 300px" />](http://csunplugged.org/public-key-encryption)For example of how this idea would work, we can look at _K-9_ email again. If an incoming email includes a public key or fingerprint, either of these can be sent to the OpenPGP provider for importing. An `OPENPGP4FPR:` URI will trigger downloading the public key from a keyserver. A public key contained in an attached file will be received by the OpenPGP provider via the Android file associations, which will then prompts the user to import it. When _K-9_ goes to send a OpenPGP-encrypted email to that new key, it checks the ContactsContract to see whether the recipient has a OpenPGP key. If so, it sends the email to the OpenPGP provider to be encrypted. The OpenPGP provider can then look up which key to use in it&#8217;s local keyring by using the recipient&#8217;s email address. If there are multiple keys for that email address, it prompts the user to choose. It could also base it&#8217;s choice on the OpenPGP trust level for that key.

These are currently all ideas for how GnuPG can be integrated into Android. Some of these are implemented and ready for you to try out on your device. The common OpenPGP provider idea is still very much a work in progress.