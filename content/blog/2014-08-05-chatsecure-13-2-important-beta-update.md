---
id: 12577
title: 'ChatSecure 13.2: Important Beta!'
date: 2014-08-05T11:35:54-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=12577
permalink: /2014/08/05/chatsecure-13-2-important-beta-update/
categories:
  - New Release
tags:
  - crypto
  - jabber
  - mobile messaging
  - security
  - whatsapp
  - xmpp
---
Today is the first public beta of ChatSecure v13.2, an important update of the user interface, networking code, and overall stability. We’ve spent the last six months tracking down crashes, memory leaks and performance issues, and have reached a stable, functional point which we want to share for public use. Reliability and simplicity our the goals, as we move towards v14 in the next few months.

This beta also features a new account setup wizard that we are eager for feedback on. Our goal is to enable new users to have a much simpler experience in setting up ChatSecure to connect to existing or create new accounts. We have also provided a “one-click burner” option to quickly create throwaway accounts, that require Tor and OTR encryption always, for chatting with a single contact or even just a single conversation.

<div id='gallery-10' class='gallery galleryid-12577 gallery-columns-3 gallery-size-thumbnail'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122247.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122247-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122226.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122226-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122048.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122048-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122039.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-122039-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-121908.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-121908-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/sidebar.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/sidebar-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-121532.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2014/08/device-2014-08-05-121532-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" /></a>
    </dt>
  </dl>
  
  <br style='clear: both' />
</div>

We have also removed some features (for now), with the goal of focus on stripping down the experience, and then building it back up again. For example, there is now ONE contact list, that merges all contacts from all accounts together. It can be easily searched, and you don’t have to worry about which account is active – you just selected the person you want to communicate with, and we know which account they are associated with.

We have also removed the ability to manually set presence and status (for now), while we re-think how they should work in a mobile context a bit more. The vast majority of our users do not change either value anyhow, but we do know that smartly managing online vs away, especially if you are logged in from multiple locations to the same account, is important. Expect an update here shortly, and we’d love to have your feedback and fresh ideas on mobile presence.

You can currently access the beta directly via APK download (below),  through our [F-Droid Test Build “Nightlies” Repo](https://guardianproject.info/2014/06/06/automatic-private-distribution-of-our-test-builds/), or through our [Google+ Community Beta Access](https://plus.google.com/communities/108480576214602821006). We will roll out to our release repos and Google Play public once we get through our initial feedback on the beta.

**Download ChatSecure v13.2 Beta 1 Now**

<img class="alignleft size-full wp-image-12579" src="https://guardianproject.info/wp-content/uploads/2014/08/chatsecure-latest-qr.png" alt="chatsecure-latest-qr" width="123" height="123" srcset="https://guardianproject.info/wp-content/uploads/2014/08/chatsecure-latest-qr.png 123w, https://guardianproject.info/wp-content/uploads/2014/08/chatsecure-latest-qr-100x100.png 100w" sizes="(max-width: 123px) 100vw, 123px" />  
APK: [https://guardianproject.info/releases/ChatSecure-v13.2.0-BETA-1.apk  
](https://guardianproject.info/releases/ChatSecure-v13.2.0-BETA-1.apk)  
PGP Sig: <https://guardianproject.info/releases/ChatSecure-v13.2.0-alpha-10.apk.asc>

 

 

The source is tagged here: <https://github.com/guardianproject/ChatSecureAndroid/releases/tag/13.2.0-beta-1>

The release includes fixes from our completed [v13 milestone](https://dev.guardianproject.info/projects/gibberbot/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=fixed_version_id&op%5Bfixed_version_id%5D=%3D&v%5Bfixed_version_id%5D%5B%5D=102&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&c%5B%5D=due_date&group_by=), and our [v14 milestone “Armadillo’s Agram”](https://dev.guardianproject.info/versions/121), which you can view on our project tracker (<https://dev.guardianproject.info/projects/gibberbot/>).

 

 