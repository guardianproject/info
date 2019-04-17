---
id: 11569
title: Keeping data private means it must be truly deletable!
date: 2013-08-23T17:36:49-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=11569
permalink: /2013/08/23/keeping-data-private-means-it-must-be-truly-deletable/
categories:
  - Research
tags:
  - cacheword
  - encryption
  - iocipher
  - panic button
  - privacy
  - psst
  - secure deletion
  - security
  - sqlcipher
  - wipe
---
[<img src="https://guardianproject.info/wp-content/uploads/2013/08/erase-hard-drive-150x150.jpg" alt="deleting data" width="150" height="150" class="alignright size-thumbnail wp-image-11598" />](https://guardianproject.info/wp-content/uploads/2013/08/erase-hard-drive.jpg)There are lots of apps these days that promise to keep your data secure, and even some that promise to wipe away private information mere seconds or minutes after it has been received. It is one thing to keep data out of view from people you don’t want seeing it, it is also important to be able to truly delete information. Unfortunately computers make it very difficult to make data truly disappear. When we tell a computer to delete a file, it only deletes the reference to the data. The data itself remains on the disk unchanged. For any UNIX geek out there, you can easily see an example of that by greping a partition (e.g. `sudo grep password /dev/sda3`. To solve this problem, there are “secure delete” options. Secure deletion removes the reference like regular deletion, then wipes the data on the disk by overwriting it with random data. That’s much better, but not always good enough. It turns out that its possible to remove the hard disk and read magnetic residue and recover even wiped data.

Mobile devices only make that problem worse because they almost always rely on flash memory for disk storage. Flash memory has wear-leveling programming built into it, so it is not possible to guarantee that a file will be wiped without overwriting the whole flash disk, then deleting it all and overwriting the whole thing again. Not only is it not practical to delete the whole disk just to remove one file, it also takes a long time.

[<img src="https://guardianproject.info/wp-content/uploads/2013/08/coldbootattack-300x199.jpg" alt="" width="300" height="199" class="alignleft size-medium wp-image-11600" srcset="https://guardianproject.info/wp-content/uploads/2013/08/coldbootattack-300x199.jpg 300w, https://guardianproject.info/wp-content/uploads/2013/08/coldbootattack.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2013/08/coldbootattack.jpg)So what can we do about this? Use encryption! [<a href="http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.225.6872" title="Secure Data Deletion for USB Flash Memory (2011)" target="_blank">1</a>] If the data is encrypted before its written to either a classic hard drive or flash memory disk, then the actual data is never on the disk itself. If the data is encrypted with a good passphrase, then just “forgetting” the key will make it basically impossible to recover the data. Additionally, encrypted data looks like random data, so it is easy to hide the deleted, encrypted data from the recovery techniques by adding random garbage to the disk. It turns out that with the right architecture, a key can be forgotten quite quickly, much quicker than even the most basic secure deletion.

This logic is built into our new passphrase library <a href="https://github.com/guardianproject/cacheword" target="_blank">Cacheword</a>. Cacheword is a library for securely working with and caching passphrases. It plugs right into <a href="https://guardianproject.info/code/sqlcipher" target="_blank">SQLCipher for Android</a> and <a href="https://guardianproject.info/code/iocipher" target="_blank">IOCipher</a>. SQLCipher and IOCipher are both ways for easily storing data using strong AES-256 encryption. Cacheword then handles getting the passphrase from the user. Instead of feeding that passphrase directly to SQLCipher or IOCipher, it creates an encrypted file for storing a strong AES-256 key and that is what is used to lock SQLCipher and IOCipher. The user’s passphrase then just unlocks that encrypted key file.

The means you can get rapid deletion of data stores of any size by just deleting the key file. The user never sees the actual key so they cannot divulge it. Since the user’s passphrase is not the key for the data but instead the key to the Cacheword key file, the secure deletion can first focus on that key file. The key file is small, so that can happen very quickly. Then even if the data files are recovered, the user does not has the passphrase to the data, its only locked away in the now deleted key file. The key was stored encrypted, so a standard deletion will provide decent protection: it will look like random data on the disk.

To really ensure the key and the data is gone for good, an app can implement a full wiping procedure. Normal wiping procedures can follow as a background task, making it harder and harder to recover the data, no matter who the adversary is. The full wiping procedure would go something like this (with a rough timeframe for each step):

  1. Cacheword wipes the passphrase from memory (nanoseconds to milliseconds)
  2. the Cacheword key file is deleted (milliseconds)
  3. write random garbage to disk patterned after the key file to obscure the deleted key file (milliseconds to minutes)
  4. delete the SQLCipher/IOCipher data files (seconds to minutes)
  5. fill entire memory (RAM) with random garbage (minutes to hours)
  6. fill entire disk with random garbage (hours)
  7. power off device

That’s the overview of the process. But of course, there are always annoying technical details, and I’ll continue on about some of them, for those who like such things.

To start with, the user’s passphrase will most likely be stored in memory by code outside of Cacheword, SQLCipher, and IOCipher. For example, the Android text entry widget will have the passphrase pass thru it, and inevitably will store that data in memory. It is up to the garbage collection to remove that from memory, and the garbage collection might not zero out the memory before deallocating it. We’re still looking into ideas for how to trigger that, and would love to hear suggestions.

To truly wipe the data from the disk, there would need to be multiple passes where the entire disk is filled up then the entire disk is deleted. That is rarely practical. So hiding the existence of the encrypted data stores is difficult to do in practice. The encrypted data will remain encrypted with AES-256 using a random, full length key, so it would be basically impossible to crack using publicly known technology and techniques.

The best bet for preventing the most advanced adversary from getting the deleted data would involve a few cycles of rebooting, filling up the memory and disk with random garbage after doing the procedure outlined above. A more rapid version of that would be to delay filling the disk until after a reboot. That would ensure that the key to the data is thoroughly wiped as quickly as possible before starting in on the much less important and long lasting task of wiping the entire disk to hide the deleted data files.