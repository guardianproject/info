---
id: 12545
title: Introducing TrustedIntents for Android
date: 2014-07-30T23:29:23-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12545
permalink: /2014/07/30/introducing-trustedintents-for-android/
categories:
  - News
tags:
  - android
  - identity
  - martusvmm
  - security
  - usability
---
Following up on [our research on secure Intent interactions](https://guardianproject.info/2014/01/21/improving-trust-and-flexibility-in-interactions-between-android-apps/), we are now announcing the first working version of the <a href="https://github.com/guardianproject/TrustedIntents" target="_blank"><em>TrustedIntents</em></a> library for Android. It provides methods for checking any Intent for whether the sending and receiving app matches a specified set of trusted app providers. It does this by &#8220;pinning&#8221; to the signing certificate of the APKs. The developer includes this &#8220;pin&#8221; in the app, which includes the signing certificate to trust, then _TrustedIntents_ checks `Intent`s against the configured certificate pins. The library includes pins for the Guardian Project and Tor Project signing certificates. It is also easy to generate the pin using our new utility <a href="https://github.com/guardianproject/checkey" target="_blank">Checkey</a> (available in <a href="https://guardianproject.info/2014/06/30/new-official-guardian-project-app-repo-for-fdroid/" target="_blank">our FDroid repo</a> and in <a href="https://play.google.com/store/apps/details?id=info.guardianproject.checkey" target="_blank">Google Play</a>).

<div id="attachment_12560" style="width: 310px" class="wp-caption alignright">
  <a href="https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone.png"><img aria-describedby="caption-attachment-12560" src="https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-300x168.png" alt="Checkey displaying the signing certificate of ChatSecure" width="300" height="168" class="size-medium wp-image-12560" srcset="https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-300x168.png 300w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-1024x576.png 1024w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-100x56.png 100w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-150x84.png 150w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-200x112.png 200w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-450x253.png 450w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-600x337.png 600w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone-900x506.png 900w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-phone.png 1280w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-12560" class="wp-caption-text">
    Checkey displaying the signing certificate of ChatSecure
  </p>
</div>

We hope to make this process as dead simple as possible by providing developers with this library. _TrustedIntents_ is currently set up as an &#8220;Android Library Project&#8221; but it could easily be a jar too, the code is currently quite simple, the plan is to add more convenience methods and also support for TOFU/POP in addition to pinning. For usage examples, check out <a href="https://github.com/guardianproject/TrustedIntentsExample" target="_blank"><em>TrustedIntentsExample</em></a> and the test project under the test/ subdir of the _TrustedIntents_ library source repo.

  * _TrustedIntents_ source: <a href="https://github.com/guardianproject/TrustedIntents" target="_blank">https://github.com/guardianproject/TrustedIntents</a>
  * example project: <a href="https://github.com/guardianproject/TrustedIntentsExample" target="_blank">https://github.com/guardianproject/TrustedIntentsExample</a>
  * wiki, issue tracker, etc: <a href="https://dev.guardianproject.info/projects/trustedintents/wiki" target="_blank">https://dev.guardianproject.info/projects/trustedintents/wiki</a>
  * _Checkey_ source: <a href="https://github.com/guardianproject/Checkey" target="_blank">https://github.com/guardianproject/Checkey</a>

_Checkey_ includes a simple method for generating the certificate pins. The pin is in the format of Java subclass of `ApkSignaturePin`, which provides all needed utility functions. The create the pin file, first install the app whose certificate you want to trust. Be sure to get it from a trusted source since you are going to be trusting the signing certificate of the APK that you have installed. Launch _Checkey_ and select that app in the list, you will see the certificate details show up on the top. To generate the .java file for pinning Intents, select **Generate Pin** from the menu and send the resulting file to yourself. That file is the pin, include it in your project, then load it into TrustedIntents by doing in `onCreate()` or wherever is appropriate:  
`<br />
TrustedIntents ti = TrustedIntents.get(context);<br />
ti.isTrustedSigner(MySigningCertificatePin.class);<br />
` 

<div id="attachment_12565" style="width: 610px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin.png"><img aria-describedby="caption-attachment-12565" src="https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin.png" alt="How to generate a pin file with Checkey" width="600" height="444" class="size-medium wp-image-12565" srcset="https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin-300x222.png 300w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin-100x74.png 100w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin-150x111.png 150w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin-200x148.png 200w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin-450x334.png 450w, https://guardianproject.info/wp-content/uploads/2014/07/checkey-generate-pin-600x445.png 600w" sizes="(max-width: 600px) 100vw, 600px" /></a>
  
  <p id="caption-attachment-12565" class="wp-caption-text">
    How to generate a pin file with Checkey
  </p>
</div>

### Gathering all the edge cases

One of the things I&#8217;ve focused on in the _TrustedIntents_ library is thinking about all the possible edge cases and how to check for them. It is rare that the main part of a security check algorithm fails, its almost always the edge cases that are the gotcha.

One example: _TrustedIntents_ should properly check all signing certificates on an APK. From what I&#8217;ve seen, it is rare that APKs are signed by more than one certificate, but the spec allows for that. There might be exploits related to not handling that.

Another thing is that _TrustedIntents_ uses the method that the Android code uses for comparing signatures: it does a byte-by-byte comparison of the signature byte arrays. Some apps area already doing something similar based on the hash of the signing certificate (i.e. the &#8220;fingerprint&#8221;). The Android technique will also be faster than hashing since the hash algorithm has to read the whole signature byte array anyway.

We&#8217;d love to have feedback, flames, comments, etc on any and all of this. [Let us know](https://guardianproject.info/contact/) how it works for you!