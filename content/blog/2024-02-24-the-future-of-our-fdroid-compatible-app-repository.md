---
title: The future of our fdroid-compatible app repository
author: eighthave
categories:
  - News
tags:
  - Android
  - F-Droid
  - fdroid
  - free software
  - net.opendasharchive.openarchive.release
  - open source
  - org.article19.circulo
  - org.havenapp.main
  - org.torproject.android
  - org.torproject.torbrowser
  - org.witness.proofmode
  - privacy

---

Guardian Project has been running its own [fdroid-compatible app repository](https://guardianproject.info/fdroid/) since [2012](https://guardianproject.info/2012/03/15/our-new-f-droid-app-repository-out-of-date/). Up until now, we worked to ensure that our repository had the same standards of free software as the official F-Droid repository.  Therefore, the Guardian Project repository was included in the official F-Droid client app by default.  A lot has changed since then, for the better.  F-Droid has long since stopped shipping pre-built binaries from any provider.  Back in the day, F-Droid shipped some binaries, like Mozilla's Firefox APKs, and allowed some non-free libraries in apps.  The free software ecosystem on Android has since blossomed, so F-Droid no longer needs to make those kinds of compromises.  And F-Droid is completing a big update on how repositories are handled.

Guardian Project remains committed to producing free software.  But for some of our key use cases, it is unfortunately not yet possible to address them without including some proprietary libraries in our free software apps.  This means that the Guardian Project repository is [no longer included](https://gitlab.com/fdroid/fdroidclient/-/merge_requests/1302) in F-Droid by default.  Now, F-Droid can enforce that apps only use free software libraries while Guardian Project cannot yet.  This ties in nicely to two other key development efforts with the official F-Droid client app.  First, the index signer keys for selected repositories are now [built-in](https://gitlab.com/fdroid/fdroidclient/-/merge_requests/1296/diffs?commit_id=54e3975660f97c60ffdd038b1965a30822e033db), that means that the client will automatically verify that the user added the real repository.  Second, F-Droid [v1.20](https://gitlab.com/fdroid/fdroidclient/-/merge_requests?milestone_title=1.20) will ship a massive overhaul of the core plumbing and user experience for adding, removing, and managing repositories.  This makes it much easier and safer for users to use repositories that are not built-in.

What kinds of exceptions does Guardian Project make?  We still work to avoid as many kinds of tracking as possible.  And the code that we create is free software.  The exceptions are all related to proprietary libraries getting built into some of our apps:

* ProofMode uses SafetyNet to provide extra assurances about the provenance of media files generated on an Android device.
* Circulo and Haven use proprietary Google libraries to assist with accurately finding location.
* Save (aka OpenArchive) needs to integrate with widespread proprietary services like Dropbox or Google Drive. When it is useful, we produce free software versions of our apps and get them included on [f-droid.org](https://f-droid.org/packages/net.opendasharchive.openarchive.release/).
* There is work underway to get Tor Browser [included](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/27539#note_2989340) in f-droid.org.  One key blocker has been a proprietary binary library that the build system is [including](https://gitlab.com/guardianproject/fdroid-metadata/-/issues/3) anyway, even though it should be disabled in the build.
* Getting Orbot into f-droid.org is on our roadmap, it is already free software and otherwise compliant.  We welcome help maintaining the [build metadata](https://gitlab.com/fdroid/fdroiddata/-/blob/master/metadata/org.torproject.android.yml) in _fdroiddata_.

We will continue to [mark](https://gitlab.com/guardianproject/fdroid-metadata/-/issues/4) the apps in our repository with Anti-Features according to the [F-Droid standard](https://f-droid.org/docs/Anti-Features/).  If you have found something we have overlooked, please [open an issue](https://gitlab.com/guardianproject/fdroid-metadata/-/issues) so we can fix it.  One side benefit of this change is that we can now also include some other important apps for privacy, until there are free software alternatives without any proprietary libraries. Firefox and Signal are two likely candidates, since both apps can be built as free software, but the official builds include proprietary libraries.  In any case, any third party apps we might include here will have to meet the same standards as our own apps.
