---
id: 13519
title: 'Combating &#8220;Fake News&#8221; With a Smartphone &#8220;Proof Mode&#8221;'
date: 2017-02-24T02:10:47-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=13519
permalink: /2017/02/24/combating-fake-news-with-a-smartphone-proof-mode/
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "484"
discourse_permalink:
  - https://talk.developersquare.net/t/combating-fake-news-with-a-smartphone-proof-mode/349
discourse_comments_count:
  - "4"
discourse_comments_raw:
  - '{"id":349,"posts_count":5,"filtered_posts_count":5,"posts":[],"participants":[{"id":13,"username":"n8fr81","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/n8fr81/{size}/19_1.png"},{"id":224,"username":"teeks99","avatar_template":"https://avatars.discourse.org/v2/letter/t/8e8cbc/{size}.png"},{"id":222,"username":"matclab","avatar_template":"https://avatars.discourse.org/v2/letter/m/cc9497/{size}.png"},{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553110822"
wpdc_sync_post_comments:
  - "0"
image: http://guardianproject.info/wp-content/uploads/2017/02/ProofMode-feature-graphic.png
categories:
  - New Release
---
We have been working for many years with our partners at [WITNESS](https://witness.org), a leading human rights media training and advocacy organization, to figure out how best to turn smartphone cameras into tools of empowerment for activists. While it is often enough to use the visual pixels you capture to create awareness or pressure on an issue, sometimes you want those pixels to actually be treated as evidence. This means, you want people to trust what they see, to know it hasn&#8217;t been tampered with, and to believe that it came from the time, place and person you say it came from.

Enter, [**ProofMode**](https://github.com/guardianproject/proofmode), a light, minimal &#8220;reboot&#8221; of our more heavyweight, verified media app, [CameraV](https://guardianproject.info/apps/camerav). Our aim was to create a lightweight (< 3MB!), almost invisible utility (minimal battery impact!), that you can run all of the time on your phone (no annoying notifications or popups), that automatically adds extra digital proof data to all photos and videos you take. This data can then be easily shared, when you really need it, through a &#8220;Share Proof&#8221; share action, to anyone you choose over email or a messaging app, or uploaded to a cloud service or reporting platform.

&nbsp;

[<img class="size-medium wp-image-13520 alignleft" src="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-173908-169x300.jpg" alt="" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-173908-169x300.jpg 169w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-173908.jpg 540w" sizes="(max-width: 169px) 100vw, 169px" />](https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-173908.jpg)

[<img class="size-medium wp-image-13521 alignleft" src="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174004-169x300.jpg" alt="" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174004-169x300.jpg 169w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174004.jpg 540w" sizes="(max-width: 169px) 100vw, 169px" />](https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174004.jpg)

[<img class="size-medium wp-image-13522 alignnone" src="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174056-169x300.jpg" alt="" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174056-169x300.jpg 169w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174056.jpg 540w" sizes="(max-width: 169px) 100vw, 169px" />](https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174056.jpg)

&nbsp;

On the technical front, what the app is doing is automatically generating an OpenPGP key for this installed instance of the app itself, and using that to automatically sign all photos and videos at time of capture. A sha256 hash is also generated, and combined with a snapshot of all available device sensor data, such as GPS location, wifi and mobile networks, altitude,  device language, hardware type, and more. This is also signed, and stored with the media. All of this happens with no noticeable impact on battery life or performance, every time the user takes a photo or video. We have been running it for months on fairly old, low end phones, and you just forget it is happening.

&nbsp;

[<img class="alignnone size-medium wp-image-13542" src="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174146-169x300.jpg" alt="" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174146-169x300.jpg 169w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174146.jpg 540w" sizes="(max-width: 169px) 100vw, 169px" />](https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174146.jpg)   [<img class="alignnone size-medium wp-image-13544" src="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174156-169x300.jpg" alt="" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174156-169x300.jpg 169w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174156.jpg 540w" sizes="(max-width: 169px) 100vw, 169px" />](https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170222-174156.jpg)

_While we are very proud of the work we did with the CameraV and InformaCam projects, the end results was a complex application and novel data format that required a great deal of investment by any user or community that wished to adopt it._ Furthermore, CameraV is an app that you have to decide and remember to use, in a moment of crisis. With ProofMode, we both wanted to simplify the adoption of the tool, and make it nearly invisible to the end-user, while making it the adoption of the tool by organizations painless through simple formats like CSV and known formats like PGP signatures.

The source and direct APK downloads are available on Github: <https://github.com/guardianproject/proofmode>

The beta release is also available today for Android phones on [Google Play](https://play.google.com/store/apps/details?id=org.witness.proofmode). We hope to have an iPhone version in beta in the next few months.

We have also published a sample batch proof data set on Github here: <https://github.com/guardianproject/proofmode/tree/master/samples/sample-proof-1>

&nbsp;

**Our design goals included the following:**

  * Run all of the time in the background without noticeable battery, storage or network impact
  * Provide a no-setup-required, automatic new user experience that works without requiring training
  * Use strong cryptography for strong identity and verification features, but not encryption
  * Produce &#8220;proof&#8221; sensor data formats that can be easily parse, imported by existing tools (CSV)
  * Do not modify the original media files; all proof metadata storied in separate file
  * Support chain of custody needs through automatic creation of sha256 hashes and PGP signatures
  * Do not require a persistent identity or account generation

We also were able to take advantage of the new Android &#8220;Quick Settings&#8221; developer API, to add a ProofMode toggle button right along side other system functions like Wifi, Location, Bluetooth and more. This fulfills a vision that WITNESS has had for a while in mainstreaming the concept of our prototype into mainstream adoption, giving every citizen journalist a quick mode to activate when their moment arrives.

[<img class="alignnone wp-image-13532 size-large" src="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170223-220633-576x1024.png" width="576" height="1024" srcset="https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170223-220633-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170223-220633-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170223-220633-768x1365.png 768w, https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170223-220633.png 1080w" sizes="(max-width: 576px) 100vw, 576px" />](https://guardianproject.info/wp-content/uploads/2017/02/Screenshot_20170223-220633.png)

&nbsp;

You can read a bit more in the project [README](https://github.com/guardianproject/proofmode/blob/master/README.md) on the workflow we imagine being used for all of this. What we hope is that the ProofMode app is simple and low impact enough that potential users will install and forget that it is there. It will go along doing its business quietly without fuss, until the user realizes they have taken a photo or video that might have some value as digital evidence. Then, using the SHARE PROOF action, they can send their proof dataset off to an organization, journalist, lawyer, or other advocate that would be able to verify the chain of custody and integrity of the files and proof using off the shelf OpenPGP and CSV visualization tools. While we have a bit more work to do making the verification and visualization process easier, we already have many partners at human rights organizations and in newsrooms who are skilled and capable of working with this kind of data today.

If you&#8217;d like to learn more about the [CameraV](https://guardianproject.info/apps/camerav) app and our collaboration with [WITNESS](https://witness.org) and [Coletivo Papo Reto](https://www.facebook.com/ColetivoPapoReto/) video activist group in Brazil, please watch this video below from the [Al Jazeera &#8220;Rebel Geeks&#8221; documentary](http://www.aljazeera.com/programmes/rebelgeeks/2015/12/bigger-brother-151216102151145.html).

<div class="arve-wrapper" data-mode="normal" data-provider="youtube" id="arve-ssbezlRkxt8" style="max-width:945px;" itemscope itemtype="http://schema.org/VideoObject">
  <div class="arve-embed-container" style="padding-bottom:56.250000%">
  </div>
</div>

&nbsp;