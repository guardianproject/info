---
id: 12682
title: CipherKit reproducible builds
date: 2015-09-21T10:54:05-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12682
permalink: /2015/09/21/cipherkit-reproducible-builds/
discourse_post_id:
  - "258"
discourse_permalink:
  - https://talk.developersquare.net/t/cipherkit-reproducible-builds/155
catchresponsive-layout-option:
  - default
catchresponsive-header-image:
  - default
catchresponsive-featured-image:
  - default
publish_to_discourse:
  - "1"
discourse_comments_count:
  - "4"
discourse_comments_raw:
  - '{"id":155,"posts_count":5,"filtered_posts_count":5,"posts":[],"participants":[{"id":14,"username":"marvin","avatar_template":"https://avatars.discourse.org/v2/letter/m/2bfe46/{size}.png"},{"id":13,"username":"n8fr81","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/n8fr81/{size}/19_1.png"},{"id":17,"username":"hans","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/hans/{size}/33_1.png"},{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553108420"
wpdc_sync_post_comments:
  - "0"
categories:
  - News
tags:
  - android
  - bazaar
  - cipherkit
  - deterministic build
  - faketime
  - iocipher
  - martusvmm
  - reproducible build
  - reproducible builds
  - security
---
[<img src="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg" alt="alberti cipher disk" width="150" height="150" class="alignright size-thumbnail wp-image-3079" srcset="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg 245w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg)

We have been on a kick recently with making our build process support “reproducible builds” aka “deterministic builds”. What is this reproducible thing? Basically, what that means is that you can run a script and end up with the _exact_ same binary file as our official releases, be it a APK, JAR, AAR, whatever. That lets anyone verify that our releases are produced only from the source in git, without including anything else, whether deliberately or accidentally (like malware).

Our core CipherKit libraries are the more sensitive areas, so that’s where we’ve started. We generally work on Debian and Ubuntu and recommend that platform, but we recognized that OSX is a popular platform for Android developers also. So this process will work on OSX too, using your favorite package manager (e.g. Fink, MacPorts, or Homebrew).

Then you will end up with `IOCipher-v0.3.zip`, which includes the .jar and .so files. If your setup is close enough to our release build setup, the contents of that ZIP file will be the same as the official release. Right now, it is difficult to get the exact same binary file (e.g. the same sha256 sum) because of the timestamps in the .zip and varitions caused by using different versions of Java, and Android SDK and NDK. To check the contents of your build versus the official release:

<pre>sudo apt-get install faketime unzip wget meld
cd /tmp
wget https://guardianproject.info/releases/IOCipher-v0.3.zip
wget https://guardianproject.info/releases/IOCipher-v0.3.zip.sig
gpg --verify IOCipher-v0.3.zip.sig
git clone https://github.com/guardianproject/IOCipher
cd IOCipher
git checkout v0.3
./make-release-build
./compare-to-official-release IOCipher-v0.3.zip /tmp/IOCipher-v0.3.zip
</pre>

### What is happening here?

_meld_ (_FileMerge_ on OSX) will show a listing of all files listed, and which ones are different. You can see that the contents of the _.class_ files and _.so_ files all match, but there will be inevitable differences in some of the metadata. Native builds are much more sensitive to changes in the toolchain. The Java _.class_ files are usually reproducible even when using different versions of Java and the Android SDK. Native builds are almost never reproducible if the NDK version is at all different. Sometimes even the host platform where the NDK is running (e.g. Ubuntu vs OSX, or 64-bit vs 32-bit) will cause differences in the final binaries.

<div id="attachment_13105" style="width: 883px" class="wp-caption alignnone">
  <a href="https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-MANIFEST.MF-_tmp-IOCipher-v0.3-MANIFEST.MF-Meld.png"><img aria-describedby="caption-attachment-13105" src="https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-MANIFEST.MF-_tmp-IOCipher-v0.3-MANIFEST.MF-Meld.png" alt="The NDK version and build platform are listed in the manifest." width="873" height="591" class="size-full wp-image-13105" srcset="https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-MANIFEST.MF-_tmp-IOCipher-v0.3-MANIFEST.MF-Meld.png 873w, https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-MANIFEST.MF-_tmp-IOCipher-v0.3-MANIFEST.MF-Meld-300x203.png 300w" sizes="(max-width: 873px) 100vw, 873px" /></a>
  
  <p id="caption-attachment-13105" class="wp-caption-text">
    The NDK version and build platform are listed in the manifest.
  </p>
</div>

<div id="attachment_13104" style="width: 883px" class="wp-caption alignnone">
  <a href="https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-_tmp-IOCipher-v0.3-Meld.png"><img aria-describedby="caption-attachment-13104" src="https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-_tmp-IOCipher-v0.3-Meld.png" alt="The Java .class files are exactly the same, but the native .so files are not." width="873" height="591" class="size-full wp-image-13104" srcset="https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-_tmp-IOCipher-v0.3-Meld.png 873w, https://guardianproject.info/wp-content/uploads/2015/09/Screenshot-.-IOCipher-v0.3-_tmp-IOCipher-v0.3-Meld-300x203.png 300w" sizes="(max-width: 873px) 100vw, 873px" /></a>
  
  <p id="caption-attachment-13104" class="wp-caption-text">
    The Java .class files are exactly the same, but the native .so files are not.
  </p>
</div>

[<img src="https://guardianproject.info/wp-content/uploads/2015/09/1024px-End_CEST.svg_-150x150.png" alt="faketime" width="150" height="150" class="alignright size-thumbnail wp-image-13098" srcset="https://guardianproject.info/wp-content/uploads/2015/09/1024px-End_CEST.svg_-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2015/09/1024px-End_CEST.svg_-300x300.png 300w, https://guardianproject.info/wp-content/uploads/2015/09/1024px-End_CEST.svg_-200x200.png 200w, https://guardianproject.info/wp-content/uploads/2015/09/1024px-End_CEST.svg_.png 1024w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2015/09/1024px-End_CEST.svg_.png)

Timestamps are a very common issue when trying to reproduce a build. The release build process uses <a href="https://github.com/wolfcw/libfaketime" target="_blank"><code>faketime</code></a> to provide consistent timestamps, which are picked from the git commit. `faketime` freezes the clock entirely for native builds, so any timestamps from that process will always be exactly the same. Unfortunately, some parts of the `ant` Java build rely on the clock moving forward, so freezing clock makes the build freeze forever. Instead, `faketime` sets the clock using the time from the git commit, then moves time forward at 5% of the normal speed. That makes it much more likely that the timestamps will be the same, but usually what seems to happen is that the timestamps are 2 seconds off, which is the time resolution of the ZIP format. A better solution is needed here for JARs, they are easiest to verify using a sha256 sum. JAR signatures mostly seem not worth the pain they introduce. APKs signatures do not sign the whole APK, only the contents, so the varying timestamps do not matter when verifying using a APK signature. Another example of a difference: if comparing a debug build to a release build, then `BuildConfig.class` will be difference because of the debug stuff. The sort order of the metadata in the jar MANIFEST.MF might also be different.

### The end goal

Reproducing builds is an arcane process, for sure. It is a means to an end. The goal is to get to the point where well known binaries, published in places like MavenCentral or jCenter, can easily be verified by anyone who cares to try. Or people could even set up <a href="https://f-droid.org/wiki/page/Verification_Server" target="_blank">servers that automatically try</a> to reproduce any JAR used in a project.

Then people can verify those JARs in a fully decentralized manner, and publish certifications in their preferred format (GPG signatures, SHA256 sums for gradle-witness, etc). Then we can feel safe getting the release from anywhere on the internet, no matter the level of security or malware infestation.

Towards that goal, we have been getting our libraries all nicely packaged up and submitted to jCenter (the default gradle repository for Android). Here are the relevant bits to include in your build.gradle:

<pre>compile 'info.guardianproject.cacheword:cachewordlib:0.1'
compile 'info.guardianproject.iocipher:IOCipher:0.3'
compile 'info.guardianproject.netcipher:netcipher:1.2'
compile 'info.guardianproject.trustedintents:trustedintents:0.0'

compile 'net.freehaven.tor.control:jtorctl:0.2'
</pre>

SQLCipher-for-Android is coming soon:  
<a href="https://github.com/sqlcipher/android-database-sqlcipher/pull/197" target="_blank">https://github.com/sqlcipher/android-database-sqlcipher/pull/197</a>  
I hope to also get them up on MavenCentral as well, since that one is also quite common on Android, and is a community run resource versus Bintray’s jCenter, which is purely a for-profit company.