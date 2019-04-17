---
id: 12950
title: Building a trustworthy app store that respects privacy
date: 2015-06-02T16:38:03-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12950
permalink: /2015/06/02/building-a-trustworthy-app-store-that-respects-privacy/
spacious_page_layout:
  - default_layout
discourse_post_id:
  - "179"
discourse_permalink:
  - https://talk.developersquare.net/t/building-a-trustworthy-app-store-that-respects-privacy/99
publish_to_discourse:
  - "1"
discourse_comments_count:
  - "4"
discourse_comments_raw:
  - '{"id":99,"posts_count":5,"filtered_posts_count":5,"posts":[],"participants":[{"id":37,"username":"jvspl","avatar_template":"https://avatars.discourse.org/v2/letter/j/b782af/{size}.png"},{"id":13,"username":"n8fr81","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/n8fr81/{size}/19_1.png"},{"id":17,"username":"hans","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/hans/{size}/33_1.png"},{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553109705"
wpdc_sync_post_comments:
  - "0"
categories:
  - News
tags:
  - android
  - bazaar
  - cafebazaar
  - cnnic
  - fdroid
  - google play
  - master key
  - mimarket
  - pinning
  - privacy
  - security
  - xiaomi
---
One core piece of our approach is thinking about very high risk situations, like Ai Weiwei or Edward Snowden, then making the tools for operating under that pressure as easy to use as possible. That means that we might occasionally come across as a little paranoid. It is important to dive into the depths of what might be possible. That is an essential step in evaluating what the risks and defenses are, and how to prioritize them. Making usable software is not just making things easy, but rather making tools for real world situations that are a simple as possible.

