---
id: 12302
title: 'Security in a thumb drive: the promise and pain of hardware security modules, take one!'
date: 2014-03-28T16:54:39-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12302
permalink: /2014/03/28/security-in-a-thumb-drive-the-promise-and-pain-of-hardware-security-modules-take-one/
categories:
  - News
tags:
  - Android
  - ant
  - bazaar
  - encryption
  - hardware
  - howto
  - hsm
  - identity
  - jarsigner
  - keytool
  - openssl
  - smartcard
---
[<img src="https://guardianproject.info/wp-content/uploads/2014/03/cryptostick-usb-flash-drive-security-software.jpg" alt="security in a thumb drive" width="219" height="119" class="alignleft size-full wp-image-12311" srcset="https://guardianproject.info/wp-content/uploads/2014/03/cryptostick-usb-flash-drive-security-software.jpg 219w, https://guardianproject.info/wp-content/uploads/2014/03/cryptostick-usb-flash-drive-security-software-100x54.jpg 100w, https://guardianproject.info/wp-content/uploads/2014/03/cryptostick-usb-flash-drive-security-software-150x81.jpg 150w, https://guardianproject.info/wp-content/uploads/2014/03/cryptostick-usb-flash-drive-security-software-200x108.jpg 200w" sizes="(max-width: 219px) 100vw, 219px" />](https://guardianproject.info/wp-content/uploads/2014/03/cryptostick-usb-flash-drive-security-software.jpg)Hardware Security Modules (aka Smartcards, chipcards, etc) provide a secure way to store and use cryptographic keys, while actually making the whole process a bit easier. In theory, one USB thumb drive like thing could manage all of the crypto keys you use in a way that makes them much harder to steal. That is the promise. The reality is that the world of Hardware Security Modules (HSMs) is a massive, scary minefield of endless technical gotchas, byzantine standards (PKCS#11!), technobabble, and incompatibilities. Before I dive too much into ranting about the days of my life wasted trying to find a clear path through this minefield, I’m going to tell you about one path I did find through to solve a key piece of the puzzle: Android and Java package signing.

[<img src="https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs.jpg" alt="ACS ACR38-T-IBS" width="320" height="248" class="alignright size-full wp-image-12313" srcset="https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs.jpg 320w, https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs-300x232.jpg 300w, https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs-100x77.jpg 100w, https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs-150x116.jpg 150w, https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs-200x155.jpg 200w" sizes="(max-width: 320px) 100vw, 320px" />](https://guardianproject.info/wp-content/uploads/2014/03/moreinfo_acr38t_ibs.jpg)For this round, I am covering the <a href="http://www.aventra.fi/English/products_MyEID_E.html" target="_blank">Aventra MyEID PKI Card</a>. I bought a SIM-sized version to fit into an <a href="http://www.smartcardfocus.com/ilp/id~99/ACR38T_IBS/p/readers.shtml" target="_blank">ACS ACR38T-IBS-R</a> smartcard reader (it is apparently no longer made, and the <a href="http://acs.com.hk/en/products/1/acr38t-d1-plug-in-sim-sized-card-reader/" target="_blank">ACT38T-D1</a> is meant to replace it). Why such specificity you may ask? Because you have to be sure that your smartcard will work with your reader, and that your reader will have a working driver for you system, and that your smartcard will have a working PKCS#11 driver so that software can talk to the smartcard. Thankfully there is the <a href="https://github.com/OpenSC/OpenSC/wiki" target="_blank">OpenSC</a> project to cover the PKCS#11 part, it implements the PKCS#11 communications standard for many smartcards. On my Ubuntu/precise system, I had to install an extra driver, `libacr38u`, to get the ACR38T reader to show up on my system.

So let’s start there and get this thing to show up! First we need some packages. The OpenSC packages are out-of-date in a lot of releases, you need version 0.13.0-4 or newer, so you have to add our PPA (Personal Package Archive) to get current versions, which include a <a href="https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=742089" target="_blank">specific fix for the Aventra MyEID</a>: (fingerprint: `F50E ADDD 2234 F563`):

```
sudo add-apt-repository ppa:guardianproject/ppa
sudo apt-get update
sudo apt-get install opensc libacr38u libacsccid1 pcsc-tools usbutils
```

First thing, I use `lsusb` in the terminal to see what USB devices the Linux kernel sees, and thankfully it sees my reader:

```console
$ lsusb
Bus 005 Device 013: ID 072f:9000 Advanced Card Systems, Ltd ACR38 AC1038-based Smart Card Reader
```

Next, its time to try `pcsc_scan` to see if the system can see the smartcard installed in the reader. If everything is installed and in order, then `pcsc_scan` will report this:

```console
$ pcsc_scan 
PC/SC device scanner
V 1.4.18 (c) 2001-2011, Ludovic Rousseau <&#x6c;u&#x64;ov&#x69;c.&#x72;o&#x75;&#x73;s&#x65;au&#x40;f&#x72;&#x65;e&#x2e;fr>
Compiled with PC/SC lite version: 1.7.4
Using reader plug'n play mechanism
Scanning present readers...
0: ACS ACR38U 00 00

Thu Mar 27 14:38:36 2014
Reader 0: ACS ACR38U 00 00
  Card state: Card inserted, 
  ATR: 3B F5 18 00 00 81 31 FE 45 4D 79 45 49 44 9A
[snip]
```

If `pcsc_scan` cannot see the card, then things will not work. Try re-seating the smardcard in the reader, make sure you have all the right packages installed, and if you can see the reader in `lsusb`. If your smartcard or reader cannot be read, then `pcsc_scan` will report something like this:

```console
$ pcsc_scan 
PC/SC device scanner
V 1.4.18 (c) 2001-2011, Ludovic Rousseau <&#x6c;&#x75;&#x64;&#x6f;&#x76;&#x69;c.rousse&#x61;&#x75;&#x40;&#x66;&#x72;&#x65;e.fr>
Compiled with PC/SC lite version: 1.7.4
Using reader plug'n play mechanism
Scanning present readers...
Waiting for the first reader...
```

Moving right along… now `pcscd` can see the smartcard, so we can start playing with using the OpenSC tools. These are needed to setup the card, put PINs on it for access control, and upload keys and certificates to it. The last annoying little preparation tasks are finding where `opensc-pkcs11.so` is installed and the “slot” for the signing key in the card. These will go into a config file which `keytool` and `jarsigner` need. To get this info on Debian/Ubuntu/etc, run these:

```console
$ dpkg -S opensc-pkcs11.so
opensc: /usr/lib/x86_64-linux-gnu/opensc-pkcs11.so
$ pkcs11-tool --module /usr/lib/x86_64-linux-gnu/opensc-pkcs11.so \
>     --list-slots
Available slots:
Slot 0 (0xffffffffffffffff): Virtual hotplug slot
  (empty)
Slot 1 (0x1): ACS ACR38U 00 00
  token label        : MyEID (signing)
  token manufacturer : Aventra Ltd.
  token model        : PKCS#15
  token flags        : rng, login required, PIN initialized, token initialized
  hardware version   : 0.0
  firmware version   : 0.0
  serial num         : 0106004065952228
```

This is the info needed to put into a `opensc-java.cfg`, which `keytool` and `jarsigner` <a href="http://docs.oracle.com/javase/7/docs/technotes/guides/security/p11guide.html" target="_blank">need in order to talk</a> to the Aventra HSM. The name, library, and slot fields are essential, and the description is helpful. Here is how the `opensc-java.cfg` using the above information looks:

```console
name = OpenSC
description = SunPKCS11 w/ OpenSC Smart card Framework
library = /usr/lib/x86_64-linux-gnu/opensc-pkcs11.so
slot = 1
```

Now everything should be ready for initializing the HSM, generating a new key, and uploading that key to the HSM. This process generates the key and certificate, puts them into files, then uploads them to the HSM. That means you should only run this process on a trusted machine, certainly with some kind of disk encryption, and preferably on a machine that is not connected to a network, running an OS that has never been connected to the internet. A live CD is one good example, I recommend <a href="https://tails.boum.org/download/index.en.html#index4h1" target="_blank">Tails on a USB thumb drive</a> running with the <a href="https://tails.boum.org/doc/first_steps/persistence/index.en.html" target="_blank">secure persistent store</a> on it (we have been working here and there on making a TAILS-based distro specifically for managing keys, we call it <a href="https://dev.guardianproject.info/projects/psst/wiki/CleanRoom" target="_blank">CleanRoom</a>).

<div id="attachment_12321" style="width: 560px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2014/03/cstick2.jpg"><img aria-describedby="caption-attachment-12321" src="https://guardianproject.info/wp-content/uploads/2014/03/cstick2-1024x805.jpg" alt="HSM plugged into a laptop" width="550" height="432" class="size-large wp-image-12321" srcset="https://guardianproject.info/wp-content/uploads/2014/03/cstick2-1024x805.jpg 1024w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-300x235.jpg 300w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-100x78.jpg 100w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-150x117.jpg 150w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-200x157.jpg 200w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-450x353.jpg 450w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-600x471.jpg 600w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2-900x707.jpg 900w, https://guardianproject.info/wp-content/uploads/2014/03/cstick2.jpg 1600w" sizes="(max-width: 550px) 100vw, 550px" /></a>
  
  <p id="caption-attachment-12321" class="wp-caption-text">
    HSM plugged into a laptop
  </p>
</div>

First off, the HSM needs to be initialized, then set up with a signing PIN and a “Security Officer” PIN (which means basically an “admin” or “root” PIN). The signing PIN is the one you will use for signing APKs, the “Security Officer PIN” (SO-PIN) is used for modifying the HSM setup, like uploading new keys, etc. Because there are so many steps in the process, I’ve written up scripts to run thru all of the steps. If you want to see the details, <a href="https://github.com/guardianproject/smartcard-apk-signing/blob/master/Aventra_MyEID_Setup/setup.sh" target="_blank">read</a> <a href="https://github.com/guardianproject/smartcard-apk-signing/blob/master/openssl-gen/gen.sh" target="_blank">the</a> <a href="https://github.com/guardianproject/smartcard-apk-signing/blob/master/Aventra_MyEID_Setup/finalize.sh" target="_blank">scripts</a>. The next step is to generate the key using `openssl` and upload it to the HSM. Then the HSM needs to be “finalized”, which means the PINs are activated, and keys cannot be uploaded. Don’t worry, as long as you have the SO-PIN, you can erase the HSM and re-initialize it. But be careful! Many HSMs will permanently self-destruct if you enter in the wrong PIN too many times, some will do that after only three wrong PINs! As long as you have not finalized the HSM, any PIN will work, so play around a lot with it before finalizing it. Run the init and key upload procedure a few times, try signing an APK, etc. Take note: the script will generate a random password for the secret files, then echo that password when it completes, so make sure no one can see your screen when you generate the real key. Alright, here goes!

```console
code $ git clone https://github.com/guardianproject/smartcard-apk-signing
code $ cd smartcard-apk-signing/Aventra_MyEID_Setup
Aventra_MyEID_Setup $ ./setup.sh 
Edit pkcs15-init-options-file-pins to put in the PINs you want to set:
Aventra_MyEID_Setup $ emacs pkcs15-init-options-file-pins
Aventra_MyEID_Setup $ ./setup.sh 
Using reader with a card: ACS ACR38U 00 00
Connecting to card in reader ACS ACR38U 00 00...
Using card driver MyEID cards with PKCS#15 applet.
About to erase card.
PIN [Security Officer PIN] required.
Please enter PIN [Security Officer PIN]: 
Using reader with a card: ACS ACR38U 00 00
Connecting to card in reader ACS ACR38U 00 00...
Using card driver MyEID cards with PKCS#15 applet.
About to create PKCS #15 meta structure.
Using reader with a card: ACS ACR38U 00 00
Connecting to card in reader ACS ACR38U 00 00...
Using card driver MyEID cards with PKCS#15 applet.
Found MyEID
About to generate key.
Using reader with a card: ACS ACR38U 00 00
Connecting to card in reader ACS ACR38U 00 00...
Using card driver MyEID cards with PKCS#15 applet.
Found MyEID
About to generate key.
next generate a key with ./gen.sh then ./finalize.sh
Aventra_MyEID_Setup $ cd ../openssl-gen/
openssl-gen $ ./gen.sh 
Usage: ./gen.sh "CertDName" [4096]
  for example:
  "/C=US/ST=New York/O=Guardian Project &#x54;e&#x73;&#x74;/&#x43;N=&#x74;es&#x74;.&#x67;&#x75;a&#x72;di&#x61;np&#x72;o&#x6a;&#x65;c&#x74;&#x2e;i&#x6e;fo&#x2f;em&#x61;i&#x6c;&#x41;d&#x64;re&#x73;s=&#x74;e&#x73;&#x74;@&#x67;&#x75;a&#x72;di&#x61;np&#x72;o&#x6a;&#x65;c&#x74;.i&#x6e;fo"
openssl-gen $ ./gen.sh "/C=US/ST=New York/O=Guardian Project Te&#x73;t&#x2f;C&#x4e;=&#x74;e&#x73;t&#x2e;g&#x75;ardi&#x61;n&#x70;r&#x6f;j&#x65;c&#x74;.&#x69;n&#x66;o/em&#x61;i&#x6c;A&#x64;d&#x72;e&#x73;s&#x3d;t&#x65;st&#x40;g&#x75;a&#x72;d&#x69;a&#x6e;p&#x72;o&#x6a;e&#x63;t.&#x69;n&#x66;o"
Generating key, be patient...
2048 semi-random bytes loaded
Generating RSA private key, 2048 bit long modulus
.......................................+++
..................................................+++
e is 65537 (0x10001)
Signature ok
subject=/C=US/ST=New York/O=Guardian Project Test/&#x43;&#x4e;&#x3d;&#x74;&#x65;st.gu&#x61;&#x72;&#x64;&#x69;&#x61;nproj&#x65;&#x63;&#x74;&#x2e;&#x69;nfo/e&#x6d;&#x61;&#x69;&#x6c;&#x41;ddres&#x73;&#x3d;&#x74;&#x65;&#x73;t@gua&#x72;&#x64;&#x69;&#x61;&#x6e;proje&#x63;&#x74;&#x2e;&#x69;&#x6e;fo
Getting Private key
writing RSA key
Your HSM will prompt you for 'Security Officer' aka admin PIN, wait for it!
Enter destination keystore password:  
Entry for alias 1 successfully imported.
Import command completed:  1 entries successfully imported, 0 entries failed or cancelled
[Storing keystore]
Key fingerprints for reference:
MD5 Fingerprint=90:24:68:F3:F3:22:7D:13:8C:81:11:C3:A4:B6:9A:2F
SHA1 Fingerprint=3D:9D:01:C9:28:BD:1F:F4:10:80:FC:02:95:51:39:F4:7D:E7:A9:B1
SHA256 Fingerprint=C6:3A:ED:1A:C7:9D:37:C7:B0:47:44:72:AC:6E:FA:6C:3A:B2:B1:1A:76:7A:4F:42:CF:36:0F:A5:49:6E:3C:50
The public files are: certificate.pem publickey.pem request.pem
The secret files are: secretkey.pem certificate.p12 certificate.jkr
The passphrase for the secret files is: fTQ*he-[:y+69RS+W&+!*0O5i%n
openssl-gen $ cd ../Aventra_MyEID_Setup/
Aventra_MyEID_Setup $ ./finalize.sh 
Using reader with a card: ACS ACR38U 00 00
Connecting to card in reader ACS ACR38U 00 00...
Using card driver MyEID cards with PKCS#15 applet.
Found MyEID
About to delete object(s).
Your HSM is ready for use! Put the secret key files someplace encrypted and safe!
```

Now your HSM should be ready for use for signing. You can try it out with `keytool` to see what is on it, using the signing PIN not the Security Officer PIN:

```
smartcard-apk-signing $ /usr/bin/keytool -v \
>     -providerClass sun.security.pkcs11.SunPKCS11 \
>     -providerArg opensc-java.cfg \
>     -providerName SunPKCS11-OpenSC -keystore NONE -storetype PKCS11 \
>     -list
Enter keystore password:  

Keystore type: PKCS11
Keystore provider: SunPKCS11-OpenSC

Your keystore contains 1 entry

Alias name: 1
Entry type: PrivateKeyEntry
Certificate chain length: 1
Certificate[1]:
Owner: &#x45;&#x4d;&#x41;&#x49;&#x4c;&#x41;&#x44;&#x44;RESS=test@g&#x75;&#x61;&#x72;&#x64;&#x69;&#x61;&#x6e;&#x70;&#x72;oject.info, CN=test.guardianproject.info, O=Guardian Project Test, ST=New York, C=US
Issuer: E&#x4d;A&#x49;LA&#x44;D&#x52;ES&#x53;=&#x74;e&#x73;&#x74;@&#x67;u&#x61;rd&#x69;a&#x6e;pr&#x6f;j&#x65;ct&#x2e;i&#x6e;f&#x6f;, CN=test.guardianproject.info, O=Guardian Project Test, ST=New York, C=US
Serial number: aa6887be1ec84bde
Valid from: Fri Mar 28 16:41:26 EDT 2014 until: Mon Aug 12 16:41:26 EDT 2041
Certificate fingerprints:
	 MD5:  90:24:68:F3:F3:22:7D:13:8C:81:11:C3:A4:B6:9A:2F
	 SHA1: 3D:9D:01:C9:28:BD:1F:F4:10:80:FC:02:95:51:39:F4:7D:E7:A9:B1
	 SHA256: C6:3A:ED:1A:C7:9D:37:C7:B0:47:44:72:AC:6E:FA:6C:3A:B2:B1:1A:76:7A:4F:42:CF:36:0F:A5:49:6E:3C:50
	 Signature algorithm name: SHA1withRSA
	 Version: 1


*******************************************
*******************************************
```

And let’s try signing an actual APK using the <a href="https://developer.android.com/tools/publishing/app-signing.html" target="_blank">arguments that Google recommends</a>, again, using the signing PIN:

```console
smartcard-apk-signing $ /usr/bin/jarsigner -verbose \
>     -providerClass sun.security.pkcs11.SunPKCS11 \
>     -providerArg opensc-java.cfg -providerName SunPKCS11-OpenSC \
>     -keystore NONE -storetype PKCS11 \
>     -sigalg SHA1withRSA -digestalg SHA1 \
>     bin/LilDebi-release-unsigned.apk 1
Enter Passphrase for keystore: 
   adding: META-INF/1.SF
   adding: META-INF/1.RSA
  signing: assets/busybox
  signing: assets/complete-debian-setup.sh
  signing: assets/configure-downloaded-image.sh
  signing: assets/create-debian-setup.sh
  signing: assets/debian-archive-keyring.gpg
  signing: assets/debootstrap.tar.bz2
  signing: assets/e2fsck.static
  signing: assets/gpgv
  signing: assets/lildebi-common
[snip]
```

Now we have a working, but elaborate, process for setting up a Hardware Security Module for signing APKs. Once the HSM is setup, using it should be quite straightforward. Next steps are to work out as many kinks in this process as possible so this will be the default way to sign APKs. That means things like figuring out how <a href="https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=742831" target="_blank">Java can be pre-configured to use OpenSC in the Debian package</a>, as well as including all <a href="https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=742089" target="_blank">relevant fixes</a> in the `pcscd` and `opensc` packages. Then the ultimate is to add support for using HSMs in Android’s generated build files like the `build.xml` for `ant` that is generated by `android update project`. Then people could just plug in the HSM and run `ant release` and have a signed APK!