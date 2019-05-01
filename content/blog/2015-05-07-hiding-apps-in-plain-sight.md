---
id: 12937
title: Hiding Apps in Plain Sight
date: 2015-05-07T09:25:10-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=12937
permalink: /2015/05/07/hiding-apps-in-plain-sight/
image: http://guardianproject.info/wp-content/uploads/2015/05/Tanzania_0607_cropped_Nevit.jpg
categories:
  - Development
  - HowTo
tags:
  - physical security
  - stealth
---
Beyond just thinking about encryption of data over the wire, or at rest on your mobile device, we also consider physical access to your mobile device, as one of the possible things we need to defend against. Some of our apps, such as Courier, our secure news reader, include a Panic feature, enabling a user to quickly delete data or remove the app, if they fear their device will be taken from them, whether by a friend, family member, criminal or an authority figure. Most recently, with our work on CameraV, our [secure evidence camera app](https://guardianproject.github.io/informacam-guide/en/InformacamGuide.html), we have implemented a few more features that help hide the app and its data, in order to block an unintended person from seeing the photos and videos captured by it.

First, it should be said that the app utilizes [IOCipher](https://guardianproject.info/code/iocipher), [CacheWord](https://github.com/guardianproject/cacheword) and the [CameraCipher Library](https://github.com/n8fr8/CameraCipher) to store all media files it captures in an encrypted format, managed with a well-implemented service that handles key generation and life-cycle properly. This means that no photos and videos show in the device’s built-in gallery or photos app, and no pixels are ever written in plain-text to any storage space, internal or external. This helps a great deal in hiding that they exist, since often physical inspection of a device often starts with looking through any of the default apps, like messaging, gallery, contacts apps, and so on. [ChatSecure](https://guardianproject.info/apps/chatsecure/) also does this, be keeping your contacts, messages and media out of the shared, unencrypted default location.

As of this week, we have had three new features to CameraV that all fall under what could be called “Stealth Mode” (though this has also been called “Boss Mode” since the days of MS-DOS when games included a quick button to change to something that looked like a spreadsheet for when your boss walked by). We took our inspiration from a few other apps, like Amnesty International’s [Panic Button](https://panicbutton.io/) which hides itself as a calculator, ChainFire’s [SuperSU](https://play.google.com/store/apps/details?id=eu.chainfire.supersu&hl=en), which allows users to [switch the app icon](http://www.chainfire.eu/articles/133/_TUT_Supporting_multiple_icons_in_your_app/) between a few options, [Courier](https://guardianproject.info/apps/courier/), which blocks users and other apps from taking screenshots of the news it is display, and [Orbot](https://guardianproject.info/apps/orbot), which actively removes itself from the “Recent Apps” listing provided by Android. All of these features combined dramatically reduce the visual footprint that an app leaves on the device, reducing the chance that someone will discover it, even if they are looking for it.

<div id="attachment_12938" style="width: 179px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-24-36.png"><img aria-describedby="caption-attachment-12938" class="wp-image-12938 size-medium" src="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-24-36-169x300.png" alt="CameraV settings for stealth mode" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-24-36-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-24-36-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-24-36.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
  
  <p id="caption-attachment-12938" class="wp-caption-text">
    CameraV settings for stealth mode
  </p>
</div>

<div id="attachment_12939" style="width: 179px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-25-44.png"><img aria-describedby="caption-attachment-12939" class="wp-image-12939 size-medium" src="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-25-44-169x300.png" alt="CameraV marinading as "CV Settings"" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-25-44-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-25-44-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-14-25-44.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
  
  <p id="caption-attachment-12939" class="wp-caption-text">
    CameraV masquerading as “CV Settings”
  </p>
</div>

<div id="attachment_12940" style="width: 179px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-11-02-46.png"><img aria-describedby="caption-attachment-12940" class="wp-image-12940 size-medium" src="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-11-02-46-169x300.png" alt="CameraV blocking screenshots in recent apps" width="169" height="300" srcset="https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-11-02-46-169x300.png 169w, https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-11-02-46-576x1024.png 576w, https://guardianproject.info/wp-content/uploads/2015/05/Screenshot_2015-05-06-11-02-46.png 720w" sizes="(max-width: 169px) 100vw, 169px" /></a>
  
  <p id="caption-attachment-12940" class="wp-caption-text">
    CameraV blocking screenshots in recent apps
  </p>
</div>

<br style="clear:both;" /> 

CameraV (you can get [beta access here](https://rink.hockeyapp.net/apps/dafbc649fcf585d7867866d5375b6495) and find the [source here](https://github.com/guardianproject/InformaApp)), incorporates all of these as options for the user to activate. You can switch the default icon and app name to a more generic settings icon and “CV Settings” app name. We plan to enhance that feature to allow the user to define the icon and name, making the app able to act like a chameleon and blend in more completely. The app can be set to now allow screenshots to be taken of it, which also causes a black screen to show up in the recent apps list, stopping a casual inspection from identifying it as a photos-type app. It can also be set to not show up in the recent apps list at all, which is a more complete solution to that problem. The last piece, again taken from the aforementioned PanicButton app, is to, when the stealth icon is activated, to change the default home screen of the app to something innocuous like a calculator, so that even when the app is opened, it does not reveal its true nature. It is even possible to completely hide the app in the launcher, until a system event like a phone call to a specific number or a certain wifi network is connected, to make the app reveal itself again.

You can learn how to dynamically switch your app’s icon on the [Chainfire blog](http://www.chainfire.eu/articles/133/_TUT_Supporting_multiple_icons_in_your_app/) and see the code in action on the [CameraV repo here](https://github.com/guardianproject/InformaApp/commit/98d8c545c1901d03d9d238204bb45d502a623e59#diff-7ab4bf3d594a968a90e0250af33fcb9bR399). To block screenshots of your app, you can set the [FLAG_SECURE feature in any Activity](https://github.com/guardianproject/InformaApp/commit/4c153ebd8d0a6e99660a9391e99c7dd6658a0efc#diff-f9e0f2937f7b2e3f755c53e7ec2e3909R64). To complete [stop your app from showing up in the recent app list](https://github.com/guardianproject/InformaApp/blob/master/app/AndroidManifest.xml#L87), just set [‘<span class="pl-e">android</span><span class="pl-e">:</span><span class="pl-e">excludeFromRecents</span>=](https://github.com/guardianproject/InformaApp/blob/master/app/AndroidManifest.xml#L87)<span class="pl-s"><a href="https://github.com/guardianproject/InformaApp/blob/master/app/AndroidManifest.xml#L87"><span class="pl-pds">“</span>true</a><span class="pl-pds"><a href="https://github.com/guardianproject/InformaApp/blob/master/app/AndroidManifest.xml#L87">“‘</a> in the Activity entry in the manifest. </span></span>

These are just some of the initial ideas and techniques we have gathered and implemented. We plan to provide this set of capabilities in all of the apps we offer, and hope to spread them as standard features that any app that contains sensitive data or is meant for use by people in high-risk situations, should offer. I would love to hear your thoughts on other techniques that could be used, see code snippets you might have to achieve those, or discuss how and when this whole concept may or may not be effective.

For now, stay safe out there, and that goes for your data and apps, too!

_[“Tanzania 0607 cropped Nevit”](https://commons.wikimedia.org/wiki/File:Tanzania_0607_cropped_Nevit.jpg#/media/File:Tanzania_0607_cropped_Nevit.jpg) by Nevit Dilmen (talk) – Own work. Licensed under CC BY-SA 3.0 via Wikimedia Commons_

 