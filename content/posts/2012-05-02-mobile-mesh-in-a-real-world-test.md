---
id: 2036
title: Mobile mesh in a real world test
date: 2012-05-02T15:37:37-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=2036
permalink: /2012/05/02/mobile-mesh-in-a-real-world-test/
categories:
  - Development
tags:
  - android
  - commotion
  - mesh
  - olsr
  - prototype
  - usability
  - voip
  - wifi
---
Nathan, Mark, Lee, and I tried some OLSR mesh testing during the May Day protests and marches. We were able to get 4 devices to associate and mesh together, but not without some trials and travails. Two pairs of devices setup two separate BSSIDs, so were on separate networks. We turned them all off, then associated them one at a time, and then they all got onto the same BSSID and olsrd started doing its thing. This made us think that we should just use a hard-coded BSSID in the setup, with a preference to allow standard ad-hoc association to find a BSSID. [<img src="https://guardianproject.info/wp-content/uploads/2012/05/526191_338865336181237_184749301592842_866151_1316470506_n-300x225.jpg" alt="" width="300" height="225" class="alignright size-medium wp-image-2037" srcset="https://guardianproject.info/wp-content/uploads/2012/05/526191_338865336181237_184749301592842_866151_1316470506_n-300x225.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/05/526191_338865336181237_184749301592842_866151_1316470506_n.jpg 600w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2012/05/526191_338865336181237_184749301592842_866151_1316470506_n.jpg)

Next we tried to use some services. We were going to try running a <a href="https://crypto.cat/" target="_blank">cryptocat</a> session, but the phone that was running cryptocat via a <a href="https://github.com/guardianproject/lildebi" target="_blank">Lil&#8217; Debi</a> Debian install was having trouble staying connected to the mesh. Next we tried a serverless direct SIP call using <a href="http://code.google.com/p/csipsimple/" target="_blank">CSIPSimple</a>. 

CSIPSimple uses the Android Java API to determine if the device is online. The current approach to configuring the ad-hoc mode used by Android-Wifi-Tether-based apps including Serval and Barnacle-based apps including OLSR-Mesh-Tether disables the wifi via the Android Java API, then configures ad-hoc mode using command line tools. This means that Android believe that the wifi is off, and when apps query the network status via the normal Android API, Android will tell it what it believes: there is no network connection.

This works in <a href="http://www.servalproject.org/" target="_blank">Serval</a> because Serval is a self-contained system with its own SIP client and server, etc. This does not work for situations where we want to provide generic IP service using OLSR mesh on Android phones. I&#8217;m going to try to see if I can get the ad-hoc setup to work while making Android believe that the wifi is an and associated with infrastructure-mode network.

Also, in the process of setting up the mesh while mixing in a crowd and walking with a crowd down the street we realized two key things: 1) the setup process should be tolerant of frequent interruptions, and 2) it should be as easy as possible for people to give the mesh app itself from one phone to another. We&#8217;ll be working on #1 as part of our <a href="https://code.commotionwireless.net/projects" target="_blank">Commotion</a> work and we will focus on making a UI that clearly shows its status and lets the user continue where they left off. We will be working directly on #2 as part of a separate project, so we&#8217;ll try to keep everyone informed on our progress with that.

Another idea we discussed was how to have a &#8220;strength meter&#8221; for mesh, like the GSM or wifi bars. We talked about taking a tally of how many first hop connections there are, the total connections, and the total willingness of all of the first hop connections.