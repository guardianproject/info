---
title: NetCipher + Conscrypt for the best possible TLS
author: Hans-Christoph Steiner
categories:
  - News
tags:
  - security
  - privacy
  - android
  - netcipher
  - conscrypt
  - tls
  - esni
---

A new NetCipher library has recently been merged:
[_netcipher-conscrypt_](https://gitlab.com/guardianproject/NetCipher/merge_requests/86).
In the same vein as the other NetCipher libraries,
_netcipher-conscrypt_ wraps the Google
[Conscrypt](https://source.android.com/devices/architecture/modular-system/conscrypt)
library, which provides the latest
[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) for any
app that includes it.  _netcipher-conscrypt_ lets apps then disable old
TLS versions like TLSv1.0 and TLSv1.1, as well as disable TLS Session
Tickets.  This is an alpha release because it only works on recent
Android versions (8.1 or newer).  The actual functionality works well,
the hard part remains making sure that it is possible to inject
_netcipher-conscrypt_ as the TLS provider on all Android devices and
versions.  And the last missing piece is finding the right place in
Conscrypt to configure proxying to support Tor or other privacy
proxies

Before Conscrypt, Android apps relied on the Android OS itself to
provide TLS.  Normally, software uses the TLS provided by the
operating system.  Since too often Android devices do not get software
updates, lots of users are stuck on old TLS versions.  So Google split
out the TLS stack from Android itself and made the Conscrypt library
from it so it can be independently updated.  Guardian Project has been
taking this approach for almost 10 years, starting with
SQLCipher-for-Android and IOCipher libraries.  We are happy to see
Google doing this themselves to give us more platform flexibility and
security.  We plan on using this as a platform for making [ESNI
(Encrypted SNI)](https://tools.ietf.org/html/draft-ietf-tls-sni-encryption)
available to all Android apps.

It is exciting to see ideas that we have been championing over the
past decade to get mainstream adoption.  TLS Session Tickets have
always had serious [security](https://blog.filippo.io/we-need-to-talk-about-session-tickets/) and [privacy](https://www.theregister.co.uk/2018/10/19/tls_handshake_privacy/) issues, Android 10 [now
provides](https://source.android.com/devices/architecture/modular-system/conscrypt#consrypt-q)
an official API for disabling TLS Session Tickets:
[android.net.ssl.SSLSockets](https://developer.android.com/reference/android/net/ssl/SSLSockets.html)
and
[android.net.ssl.SSLEngines](https://developer.android.com/reference/android/net/ssl/SSLEngines.html).
And the idea of per-app file encryption, which _IOCipher_ provides, can
now be largely provided by the built-in [Android File-Based Encryption
(FBE)](https://source.android.com/security/encryption/file-based).
