---
title: Arti, next-gen Tor on mobile
date: 2023-03-04T10:00:00-04:00
author: uniq
layout: post
permalink: /blog/2023-04-11-arti_mobile_ex.md
categories:
  - News
tags:
  - Android
  - Tor
  - Privacy
  - open source
  - pluggable transports
  - rust

---

For software projects with recurring bugs, efficiency or security issues
there's a joke making the rounds in the software industry: "Let's re-write it
in [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language))!"  It's a
fairly new low-level programming language with the declared goal to help
developers avoid entire classes of bugs, security issues and other pitfalls.
Re-writing software is very time consuming, so it rarely happens, especially
when just one more fix will keep a project up and running.

[Tor-Project](https://torproject.org) was started in 2001 using the [C
programming lanugage](https://en.wikipedia.org/wiki/C_(programming_language)).
However a few years ago they set out to actually re-write their project in
Rust.  That projects codename is [Arti](https://arti.torproject.org/) and it
was [first released](https://blog.torproject.org/arti_100_released/) in 2022.
While Arti is working great, it doesn't have all features of the original Tor
implementation yet.  However, they are steadily working on getting there.  For
example, rough [Pluggable Transports](https://www.pluggabletransports.info/)
support was added to Arti in the recent 1.1.0 release.

We already have early [test builds of
Arti](https://gitlab.com/guardianproject/arti-mobile-ex/) running on both
Android and iOS.  The integration we came up with is pretty basic, but so far
it seems to work reliable for accessing the Tor network.  Maintaining code for
both iOS and Android in the same project will hopefully simplify shipping new
Arti releases for us, make integrating Tor capabilities into any app simpler.
To make it useful for the broader mobile developer community, we're also
investigating whether we can provide easy to use API bindings.  We've created a [sample
app](https://gitlab.com/guardianproject/arti-mobile-ex/-/tree/main/android/sample)
on Android to test and illustrate what a minimalistic integration of Arti looks
like.  It's as simple as adding a few lines of code.

Support for features like advanced censorship circumvention or onion services is not
exactly straight forward on mobile operating systems, because they tend to be
way more locked down than traditional computers.  Currently, we can successfully test
pluggable transports in "managed" mode on old versions of Android.  However
this technique will likely not work on the latest version of Android and never
worked iOS to begin with.  We have shared our findings with the Arti developer
team and hope they'll work on getting us to full Pluggable Transports support, integraing
with our existing [IPtProxy Library](https://gitlab.com/guardianproject/IPtProxy) soon.
