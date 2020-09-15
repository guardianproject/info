---
id: 12459
title: Automatic, private distribution of our test builds
date: 2014-06-06T17:17:01-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12459
permalink: /2014/06/06/automatic-private-distribution-of-our-test-builds/
categories:
  - News
tags:
  - android
  - bazaar
  - distribution
  - fdroid
  - orbot
  - privacy
  - prototype
  - tor
---
One thing we are very lucky to have is a good community of people willing to test out unfinished builds of our software. That is a very valuable contribution to the process of developing usable, secure apps. So we want to make this process as easy as possible while keeping it as secure and private as possible. To that end, we have set up an <a href="https://f-droid.org" target="_blank">FDroid</a> repository of apps generated from the test builds that our build server generates automatically every time we publish new code.

After this big burst of development focused on FDroid, it has become clear that FDroid has lots of promise for becoming a complete solution for the whole process of delivering software from developers to users. We have tried other ways of delivering test builds like HockeyApp and Google Play’s Alpha and Beta channels and have found them lacking. The process did not seem as easy as it should be. And of course, both of them leave a lot to be desired when it comes to privacy of the users. So this is the first step in hopefully a much bigger project.

To use our new test build service, first install FDroid by downloading it from the official source: https://f-droid.org. Then using a QR Code scanner like <a href="https://play.google.com/store/apps/details?id=com.google.zxing.client.android" target="_blank">Barcode Scanner</a>, just scan the QR Code below, and send it to FDroid **Repositories**. You can also browse to this page on your Android device, and click the link below to add it to FDroid: 

  * [https://dev.guardianproject.info/fdroid/repo](https://dev.guardianproject.info/fdroid/repo?fingerprint=F8ED4C73C125E7A67F99DB269480DAF50BE1758952E07EE5ABF116FE4B2DB1E8)

[<img src="https://guardianproject.info/wp-content/uploads/2014/06/dev.guardianproject.info-QR-e1402010770323.png" alt="dev.guardianproject.info" width="245" height="245" class="aligncenter size-full wp-image-12462" />](https://dev.guardianproject.info/fdroid/repo?fingerprint=F8ED4C73C125E7A67F99DB269480DAF50BE1758952E07EE5ABF116FE4B2DB1E8)

You can also use our test repo via an anonymized connection using the Tor Hidden Service (as of this moment, that means downloading an [official FDroid v0.71 build](https://f-droid.org/repo/org.fdroid.fdroid_710.apk)). Just get <a href="https://play.google.com/store/apps/details?id=org.torproject.android" target="_blank">Orbot</a> and turn it on, and the following .onion address will automatically work in FDroid, as long as you have a new enough version (0.69 or later).

  * [http://k6e4p7yji2rioxbm.onion/fdroid/repo](http://k6e4p7yji2rioxbm.onion/fdroid/repo?fingerprint=F8ED4C73C125E7A67F99DB269480DAF50BE1758952E07EE5ABF116FE4B2DB1E8)

[<img src="https://guardianproject.info/wp-content/uploads/2014/06/k6e4p7yji2rioxbm.onion-QR-e1402010779963.png" alt="k6e4p7yji2rioxbm.onion" width="245" height="245" class="aligncenter size-full wp-image-12463" />](http://k6e4p7yji2rioxbm.onion/fdroid/repo?fingerprint=F8ED4C73C125E7A67F99DB269480DAF50BE1758952E07EE5ABF116FE4B2DB1E8)