[<img src="https://guardianproject.info/wp-content/uploads/2015/06/hrome-crash.png" alt="chrome crash" width="150" height="150" class="alignright size-full wp-image-12966" />](https://guardianproject.info/wp-content/uploads/2015/06/hrome-crash.png)

We recently received some vindication of our paranoia: we have been resistant to putting all of our trust into the Google Play app store, despite many obvious advantages. Even though Google Play is probably the most secure of the big app stores, its security approach is rather thin, <a href="https://jon.oberheide.org/blog/2010/06/28/a-peek-inside-the-gtalkservice-connection/" target="_blank">relying mainly on HTTPS with no signature for verification</a>, and the Five Eyes partnership (NSA, GCHQ, etc) noticed this, and <a href="https://firstlook.org/theintercept/2015/05/21/nsa-five-eyes-google-samsung-app-stores-spyware" target="_blank">worked to exploit it</a>.

The Android/Google Play security model is relatively simple, and that is mostly a good thing. There are two essential pieces: the signature on the APK file itself and the TLS connection to Google that provides the APK file. Once an app is installed, all APK files used to update an app must have a matching signing key. That provides a reasonably strong mechanism to defend against malware that wants to install over existing apps.

Unlike package systems like Debian, there is no path to verify that the APK signing key. That means Google Play relies heavily on the TLS transport encryption to protect the APK files for when installing an Android apps for the first time. The first time an app is installed, the signing key in that app’s APK file is blindly trusted (this is called “Trust On First Use” or TOFU). It turns out that TOFU has a solid track record for security in the real world. One key aspect of implementing a good TOFU system is to make the first use indistinguishable from any other use, so that it is difficult to target only first uses while ignoring repeat uses. Intercepting repeat uses is very likely to trigger a warning and alert the user that something is wrong.

Now let’s put together the pieces based on what the Chinese government can do. A few TLS certificate authorities have been caught <a href="http://arstechnica.com/security/2010/03/govts-certificate-authorities-conspire-to-spy-on-ssl-users/" target="_blank">issuing </a><a href="http://arstechnica.com/security/2011/08/earlier-this-year-an-iranian/" target="_blank">fake</a> <a href="http://arstechnica.com/business/2012/02/critics-slam-ssl-authority-for-minting-cert-used-to-impersonate-sites/" target="_blank">certificates</a>. A company affiliated with CNNIC <a href="https://arstechnica.com/security/2015/04/google-chrome-will-banish-chinese-certificate-authority-for-breach-of-trust/" target="_blank">was caught issuing certificates for Google domains</a>. A trusted certificate authority can issue usable certificates for any domain, so any computer that trusts CNNIC would trust their fake certificates for Google. That lets the Chinese government transparently Man-in-the-Middle traffic to Google servers. China could then use the Great Firewall to generate targeted malware on the fly, seeing the user credentials that Google Play requires, seeing the list of apps that each user has installed, etc. Then when the targeted user goes to install a new app, the APK file is intercepted, malware is added, then it is re-signed and transparently sent off to the user.

This targeted malware can be designed to avoid the malware scanners in Google Play, Lookout, etc. since it would be direct addition of code rather than via an exploit. It would be just adding Java classes to the APK. Or alternatively, in combination with some of the signing exploits that have been discovered in Android, like <a href="http://www.saurik.com/id/19" target="_blank">Master Key</a>, the Great Firewall is able to inject malware into the real APK itself without changing the signature.

Of course, when Google Play’s TLS connection includes X.509 <a href="https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning" target="_blank">certificate pinning</a>, then the above attack would not be possible since the client would have a whitelist of certificate authorities that it trusts for play.google.com, and CNNIC would probably not be on that whitelist. This highlights the importance of pinning certificate authorities in apps that need good security over TLS or HTTPS. All TLS connections <a href="http://nelenkov.blogspot.com/2012/12/certificate-pinning-in-android-42.html" target="_blank">support pinning at the system level</a> starting in Android 4.2. We are crazy enough to support down to Android 2.3 since there are lots of older Android devices in use, and even <a href="https://arstechnica.com/gadgets/2014/12/android-2-3-gingerbread-four-years-later-the-os-just-wont-die/" target="_blank">new devices being sold with Android 2.3.3</a>. That means we think about making apps self-contained in terms of security improvements like pinning.

[<img src="https://guardianproject.info/wp-content/uploads/2015/06/sadballs-150x300.png" alt="sad balls" width="150" height="300" class="alignright size-medium wp-image-12969" srcset="https://guardianproject.info/wp-content/uploads/2015/06/sadballs-150x300.png 150w, https://guardianproject.info/wp-content/uploads/2015/06/sadballs.png 400w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2015/06/sadballs.png)

**It gets worse**

Many indigenous app stores like <a href="http://cafebazaar.ir" target="_blank">Cafe Bazaar</a> and Xiaomi’s <a href="http://app.mi.com" target="_blank">MiMarket</a> lack basic protections like TLS, making targeted attacks trivial for governments, or even anyone who gains control of a piece of the network path. These days that is actually easy to do by exploiting home routers, which are <a href="https://arstechnica.com/security/2015/05/researchers-uncover-self-sustaining-botnets-of-poorly-secured-routers/" target="_blank">generally</a> <a href="https://arstechnica.com/security/2015/04/no-patch-for-remote-code-execution-bug-in-d-link-and-trendnet-routers/" target="_blank">easy</a> to <a href="https://arstechnica.com/security/2015/05/the-moose-is-loose-linux-based-worm-turns-routers-into-social-network-bots/" target="_blank">exploit</a>. One of those botnets would easily start looking for app installs in the network traffic, then add exploits accordingly. As long as the first install is easy to detect and the user easy to track, then the malware can transparently inject malware designed to be difficult to detect by malware scanners and people alike.

[<img src="https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3.png" alt="fdroidheader3" width="720" height="180" class="alignnone size-full wp-image-11906" srcset="https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3.png 720w, https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3-300x75.png 300w" sizes="(max-width: 720px) 100vw, 720px" />](https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3.png)  
**The Alternative**

<a href="https://f-droid.org" target="_blank">FDroid</a> also has the key advantage of being designed from the beginning to avoid tracking users, and to use proven methods of delivering software, following the signed repository model of Debian, Ubuntu, etc. but then served over a solid HTTPS channel for increased privacy and a backup layer of security. It is also possible to use privacy proxies like Tor or I2P via the proxy settings. There is no user credentials needed, it is all free software, so FDroid users can even hide themselves from the server delivering the apps, as well as any network observers. Since all APKs are delivered via signed metadata that is verified using a key built into the FDroid client app, there is no risk of getting served malware even if the HTTPS connection is completely and transparently broken.

As part of our <a href="https://dev.guardianproject.info/project/bazaar/wiki" target="_blank">Bazaar Project</a>, we have been putting more and more efforts into the FDroid project, and working to make it much easier to use. All Guardian Project apps are available in FDroid, as well as all the core apps that you might need like Firefox, a Twitter client, K-9 email, etc. Tech journalist <a href="https://medium.com/backchannel/why-i-m-saying-goodbye-to-apple-google-and-microsoft-78af12071bd" target="_blank">Dan Gillmor agrees</a>: free software that respects privacy is not only for the über-geek anymore.