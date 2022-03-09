---
title: 'TorService: Tor library for Android'
author: eighthave
menu:
  main:
    parent: code
aliases:
  - /code/torservice/
---

{{< source-code name="tor-android" >}}

This is native Android `TorService` built on the Tor shared library built for
Android.  It is designed around the Android lifecycle.  The included _libtor.so_
binaries can also be used directly as a tor daemon.  This is used in
[Orbot](https://orbot.app/),
[TorServices](https://gitlab.com/guardianproject/torservices),
[OnionShare](https://github.com/onionshare/onionshare-android), and more.


### Features

  * Native Android `TorService` for running Tor in a background service
  * Designed around modern Android tools like [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/long-running)
  * Reproducible Build with included Vagrant setup for running them

## Source Code Repository

  * library, helpers, tests, and sample project: <https://github.com/guardianproject/tor-android></ul>


{{< gradle-line groupId="info.guardianproject" artifactId="tor-android" >}}
