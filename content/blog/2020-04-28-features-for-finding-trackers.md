---
title: '"Features" for Finding Trackers'
author: Hamilton Kaplan
categories:
  - Development
  - News
tags:
  - android
  - Exodus Privacy
  - feature extraction
  - research
  - machine learning
  - tracking
  - Tracking the Trackers
---

One key component of the Tracking the Trackers project is building a
machine learning (ML) tool to aide humans to find tracking in Android
apps. One of the most important pieces of developing a machine
learning tool is figuring out which "features" should be fed to the
machine learning algorithms. In this context, features are
constrained data sets derived from the whole data set. In our case,
the whole data set is terabytes of APKs. This post is an outline of
the features that we are focusing on in this current project.


# Confirmed Features

These are features that we will definitely used, and already have good
tooling to do the [feature
extraction](https://en.wikipedia.org/wiki/Feature_extraction).

## Permissions

Android apps must request
[permissions](https://developer.android.com/guide/topics/permissions/overview)
from the Android OS to access sensitive user data as well as certain
system features. This can naturally give big hints towards tracking
attempts. Basically an app which does not request any permissions will
have a much harder time of tracking its users, while an app aimed
towards tracking will require a myriad of permissions depending on the
properties it desires to track (e.g. location, contacts, phone IDs,
Bluetooth IDs, WiFi IDs, camera/microphone-access, call-logs and many
more)


## Tracking Libraries and SDKs

Code re-use plays a big role in any software project, why write your
own tracking functionality when someone else has already implemented a
whole library geared towards tracking users. This functionality is
provided by different SDKs, which are pre-configured bundles of
functionality which in turn (for this use case) are provided by
tracking companies. The app developer often has to choose the desired
functionality. While importing a tracking library is no guarantee for
tracking activities it is certainly a red flag. We compare the
libraries imported by the app with a list of known tracking libraries.


## Domain Names

Developers leave URLs in form of strings in the code to allow exchange
of information with the world outside of the app. This can be used to
transfer information about the user which in turn can be used for
tracking. The domains often contain a hint about the purpose behind
the data transfer (e.g. `https://www.google-analytics.com`). Domain names
are data sinks for collecting data, which gives us a clear point to
focus on analyzing since collecting tracking data does not matter if
it never leaves the local device, while domain names are the point in
the code where data leaves the device and is sent to be collected and
analyzed on a remote server. Combined with other features like
permissions and seeing tracking libraries being imported a human
reviewer could get a pretty good idea of what type of information
could be sent. This human "gut feeling" of recognizing fishy
combinations of features is something a neural network can often learn
to approximate by being trained on a sufficient amount of training
data. Domain names known to be relevant to tracking are collected and
maintaned by [Exodus Privacy](https://exodus-privacy.eu.org/en/).


# New Experimental Features

These are features that show a lot of promise, but there is not
existing tooling to easily work with them.  We are working to make it
easier, and will cover that work in future posts.

## API Key ID

The [_API Key ID_](https://github.com/Exodus-Privacy/etip/issues/62)
is a string that identifies bit of authentication data for enabling
access to an online service. Many online services require an _API Key_
even if a library or SDK is not required to access it. Even when the
SDK is detected, the presence of an _API Key_ shows that the tracking
function is actually enabled. For example, the Google Firebase SDK
includes lots of functionality, not only tracking, each of which must
be enabled with an _API Key_. So the presence of Firebase is not
enough to confirm tracking. A [current
example](https://en.epicenter.works/content/analysis-of-the-stopp-corona-app-improvements-through-expert-report)
of exactly this is the Austrian Red Cross' _Stopp Corona_ app to track
the spread of covid-19 in Austria.


## Natural Language Processing (NLP)

As mentioned under the section on domain names, domain names can
already give a clear hint at intent. However since this property is
well known, URLs might be obfuscated to hide this information. This
domain name obfuscation is a well known technique in the world of
malware, there is some evidence of use by tracking companies. In this
case, a language model might learn that any URL that looks like random
letters and numbers might be a sign to consider increasing the
probability of classifying this app as tracking slightly, depending on
other features like requested permissions, and imported tracking
libraries.


## Broadcast Receivers

Android provides a system for data to be broadcast to all apps on a
device, this is known as a [_Broadcast
Receiver_](https://developer.android.com/guide/components/broadcasts).
A wide range of data is available via this mechanism, both from the
Android system as well as apps.  The Android OS broadcasts detailed
information about the [battery level, health, and charging
status](https://developer.android.com/training/monitoring-device-state/battery-monitoring),
including details of [how its
charging](https://developer.android.com/reference/android/os/BatteryManager#BATTERY_PLUGGED_AC).
Many music apps will broadcast detailed information about the song
being played, while also [collecting those
events](https://gitlab.com/trackingthetrackers/wiki/-/issues/5) from
the system and other apps.  The full extent of this activity is not
well described, both what data is broadcasted, what apps are doing
with it, and which apps are collecting.  As a feature, _Broadcast
Receivers_ have a lot of promise since they fit the patterns of useful
features for machine learning: small, globally unique, and easy to
extract.


# Feature Extraction Process

We are using tabular data to feed to the machine learning processes,
so the process of extracting and pre-processing different features for
classification includes similar steps for every feature. The number of
features that can reasonably be processed this way is limited to
probably tens of thousands of features, or perhaps even hundreds of
thousands. Therefore we have collections of the top-_n_ features where
_n_ is in the range of thousands: For example, the top thousand
tracking libraries, or all built-in permissions. This way we extract
the features out of the binary APK file, and source code when
available, and loop over our collections of known features. If the
feature was found in the APK/source the tabular data will be a 1, else
a 0.
