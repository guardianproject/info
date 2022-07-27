---
title: "IETF114 Conference Report: Tuesday July 26, 2022"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day Two of the [114th IETF meeting](https://www.ietf.org/how/meetings/114/) in Philadelphia USA. For the rundown on Day One, see my [daily report](https://guardianproject.info/2022/07/25/ietf114-conference-report-monday-july-25-2022/).*

Lucas Pardue, of Cloudflare and co-chair of the QUIC Working Group, gave a not-so-tongue-in-cheek [talk](https://datatracker.ietf.org/meeting/114/materials/slides-114-anrw-sessa-keynote-00) about the breakdown of the OSI layering model of the Internet. His focus was on the *top* of the stack, illustrating handsomely what QUIC and HTTP/3 have done (unknowingly to most) to our perception of layers.  A key challenge: tools for HTTP/1 are widely available and the protocol and its impacts are widely understood.  HTTP/2 and HTTP/3? Not so much (both are binary, not text-based, protocols).  Yet, here in mid-2022, the world of the Internet is predominantly (91%!) HTTP/2 and HTTP/3 traffic.  Similarly, TLS/1.3 and QUIC represent 87% of traffic. And many of the now-being-standardized protocols for privacy insert several layers of proxy into every transaction. From a *sound knowledge* perspective, we seem to have taken a rather quick, and rather deep, step backwards.

The [OHAI Working Group](https://datatracker.ietf.org/wg/ohai/about/) has brought the core draft of [Oblivious HTTP Application Intermediation](https://datatracker.ietf.org/doc/draft-ietf-ohai-ohttp/) nearly to Working Group Last Call (technical finalization). With multiple interoperable implementations said to exist, this bodes well for rapid completion and standardization. The twistingly-worded name engenders confusion (or distain) but the goal is laudable: make the requester's IP address private in any *transactional* HTTP-based protocol. Transactional protocols include DNS and Online Certification Status Protocol. But the dominant imagined use case is *telemetry* - monitoring vendor-, application- or operating system-define usage parameters on centralized systems. A few holes remain, however, for services that do not want (or need) to be tightly-coupled (systems that are not, for example, an operating system's fault reporting service).
