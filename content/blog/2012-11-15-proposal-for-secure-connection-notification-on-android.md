---
id: 2946
title: Proposal for Secure Connection Notification on Android
date: 2012-11-15T10:07:49-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=2946
permalink: /2012/11/15/proposal-for-secure-connection-notification-on-android/
bigimg: [{src: "/wp-content/uploads/2012/11/device-2012-11-08-203216.png",}]
categories:
  - Development
  - Research
tags:
  - android
  - https
  - man in the middle
  - mobile
  - ssl
  - strong cryptography
  - tls
---
A major problem of mobile applications being increasingly used over web-based applications, is that there is no standard established for notifying the user of the state of security on the network connection. With a web browser, the evolution of the “lock” icon when an [HTTPS connection](https://en.wikipedia.org/wiki/HTTP_Secure) is made, has been one that evolved originally out of Netscape’s first implementation, to an adhoc, defact industry-standard way of letting the user know if their connection is secure. Beyond just a binary on/off, the lock icon is also the entry point into viewing more information about the digital security tokens, keys and certificates that are powering the connection – who authorized them, who requested them, and so on. More recently, with browsers such as Chrome, there has been the user of color schemes (Green is good, Red is bad), verified domain display and other indicators to help ensure the user knows when to trust their connection, and when to be wary.

[<img class="alignnone size-medium wp-image-2952" title="Firefox_3_rc1_Extended_Validation_SSL_address_bar_and_certificate_detail" src="https://guardianproject.info/wp-content/uploads/2012/11/Firefox_3_rc1_Extended_Validation_SSL_address_bar_and_certificate_detail-300x182.png" alt="" width="300" height="182" srcset="https://guardianproject.info/wp-content/uploads/2012/11/Firefox_3_rc1_Extended_Validation_SSL_address_bar_and_certificate_detail-300x182.png 300w, https://guardianproject.info/wp-content/uploads/2012/11/Firefox_3_rc1_Extended_Validation_SSL_address_bar_and_certificate_detail.png 429w" sizes="(max-width: 300px) 100vw, 300px" />  
](https://guardianproject.info/wp-content/uploads/2012/11/Firefox_3_rc1_Extended_Validation_SSL_address_bar_and_certificate_detail.png) _Firefox’s HTTPS certificate display_

While many people claim that HTTPS/TLS/SSL are fundamentally broken, they are still an essential piece of basic frontline security on the web. In addition, when making a connection through a proxy network like Tor or a free VPN service, utilizing TLS/SSL is critical in making sure you network is not being intercepted along the way. The notification icon and related certificate viewing, is a critical component for the user, and one that is entirely missing in the mobile application space. The Android API does not provide a standardized method to share this information with the user, and the implementation on iOS is unclear, as well. Even worse, the proper implementation of a strong HTTP/S connection that properly handles verification of certificates, and provides an interactive option for users to accept or decline is entirely missing for the majority of mobile apps.

With that in mind, we have added a Secure Connection Notification feature into our new [OnionKit for Android](https://github.com/guardianproject/OnionKit) library. Build upon our previous work on [implementing custom Root CA Certificate stores for Android](https://github.com/guardianproject/cacert), this library not only provides a clear way to enable HTTP and SOCKS proxying for your network requests (to enable use with our app, [Orbot: Tor for Android](https://guardianproject.info/apps/orbot/)), but it also includes a [StrongTrustManager](https://github.com/guardianproject/OnionKit/blob/master/library/src/info/guardianproject/onionkit/trust/StrongTrustManager.java) and a [StrongHTTPSClient](https://github.com/guardianproject/OnionKit/blob/master/library/src/info/guardianproject/onionkit/trust/StrongHttpsClient.java) implementation, that works to defend against man-in-the-middle attacks, and other means to intercept a TLS or SSL connection between a mobile app and a remote server. Part of the defense, is providing a clear indicator to the user when a secure connection is in use.

We have provided a [sample Android app](https://github.com/guardianproject/OnionKit/blob/master/sample/src/sample/onionkit/OnionKitSampleActivity.java) to demonstrate how simple it is to enable this capability. The screenshots below are from that app.

In this first screenshot, the app has connected to https://check.torproject.org and you can see in the Notification bar a “key” icon indicating there is a secure connection active.

[<img class="size-medium wp-image-2947 alignnone" title="noTor" src="https://guardianproject.info/wp-content/uploads/2012/11/noTor-254x300.png" alt="" width="254" height="300" srcset="https://guardianproject.info/wp-content/uploads/2012/11/noTor-254x300.png 254w, https://guardianproject.info/wp-content/uploads/2012/11/noTor.png 800w" sizes="(max-width: 254px) 100vw, 254px" />](https://guardianproject.info/wp-content/uploads/2012/11/noTor.png)

When you drag the notification bar down, you can see a more complete view of the Secure Connection Notification (SCN) message, which indicates the connection is Active and shows a summary of the secure certificate information. In a recent update to the OnionKit SCN code, it also allows for the application to include its name and icon in this notification.

[<img class="alignnone size-medium wp-image-2948" title="device-2012-11-08-204130" src="https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-204130-300x139.png" alt="" width="300" height="139" srcset="https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-204130-300x139.png 300w, https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-204130.png 800w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-204130.png)

Finally, you can tap on the SCN notification and bring up a larger pop-over view of the certificate information. We intend to develop this view further, to allow for better manual management of trust – meaning you may have the option to accept/decline or disable trust of this certificate or the certificate authority that provides it.

[<img class="alignnone size-medium wp-image-2949" title="device-2012-11-08-203216" src="https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-203216-300x222.png" alt="" width="300" height="222" srcset="https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-203216-300x222.png 300w, https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-203216.png 800w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2012/11/device-2012-11-08-203216.png)

Beyond “Active” messages, the notification system will also warn or block connections that are deemed risky, invalid or otherwise unverifiable. You can use OnionKit in concert with the [MemorizingTrustManager](https://github.com/ge0rg/MemorizingTrustManager) to manually override this verification process, if your application is expected to often connect to servers with unverifiable certificates. Finally, using our [CACert project](https://github.com/guardianproject/cacert), you can generate custom Root CA stores for use with OnionKit, that utilize your own certificate authorities, or a custom rolled set.

Our goal is not to overwhelm the user, but instead to provide them a simple notification so they can understand which applications have their best interests in mind, and which do not. It is amazing how many popular mobile apps transmit personal information using HTTP completely in plain text, in the clear, allowing any number of parties along the network path between the device and server to passively vacuum up this data. Users generally are not aware or do not care about this issue. It is up to the mobile application developer, to adopt an approach like our Secure Connection Notification, or to directly utilize our OnionKit library itself.

Finally, we would like to see Android and other mobile operating systems, adopt a system such as this device-wide, such that it becomes as standard as the desktop web browser HTTPS lock.

If you are a developer, please check out OnionKit for Android today, and let us know what you think: <https://github.com/guardianproject/OnionKit/>