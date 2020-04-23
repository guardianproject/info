---
title: The Promise and Hazards of COVID Contact Tracing Apps
author: Hans-Christoph Steiner
categories:
  - News
tags:
  - covid
  - free software
  - open source
  - privacy
  - trust
  - usability
---

There has been increasing interest in the possibilities of tracking
people who are infected with Coronavirus using all of the various
methods that smart phones provide.  There is good reason: "[contact
tracing](https://en.wikipedia.org/wiki/Contact_tracing)" has been a
pillar of public health efforts for decades.  It is an effective means
to curtail the spread of infectious disease.  At the same time,
governments, companies, and organizations are acting fast to offer
services to help end this current pandemic.  The problem is that many
of these are taking advantage of these times to introduce more
tracking of people, more data collection, and more control over
people.  We must not let contact tracing be used to reduce privacy
and increase unnecessary data collection.

Privacy International has been collecting examples of
[new data and tracking that are being introduced](https://privacyinternational.org/examples/tracking-global-response-covid-19).

Then there this is the specific issue of contact tracing apps that are
being introduced around the world.  These apps can be made in a way to
fully respect privacy, and to build trust with its users.  Unfortunately the majority of the ones introduced are failing to live up to this promise.  Singapore's TraceTogether was the first to rise to prominence, it is proprietary software with obfuscated operations. (_update: the source for a [reference implementation](https://github.com/opentrace-community) has since been released, but TraceTogether is still proprietary_)   A [some](https://medium.com/@zerotypic/reversing-tracetogether-initial-analysis-edc940e86aa8) [audits](https://splira.com/2020-03-28/) pointed to failings, including potentially sending location data to a third-party analytics service.  There are now many of these apps, and based on [this analysis](https://forensic.defensive-lab.agency/covid/), most of them are sending data to third party tracking companies.

On top of that, these audits took much more effort because the apps
were not open source.  There have been many pledges of making these
apps open source, but the only one that we have found that is actually
open source is [Private Kit](https://privatekit.mit.edu/).  [Free, open
source software is essential](https://fsfe.org/news/2020/news-20200402-02.en.html)
for software that needs to be widely
trusted.  This is only key design element, the CCC has laid out a
complete list of [requirements for creating trustworthy contact
tracing apps](https://www.ccc.de/en/updates/2020/contact-tracing-requirements).

We stand ready to help any of these efforts achieve real privacy and
build public confidence.  People must trust these apps for them to be
effective.  Transparency is essential to building trust.  They must be
secure so they do not leak personal data.  And they must be usable by
the vast majority of the population.
