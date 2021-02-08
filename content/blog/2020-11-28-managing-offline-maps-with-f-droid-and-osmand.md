---
title: Managing offline maps with F-Droid and OsmAnd
author: Hans-Christoph Steiner
categories:
  - Development
tags:
  - F-Droid
  - fdroid
  - offline
  - OsmAnd
  - Wind
  - WINS
---

When disaster strikes, our mobile devices can provide us with many
tools to deal with a wide variety of problems.  The internet is not
available in every corner of the planet, and large scale outages
happen.  Digital maps allow us to carry detailed maps of the entire
planet in our pockets.  And the good map apps allow the user to
download entire regions to the device so that they operate without
internet at all.  Unfortunately, the big map apps from Google and
Apple provide limited offline capabilities.  For example, it is
[not possible](https://annoyingtechnicaldetails.wordpress.com/2020/09/23/cannot-easily-redistribute-downloaded-offline-files-for-google-maps/)
to share offline data from one device to another.  Online maps are
also a major privacy leak, since location data is the most sensitive
data.  With online maps, the service operator sees each tile of the
map that you look at, each time you look at it, as well as all the
locations you search for.

[OsmAnd](https://osmand.net/) is a great map app for offline usage,
since offline usage is the primary mode of operation.  It lets you
download entire regions to your device, then search and navigate
without any network connection at all. This is also a big win for
privacy: In offline mode, OsmAnd can only see which regions you have
downloaded, and nothing else.  OsmAnd provides private, resilient
services. The maps will work as long as your device is working.  The
maps are still usable even if GPS is unavailable, since they can be
searched and operated with only your fingertips.

F-Droid is the most private and flexible mobile distribution system,
so we recently worked to make it a lot easier to ship OsmAnd map files
via F-Droid repos.  That means that entire countries can be made
available through the F-Droid distribution methods, including offline
methods like mirrors on USB-OTG drives and local repos on a Raspberry
Pi that provides the WiFi connection.

To see an example of this in action, try adding our new
[Wind Offline repo](https://guardianproject-wind.s3.amazonaws.com/fdroid/repo?fingerprint=182CF464D219D340DA443C62155198E399FEC1BC4379309B775DD9FC97ED97E1)
to F-Droid, and look for the "OsmAnd" category.  The whole repo is
managed by scripts, which is available on
[GitLab](https://gitlab.com/guardianproject/wind-repo/).

(_This work was supported by the prize money from the [Mozilla WINS](https://wirelesschallenge.mozilla.org/#winners) competition as part of the [Wind](https://guardianproject.info/code/wind/) project._)
