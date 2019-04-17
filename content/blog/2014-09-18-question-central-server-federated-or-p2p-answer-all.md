---
id: 12628
title: 'Question: central server, federated, or p2p? Answer: all!'
date: 2014-09-18T00:30:57-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12628
permalink: /2014/09/18/question-central-server-federated-or-p2p-answer-all/
categories:
  - News
tags:
  - bazaar
  - bluetooth
  - fdroid
  - nfc
  - p2p
  - wifi
---
There are many ideas of core architectures for providing digital services, each with their own advantages and disadvantages. I break it down along the lines of central servers, federated servers, and peer-to-peer, serverless systems. 

<div id="attachment_12631" style="width: 210px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2014/09/200px-Server-based-network.svg_.png"><img aria-describedby="caption-attachment-12631" src="https://guardianproject.info/wp-content/uploads/2014/09/200px-Server-based-network.svg_.png" alt="a central service with clients connecting to it" width="200" height="207" class="size-full wp-image-12631" srcset="https://guardianproject.info/wp-content/uploads/2014/09/200px-Server-based-network.svg_.png 200w, https://guardianproject.info/wp-content/uploads/2014/09/200px-Server-based-network.svg_-100x103.png 100w, https://guardianproject.info/wp-content/uploads/2014/09/200px-Server-based-network.svg_-150x155.png 150w" sizes="(max-width: 200px) 100vw, 200px" /></a>
  
  <p id="caption-attachment-12631" class="wp-caption-text">
    a central service with clients connecting to it
  </p>
</div>

Most big internet companies operate in effect as a central server (even though they are implemented differently). There is only facebook.com, there are no other services that can inter-operate with facebook.com. Have a single, central repo makes problems of finding the service and finding people within the service a lot easier. Once you are in Facebook, you just need to know the name of the person you want to contact and you are connected. The Facebook apps just need to talk to facebook.com, so the user does not need to know which service they are using in order to configure the app.

<div id="attachment_12633" style="width: 310px" class="wp-caption aligncenter">
  <a href="http://www.bendevane.com/RDC2012/ians/2012/10/09/campsiteofthefutur/"><img aria-describedby="caption-attachment-12633" src="https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-300x170.png" alt="email as federated service" width="300" height="170" class="size-medium wp-image-12633" srcset="https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-300x170.png 300w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-100x56.png 100w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-150x85.png 150w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-200x113.png 200w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-450x255.png 450w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-600x341.png 600w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582-900x511.png 900w, https://guardianproject.info/wp-content/uploads/2014/09/Federated-01-1024x582.png 1024w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-12633" class="wp-caption-text">
    email as federated service
  </p>
</div>

Email is a great example of a federated system. Each email provider acts like a central server, but then each of those central servers can easily talk to each other and exchange data. So fastmail.fm and gmail.com are both centralized services, but users do not need to know any extra information in order to exchange emails between the two services, or any other of the millions of email servers out there. A federated system provides a lot of the benefits of a centralized server with more flexibility. The downside is that federated services generally require more configuration to use them (though webmail makes that much less of an issue).

<div id="attachment_12632" style="width: 310px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2014/09/300px-Unstructured_peer-to-peer_network_diagram.png"><img aria-describedby="caption-attachment-12632" src="https://guardianproject.info/wp-content/uploads/2014/09/300px-Unstructured_peer-to-peer_network_diagram.png" alt="a peer-to-peer network" width="300" height="245" class="size-full wp-image-12632" srcset="https://guardianproject.info/wp-content/uploads/2014/09/300px-Unstructured_peer-to-peer_network_diagram.png 300w, https://guardianproject.info/wp-content/uploads/2014/09/300px-Unstructured_peer-to-peer_network_diagram-100x81.png 100w, https://guardianproject.info/wp-content/uploads/2014/09/300px-Unstructured_peer-to-peer_network_diagram-150x122.png 150w, https://guardianproject.info/wp-content/uploads/2014/09/300px-Unstructured_peer-to-peer_network_diagram-200x163.png 200w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-12632" class="wp-caption-text">
    a peer-to-peer network
  </p>
</div>

Peer-to-peer systems can provide unique benefits of bandwidth efficiency as well as working around blockages in the internet. Sharing large files with thousands of people is quite expensive when using a central server, but with bittorrent, anyone can share large files to many many people using only a basic broadband connection. 

