---
id: 279
title: 'Beem+Orbot: Mobile Instant Messaging over Tor'
date: 2010-05-10T16:32:01-04:00
author: n8fr8
layout: post
guid: http://guardianproject.info/?p=279
permalink: /2010/05/10/mobile-im-over-tor/
bigimg: [{src: "http://guardianproject.info/wp-content/uploads/2010/05/friends-64x64.png",}]
categories:
  - App Reviews
tags:
  - im
  - jabber
  - torproject
  - xmpp
---
It is no secret that we are big fans of open-source here at Guardian. In fact, it is [what we are made of](http://github.com/guardianproject). Guardian is not just a single app or just one phone, it is a vision for a more private and secure future for personal mobile telecommunications. As part of our work, we are constantly on the lookout other similar, like-minded projects that are developing open-source communications tools for the Android OS which we can make to work with our underlying security platform.

[BEEM – Android XMPP](http://www.beem-project.com/) happens to be one of these. You can find BEEM in the Android Market or you can [download it here](http://www.beem-project.com/news/11). The goal of BEEM is to provide a full featured and easy to use Jabber client on Android. Jabber is another name for XMPP, the [Extensible Messaging and Presence Protocol](http://en.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol), which is another name for Instant Messaging and Status Updates. XMPP is the open-protocol that grew out of the AIM vs. Yahoo vs. MSN vs. ICQ protocol wars of a few years ago. It is now managed by a [standards foundation](http://xmpp.org/), and is supported by an amazing number of [client](http://xmpp.org/software/clients.shtml) and [server](http://xmpp.org/software/servers.shtml) apps.

Beem, available as source code and in the Android Market, is a great looking, highly functional IM application that supports a number of advanced options including SSL/TLS support and SOCKS Proxying. These two features make it ideal for use with running over the [Tor anonymity network](http://torproject.org) and [Orbot](/apps/orbot). By combining Beem with Orbot, mobile instant messaging can be more private (even anonymous if one chooses), usable without fear of eavesdropping by network operators, and made accessible in places where filtering technologies blocks access to popular instant messaging services.

**1) Connect to the Tor network using the Orbot app**

First, if you do not have Orbot installed, first [download it from the Tor Project](https://www.torproject.org/docs/android.html) or scan the barcode below:

<img class="alignnone" src="https://www.torproject.org/img/android/orbot-qr-code-latest.png" alt="" width="123" height="123" /> 

The Orbot app contains an HTTP and SOCKS proxy server which allows any Android app to proxy its network traffic through Tor. By installing and activating Orbot (tap on the big power button!), this proxy server is activated and runs in the background as long as you are connected to the Tor network.

[<img class="alignnone size-medium wp-image-295" title="torboot" src="http://guardianproject.info/wp-content/uploads/2010/05/torboot-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/torboot-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/torboot.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/torboot.png) [<img class="alignnone size-medium wp-image-294" title="toron" src="http://guardianproject.info/wp-content/uploads/2010/05/toron-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/toron-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/toron.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/toron.png)

**2) Configure your XMPP-compatible account using Beem settings**

If you don’t have BEEM installed, you can [download it here](http://www.beem-project.com/news/11) or scan the barcode below:

<img class="alignnone" src="http://dev.beem-project.com/screenshot_rc1/qr-code.png" alt="" width="100" height="100" /> 

You can use any XMPP service, but we recommend one that supports TLS or SSL security. You can use your Gmail / Google Talk account or you can find a list of public services here: http://xmpp.org/services/</p> 

</a>

[<img class="alignnone size-medium wp-image-293" title="beemsettings" src="http://guardianproject.info/wp-content/uploads/2010/05/beemsettings-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/beemsettings-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/beemsettings.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/beemsettings.png) [<img class="alignnone size-medium wp-image-292" title="beemusername" src="http://guardianproject.info/wp-content/uploads/2010/05/beemusername-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/beemusername-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/beemusername.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/beemusername.png)

**3) Check the SSL/TLS option in the Advanced Menu**

You must enable this option to protect your password and chat communications when they exit the Tor network. You can learn more about [exit node eavesdropping on the TorFAQ](https://trac.torproject.org/projects/tor/wiki/TheOnionRouter/TorFAQ#CanexitnodeseavesdroponcommunicationsIsntthatbad).

**[<img class="alignnone size-medium wp-image-291" title="advsetings" src="http://guardianproject.info/wp-content/uploads/2010/05/advsetings-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/advsetings-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/advsetings.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/advsetings.png) [<img title="tls" src="http://guardianproject.info/wp-content/uploads/2010/05/tls-180x300.png" alt="" width="180" height="300" />](http://guardianproject.info/wp-content/uploads/2010/05/tls.png)**

**4) Enable the SOCKS Proxy Setting in the Proxy Menu**

The “Use a proxy server” should be checked, the Protocol set to “SOCKS5”. The Server is “localhost” and the Port is “9050”. You must use the SOCKS5 protocol, as it ensures that domain name resolution is also routed through Tor, stopping from someone snooping on which chat service you are using.

**[<img class="alignnone size-medium wp-image-289" title="proxyon" src="http://guardianproject.info/wp-content/uploads/2010/05/proxyon-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/proxyon-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/proxyon.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/proxyon.png)[<img class="alignnone size-medium wp-image-288" title="socks5" src="http://guardianproject.info/wp-content/uploads/2010/05/socks5-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/socks5-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/socks5.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/socks5.png)**

**[](http://guardianproject.info/wp-content/uploads/2010/05/socks5.png)[<img class="alignnone size-medium wp-image-287" title="localhost" src="http://guardianproject.info/wp-content/uploads/2010/05/localhost-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/localhost-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/localhost.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/localhost.png)[<img class="alignnone size-medium wp-image-286" title="port" src="http://guardianproject.info/wp-content/uploads/2010/05/port-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/port-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/port.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/port.png)**

**5) Connect to the XMPP Service**

If Orbot is connected, and you have configured the proxy settings correctly, you should be able to connect and see your contacts or buddy list. From here, you can use Beem as you normally would ([download user documentation here](http://www.beem-project.com/documents/4)).

**IMPORTANT:** _To ensure Beem is routing through Tor, you should deactivate Orbot, and then try connecting to your XMPP service with Beem again. This SHOULD fail, else you haven’t setup the proxying correctly._

**[<img class="alignnone size-medium wp-image-285" title="coonnecting" src="http://guardianproject.info/wp-content/uploads/2010/05/coonnecting-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/coonnecting-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/coonnecting.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/coonnecting.png)[<img class="alignnone size-medium wp-image-284" title="friends" src="http://guardianproject.info/wp-content/uploads/2010/05/friends-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/05/friends-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/05/friends.png 480w" sizes="(max-width: 180px) 100vw, 180px" />](http://guardianproject.info/wp-content/uploads/2010/05/friends.png)**

**6) Chat away!** 

**<span style="font-weight: normal;">At this point, you should be happily chatting away with your buddies. It is important to note that this solution </span>DOES NOT provide end-to-end encryption<span style="font-weight: normal;">, so once your chat reaches the server, it is not secure, both because the service provide can view it if they choose, and the other members of your chat may not be secured themselves.</span>**

We do plan to implement and end-to-end extension to Beem using the [Pidgin+Off The Record](http://www.cypherpunks.ca/otr/) approach that has provided effective on desktop systems. If anyone wishes to contribute development cycles to this effort, please let us know!

If you find issues with Beem, please report them: <http://www.beem-project.com/projects/beem/issues/new>

If you find issues with Orbot, please report them: <https://trac.torproject.org/projects/tor/newticket>