---
id: 11733
title: 'How to Migrate Your Android App’s Signing Key'
date: 2015-12-29T12:03:54-04:00
author: Abel Luck
layout: post
guid: https://guardianproject.info/?p=11733
permalink: /2015/12/29/how-to-migrate-your-android-apps-signing-key/
categories:
  - Development
  - HowTo
  - Research
tags:
  - Android
  - bazaar
  - encryption
  - F-Droid
  - fdroid
  - howto
  - identity
  - rsa
  - security
  - signing key
  - TrustedIntents
---
  


**It is time to update to a stronger signing key for your Android app! The old default RSA 1024-bit key is weak and officially deprecated.**

## What?

The Android OS requires that every application installed be signed by a digital key. The purpose behind this signature is to identify the author of the application, allow this author and this author alone to make updates to the app, as well as provide a mechanism to establish inter-application trust. The Android security model defines an app by two things: the package name (aka <a href="https://developer.android.com/reference/android/content/Context.html#getPackageName%28%29" target="_blank"><code>packageName</code></a>, <a href="https://sites.google.com/a/android.com/tools/tech-docs/new-build-system/applicationid-vs-packagename" target="_blank"><code>ApplicationID</code></a>, <a href="https://developer.android.com/guide/topics/manifest/manifest-element.html#package" target="_blank"><code>package</code></a>) and the signing key. If either of those are different, then Android considers it a different app. When the package name and signing key of one APK match an installed app, then the APK is considered an update and Android will replace the installed app with the APK. If the APK is signed by a different key, then Android will prevent installing and updating.

First thing is to see what the current signing key is. Check any app’s signing key using our free utility app <a href="https://play.google.com/store/apps/details?id=info.guardianproject.checkey" target="_blank">Checkey</a>:

<div id="attachment_13170" style="width: 790px" class="wp-caption alignnone">
  <a href="https://guardianproject.info/wp-content/uploads/2015/12/checkey-1.png" rel="attachment wp-att-13170"><img aria-describedby="caption-attachment-13170" src="https://guardianproject.info/wp-content/uploads/2015/12/checkey-1-1024x576.png" alt="Lookout needs to generate a new key!" width="780" height="439" class="size-large wp-image-13170" srcset="https://guardianproject.info/wp-content/uploads/2015/12/checkey-1-1024x576.png 1024w, https://guardianproject.info/wp-content/uploads/2015/12/checkey-1-300x169.png 300w, https://guardianproject.info/wp-content/uploads/2015/12/checkey-1-768x432.png 768w, https://guardianproject.info/wp-content/uploads/2015/12/checkey-1-350x197.png 350w, https://guardianproject.info/wp-content/uploads/2015/12/checkey-1-860x484.png 860w, https://guardianproject.info/wp-content/uploads/2015/12/checkey-1.png 1280w" sizes="(max-width: 780px) 100vw, 780px" /></a>
  
  <p id="caption-attachment-13170" class="wp-caption-text">
    Lookout needs to generate a new key!
  </p>
</div>

The official Android docs have tons of useful information about what the signing keys are good for, how to generate them, and how to use them. Unfortunately, it doesn’t provide any instructions for migrating, and for many years, 1024-bit RSA was the default. But first, why would you want or need to migrate?

## Why?

Depending on when you created your signing key, you might have a particularly weak key. The primary danger of a weak key is that an adversary could break your key in order to generate fake APK signatures. Then those malicious APKs can be installed as updates to your app. There are other nefarious purposes depending on how you use the signing key in your apps. Or if you are unfortunate enough to have suffered a loss of your private key material, then it is definitely time for a new signing key.

