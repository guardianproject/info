---
title: "New Data Sources: API Key Identifiers and BroadcastReceiver Declarations"
author: Hans-Christoph Steiner
categories:
  - Development
  - News
tags:
  - android
  - Exodus Privacy
  - F-Droid
  - fdroid
  - feature extraction
  - NGI0 PET
  - NLnet
  - tracking
  - Tracking the Trackers
---

A central focus of the [Tracking the
Trackers](https://gitlab.com/trackingthetrackers/wiki) project has
been to find simple ways to detect whether a given Android APK app
file contains code which tracks the user.  The ideal scenario is a
simple program that can scan the APK and tell a non-technical user
whether it contains trackers, but as decades of experience with
anti-virus and malware scanners have clearly demonstrated, scanners
will always contain a large degree of approximation and guesswork.
Tracking the Trackers grew out of experiments in using machine
learning to detect malware.  This provided the spark to apply this to
privacy issues.

The malware research clearly demonstrates that network domain names
and code signatures are quite reliable techniques for identifying
malware.  This also applies to tracking, since the majority of
tracking happens via tracking companies' SDKs which send data to
specific domain names.  The hard part is that code signatures and
domain names are not easy to reliably extract, and are often easy to
obfuscate when someone is looking to hide what an app is actually
doing.  This is common in malware, and we are also starting to see
obfuscation in the world of tracking.

Android gives us a break with its
[_AndroidManifest.xml_](https://developer.android.com/guide/topics/manifest/manifest-intro).
It is a hard requirement for Android apps so it is always there, it
contains some key declarations that set up how the code is run, and it
is easy to extract and parse.  So we put extra effort in thinking
about the data that is contained in the _AndroidManifest.xml_.

Towards the goal of simple scanners for tracking, we are excited by
two new data sources that we found in the _AndroidManifest.xml_ that
are useful signals for automatically detecting tracking in Android
apps: API Key Identifiers and _BroadcastReceiver_ Declarations.


### API Key Identifiers

Tracking services provide their customers with servers to submit the
data for processing and analytics.  These are usually part of the
service's API.  A common pattern for publicly accessible network APIs
is to require the use of an API Key.  This key grants access to the
service and provides an unique identifier for the customer so that the
submitted data goes to the right place.  In order to submit the key to
the API, the key data must be identified to the server somehow.  That
is the API Key Identifier.  This is generally something that never
changes, since changing it could mean locking out all customers.  For
example, [Google Firebase
Analytics](https://developers.google.com/android/reference/com/google/android/gms/analytics/Tracker)
has used `ga_trackingId` as its API Key Identifier for many years. API
Key Identifiers are a great way to track trackers.  They are tiny and
easy to extract.  Most services require them.  The entire set that we
have found is small enough to fit into a single machine learning
search space.  And it is quite unlikely that an app would include them
by accident or without having set up a tracking service.

We also found [some
evidence](https://github.com/Exodus-Privacy/etip/issues/62#issuecomment-613964965)
of obfuscated API Key Identifiers, the source has not yet been
identified.  We found many API Key Identifiers that were not the same
but matched a pattern.  This pattern looks like it could be encoding
some information:

* <tt>com.APpuz.lHMBA142332.APIKEY</tt>
* <tt>com.BCcyZzWehh.IOfazFfwIH109433.APIKEY</tt>
* <tt>com.CDwo.buYv134822.APIKEY</tt>
* <tt>com.DErSuvPp.bEyhwTQb93737.APIKEY</tt>
* <tt>com.EOoOEpvG.ZuepOuto31966.APIKEY</tt>
* <tt>com.FIKDGlAZIZ.vrlGNzSLEm110206.APIKEY</tt>
* <tt>com.GicPdlXU.iXbdAAkA69030.APIKEY</tt>


API Key Identifiers are now [included as a data
point](https://github.com/Exodus-Privacy/etip/issues/62) gathered in
[Exodus ETIP]({{< ref
2020-12-11-exodus-etip-canonical-database-for-tracking-trackers >}}).
If you have some clues about any of this, please [let us
know](https://gitlab.com/trackingthetrackers/wiki/-/issues/6).


### _BroadcastReceiver_ Declarations

In Android, apps and the
[system](https://developer.android.com/about/versions/11/reference/broadcast-intents-30)
can publicly broadcast events, and any app can listen for these
events.  Some of these events contain detailed information, like the
[complete metadata](https://gitlab.com/trackingthetrackers/wiki/-/issues/5)
about which song is currently playing.  Charging and battery status
can be used to
[re-identify users](https://blog.lukaszolejnik.com/battery-status-readout-as-a-privacy-risk/).
These broadcast events are generic Android `Intents` which an app
registers a receiver by name in order to get the info when it is sent.
The specific pieces of interest are the
_[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)
[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)
[Action](https://developer.android.com/guide/components/intents-filters#Building)_
names.

Like other bits in the _AndroidManifest.xml_, the _BroadcastReceiver_
Declarations are easy to extract.  Unfortunately, _BroadcastReceiver_
Declarations are not nearly has definitive when it comes to marking
tracking.  They are still worth including, since they are easy to
extract, and the whole set of unique, extracted names is small enough
to be used as a search space for the machine learning.

The scope of how apps can receive data via _BroadcastReceivers_ was
also recently
[narrowed](https://developer.android.com/about/versions/oreo/background#broadcasts)
to a large degree by Google, due to privacy concerns.  The upside is
that apps cannot receive system-wide broadcasts unless they are
already running.  The downside is that scanners have to do static code
analysis, and perhaps even dynamic analysis, in order to see which
_BroadcastReceiver IntentFilter Action_ names an app has declared.


## Usage Considerations

The possibility of false positives is still there.  For example, if
someone makes a "build flavor" that builds without tracker SDKs but
forgets to exclude the API Key Identifiers, then a simple scanner will
flag this as tracking, even though it could not be.  The tracker SDK
is not included, which is the code that gathers and uploads the
tracking data.  In this example, the developer can easily fix it after
a scanner flags the app as a tracker, by moving the API key
configuration out of the "build flavor".

A trickier case to review is when an app includes opt-in tracking.  We
believe that opt-in tracking and data reporting should not be flagged
as a tracker, especially when the opt-in user experience makes it
clear to the user what data is being gathered, and under what
condition it is being sent.  In that case, the simple scanner will
flag the app, since it contains the API Key Identifier.

This is why we think that machine learning is very promising for
tracking apps that track us.  There are many good signals, but none of
them definitely mark an app as a tracker.  They must always be
considered as a group with the whole picture, and given well-labeled
data, machine learning can do this kind of task quite accurately.


## Join the Hunt!

Finding API Key Identifiers is work that can be done in bite-sized
pieces, by people in their spare time.  Many if not most tracker SDKs
require API keys in order to use their service, so start by looking
through [ETIP](https://etip.exodus-privacy.eu.org/trackers/all) for
entries that are missing `Api_key_ids` entries.  Usually, this is
documented in their SDK developer documentation.  There are also many
SDKs which set the API Key via a [method
call](https://github.com/Exodus-Privacy/etip/issues/62#issuecomment-598272804)
rather than a declaration in an XML file.  In that case, the API Key
Identifier might be found by reading the strings out of the JAR
file. We also welcome more information about _BroadcastReceiver_
declarations.  We are tracking new data sources and approaches in our
[issue tracker](https://gitlab.com/trackingthetrackers/wiki/-/issues).

For any kind of mass scanning to be usable, future work should focus
on expanding the set of easy to extract features, and finding which of
those are useful.  Complicated and resource-intensive extractions like
domain names, code signatures, and source/sink tracing still hold
promise for delivering high accuracy, but would likely remain only
useful when scanning individual or small sets of apps.

(_This work was supported by NLnet's [NGI Zero PET](https://nlnet.nl/thema/NGIZeroPET.html) fund._)
