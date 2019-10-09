---
title: 'Onions on Apples: A New Release of Onion Browser for iOS'
categories:
  - News
tags:
  - iOS
  - Apple
  - tor
  - iPhone
---
During 2019, Guardian Project has been working with developer Mike Tigas to make improvements to his Tor-enabled web browser for iOS, [Onion Browser](https://onionbrowser.com/).  Here we re-cap the major improvements currently - and soon-to-be - available.

Mike developed Onion Browser on his own, in close collaboration with the Tor Project.  Though we’ve worked with Mike in the recent-past, this 2019 project -- funded by the Open Technology Fund -- gave us significantly more bandwidth to address the challenges of running Tor on iOS, especially alongside a full web-browsing feature set. 

In Onion Browser, our Tor connectivity runs in the same process as the browser itself.  Tor Browser for Android uses a similar model, though the general purpose Orbot app for Android is separate from the applications using its services (apps configure Orbot as a proxy, in the same manner as SOCKS).  This latter model is not available on iOS and, it turns out, iOS puts some additional restrictions on apps like ours as well.  These have, over time, created some thorny problems for Onion Browser. 

The newest release of Onion Browser upgraded to Tor version 0.4.0.5 which greatly improves reliability when the app comes back from background. The application was updated with modern versions of all the incorporated 3rd-party libraries.  This includes an upgrade to the underlying Endless browser-core.  The often-requested ability to "open the app in its last state" feature was added as well as a mechanism to hide the browser’s content when switching between applications.  Advanced users of the app had reported issues configuring bridges in previous releases and these have been fixed.  It’s now possible to report a bug or rate the app from within the application.

With our new work, an important network traffic leakage discovered in earlier releases have been mitigated.  Web browsers generally utilize the services of the Online Certificate Status Protocol (OCSP) to determine if a website’s security certificate is still valid. Status checks on iOS are provided by a system library that can’t use the Tor service, so these service calls leak.  A mechanism has been found to prevent leakage in a large number of circumstances, but not completely.

We’re now completing our second big development push which will feature an upgraded and simplified on-boarding experience as well as improvements to the organization of application settings.  We’ve also upgraded the experience of setting per-website security parameters (which can be either one-time-only or “sticky”).  The leakage corrections we implemented will also allow us to implement the ability to download and save files in non-HTML content formats, or share such files with other applications. Additionally, we implemented an improved technique to limit Javascript “re-insertion” attacks in WebRTC pages. We expect this release to happen during October or early November.

Onion Browser’s medium- and long-term maintenance are a volunteer effort.  If you wish to support this project into the future, please visit Mike Tigas’s Patreon page.