According to our friends at the [Android Observatory](https://androidobservatory.org/stats "Android Observatory"), over 64% of Android apps in their data store use 1024-bit signing keys (RSA or DSA).

<div id="visualization" style="width: 600px; height: 400px;">
</div>

There are several good reasons to migrate off of 1024-bit RSA keys, even though there is no _public_ proof of a 1024 prime factorization required to generate any 1024-bit key at will. The evidence has been mounting for a decade.

NIST’s [official guidelines](http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57_part1_rev3_general.pdf) (PDF, page 64 and 67) deprecated 1024-bit RSA keys at the end of 2013. This deprecation by NIST isn’t an indication that 1024-bit RSA is compromised, instead it is a preemptive move to stay ahead of attacks. Confidence in NIST might be shaken in light of [recent revelations](http://blog.cryptographyengineering.com/2013/09/on-nsa.html), but in this case increasing the RSA key size is unlikely to trigger any secret NSA backdoors. If anything, the deprecation year could have been extended slightly to allow the NSA a window where they had the capacity to factor 1024-bit keys and everyone was still using them. So, it’s time to move on.

For an example, a decade ago the cost of building special purpose hardware capable of breaking a single 1024-bit RSA key in one year was estimated at $10 million ([Adi Shamir, Eran Tromer, On the cost of factoring RSA-1024](http://tau.ac.il/~tromer/papers/cbtwirl.pdf), 2003). Presumably the techniques have improved by orders of magnatude, and the hardware value depreciated. It is conceivable the cost has fallen enough to be affordable not only by nation-state actors, but by large criminal enterprises too. 

For a comprehensive talk on the state of the art (as of December 2012) when it comes to breaking 1024-bit RSA, check out the 29C3 talk [FactHacks: RSA factorization in the real world](http://events.ccc.de/congress/2012/Fahrplan/events/5275.en.html "FactHacks: RSA factorization in the real world") with the cryptographers Daniel J. Bernstein, Nadia Heninger, and Tanja Lange ([watch recording](http://events.ccc.de/congress/2012/wiki/Documentation#Recordings "29C3 Recordings"))

## How?

Migrating to a strong key for an Android app is, unfortunately, not so simple. If you are publishing a _new_ app to the app store, then simply generate a new strong signing key and you’re done. Congratulations! However, there exists no easy way to update your signing key for an existing application, because an installed application can only take updates from an APK signed with _the same_ key. 

Here we outline a basic method with which you can use to fake an update to your signing key. This is not as user friendly as we would like. Some of the hard facts of performing this process is that for most app stores including Google Play, you will lose ratings and reviews since the app will show up with a new package name, and the app store will treat it like an entirely new app. Also, the user will have to manually uninstall the original app once they finish the procedure. Here is a rough outline of the process:

  1. generate the new signing key, _RSA 4096_
  2. Update the first app, _App1_, with a mechanism for exporting private data, using <a href="https://github.com/guardianproject/TrustedIntents" target="_blank">TrustedIntents</a> with a signature pin of the new key, _RSA 4096_, which <a href="https://guardianproject.info/2014/07/30/introducing-trustedintents-for-android/" target="_blank">Checkey will generate for you</a>
  3. Create a new version of the app with a different package name, _App2_
  4. sign _App2_ with new key, _RSA 4096_
  5. Add method to _App2_ for receiving user data from _App1_, including a signature pin of the old signing key, _RSA 1024_, for use with TrustedIntents
  6. Publish _App2_ to the app stores
  7. From _App1_, prompt user to install _App2_
  8. runs and imports data from _App1_
  9. _App2_ prompts user to uninstall _App1_

For <a href="https://f-droid.org" target="_blank">F-Droid</a>, there will be some easier tools for handling this. The F-Droid system is already used to multiple signing keys per app since F-Droid uses its own signing key for many of the apps it releases, and that F-Droid signing key is different from the signing key that the original developer used in their Google Play uploads. F-Droid will likely be able to support APKs with the same package name but with multiple signing keys.

### A Note on Compatibility

There is security vs compatibility trade off a few might be interested in. Pre-4.3, Android did not support any signature algorithms except SHA1. With Android >= 4.3, SHA256 support was fixed, and SHA384, SHA512, and ECDSA were added ([source](https://code.google.com/p/android/issues/detail?id=38321)). There are still android 2.3.3 (`android-10`) devices being sold, so anyone interested in backwards compatibility will have to heed this.

Also, the larger the keysize and hashsize used, the longer it takes to install and update the application. So extremely large values might be unsuitable for slower hardware. The following probably doesn’t buy you a tremendous amount of additional security but cranks the paranoia to 11. It does so at the cost of compatibility and performance.  
`<br />
Gen with:<br />
  keytool -genkey -v -keystore test.keystore -alias testkey -keyalg RSA -keysize 4096 -sigalg SHA512withRSA -dname "cn=Test,ou=Test,c=CA" -validity 10000</p>
<p>Sign with:<br />
  jarsigner -verbose -sigalg SHA512withRSA -digestalg SHA512 -keystore test.keystore test.apk testkey<br />
` 

We have some scripts that we use to generate keys in our <a href="https://github.com/guardianproject/smartcard-apk-signing" target="_blank">smartcard-apk-signing</a> repo. It is also possible to generate an Android signing key using openssl or other libraries. It is often wise to use different software than standard for doing things like generating keys. Since the Java `keytool` approach that is the standard, recommended method for Android, that makes it a target for adversaries that are interested in breaking keys. If a key was generated using `openssl` or GNU TLS instead, for example, then that key would not be affected if `keytool` had <a href="https://freedom-to-tinker.com/blog/kroll/software-transparency-debian-openssl-bug/" target="_blank">a bug like Debian’s</a> <a href="https://security-tracker.debian.org/tracker/CVE-2008-0166" target="_blank">CVE-2008-0166</a>.