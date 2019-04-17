---
id: 13619
title: 'Announcing new libraries: F-Droid Update Channels'
date: 2017-05-31T11:40:27-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13619
permalink: /2017/05/31/announcing-new-libraries-f-droid-update-channels/
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "539"
discourse_permalink:
  - https://talk.developersquare.net/t/announcing-new-libraries-f-droid-update-channels/390
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":390,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553025155"
wpdc_sync_post_comments:
  - "0"
categories:
  - News
tags:
  - android
  - bazaar
  - fdroid
  - open-source
  - security
---
[<img src="https://guardianproject.info/wp-content/uploads/2017/05/refresh-525698_640-150x150.png" alt="" width="150" height="150" class="alignleft size-thumbnail wp-image-13626" srcset="https://guardianproject.info/wp-content/uploads/2017/05/refresh-525698_640-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2017/05/refresh-525698_640-300x297.png 300w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2017/05/refresh-525698_640.png)  
In many places in the world, it is very common to find Android apps via a multitude of sources: third party app stores, Bluetooth transfers, swapping SD cards, or directly downloaded from websites. As developers, we want to make sure that our users get secure and timely update no matter how they got our apps. We still recommend that people get apps from trusted sources like F-Droid or Google Play.

Building upon the F-Droid distribution ecosystem, there is a new suite of libraries: “<a href="https://gitlab.com/fdroid/update-channels/" target="_blank">F-Droid Update Channels</a>“. It is a suite of libraries for making sure your that your app can always find updates, no matter where someone got it from. Currently, there are two specific libraries: “Get F-Droid” and “App Updater”.

#### “Get F-Droid” aka `org.fdroid.getfdroid`

Checks whether F-Droid is installed. If not, it will help the user to download and install F-Droid. F-Droid then provides the update channel. This is the preferred method of getting updates since F-Droid provides strong privacy protection and lets the user control when and where updates happen. Also, if F-Droid came pre-installed on the device or was “flashed” onto it as part of a custom Android ROM, then F-Droid does not need “Unknown Sources” enabled.

#### “App Updater” aka `org.fdroid.appupdater`

Keeps the app current by checking the hard-coded app repository set up by the developer. This is similar to the popular “App Updater” library, but is secure due to the F-Droid signed metadata. The _<a href="https://gitlab.com/fdroid/fdroidserver" target="_blank">fdroidserver</a>_ tools handle the creation and maintenance of the app repository.

Both of these libraries also check whether Google Play is installed, if so, will disable itself. This allows apps to include this library in APKs that are uploaded to Google Play since it will not violate the Google Play Terms of Service.