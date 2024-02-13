---
title: 'NetCipher update: global, SOCKS, and TLSv1.2'
author: Hans-Christoph Steiner
categories:
  - Development
  - News
tags:
  - Android
  - netcipher
  - orbot
  - proxy
  - security
  - tor
  - webkit
---

[NetCipher](/code/netcipher) has been relatively quiet in recent years, because it kept
on working, doing it was doing. Now, we have had some recent
discoveries about the guts of Android that mean NetCipher is a lot easier
to use on recent Android versions.  On top of that, TLSv1.2 now reigns
supreme and is basically everywhere, so it is time to turn TLSv1.0 and
TLSv1.1 entirely off.


## A single method to enable proxying for the whole app

As of Android 8.0 (26 aka Oreo), it is now possible to set a
`URLStreamHandlerFactory`, which creates `URLConnection` instances
with custom configurations.  If an app is using the built-in
`HttpURLConnection` API for its networking, it is now possible to
enable global proxying with a single method call when the app starts:
[`NetCipher.useGlobalProxy()`](https://guardianproject.github.io/NetCipher/libnetcipher/info/guardianproject/netcipher/NetCipher.html#useGlobalProxy--).
Then the actual proxy configuration can be set dynamically, using
things like
[`NetCipher.useTor()`](https://guardianproject.github.io/NetCipher/libnetcipher/info/guardianproject/netcipher/NetCipher.html#useTor--)
or
[`NetCipher.clearProxy()`](https://guardianproject.github.io/NetCipher/libnetcipher/info/guardianproject/netcipher/NetCipher.html#clearProxy--).

The `URL.setURLStreamHandlerFactory()` method is a little odd because it cannot be unset or changed after it has been set.  NetCipher handles this by letting the app configure the proxy settings separately, so they can be disabled even though the custom `URLStreamHandlerFactory` is still active.  Also, it is possible to use `URL.setURLStreamHandlerFactory` on Android 7.x also, but it leaks DNS, so it is not recommended for privacy proxies.  It would still be useful as a failsafe for apps that use [`NetCipher.getHttpURLConnection()`](https://guardianproject.github.io/NetCipher/libnetcipher/info/guardianproject/netcipher/NetCipher.html#getHttpURLConnection-java.lang.String-), in case there are any calls to `URL.openConnection()` added with the right proxy setup.  At the very least, the content will be proxied on Android 7.x, even if it leaks DNS.


## Native SOCKS Support

In Android 7.0 (24 aka Nougat), Google switched over to OpenJDK, which brought working SOCKS support to Android.  SOCKS is the best protocol for effective proxying, and it is the protocol that Tor itself has always natively supported.  Orbot has always provided a separaete HTTP Proxy to support Android, but that has always proven brittle, and was often the source of problems.  Since Android 7.0 and above natively support SOCKS, calling `NetCipher.useTor()` will now default to using SOCKS if the device is running Android 7.0 or higher.


## Bye bye TLSv1.0 and TLSv1.1

Transport Layer Security (TLS) is the protocol that powers most of the internet these days.  It gives HTTPS the S for "Secure". After many years of slow updates and an increasing number of vulnerabilities, there is finally critical mass to stop using the old, broken versions.  TLS version 1.2 is not seriously vulnerable and is supported basically everywhere.  TLSv1.2 was finalized in 2008, so this is very far from the bleeding edge.  TLSv1.2 is supported all the way back to [Android 4.1](https://developer.android.com/reference/javax/net/ssl/SSLSocket#protocols).  TLSv1.0 and TLSv1.1 are due to be officially deprecated by the IETF, the standards body that actually creates the TLS standard.  The major browser vendors have all promised to drop them in 2020.

One way to enforce TLSv1.2 support would be to configure the server-side to stop supporting TLSv1.0 and TLSv1.1, like is recommend with SSLv2 and SSLv3.  Using NetCipher to do this on the client side
means that old app versions and devices of F-Droid and old devices will continue to work.
Also, doing it client-side means that all TLS connections will gain this protection regardless of which server the client is connecting to.

The _NetCipher_ approach means apps will never use TLS older than v1.2 since they will refuse to connect unless TLSv1.2 is available.  The server-side can then safely support TLSv1.0 and TLSv1.1, so older clients and Android devices will still be able to connect, even if they do not support TLSv1.2.  It is win-win
for everyone.

The one case that will fail entirely is connections to servers that do not support TLSv1.2.  If a webserver does not support TLSv1.2, it is really too old to be used safely anyway.  Even the oldest supported Red Hat Enterprise Linux release (6) supports TLSv1.2, and that was released in 2010.


## `WebView` Proxying!

[`WebView`](https://developer.android.com/reference/android/webkit/WebView) provides an easy way to show a webpage or build a web app.  If you want that page to always go over Tor, that is difficult since `WebView` has no API to configure proxying.  NetCipher has a long running collection of hacks that span the Android versions to get proxying working in `WebView`.  We have revived those, modernized them, and added a full test suite to confirm whether the proxying is leaking.  The good news is that proxying is working pretty well on all but Android 5.x (21 and 22), where it totally fails.

Another new Android API we discovered is [`WebViewClient.shouldInterceptRequest()`](https://developer.android.com/reference/android/webkit/WebViewClient.html#shouldInterceptRequest(android.webkit.WebView,%20android.webkit.WebResourceRequest)).  This is an official API for manipulating HTTP requests in `WebView`.  It is an an easy place to insert custom `HttpURLConnection` instances, like NetCipher needs to configure proxy support and stronger TLS.  Using this API means eliminating Java reflection hacks.  But it has a large caveat: it only works for _GET_ requests.  Since the request body is not accessible via this API, it is not possible to implement _POST_ or _PUT_ requests.  One nice approach for the best of both works is to handle _GET_ with `WebViewClient.shouldInterceptRequest()`, then _POST_ and _PUT_ could then be implemented separately using the reflection methods in NetCipher WebView.


## Tests!

This release also brings with it an extensive, new test suite.  These let us confirm that things are working on all the supporting Android versions, while also serving as simple example cases.  For example, the tests now confirm which Android releases support `WebView` proxying, based on Cure53's very useful [HTTPLeaks](https://github.com/cure53/HTTPLeaks).
