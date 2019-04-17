---
id: 3372
title: Gibberbot v11 is not just secure, its also simple, snappy and super fun!
date: 2013-03-08T12:54:50-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=3372
permalink: /2013/03/08/gibberbot-v11-secure-usable/
categories:
  - New Release
  - News
  - Research
tags:
  - messaging
  - otr
  - usability
  - xmpp
---
_Gibberbot v11 is now final as of RC3 release: <https://github.com/guardianproject/Gibberbot/tree/0.0.11-RC3>. From here, the only changes to v11 we will be making will be critical bug fixes. We are now focused on our v12 release, which you can track here: <https://dev.guardianproject.info/versions/39>_

_**Please promote our new Gibberbot how-to interactive tutorial available here: <a href="https://guardianproject.info/howto/chatsecurely/" target="_blank">https://guardianproject.info/howto/chatsecurely/</a>**_

If you have been tracking our efforts here for the last few years, you will know that Gibberbot, our secure instant messaging app, started out as a big old mess of an app called “ORChat” as and then “OTRChat” and then “Gibber” (or “Jibber”?), and then finally settled down into the name and app it is known as now. Really it was a proof of concept, showing that you could indeed use the [OTR4J library](https://github.com/gpolitis/otr4j) built for desktops app, on Android.

Gibberbot was the first Android app, and perhaps real mobile app, that supported end-to-end encrypted chat using open standards like OTR and XMPP. In the early days, we were just so excited this was possible, and that we could also send the chat connections over Tor, that we didn’t think too much about how easy or fun it was to use the app itself. We were focused on our magic tricks, and not how it was to live and use the app on a daily basis.

A few months ago, we realized that on Google Play, we had a lot of reviews that basically said “This is a great idea, but it doesn’t work for me”, or “I like these guys, but the app is kinda buggy”, and even “This app gives my device crazy flash seizures”. All of these reviews were true, and we swallowed the hard medicine, that if we didn’t spend more time focusing on how the core features of being a mobile instant messaging chat client worked, that nobody would care about how secure the app was, because there would be no one using it.

We set about then not only continuing our focus on improving the core security and technical core of Gibberbot, but also focusing on a user interface update. We completed “stage 1” of that update, with another major round of effort planned for v12.

Here a few new features and improvements along those lines, that were completed for v11:

  * <span style="line-height: 13px;"><span style="line-height: 13px;"><strong>Simplify setup of Google Gmail and Google Domain accounts…. DONE!</strong> We now support the built-in authentication system on your Android phone, so if you phone is already setup with a Google account, we can tap right into that. No extra password entry needed, no need to enter anthing really. Just choose “Google Account” from the account type list.</span></span> 
  * **Streamline Orbot integration to make Tor user easier… DONE! **Using the new [OnionKit library](/code/onionkit), Gibberbot can now tell if Orbot is installed and running, and if not, prompt the user to either install it, or ask if they want to start up and connect to the Tor network.
  * **Make it easy for services using SSL certs not signed by the Root CA cartel to be easily verified and accepted by the user… DONE!** Increasingly, it has become less and less valuable to have the TLS or SSL certificate you use with your website or XMPP server to be signed by a Root Certificate Authority, because as many point out, the SSL is broken, as long as trust this strange collection of hundreds of organizations we have no reason to really trust. Previously, Gibberbot would not handle non-Root CA certs very well, so you would just have to turn off verification. Now thanks to the concept of TOFU-POP (Trust on First Use, Persistence of Psuedonym) and the excellent [MemorizingTrustManager](https://github.com/ge0rg/MemorizingTrustManager/wiki) library, user’s can now decided in an on-demand and interactive manner, whether or not they want to trust the TLS connection they are using. 
  * **Ensure Gibberbot only runs and signs in when the user wants it to… DONE! **Previously, Gibberbot was a bit too aggresive about trying to stay connecting to your account, and starting up on device boot. Many users want to conserve battery, and some do not like apps that run without them asking them to first (imagine that?!). We have put Gibberbot now at the user’s beck and call, such that there are preferences to control starting on boot, and when you SIGN OUT, it really means do not every login again, until I login.
  * **Improve the user interface to make app that is clean, fast, modern and customizable… DONE! **Not only have we continued to focus on a clean, simple user interface that uses the latest interface conventions and guidelines from Google, we also wanted to start adding some fun user personalization options. One size does not fit all, and just because our app is secure, does not mean it has to be boring. As you can see below, Gibberbot now supports light and dark themes, as well as user configured app wallpaper.

I am happy to say, that will all of these improvements, we are much happier users, and are receiving much better reviews on Google Play, such as:

_“Easy to set up and pretty stable and easy to use.” “Fixed on jelly bean and does exactly what it should do” and the best… “Perfect (but no ICQ Support*)” _

<em id="__mceDel">*We may add ICQ support, just so we can be extra perfect for that one user who wants it! 🙂</em>

All in all, we hope you agree, and that our new found focus on usability can push us from 100,000+ downloads to over 500,000+ in the coming months. We have big ideas for the future of secure mobile messaging, and making Gibberbot the best it can be is a huge part of that plan.

As always you can find the Gibberbot download (and [all of our apps](/apps)) in a variety of places:

  * <span style="line-height: 13px;">Through our direct APK download: <a href="https://guardianproject.info/releases/gibberbot-latest.apk">https://guardianproject.info/releases/gibberbot-latest.apk</a> (and <a href="https://guardianproject.info/releases/gibberbot-latest.apk.asc">gpg sig</a>)</span>
  * on [Google Play](https://play.google.com/store/apps/details?id=info.guardianproject.otr.app.im)
  * or through our [F-Droid Repo](https://guardianproject.info/2012/03/15/our-new-f-droid-app-repository/), which you can [learn how to use here](https://guardianproject.info/2012/03/15/our-new-f-droid-app-repository/).

You can also scan this QR code, which links to the direct APK download above:

[<img class="alignnone size-full wp-image-3373" alt="gibberbotqr" src="https://guardianproject.info/wp-content/uploads/2013/03/gibberbotqr.png" width="123" height="123" />](https://guardianproject.info/wp-content/uploads/2013/03/gibberbotqr.png)

 

<img class="alignnone" alt="" src="https://lh4.ggpht.com/TAtK2o9v79g1dVsAuii2XWQcdN1JdZgnRPAT0inGrQjDKkPLO_zLWLHlGdm6xxki6w" width="288" height="512" />  [<img alt="device-2013-02-20-021839" src="https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-021839.jpg" width="288" height="512" />](https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-021839.jpg)

<img class="alignnone" alt="" src="https://lh4.ggpht.com/ShD1S-pNv-1nUdK4e4C4d-GBNz4A1Vr7bS6_-uYMm2zjOZ2T88HL_Iogsn71ePBVmTWk" width="288" height="512" />   <img class="alignnone" alt="" src="https://lh4.ggpht.com/cLhiajC5VIk8SZ4iDq08PKAmhiZQMze62avh0h2JNArZFRHKR4LJgWdS0tfALe1uFeHg" width="288" height="512" />

[<img class="alignnone  wp-image-3375" alt="device-2013-02-20-025148" src="https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-025148.png" width="538" height="302" srcset="https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-025148.png 1280w, https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-025148-300x168.png 300w, https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-025148-1024x576.png 1024w" sizes="(max-width: 538px) 100vw, 538px" />](https://guardianproject.info/wp-content/uploads/2013/03/device-2013-02-20-025148.png)