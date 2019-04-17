---
id: 1538
title: Open Secure Telephony Network
date: 2012-02-22T15:39:26-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=1538
permalink: /2012/02/22/open-secure-telephony-network-ostn/
categories:
  - Development
tags:
  - ostn
  - voip
  - zrtp
---
Over the last two months, I have been working on a project to research and develop a set of tools to provide secure peer to peer Voice over IP on the Android mobile platform. It is called the Open Secure Telephony Network, or [OSTN](https://guardianproject.info/wiki/OSTN). This work is done under the umbrella of [The Guardian Project](http://guardianproject.info/).

[<img src="http://farm6.staticflickr.com/5119/5893549665_24943d362e.jpg" alt="Telephone wires" width="500" height="333" />  
](http://www.flickr.com/photos/stuartbarr/5893549665/ "Telephone wires by Stuart Barr, on Flickr") _this is not the type of “open” we mean, and definitely not secure_

The project will continue for another four months and I will post my public findings here. It’s well underway and I have developed a functional system in the SATELLITE lab in New York City. The goal by the the end of the project is to offer an alternative to Skype or Google Talk, which are both good voice services but don’t offer the kind of security needed by human rights activists and journalists.

Right now the stack looks like this

  * A client that understands the [SIP](http://en.wikipedia.org/wiki/Session_Initiation_Protocol) protocol and the [ZRTP](http://en.wikipedia.org/wiki/ZRTP) protocol
  * A server that can register SIP users and pass off the ZRTP traffic to peers

Sounds simple enough, though the development landscape for these applications changes quickly, as does the legal implications of various implementations of both protocols.

On top of that, there are networking issues that make building this kind of network a challenge.

[Stay tuned at https://guardianproject.info/wiki/OSTN](https://guardianproject.info/wiki/OSTN)!

Originally published at 2012-01-10 22:03:09 UTC [Permalink](http://lee.rockingtiger.com/posts/76)