Over the past year and a half of our Bazaar project, we have been thinking a lot about how to distribute apps to people who face a number of challenges. Each of these systems offers distinct advantages and disadvantages, so it is quite difficult to choose only one. Instead, we thought why not try to make a system that combines all three? Android&#8217;s APK app package format is a good format to work in this model because they are self-contained and containing a form of embedded identity in the app signature. So if you already have an Android app installed, then Android will enforce that only APKs signed by the same key as the installed app can be installed over it.

That means in theory, it does not matter where the APK came from as long as it has a valid signature. There are some details where it does matter, mostly related to exploits like &#8220;Master Key&#8221; that can inject code into an existing APK. The FDroid app repository signature has a similar property: once you trust the repository signing key, it does not matter how you got the repository files as long as the signature validates. This is a model proven by GNU/Linux distros like Debian. The repository metadata also provides a way to validate APKs have not been modified since they were added to the signed repository. Since both of these do not rely on the method of transport to prove their authenticity, this combination provides a great testbed for this idea of combining a central service, with decentralized servers and peer-to-peer distribution.

This work was all incorporated in the <a href="https://f-droid.org" target="_blank">FDroid</a> app store for Android. The central f-droid.org app repository means that FDroid can deliver well over one thousand apps without any configuration on the part of the user. The &#8220;fdroidserver&#8221; developer tools means that anyone can set up their own repository of apps, and users can easily add that repository to FDroid. It is not quite zero configuration, but the process is not too difficult, and there is more we are planning to do to smooth out that process even more. This also provides a channel for users to get apps via &#8220;collateral freedom&#8221; techniques like using Amazon S3, Akamai, etc. to distribute files where many such services are filtered or blocked. Lastly, we made it possible to have the FDroid app itself act as an app repository, and other devices can connect to that repository using local WiFi, mesh, Bluetooth, and removable media.

This stuff is all implemented and included in the FDroid app and fdroidserver developer tools. The big remaining challenge is combining them all into a usable experience for people who do not know the technical details. This has been tested, discussed, sketched out, and there is a prototype implementation in the works. So I can end with a quick overview of some positive and negative observations about the various peer-to-peer connections that we experimented with:

<ul style="list-style-type: none;">
  <li>
    <strong>+</strong> Bluetooth is ubiquitous
  </li>
  <li>
    <strong>&ndash;</strong> very slow data rate
  </li>
  <li>
    <strong>&ndash;</strong> pairing is difficult
  </li>
</ul>

<ul style="list-style-type: none;">
  <li>
    <strong>+</strong> WiFi is very widespread
  </li>
  <li>
    <strong>+</strong> local connections are very fast
  </li>
  <li>
    <strong>&ndash;</strong> access points and proxies can block host-to-host connections
  </li>
  <li>
    <strong>&ndash;</strong> running access points on a device is not common nor easy
  </li>
</ul>

<ul style="list-style-type: none;">
  <li>
    <strong>+</strong> NFC makes Bluetooth very easy to use
  </li>
  <li>
    <strong>&ndash;</strong> NFC is not commonly used or available
  </li>
  <li>
    <strong>&ndash;</strong> NFC is far to slow and fiddly to be used as the data transmission medium
  </li>
</ul>

<ul style="list-style-type: none;">
  <li>
    <strong>+</strong> SD cards can move lots of data securely
  </li>
  <li>
    <strong>&ndash;</strong> not all devices have removable SD cards
  </li>
  <li>
    <strong>&ndash;</strong> swapping SD cards can be a fiddly process
  </li>
  <li>
    <strong>&ndash;</strong> swapping SD cards can not be automatic
  </li>
</ul>

<ul style="list-style-type: none;">
  <li>
    <strong>+</strong> USB thumb drives can move lots of data securely
  </li>
  <li>
    <strong>+</strong> they can be easily swapped between devices
  </li>
  <li>
    <strong>&ndash;</strong> swapping SD cards can not be automatic
  </li>
  <li>
    <strong>&ndash;</strong> not all devices support USB-OTG i.e. attached devices
  </li>
  <li>
    <strong>&ndash;</strong> USB-OTG is not widely used
  </li>
</ul>