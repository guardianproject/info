---
id: 11689
title: 'KeySync: Syncing Trusted Identities'
date: 2013-09-12T15:50:07-04:00
author: mark
layout: page
guid: https://guardianproject.info/?page_id=11689
image: http://guardianproject.info/wp-content/uploads/2013/09/keysync.png
---
[<img src="https://guardianproject.info/wp-content/uploads/2013/09/keysync.png" alt="KeySync" width="196" height="196" class="alignright size-full wp-image-11797" srcset="https://guardianproject.info/wp-content/uploads/2013/09/keysync.png 256w, https://guardianproject.info/wp-content/uploads/2013/09/keysync-150x150.png 150w" sizes="(max-width: 196px) 100vw, 196px" />](https://guardianproject.info/wp-content/uploads/2013/09/keysync.png)Privacy and security software like OTR encryption for chat and GnuPG for email and files all create digital identities that we can mark as trusted through a verification process. When using this software, each app needs completely new security identities that are separate from any existing identities used by the other apps. Then again, mobile software needs it own versions of these identity files. When setting up ChatSecure on a mobile device, all of the trust information from existing chat apps like Adium or Pidgin also needs to be converted and transferred so that ChatSecure has the same trusted identities. Or when switching from Pidgin to Jitsi for instant messaging, the trust information needs to be converted and synced so the trust information is not lost.

This is where KeySync comes in. KeySync reads and writes many different formats of OTR chat apps and converts between them. It also makes it easy to sync the trust information to your Android device for use with ChatSecure. There is also some exploratory support for syncing identities between OTR and OpenPGP via GnuPG support in KeySync.

## How To Sync To ChatSecure

To sync between ChatSecure and your desktop apps, First plug in your phone or device  
via USB. Start KeySync and it should automatically detect your device. If KeySync cannot find your device, it will save the file for you to manually copy the **otr_keystore.ofcaes** file over to your device&#8217;s SD Card, where ChatSecure looks for it. Once the file is in place on your device, start ChatSecure. In ChatSecure, go to the **Accounts**, then select **Activate KeySync** from the menu. This will guide you to scan the QRCode that KeySync shows you in order to complete the sync.

The `otr_keystore.ofcaes` file is encrypted to prevent your private information from leaking out. That QRCode is the password to your keystore, so do not share it with anyone. Also, the `otr_keystore.ofcaes` file is only intended for use in this sync procedure. Do not email it or send it anywhere over the internet!

## Warning!

This is beta software, do not rely on it for strong identity verification. It is unlikely to mess up so bad as to produce compromised private keys, but anything is possible. Also, keep in mind that program is handling your private OTR keys, so make sure that you don&#8217;t copy, send or email the \`otr_keystore.ofcaes\` file somewhere nsafe. All that said, testing and feedback is greatly appreciated, so we can get it to the point where we can trust it.

## Reporting Bugs

Please report any bugs or issues that you have with this app! We want to hear from you, no need to worry about technical details or language skills. Help us improve this software by filing bug reports about any problem that you encounter. Feature requests and patches are also welcome!

  * [<img src="https://guardianproject.info/wp-content/uploads/2011/02/reportbug-150x150.jpg" alt="report bug" width="150" height="150" class="size-thumbnail wp-image-12362" srcset="https://guardianproject.info/wp-content/uploads/2011/02/reportbug-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug-100x100.jpg 100w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug-200x200.jpg 200w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug.jpg 225w" sizes="(max-width: 150px) 100vw, 150px" /> <strong style="font-size: 200%">Report a Bug or Issue</strong>](https://dev.guardianproject.info/projects/keysync/issues/new)

  * <a href="https://dev.guardianproject.info/projects/keysync/issues?query_id=27" title="Issue Tracker" target="_blank">List of all open issues</a>
  * <a href="https://dev.guardianproject.info/projects/keysync/issues/new" title="New Issue Tracker" target="_blank">submit a new issue report</a>

<a name="download"></a>

## Download

  *![Windows](https://guardianproject.info/builds/.icons/platform_windows.gif) **Windows** executable 
      * Download and install OpenSSL: [Win32OpenSSL\_Light-1\_0_1f.exe](https://slproweb.com/download/Win32OpenSSL_Light-1_0_1f.exe)
      * When prompted install into the &#8220;Windows system directory&#8221;
      * Note: The prompt asking for a donation will go to the company that produces OpenSSL installers for Windows, not The Guardian Project.
      * If you get an error when trying to install OpenSSL, you probably need in stall the [Visual C++ 2008 Redistributables](https://www.microsoft.com/downloads/details.aspx?familyid=9B2DA534-3E03-4391-8A4D-074B9F2BC1BF) from Microsoft.
      * Download KeySync &#8211; no installation required: [KeySync-0.2.exe](https://guardianproject.info/releases/KeySync-0.2.exe) 
          * [detached gpg signature](https://guardianproject.info/releases/KeySync-0.2.exe.asc)
          * MD5: `1fb7a5ec050d03f59104a41494c559fd`
          * SHA256: `422fd0ddb6d85a6f509a1c9a868ce87437af7ac895ba8c4fa7f366d83114be07`
      *![Mac OS X](https://guardianproject.info/builds/.icons/platform_mac_os_x.gif) **Mac OS X** _(10.6 or newer, 64-bit only)_: [KeySync-0.2.app.zip](https://guardianproject.info/releases/KeySync-0.2.app.zip) 
          * [detached gpg signature](https://guardianproject.info/releases/KeySync-0.2.app.zip.sig)
          * MD5: `f6a1744a783d1cc5dc3070e1a16d79fd`
          * SHA256: `429dc303fb1d2673b953a2543b0e168f0410ce1cd14d4167f0dbf888fdf162d0`
      *![Ubuntu](https://guardianproject.info/builds/.icons/platform_ubuntu_linux.gif) **Ubuntu, Linux Mint, etc.** Run this in the Terminal to add <a href="https://launchpad.net/~guardianproject/+archive/ppa/" title="Guardian Project PPA on Launchpad" target="_blank">our PPA</a> to your package sources. You only need to do this once, you&#8217;ll get updated versions automatically once this is complete (fingerprint: `F50E ADDD 2234 F563`): <pre style="font-size: small;">sudo add-apt-repository ppa:guardianproject/ppa
sudo apt-get update
sudo apt-get install keysync
</pre>
    
      *![Fedora](https://guardianproject.info/builds/.icons/platform_fedora_linux.gif) **Fedora 17, 18, 19**: Run this in your Terminal to add <a href="https://build.opensuse.org/project/show/security:guardianproject"  target="_blank">our repository</a> to your package sources. You only need to do this once, you&#8217;ll get updated versions automatically once this is complete (fingerprint: `AC38 BED1 E879 79EA FD54`): <pre style="font-size: small;">source /etc/os-release
sudo wget http://download.opensuse.org/repositories/security:guardianproject/Fedora_${VERSION_ID}/security:guardianproject.repo -O /etc/yum.repos.d/security:guardianproject.repo
sudo yum install keysync
</pre>
    
      *![Debian](https://guardianproject.info/builds/.icons/platform_debian_gnu_linux.gif) **Debian**: <a href="http://packages.debian.org/search?keywords=keysync" target="_blank">included in the official repos</a>. For wheezy, get it from backports: <pre style="font-size: small;">apt-get -t wheezy-backports install keysync
</pre>
    
      *![Arch Linux](https://guardianproject.info/builds/.icons/platform_arch_linux.gif) **Arch Linux**: <a href="https://aur.archlinux.org/packages/keysync/" target="_blank">included in the AUR</a>. Please vote for it so it can be included in the official community repository. 
      *![Python pypi](https://guardianproject.info/builds/.icons/python-logo.gif) Any Platform with Python, install via <a href="https://pypi.python.org/pypi/keysync" target="_blank">pypi</a> (see the <a href="https://github.com/guardianproject/keysync/blob/master/win32/README.md" target="_blank" title="Building KeySync on Windows">special instructions for Windows</a>) <pre style="font-size: small;">pip install keysync
</pre></ul> 
    
    <a name="source"></a>
    
    ### Source
    
      * For more info on the code and installation, <a href="https://github.com/guardianproject/keysync/blob/master/README.md" target="_blank">see the README</a>
      * github: <a href="https://github.com/guardianproject/keysync" title="KeySync source repo" target="_blank">https://github.com/guardianproject/keysync</a>
      * <a href="https://github.com/guardianproject/keysync/releases" title="KeySync source tarballs" target="_blank">downloadable tags on github</a>
    ## Known Issues
    
    See the <a href="https://dev.guardianproject.info/projects/keysync/roadmap" title="KeySync Development Roadmap" target="_blank">KeySync Roadmap</a> for our development plan. Here are some notable known issues:
    
      * does not handle multiple keys/fingerprints for a given account (<a href="https://dev.guardianproject.info/issues/1868" target="_blank">#1868</a>)
      * GUI only syncs to ChatSecure (full two-way sync is planned) (<a href="https://dev.guardianproject.info/issues/1968" target="_blank">#1968</a>)
      * no way to handle conflicting private keys for an account (<a href="https://dev.guardianproject.info/issues/1963" target="_blank">#1963</a>)
      * no translations, only in English (<a href="https://dev.guardianproject.info/issues/2170" target="_blank">#2170</a>)
      * <a title="existing KeySync issues" href="https://dev.guardianproject.info/projects/keysync/issues" target="_blank">View all open issues</a>