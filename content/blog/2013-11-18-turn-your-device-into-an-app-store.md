---
id: 11953
title: Turn Your Device Into an App Store
date: 2013-11-18T16:27:30-04:00
author: cpu
layout: post
guid: https://guardianproject.info/?p=11953
permalink: /2013/11/18/turn-your-device-into-an-app-store/
categories:
  - Development
  - New Release
  - News
  - Research
tags:
  - android
  - bazaar
  - distribution
  - F-Droid
  - fdroid
  - open-source
  - privacy
---
As we’ve touched upon in [previous blog posts ](https://guardianproject.info/2013/11/05/setting-up-your-own-app-store-with-f-droid/) the Google Play model of application distribution has some disadvantages. Google does not make the Play store universally available, instead limiting availability to a subset of countries. Using the Play store to install apps necessitates both sharing personal information with Google and enabling Google to remotely remove apps from your device (colloquially referred to as [having a ‘kill switch’](http://www.engadget.com/2008/10/16/google-implemented-an-android-kill-switch-those-rascals/)). Using the Play store also requires a functional data connection (wifi or otherwise) to allow apps to be downloaded. Often there is a need to quickly bootstrap users during training sessions in countries with unreliable/restricted data connectivity, or in extreme cases, [no internet connectivity at all](http://www.nytimes.com/2011/01/29/technology/internet/29cutoff.html?_r=0).

[F-Droid](https://f-droid.org/) addresses many of these concerns, but still requires a functional data connection in order to access the repository housing applications available for install. Wouldn’t it be great if there was an easy way for users to share applications amongst themselves, in absence of a reliable data connection? Today we would like to announce initial steps the Guardian Project is taking to enable this exact functionality. We’ve been working on a prototype application capable of building F-Droid repositories **on-device**, allowing users to share apps they already have installed to other users through F-Droid. In this way savvy users can quickly and securely share applications they already know and trust with friends and family without requiring a central market/repository or a reliable internet connection.

To start, we’ve built a stand-alone prototype application we call “_**Kerplapp**_” (as in _Kerplop for Apps)_. Using Kerplapp an established user can select applications already installed on their phone that they wish to make available to other users. Using the selected applications Kerplapp builds a [simple binary F-Droid repostiory](https://f-droid.org/manual/fdroid.html#Simple-Binary-Repository) on the user’s device. The local on-device repository is then made available over a WiFi connection to other users on the local area network. Kerplapp will even display a QR code with the information required to add the local Kerplapp repo as a source repository for an F-Droid client running on another device. We hope to eventually merge our work back into the official F-droid Android client, but while we work out the kinks the Kerplapp application operates side-by-side with the F-Droid client app.

<div id="attachment_11966" style="width: 190px" class="wp-caption alignright">
  <a href="https://guardianproject.info/wp-content/uploads/2013/11/Screenshot_2013-11-18-16-02-48.png"><img aria-describedby="caption-attachment-11966" class="size-medium wp-image-11966" alt="Sharing access to a Kerplapp repo with a QR code." src="https://guardianproject.info/wp-content/uploads/2013/11/Screenshot_2013-11-18-16-02-48-180x300.png" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2013/11/Screenshot_2013-11-18-16-02-48-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2013/11/Screenshot_2013-11-18-16-02-48-614x1024.png 614w, https://guardianproject.info/wp-content/uploads/2013/11/Screenshot_2013-11-18-16-02-48.png 768w" sizes="(max-width: 180px) 100vw, 180px" /></a>
  
  <p id="caption-attachment-11966" class="wp-caption-text">
    Sharing access to a Kerplapp repo with a QR code.
  </p>
</div>

Building on top of F-Droid has a number of advantages. First, we can directly benefit from the tremendous effort and success of the F-Droid project! We’ve been actively contributing improvements [back to both the F-droid client](https://gitorious.org/f-droid/fdroidclient/merge_requests/39) and [the F-droid server](https://gitorious.org/f-droid/fdroidserver/merge_requests/127), making it easier for everyone to set up new F-Droid repos and share connection details. Secondly, by using a binary F-Droid repository we can ensure that when users share apps between each other that the apps will continue to receive updates through other channels. That is, if I share an app with you through Kerplapp you will be able to install updates to the app from other F-Droid binary repos and other Kerplapp users – wherever the app and its updates are available with the same APK signature. The F-Droid client will do the hard work of determining what updates are available and compatible with your device

There’s a lot of work left to be done! One of our short term goals include enabling Bonjour support so that the F-Droid client can find repositories on the local network without requiring them to be added manually. We’re interested in supporting device to device app transfer over a number of channels, starting with HTTPS and eventually adding support for bluetooth and NFC. Building on the success of ChatSecure we’re actively working on supporting F-Droid app transfer over [OTR-Data](https://dev.guardianproject.info/projects/gibberbot/wiki/OTRDATA_Specifications), the ChatSecure proposal for in-band OTR encrypted file transfers. With F-Droid as an OTR-DATA endpoint we can support peer to peer app transfer over a trusted, authenticated, and encrypted channel. We’re also exploring how we can use the OTR keys your contacts already trust to [sign the F-Droid repository metadata index](https://f-droid.org/manual/fdroid.html#Signing), providing greater trust in the accuracy of the metadata provided by peer to peer repositories.

If you’re curious you can [follow Kerplapp’s development on our project tracker.](https://dev.guardianproject.info/projects/bazaar) We’re also looking for adventurous users [to install the Kerplapp prototype application](https://guardianproject.info/builds/Kerplapp/) to provide feedback and testing.