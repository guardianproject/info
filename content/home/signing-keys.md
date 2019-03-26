---
id: 12059
title: Signing Keys
date: 2013-12-16T14:01:41-04:00
author: Hans-Christoph Steiner
layout: page
guid: https://guardianproject.info/?page_id=12059
force_ssl:
  - "1"
---
We have a number of signing keys used for signing software releases. There are a number of different keys because there are a number of different ways of signing software. This list aims to be the comprehensive list of all the release signing keys that we use.

## OpenPGP

We sign all of our releases using OpenPGP detached binary signatures in a `.sig` file.

#### People signing official releases

  * <a href="http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0x9F0FE587374bbe81" target="_blank">Hans-Christoph Steiner <&#104;&#x61;&#110;&#x73;&#64;&#x67;&#117;&#x61;&#114;&#x64;&#105;&#x61;&#110;&#x70;&#114;&#x6f;&#106;&#x65;&#99;&#x74;&#46;&#x69;&#110;&#x66;&#111;><br /><code>5E61 C878 0F86 295C E17D 8677 9F0F E587 374B BE81</code></a>
  * <a href="http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0xA801183E69B37AA9" target="_blank">Nathan Freitas <&#x6e;a&#x74;&#x68;a&#x6e;&#64;g&#x75;&#97;r&#x64;i&#x61;&#x6e;p&#x72;&#111;j&#x65;&#99;t&#x2e;i&#x6e;&#x66;o><br /><code>BBE2 0FD6 DA48 A3DD 4CC7  DF41 A801 183E 69B3 7AA9</code></a>
  * <a href="http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0x97d05003da731a17" target="_blank">Abel Luck <&#x61;&#x62;&#101;l&#64;g&#x75;&#x61;&#x72;&#100;ia&#x6e;&#x70;&#x72;&#111;je&#x63;&#x74;&#x2e;&#105;nf&#x6f;><br /><code>1893 0780 A043 3A61 B8B2  17D6 97D0 5003 DA73 1A17</code></a>

#### Keys from the build servers

  * <a href="http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0x2A1E2A34308D1650" target="_blank">build@halfparanoid <root&#64;&#103;&#x75;&#x61;&#x72;&#x64;&#x69;&#x61;nproj&#101;&#99;&#x74;&#x2e;&#x69;&#x6e;&#x66;&#x6f;><br /><code>6F57 3CDC 0E19 0E0F 4C0A  B155 2A1E 2A34 308D 1650</code></a>
  * <a href="http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0x3C0966BA81079F68" target="_blank">build@semiparanoid <&#x72;&#x6f;ot&#x40;&#x67;&#117;ar&#x64;&#x69;&#97;np&#x72;&#x6f;&#106;ec&#x74;&#x2e;in&#x66;&#x6f;><br /><code>C85A 83E6 BE71 EA3C 8BA2  FB16 3C09 66BA 8107 9F68</code></a>

#### Launchpad Ubuntu Package Archive (PPA)

For easy installation on Ubuntu/Mint/etc. of our official releases, as well as backported software that we use, we have an Launchpad PPA with its own signing key provided by Launchpad:

  * <a href="http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=0xF50EADDD2234F563" target="_blank">Launchpad PPA for Guardian Project<br /><code>6B80 A842 07B3 0AC9 DEE2  35FE F50E ADDD 2234 F563</code></a>

## Android APK

We currently have two signing keys: a 4096-bit RSA key used for all new apps, and a 1024-bit RSA key that we use for all apps that we first released before 2014. You can download the whole public keys and verify it using the OpenPGP signature:

**4096-bit RSA**

  * [guardianproject-rsa4096-signing-certificate.pem](https://guardianproject.info/releases/guardianproject-rsa4096-signing-certificate.pem)
  * [guardianproject-rsa4096-signing-certificate.pem.sig](https://guardianproject.info/releases/guardianproject-rsa4096-signing-certificate.pem.sig)
  * [guardianproject-rsa4096-signing-publickey.pem](https://guardianproject.info/releases/guardianproject-rsa4096-signing-publickey.pem)
  * [guardianproject-rsa4096-signing-publickey.pem.sig](https://guardianproject.info/releases/guardianproject-rsa4096-signing-publickey.pem.sig)
  * You can see a survey of APKs signed by this key on Android Observatory:  
    <a href="https://androidobservatory.org/cert/4CB3F539F63B32ACA13B4450638D605F531D4F4A" target="_blank">https://androidobservatory.org/cert/4CB3F539F63B32ACA13B4450638D605F531D4F4A</a> 

**1024-bit RSA**

  * [guardianproject-rsa1024-signing-key.cer](https://guardianproject.info/releases/guardianproject-rsa1024-signing-key.cer)
  * [guardianproject-rsa1024-signing-key.cer.sig](https://guardianproject.info/releases/guardianproject-rsa1024-signing-key.cer.sig)
  * You can see a survey of APKs signed by this key on Android Observatory:  
    <a href="https://androidobservatory.org/cert/9F1960C9584FEE5E166419354985A2B5FE413570" target="_blank">https://androidobservatory.org/cert/9F1960C9584FEE5E166419354985A2B5FE413570</a> 

## FDroid Repo

Our official releases are also posted on our own FDroid repo, which is accessible at <https://guardianproject.info/fdroid/repo>. The signing key for that repo is available here:

  * [guardianproject-rsa4096-fdroid-repo-signing-key.pem](https://guardianproject.info/releases/guardianproject-rsa4096-fdroid-repo-signing-key.pem)
  * [guardianproject-rsa4096-fdroid-repo-signing-key.pem.sig](https://guardianproject.info/releases/guardianproject-rsa4096-fdroid-repo-signing-key.pem.sig)

The fingerprints for this signing key are:

<pre>Owner: &#69;&#x4d;&#65;&#x49;&#76;&#x41;D&#x44;R&#x45;S&#x53;=&#x72;o&#x6f;t&#x40;g&#x75;a&#x72;d&#105;&#x61;&#110;&#x70;&#114;&#x6f;&#106;&#x65;c&#x74;.&#x69;n&#x66;o, CN=guardianproject.info, O=Guardian Project, OU=FDroid Repo, L=New York, ST=New York, C=US
Issuer: &#69;&#x4d;&#65;&#x49;L&#x41;D&#x44;R&#x45;S&#x53;=&#x72;o&#111;&#x74;&#64;&#x67;&#117;&#x61;r&#x64;i&#x61;n&#x70;r&#x6f;j&#x65;c&#116;&#x2e;&#105;&#x6e;f&#x6f;, CN=guardianproject.info, O=Guardian Project, OU=FDroid Repo, L=New York, ST=New York, C=US
Serial number: a397b4da7ecda034
Valid from: Thu Jun 26 15:39:18 EDT 2014 until: Sun Nov 10 14:39:18 EST 2041
Certificate fingerprints:
 MD5:  8C:BE:60:6F:D7:7E:0D:2D:B8:06:B5:B9:AD:82:F5:5D
 SHA1: 63:9F:F1:76:2B:3E:28:EC:CE:DB:9E:01:7D:93:21:BE:90:89:CD:AD
 SHA256: B7:C2:EE:FD:8D:AC:78:06:AF:67:DF:CD:92:EB:18:12:6B:C0:83:12:A7:F2:D6:F3:86:2E:46:01:3C:7A:61:35
 Signature algorithm name: SHA1withRSA
 Version: 1
</pre>