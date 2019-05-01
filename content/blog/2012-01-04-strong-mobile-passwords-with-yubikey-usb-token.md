---
id: 1383
title: Strong Mobile Passwords with Yubikey USB Token
date: 2012-01-04T00:45:43-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=1383
permalink: /2012/01/04/strong-mobile-passwords-with-yubikey-usb-token/
categories:
  - Development
---
We have been experimenting with the [Yubikey](http://www.yubico.com/yubikey), a USB hardware password token, a bit over the last few weeks and would like to share our initial findings. We have not received any financial support or donation from Yubico for this work. We simply think they have a very affordable, interesting product that, due to its design, does \*not\* require any on-device driver software and can easily work with any Android device that supports USB Host/HID mode.

[<img title="2012-01-03 14.05.17" src="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.05.17-300x225.jpg" alt="" width="300" height="225" />  
](https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.05.17.jpg) _Yubikey is small, light and attaches to a keychain_

Our motivation for investigating this device was in finding a way to encourage the use of strong (aka long, mixed-case, etc) passwords on mobile devices, for use with SQLCipher, screenlock passwords, and on boot disk encryption. The issue is that most users rely on short PINs or a visual unlock pattern, which does not provide enough randomness to ensure security of their data. In addition, due to the use of a touchscreen, fingerprint oil smudges on the screen often reveal the numbers entered or the pattern drawn to unlock the device (See the [“Smudge Attacks on Smartphone Touch Screens”](https://docs.google.com/viewer?url=http%3A%2F%2Fwww.usenix.org%2Fevents%2Fwoot10%2Ftech%2Ffull_papers%2FAviv.pdf) paper.)

[<img class="alignnone size-full wp-image-1397" title="medium_nexus-one-gesture-password-insecure-536x587_01" src="https://guardianproject.info/wp-content/uploads/2012/01/medium_nexus-one-gesture-password-insecure-536x587_01.jpg" alt="" width="300" height="298" srcset="https://guardianproject.info/wp-content/uploads/2012/01/medium_nexus-one-gesture-password-insecure-536x587_01.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/01/medium_nexus-one-gesture-password-insecure-536x587_01-150x150.jpg 150w" sizes="(max-width: 300px) 100vw, 300px" />  
](https://guardianproject.info/wp-content/uploads/2012/01/medium_nexus-one-gesture-password-insecure-536x587_01.jpg) _On-screen password entry can leave smudges ([Gizmodo](http://gizmodo.com/5613737/your-greasy-fingers-are-giving-up-your-android-passcode))_

Even when a user enters a traditional character based pattern, it is often laborious on a mobile device to use symbols and mixed case characters.

[<img class="alignnone size-medium wp-image-1386" title="2012-01-03 14.05.55" src="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.05.55-300x225.jpg" alt="" width="300" height="225" srcset="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.05.55-300x225.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.05.55.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />  
](https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.05.55.jpg) _Yubikey with inexpensive micro-USB adapter_

The Yubikey is a hardware token that plugs into a USB port, and is activated by a short press on the touch sensitive gold-colored disc. It essentially looks and acts like an external hardware keyboard, which is how it works in a drivelress manner. While the primary function of the Yubikey is as a generator for one-time passwords to be verified over a network with a back-end authentication system, it can also be used to store and generate local strong static passwords. It is the static password mode which we have initially worked with for use with Android devices, in order to do local authentication for disk encryption, screen unlock and local encrypted application databases. _(We do plan to investigate the other modes of the Yubikey in future posts.)_

[<img class="alignnone size-medium wp-image-1384" title="yubikey" src="https://guardianproject.info/wp-content/uploads/2012/01/yubikey-300x246.png" alt="" width="300" height="246" srcset="https://guardianproject.info/wp-content/uploads/2012/01/yubikey-300x246.png 300w, https://guardianproject.info/wp-content/uploads/2012/01/yubikey.png 902w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2012/01/yubikey.png)

_Yubikey Personalization Tool – simple and free_

Android has a limit of 17 characters for its disk encryption and screen unlock password. Using the [Yubikey Personalization Tool](http://www.yubico.com/personalization-tool), we were able to generate a strong password of that limit, as well as a 13 character password, which we combined with a memorized, manually entered 4 digit pin. By combining the long password from the Yubikey with a short memorized version, a certain amount of security is preserved even if the key is physically stolen along with your mobile device.

[<img class="alignnone size-medium wp-image-1388" title="2012-01-03 14.07.10" src="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.07.10-300x225.jpg" alt="" width="300" height="225" srcset="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.07.10-300x225.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.07.10.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />  
](https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.07.10.jpg) _Yubikey activation via micro-USB on Motorola Xoom_

__At this point in time, it seems that only Android tablets, such as the Viewsonic GTab, Motorola Xoom and Toshiba Thrive support the necessary [USB Human Interface Device mode](http://en.wikipedia.org/wiki/USB_human_interface_device_class) to enable the Yubikey to work. We have not yet found a smartphone that supports external keyboard hardware, but we are sure they are out there, or else it will not be long. Our initial tests were with the Motorola Xoom, which only includes a micro USB port. Fortunately, using a [very simple adapter purchased on Amazon](http://www.amazon.com/Micro-USB-Male-Female-Adapter/dp/B0027YYMU6/ref=sr_1_1?ie=UTF8&qid=1325636089&sr=8-1), we were able to make it work. Open the Android settings to the Location & Security screen, and configure your lock screen to be “Secured with password”. When asked to type it in, plug in the Yubikey with adapter, touch the disc, and the pre-configured static password spits out into the password field that is currently in focus on the device.

[<img class="alignnone size-medium wp-image-1390" title="2012-01-03 14.09.04" src="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.09.04-300x225.jpg" alt="" width="300" height="225" srcset="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.09.04-300x225.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.09.04.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />  
](https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.09.04.jpg) _Yubikey password entry_

The Toshiba and Viewsonic tablets offer full-size USB ports, which makes the use of the Yubikey much easier, as seen below. However, as a best practices policy, even if the key can be left plugged in to the device while in use and in motion, it makes most sense to remove the Yubikey immediately, and have it attached to a keychain or other physical item you always keep on your person.

[<img class="alignnone size-medium wp-image-1389" title="2012-01-03 14.08.08" src="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.08.08-300x225.jpg" alt="" width="300" height="225" srcset="https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.08.08-300x225.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.08.08.jpg 1024w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2012/01/2012-01-03-14.08.08.jpg)

Yubikey also offers an [RFID-enabled version of their key](http://www.yubico.com/rfid-yubikey) which is compatible with the Near Field Communication (NFC) technology found in some newer Android phones. Using this solution, it may be possible to not require actually plugging in the key at all, but instead just having it in the vicinity of your mobile device. You would still need to combine this with a short directly entered password or PIN, in case the NFC signal is somehow wirelessly sniffed by an attacker, though the risk of that is very low for most typical deployments, and NFC itself does provide some amount of security.

All in all, we find the Yubikey to server a useful purpose in improving the base level of local device security on compatible Android devices. While one could type in a 17 character, mixed-case, number and symbol password directly into a device, it would grow old quickly, especially with typical, end-users. The act of plugging in a Yubikey takes very little effort, and combined with a short manually entered PIN, provides the maximum amount of password security for disk encryption, screen locking, and application-based security on Android.

Look for future posts on the use of the Yubikey and other hardware token devices, specifically investigating their use in one-time password, challenge-response, and RFID/NFC modes.

 