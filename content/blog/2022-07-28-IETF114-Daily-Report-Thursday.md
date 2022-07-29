---
title: "IETF114 Conference Report: Thursday July 28, 2022"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day Four of the [114th IETF meeting](https://www.ietf.org/how/meetings/114/) in Philadelphia USA. For the rundown on Day Three, see my [daily report](https://guardianproject.info/2022/07/27/ietf114-conference-report-wednesday-july-27-2022/).*

At IETF112 (online) a formal Birds of a Feather (BoF) session was held on the concept of [Privacy Preserving Measurement](https://datatracker.ietf.org/meeting/112/materials/slides-112-priv-chair-slides-agenda-01).  A Working Group was [chartered](https://datatracker.ietf.org/wg/ppm/about/) and, at IETF113 in Vienna, we were treated to an incredibly detailed presentation on [Prio](https://eprint.iacr.org/2021/576.pdf), an academic concept for supporting privacy in the context of Internet-scale measurement. Quickly following that presentation was an IETF proposal for a [defined protocol](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/) for *distributed aggregation* of measurement data, based on Prio's core concepts and using a range of cryptographic and system architecture techniques to separate measurements from the identities of the human users being measured. 

Here at IETF114, an alternative proposal was brought forward by [Brave Software](https://brave.com/about/) called [STAR](https://datatracker.ietf.org/doc/html/draft-dss-star).  STAR uses techniques (specifically, distributed [Shamir Secret Sharing](https://www.geeksforgeeks.org/shamirs-secret-sharing-algorithm-cryptography/)) which make the system simpler to build and presents a smaller attack surface for adversaries.  Brave reported that STAR is in production use for some telemetry in the current [Brave browser](https://brave.com/download/).  Several enhancements are planned, among them use of Oblivious HTTP Application Intermediation ([OHAI](https://www.ietf.org/id/draft-ietf-ohai-ohttp-02.html)) to reduce exposure of Brave users' IP addresses when they share telemetry data.


In what is certainly a milestone in the IETF's efforts to have positive impact on user privacy, Apple presented its experience with deploying its *private label* version of the [Privacy Pass protocol](https://datatracker.ietf.org/wg/privacypass/about/) called Private Access Tokens - defined [here](https://www.ietf.org/archive/id/draft-private-access-tokens-01.html) and announced [here](https://developer.apple.com/news/?id=huqjyh7k). Private Access Tokens is a service fully compliant with Type 2 (Publicly Verifiable Basic Tokens) of the Privacy Pas specification, using the Split Origin/Attester/Issuer model and supporting origin-bound or cross-origin tokens.  Apple has also made developer tools available so applications (and not just browsers) can make use of the technology. Importantly, two open source implementations of the Type 2 spec are also available, and several CDN vendors are cooperating in providing test points. See more [here](https://datatracker.ietf.org/meeting/114/materials/slides-114-privacypass-deployment-experience-00).

Significant progress has been made on the protocol's [three base drafts](https://datatracker.ietf.org/meeting/114/materials/slides-114-privacypass-base-drafts-update-00). The success of these drafts might, however, be overtaken by the need to support an important use case - rate limiting.  Rate limiting can be used to subjugate DDoS type attacks and it can also be used to enforce *paywall* type subscription services.  The challenge? Rate limiting necessarily weakens the privacy guarantees that form the basis for Privacy Pass. The Working Group [is debating](https://datatracker.ietf.org/meeting/114/materials/slides-114-privacypass-rate-limited-tokens-slides-v2-00) what sort of damage limitation needs to be applied to this degradation in order to keep the value of the idea strong enough to justify the expense of maintaining it while also encouraging trust in the service by users.  

With the HTTP protocol [long defined](https://httpwg.org/specs/), the [HTTPbis Working Group](https://datatracker.ietf.org/wg/httpbis/charter/) is chartered to maintain and develop the core specifications as well as extensions to the protocol agreed to be generally useful.  To that end, the Working Group heard four new proposals for extension. Important for privacy are [GeoIP](https://datatracker.ietf.org/doc/draft-pauly-httpbis-geoip-hint/) and [HTTP Transport Authentication](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-transport-auth/). 

GeoIP attempts to address the problem of sharing personal location data, but in a manner that doesn't induce harm or threaten privacy.  The author's idea is to support a location *hint*, as an option, on HTTP transactions. They were quickly reminded that IETF has tried to address location privacy for over a decade with nothing to show for it. In the end, however, most participants agreed it was important for IETF to address this area, even if the specific proposal was (tragically?) flawed. 

[HTTP Transport Authentication](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-transport-auth/) has been revived after a long period of dormancy caused by the work on proxying over HTTP/3 (now almost complete).  Impacted by that proxying work as well as many of the new concepts being developed around *oblivious* services (those that don't leak the user's IP address), this proposal has moved away from it's focus on CONNECT tunnel authentication to a proxy server in favor of a general authentication scheme to suit situations in which servers do not want to expose the fact they are hosting authenticated services (*silent* or non-probe-able authentication). The Working Group found the concept useful but asked for a number of editorial changes before they would vote to accept it as a work item.  A technical flaw will need to be addressed as well.
