---
id: 3609
title: 'NetCipher: Secured Networking'
date: 2013-04-29T11:00:55-04:00
author: n8fr8
guid: https://guardianproject.info/?page_id=3609
menu:
  main:
    parent: code
---

{{< source-code name="NetCipher" >}}

**Better TLS and Tor App Integration**

NetCipher is a library for Android that provides multiple means to
improve network security in mobile applications. It provides best
practices TLS settings using the standard Android <tt>HttpURLConnection</tt> methods, <a
href="https://developer.android.com/reference/java/net/HttpURLConnection.html"
target="_blank"><code>HttpURLConnection</code></a>, OkHTTP3, Volley, and <a
href="https://hc.apache.org/httpcomponents-client-4.3.x/index.html"
target="_blank">Apache HTTP Client</a>, provides simple Tor
integration, makes it easy to configure proxies for HTTP connections
and <code>WebView</code> instances.

More specifically this library provides:

  * Hardening of TLS protocol support and cipher suites, especially on older  
    versions of Android
  * Proxied Connection Support: HTTP and SOCKS proxy connection support for HTTP  
    and HTTPS traffic through specific configuration
  * OrbotHelper: a utility class to support application integration with Orbot  
    (Tor for Android). Check if its installed, automatically start it, etc.
  * Optional, custom certificate store based on the open Debian root CA trust  
    store, which is built with Mozilla&#8217;s CA collection.

IT MUST BE NOTED, that you can use this library without using Orbot/Tor, but obviously we think using strong TLS/SSL connections over Tor is just about the best thing in the world.

<a title="onionkit" href="https://github.com/guardianproject/NetCipher" target="_blank">https://github.com/guardianproject/NetCipher</a>

_This library was formerly named OnionKit_

## Getting Started

For examples and more info on using NetCipher, see the <a
href="https://github.com/guardianproject/NetCipher#readme"
target="_blank">README</a> and included sample projects.  Many apps
include NetCipher, so they can also serve as examples of NetCipher in
action:

### Sample Projects

* [Android HttpURLConnection](https://github.com/guardianproject/NetCipher/tree/master/sample-hurl)
* [Apache HTTP Client](https://github.com/guardianproject/NetCipher/tree/master/sample-httpclient)
* [chboye](https://github.com/guardianproject/NetCipher/tree/master/sample-chboye)
* [OkHTTP3](https://github.com/guardianproject/NetCipher/tree/master/sample-okhttp3)
* [Volley](https://github.com/guardianproject/NetCipher/tree/master/sample-volley)
* [WebKit](https://github.com/guardianproject/NetCipher/tree/master/sample-webkit)
* [WebViewClient](https://github.com/guardianproject/NetCipher/tree/master/sample-webviewclient)


### Apps

* <a href="https://gitlab.com/fdroid/fdroidclient/commit/2c88703588a6192cbf3ffd7ccb8d01b65c693ed3" target="_blank">F-Droid</a>

{{< gradle-line groupId="info.guardianproject.netcipher" artifactId="netcipher" >}}

{{< netcipher-downloads >}}
