---
id: 1551
title: Free SIP Providers with ZRTP support
date: 2012-02-22T19:10:11-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=1551
permalink: /2012/02/22/free-sip-providers-with-zrtp-support/
force_ssl:
  - "1"
categories:
  - Development
tags:
  - ostn
  - secure
  - voip
  - zrtp
---
This post is part of a series on our work researching the [Open Secure Telephony Network](https://guardianproject.info/tag/ostn/). After you have [CSipSimple installed](http://code.google.com/p/csipsimple/) on your mobile handset, you will need a place to register a SIP username so you can contact others. The fastest way to get started with this is to use one of a handful of free SIP providers. I like the [Ekiga free SIP service](https://www.ekiga.net/index.php?page=register).

[<img src="http://farm1.staticflickr.com/26/45070135_a1dd5889a7.jpg" alt="Red Telephone Boxes" width="500" height="375" />](http://www.flickr.com/photos/andwar/45070135/ "Red Telephone Boxes by Andwar, on Flickr")

The only drawback to this service is the userbase is large enough that the namespace of easy to remember words is frequently occupied. Chances are you will not be able to register your name and must make some novel admendments to ensure a unique name. Since telephony is closely associated with numbers, not words, it will be easier to find a 10 digit number combination to use as your username. This makes username input simpler since CSipSimple gives you the familliar telephone dial pad as the default interface.

After you create a user with Ekiga, you must input the username and password into CSipSimple to register with the service. There is a preset configuration screen for the Ekiga service in the Account Add interface. Fill in the forms and your handset will be registered if you have an active data connection.

Calling another user with CSipSimple will initiate the ZRTP handshake if both people have enabled it. Subsequent calls do not require this verfication, since it checks a Short Authentication String (SAS) for each peer.

Another SIP provider that is similar to Ekiga is [IPtel](http://www.iptel.org/service). It supports the same features, including ZRTP.

At this point, now you should have everything you need to start an anonymous conversation on a mobile handset. The one drawback of this configuration is you may not fully trust the third-party SIP registrar, namely Ekiga. The solution to this is to run your own registrar, which is the [next installment](http://lee.rockingtiger.com/posts/79).

ZRTP me ASAP!