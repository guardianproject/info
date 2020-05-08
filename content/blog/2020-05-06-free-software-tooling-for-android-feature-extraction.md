---
title: Free Software Tooling for Android Feature Extraction
author: Hans-Christoph Steiner
categories:
  - Development
  - News
tags:
  - android
  - debian
  - Exodus Privacy
  - feature extraction
  - free software
  - machine learning
  - NGI0 PET
  - NLnet
  - open source
  - Tracking the Trackers
---

As part of the Tracking the Trackers project, we are inspecting
thousands of Android apps to see what kinds of tracking we can find.
We are looking at both the binary APK files as well as the source
code.  Source code is of course easy to inspect, since it is already a
form that is meant to be read and reviewed by people.  Android APK
binaries are a very different story.  They are first and foremost a
machine-executable format.  On top of that, many developers
deliberately obfuscate as much as possible in the APK to resist
inspection.

That means inspection requires using tools to look into the binary APK
format.  There is actually a massive amount of work that goes into
inspecting APKs because this is required in order to do useful malware
analysis.  For the most part, these inspection techniques are the
malware companies' "special sauce", so they are proprietary and
generally kept secret.  On top of that, malware companies keep secret
a lot of the conclusions they about what is useful data to collect,
and what should be ignored.

One key piece of the Tracking the Trackers project is to make all of
research, tooling, and conclusions free, open, and publicly available.
First and foremost, that means the tools must be free software.  They
should also be easily installable so the barrier to entry for new
inspectors is as low as possible.  We focus on getting software as
part of Debian, since once there, so many people have access to those
packages since Ubuntu, Kali, and so many other GNU/Linux distros are
based on Debian.

## What is available in Debian already

[Our
work](https://guardianproject.info/2015/04/30/getting-android-tools-into-debian/)
with the [Debian Android Tools
Team](https://wiki.debian.org/AndroidTools) and [Debian Java
Team](https://java.debian.net/) over the years means many key tools
are already included in Debian and its derivatives, including:

* key Android SDK components like _apksigner_, _dx_ and _android.jar_
* _apktool_
* _dexdump/dexlist_
* _enjarify_
* _LibScout_
* _libsmali_
* _procyon_


## Tools we are using

One key aspect of our research is that working with terabytes of APKs,
this is necessary to be able to spot and map out as many trackers as
possible.  Since feature extraction can be a slow and resource
intensive process, we needed to use some tools that emphasize speed
over flexibility.  Even with fast extraction tools, we still have to
build up tailored processes to speed things up.  Some of these
straightforward feature extraction processes would take months to run
on ~3TB of APKs on a 32-thread machine with 144GB of RAM.

* [LibScout](https://github.com/reddr/LibScout) - detect SDKs/libraries with their version in binary APKs
* https://github.com/avast/apkparser - faster manifest/resources parser
* https://github.com/avast/apkverifier - faster APK signature verifier
* https://github.com/jedisct1/ipgrep - ipgrep extracts possibly obfuscated host names and IP addresses from text, resolves host names, and prints them, sorted by ASN.
* https://github.com/stricaud/faup - Fast URL decoder library
* https://github.com/cryptax/droidlysis - Quickly analyze APKs for the most essential features: permissions, `Activity` and `BroadcastReceiver` names, and key method calls.

_apkverifier_, _apkparser_, and _droidlysis_ are generally useful, but
not yet in Debian.  So we packaged them to make them easily available.
They are currently in the [Debian
NEW](https://ftp-master.debian.org/new.html) queue, awaiting final
review before inclusion.

These tools have been assembled into scripts to run the actual feature
extract processes, they are maintained in the
https://gitlab.com/trackingthetrackers/extracted-features repo.  When
the actual data generated is small enough and there are not copyright
conflicts, the data is also included there.  Mostly, the data sets are
too large and sometimes touch on copyright restrictions, so they are
unfortunately not publicly available.

There are lots of other tasks, including managing large APK
collections, gathering data to generate statistics about the features,
and downloading publicly available tracker SDK.  Those scripts are
maintained in https://gitlab.com/trackingthetrackers/scripts.


### Gradle Plugins

When working with source code, then it is possible to do other kinds
of analysis.  Most Android apps are built with the Gradle tool.  So we
reviewed a wide range of Gradle plugins, and found these three useful
in our investigations.

* [dependency-analysis-android-gradle-plugin](https://github.com/autonomousapps/dependency-analysis-android-gradle-plugin) - Produce a report of unused direct dependencies and used transitive dependencies.
* [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck) - utility that detects publicly disclosed vulnerabilities in application dependencies
* [gradle-dependency-graph-generator-plugin](https://github.com/vanniktech/gradle-dependency-graph-generator-plugin/) - Gradle plugin that lets you visualize your Java library dependencies in a graph.


## Tools we reviewed

We looked at quite a few existing tools, and found many interesting
and useful ones.  While they all produced useful output, many of these
were not useful to this project because they were tailored around the
use case of a person inspecting a small set of apps, so for example,
they were too slow or did not produce machine readable output suitable
for working with large APK collections.

* [android_permissions_harvester](https://github.com/U039b/android_permissions_harvester) - for finding which permissions are used based on method calls
* [droidlysis](https://github.com/cryptax/droidlysis) - cryptax's (aXelle's) tool: "DroidLysis is a property extractor for Android apps". See also her [talk at hacklu 2019](https://cfp.hack.lu/hacklu19/talk/ZZKNSM/)
* [APKiD](https://github.com/rednaga/APKiD) - "In addition to detecting packers, obfuscators, and other weird stuff, it can also identify if an app was compiled by the standard Android compilers or dexlib"[[1]](https://rednaga.io/2016/07/31/detecting_pirated_and_malicious_android_apps_with_apkid/)
* [redex](https://github.com/facebook/redex) - "taking advantage of Redex allows us to normalise the applications prior to analysis"[[1]](https://blog.quarkslab.com/android-application-diffing-analysis-of-modded-version.html)
* [kaitai_struct_formats](https://github.com/kaitai-io/kaitai_struct_formats/blob/master/executable/dex.ksy) - generic binary struct parser tool, useful for directly parsing Android _classes.dex_ files.
* [binaryanalysis-ng](https://github.com/armijnhemel/binaryanalysis-ng) - a framework for unpacking files recursively and running checks on the unpacked files.  Great for someone who needs to inspect small sets of a wide variety of file types.
* [redexer](https://github.com/plum-umd/redexer) - infer with which parameters the app uses certain permissions (we name this feature RefineDroid)
* [apk-static-xref](https://github.com/ytliu/apk-static-xref) - staticallly generate a cross-reference-graph (XRG) of a component (e.g., Service) of Android APK file
* [smalisca](https://github.com/dorneanu/smalisca) - Static Code analysis tool that generates call graphs
