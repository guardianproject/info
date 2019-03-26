---
id: 12819
title: First working test of IOCipher for Obj-C
date: 2015-01-26T04:32:29-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12819
permalink: /2015/01/26/first-working-test-of-iocipher-for-obj-c/
spacious_page_layout:
  - default_layout
categories:
  - News
tags:
  - android
  - encryption
  - full disk encryption
  - hsm
  - iocipher
  - ios
  - mobile
  - obj-c
  - osx
  - prototype
  - security
  - smartcard
  - sqlcipher
---
[<img src="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg" alt="alberti cipher disk" width="150" height="150" class="alignright size-thumbnail wp-image-3079" srcset="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg 245w" sizes="(max-width: 150px) 100vw, 150px" />](/code/iocipher)Every so often, we revisit our core libraries in the process of improving our existing apps, and creating new ones. IOCipher has become a standard part of our apps since it provides a really easy way to include encrypted file storage in Android apps. And we are now working on spreading it to iOS as well, headed up by Chris Ballinger, with the first preliminary tests of <a href="https://github.com/ChatSecure/IOCipher-ObjC" target="_blank">IOCipher for Obj-C</a>. Testing and contributions are most welcome! Find us in our <a href="/contact/" target="_blank">chat room or mailing list</a> for questions, or just post a comment below! Since the iOS version is based on the exact same core library, libsqlfs, the container files they produce will also be fully compatible with each other.

Now that iOS 8 has full disk encryption by default and a <a href="https://www.blackbagtech.com/blog/2014/09/24/ios-8-and-its-impact-on-investigations" title="iOS 8 and its Impact on Investigations" target="_blank">host of other security improvements</a>, you might be wondering why you would bother with app-specific encryption. The problem with full disk encryption is that the disk is only locked when your iPhone is fully turned off. Using IOCipher adds protection for sensitive data that helps in a few different scenarios.

First, full disk encryption does not protect the data at all if malware is able to get root on the device. That malware will be free to read all files on the device. Second, for people who have not set up a strong passphrase on their iOS device, using app-specific encrypted storage make it harder to access that app&#8217;s data on devices with no passcode set, especially if any additional passphrase is stored in the keychain and disallowed from backup, or if it&#8217;s just stored in your own memory. 

Third is for added protetion from forensic acquisition systems, which often work using root exploits in order to read the entire filesystem without unlocking the screen<a href="https://www.elcomsoft.com/news/591.html" target="_blank">[1]</a><a href="https://www.elcomsoft.com/news/586.html" target="_blank">[2]</a><a href="http://www.htcia.org/2013/12/iphone-forensics-what-you-need-to-know/" target="_blank">[3]</a>. By having an app-specific encrypted file container that is not mounted like a filesystem, then even root cannot directly access the files in the container. Even root needs to get the key in order to unlock the IOCipher container, whether it is in use or not, and getting that key means either a key logger, which means planning ahead, or reading they key from memory if the container is unlocked, which is a more elaborate and targeted attack that full disk acquisition after rooting.

Now consider that there is a large market 0days, i.e. unpublished exploits, and companies like <a href="https://netzpolitik.org/2014/gamma-finfisher-hacked-40-gb-of-internal-documents-and-source-code-of-government-malware-published/" target="_blank">VUPEN, FinFisher</a>, and <a href="https://citizenlab.org/2014/06/backdoor-hacking-teams-tradecraft-android-implant/" target="_blank">Hacking Team</a> making it easy to purchase them, even providing guarantees that one of their exploits will work within 30 days, it seems quite likely that customers of such companies have access to secret root exploits to even iOS 8. While there are ethical and lawful reasons to use software like this, many governments are also using them for <a href="https://www.eff.org/deeplinks/2012/02/spy-tech-companies-their-authoritarian-customers-part-i-finfisher-and-amesys" target="_blank">illegal</a> <a href="http://www.economist.com/blogs/pomegranate/2014/07/internet-monitoring-gulf" target="_blank">and</a> <a href="http://www.theguardian.com/technology/2014/sep/16/wikileaks-finfisher-files-malware-surveillance" target="_blank">unethical</a> <a href="https://citizenlab.org/2013/03/you-only-click-twice-finfishers-global-proliferation-2/" target="_blank">things</a>. Since we believe that everyone has a right to privacy, to speak freely, and to peaceably protest, it is important to provide protection to people who are unfairly targeted.

[<img src="https://guardianproject.info/wp-content/uploads/2010/05/skitch.png" alt="SQLCipher" width="64" height="72" class="alignleft size-full wp-image-3613" />](https://www.zetetic.net/sqlcipher/open-source/)There is also another key advantage of the IOCipher approach when it comes to mobile devices. IOCipher is ultimately based on SQLite transactions in <a href="https://www.zetetic.net/sqlcipher/" target="_blank">SQLCipher</a>, which means that it does not require being mounted in the normal sense. There is no open state once a transaction is complete. Each read or write operation is a self-contained SQLite transaction, so if the file system is forcably quit, SQLite&#8217;s transactions prevent the whole file system from being corrupted. This is important in mobile operating systems like Android and iOS since any app or process can be killed at any moment without warning. That means that the worst that can happen to an IOCipher volume is a single write command does not get written. The whole file system will not be corrupted if the process is killed.

**Coming Soon**

When IOCipher is used in conjunction with our <a href="https://github.com/guardianproject/CacheWord" target="_blank">CacheWord</a> library, it is possible for an app to provide protection even against the <a href="https://xkcd.com/538/" target="_blank">$5 wrench attack</a>. CacheWord generates a strong passphrase and manages feeding it to IOCipher and SQLCipher. The user provides their own password for encrypting that strong passphrase. That CacheWord file is tiny, and can be rapidly deleted. Once it is gone, the actual passphrase that unlocks the IOCipher encryption is gone, the user&#8217;s passphrase will not unlock IOCipher directly. This is something we are working to add in all of our apps, and to also hook it up to panic button triggers. We would be quite happy to see you beat us to it by adding this feature to your app!

IOCipher with a hardware security module (HSM) aka smartcard would be really nice, since it would provide some measure of added protection without the user setting an app-specific passphrase. HSMs provide write-only private key storage locked by pin code, so even if some was able to get the encrypted file and the pincode, they would not be able to retrieve the key to unlock the encrypted file. The only way to unlock the file would be with the physical device itself, or by finding the key backup, if that existed. This is possible now using an external <a href="http://www.smartcard-hsm.com/features.html" target="_blank">microSD</a> <a href="http://www.go-trust.com/nist-adds-go-trusts-sdencrypter-microsd-hsm-to-the-in-process-fips-140-2-module-validation-list/" target="_blank">HSM</a>