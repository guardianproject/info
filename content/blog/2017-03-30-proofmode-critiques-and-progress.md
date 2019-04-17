---
id: 13577
title: ProofMode critiques and progress
date: 2017-03-30T09:53:22-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=13577
permalink: /2017/03/30/proofmode-critiques-and-progress/
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "498"
discourse_permalink:
  - https://talk.developersquare.net/t/proofmode-critiques-and-progress/358
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":358,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553108600"
wpdc_sync_post_comments:
  - "0"
image: http://guardianproject.info/wp-content/uploads/2017/03/Sherlock-Holmes-and-the-Tools-of-Deduction-spillwords.jpg
categories:
  - Advisory
  - Development
tags:
  - proofmode
---
Bruce Schneier was kind enough to [post about our work on ProofMode](https://www.schneier.com/blog/archives/2017/03/proof_mode_for_.html?utm_source=dlvr.it&utm_medium=twitter) to his [blog](https://www.schneier.com). A decent set of comments ensued, which we have considered, measured and weighed. We posted the response below on the post, and now also here. We also received an excellent set of [feedback from the Lieberbiber blog](http://www.lieberbiber.de/2017/03/07/the-guardian-projects-proof-mode-app-for-activists-doesnt-work/). Below are responses to the various concerns raised, and links to work completed or in progress.

* * *

At a high level, securely dating files, digital notarization, easy capture of sensor metadata, among other things, are not solved problems. For every day activists around the world, who may only have a cheap smartphone as their only computing device, they have no easy way to do any of these things. Even for high-level war crimes investigators, they are often using consumer point and shoot digital cameras, and documenting everything on paper.

ProofMode is a simplified version of a much more complex and thorough system and app that we have built, called CameraV. In that model, we use a built-in custom camera, encrypted internal storage and much more complex set of metadata to generate the evidence and proof. We also capture baseline images from the sensor, and require those to be shared with the key, so that we can later match evidence photos from the sensor itself. You can read more about some of this here:  
<a href="https://guardianproject.github.io/informacam-guide/en/InformacamGuide.html" rel="nofollow">https://guardianproject.github.io/informacam-guide/en/InformacamGuide.html</a>

We loved CameraV, but it was too complicated. Many frontline activists looking for a means to timestamp, sign, and otherwise add extra verifiable metadata to photos and videos they were capturing, found CameraV to be too complicated and burdensome. They helped us to design ProofMode, to strip it down to its bare essentials. In this case, we are working within pre-existing communities, with a shared set of pre-existing trust. What the activists are looking for is richer metadata, in easy to parse formats, that has timestamping, and some kind of cryptographic verification around it.

We know our approach is not bulletproof, and that smart people like this who comment on this blog can fool it six ways from Sunday. This ProofMode release was versioned &#8220;0.0.x&#8221; for a reason. We are not saying it is finished by any means, clearly. We are actively developing it, and have a roadmap that will address most of not all of the major concerns pointed out here, while ALSO keeping it simple, streamlined, focused and easy to use.

For example, we have implemented the Google SafetyNet API (https://koz.io/inside-safetynet/) for automatically signing the hashes of the media, checking that the app is running on an actual Android device that wasn&#8217;t tampered with, and verifying the hash of the APK app itself matches our officially released version. Google&#8217;s servers produced a signed blob of data that gets appending to our proof data, and that can be verified later on a desktop or server. This one feature counteracts most of the &#8220;hey I can just fake this by hand with GPG&#8221; comments:  
<a href="https://github.com/guardianproject/proofmode/issues/15" rel="nofollow">https://github.com/guardianproject/proofmode/issues/15</a>

We are integrating supporting for OpenTimestamps and other blockchain based notary systems like Stampery: <a href="https://github.com/guardianproject/proofmode/issues/8" rel="nofollow">https://github.com/guardianproject/proofmode/issues/8</a>  
For now, the app makes it very easy to send out a tweet, SMS or even a Signal message of the media&#8217;s hash, as a way to notarize it to various kinds of end points. We are working with human rights organizations to setup Signal-based notaries for their own internal logging.

The analysis on the <a href="http://www.lieberbiber.de/" rel="nofollow">http://www.lieberbiber.de</a> site is a good one, and also brings up the method by which we monitor for the presence of new photos and videos. We&#8217;ve had some comments about directly launching and monitoring the camera, which are helpful, but since we want to run in the background, that won&#8217;t really work:  
<a href="https://github.com/guardianproject/proofmode/issues/7" rel="nofollow">https://github.com/guardianproject/proofmode/issues/7</a>

The real progress there is moving to a new method Android provides for monitoring media, and away from just watching it at the file system. This has been implemented for newer Android devices:  
<a href="https://github.com/guardianproject/proofmode/commit/0ea9c9d73d7e55de612c89c466ef87da3524b6f1" rel="nofollow">https://github.com/guardianproject/proofmode/commit/0ea9c9d73d7e55de612c89c466ef87da3524b6f1</a>

We are also looking at how we generate and store the keys we generate in the app. We agree that we did the minimal amount of work necessary to store and secure the key, just relying on the Android app sandboxing for now. We never intended this key to be used for encryption or longterm identity. Our thinking was more focused on integrity through digital signatures, with a bit of lightweight, transient identity added on.

That said, we will be moving the key and credentials into the Android Keystore, which is the most secure key management solution possible on Android today.  
<a href="https://github.com/guardianproject/proofmode/issues/16" rel="nofollow">https://github.com/guardianproject/proofmode/issues/16</a>

All in all, it has just been a few weeks, and have already released multiple updates, that address most of the concerns that been raised. Work continues, and we hope that in no time, we&#8217;ll have an HSM-backed, yubikey-powered, blockchain-enabled, double ratchet encrypted and PQCrypto-resistent service, that will \*still\* be easy to use, under 3 MB and run on $100 Android phones.