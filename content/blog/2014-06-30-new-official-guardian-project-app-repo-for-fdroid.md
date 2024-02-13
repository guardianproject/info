---
id: 12519
title: New Official Guardian Project app repo for FDroid!
date: 2014-06-30T20:26:39-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12519
permalink: /2014/06/30/new-official-guardian-project-app-repo-for-fdroid/
categories:
  - News
tags:
  - Android
  - bazaar
  - distribution
  - F-Droid
  - fdroid
  - security
---
We now have an official <a href="https://f-droid.org" target="_blank">FDroid</a> app repository that is available via three separate methods, to guarantee access to a trusted distribution channel throughout the world! To start with, you must have FDroid installed. Right now, I recommend using the latest test release since it has support for Tor and .onion addresses (earlier versions should work for non-onion addresses):

<https://f-droid.org/repo/org.fdroid.fdroid_710.apk>

In order to add this repo to your FDroid config, you can either click directly on these links on your devices and FDroid will recognize them, or you can click on them on your desktop, and you will be presented with a QR Code to scan. Here are your options:

  * HTTPS: [https://guardianproject.info/fdroid/repo](https://guardianproject.info/fdroid/repo?fingerprint=B7C2EEFD8DAC7806AF67DFCD92EB18126BC08312A7F2D6F3862E46013C7A6135)
  * Tor Hidden Service aka onion address: [http://bdf2wcxujkg6qqff.onion/fdroid/repo](http://bdf2wcxujkg6qqff.onion/fdroid/repo?fingerprint=B7C2EEFD8DAC7806AF67DFCD92EB18126BC08312A7F2D6F3862E46013C7A6135)
  * Amazon AWS S3 Bucket (_this does not show up in a browser_): [https://s3.amazonaws.com/guardianproject/fdroid/repo](https://s3.amazonaws.com/guardianproject/fdroid/repo?fingerprint=B7C2EEFD8DAC7806AF67DFCD92EB18126BC08312A7F2D6F3862E46013C7A6135) 

From here on out, our old FDroid repo (https://guardianproject.info/repo) is considered deprecated and will no longer be updated. It will eventually be removed. Update to the new one!

Also, if you missed it before, all of our test builds are also [available for testing only via FDroid](https://guardianproject.info/2014/06/06/automatic-private-distribution-of-our-test-builds/). Just remember, the builds in the test repo are only debug builds, not fully trusted builds, so use them for testing only.

### Automate it all!

This setup has three distribution channels that are all mirrors of a repo that is generated on a fully offline machine. This is only manageable because of lots of new automation features in the <a href="https://gitlab.com/fdroid/fdroidserver" target="_blank">fdroidserver</a> tools for building and managing app repos. You can now set up a USB thumb drive as the automatic courier for shuffling the repo from the offline machine to an online machine. The repo is generated, updated, and signed using `fdroid update`, then those signed files are synced to the USB thumb drive using `fdroid server update`. Then the online machine syncs the signed files from that USB thumb drive to multiple servers via SSH and Amazon S3 with a single command: `fdroid server update`. The magic is in setting up the config options and letting the tools do the rest.

### New Repo Signing Key

For part of this, I’ve completed the process of generating a new, fully offline fdroid [signing key](https://guardianproject.info/home/signing-keys/). So that means there is a new signing key for the FDroid repo, and the old repo signing key is being retired.

  * [guardianproject-rsa4096-fdroid-repo-signing-key.pem](https://guardianproject.info/releases/guardianproject-rsa4096-fdroid-repo-signing-key.pem)
  * [guardianproject-rsa4096-fdroid-repo-signing-key.pem.sig](https://guardianproject.info/releases/guardianproject-rsa4096-fdroid-repo-signing-key.pem.sig)

The fingerprints for this signing key are:

<pre>Owner: EMAILADDRESS=root@guardianp&#x72;&#x6f;&#x6a;&#x65;&#x63;&#x74;&#x2e;&#x69;&#x6e;&#x66;&#x6f;, CN=guardianproject.info, O=Guardian Project, OU=FDroid Repo, L=New York, ST=New York, C=US
Issuer: &#x45;&#x4d;&#x41;ILADD&#x52;&#x45;&#x53;&#x53;=roo&#x74;&#x40;&#x67;&#x75;ardi&#x61;&#x6e;&#x70;&#x72;oject&#x2e;&#x69;&#x6e;&#x66;o, CN=guardianproject.info, O=Guardian Project, OU=FDroid Repo, L=New York, ST=New York, C=US
Serial number: a397b4da7ecda034
Valid from: Thu Jun 26 15:39:18 EDT 2014 until: Sun Nov 10 14:39:18 EST 2041
Certificate fingerprints:
 MD5:  8C:BE:60:6F:D7:7E:0D:2D:B8:06:B5:B9:AD:82:F5:5D
 SHA1: 63:9F:F1:76:2B:3E:28:EC:CE:DB:9E:01:7D:93:21:BE:90:89:CD:AD
 SHA256: B7:C2:EE:FD:8D:AC:78:06:AF:67:DF:CD:92:EB:18:12:6B:C0:83:12:A7:F2:D6:F3:86:2E:46:01:3C:7A:61:35
 Signature algorithm name: SHA1withRSA
 Version: 1
</pre>