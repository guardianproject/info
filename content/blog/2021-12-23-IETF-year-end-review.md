---
title: "IETF: Year End Review 2021"
author: David
categories:
  - Standards
tags:
  - standards development
  - IETF
---

In terms of potential impact on Internet Freedom, it’s been a banner year at the Internet Engineering Task Force [(IETF)](https://ietf.org/).  [QUIC](https://datatracker.ietf.org/doc/rfc9000/) (featuring the improved privacy and security of [TLS1.3](https://datatracker.ietf.org/doc/html/rfc8446)) reached Proposed Standard status, with implementations and rollouts from every major vendor on both server and client, and with multiple [open source toolkit options](https://en.wikipedia.org/wiki/QUIC#Source_Code) for developers.  [Encrypted Client Hello](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/) for TLS1.3 gained traction via the [DEfO project](https://defo.ie) that, through pull requests, makes a huge privacy enhancement easily available to the major security library (OpenSSL) underpinning the Internet’s most important service engines (nginx, apache, lighttpd, haproxy on the server, even curl on the client).  IP address privacy got new attention with a working group formed around Oblivious HTTP Application Intermediation ([OHAI](https://datatracker.ietf.org/doc/charter-ietf-ohai/)), as did Privacy-Preserving Measurement ([PPM](https://datatracker.ietf.org/doc/bofreq-privacy-preserving-measurement/)) which seeks to drastically reduce the amount of personal information swept up in the pervasive monitoring of all public Internet activity.  Meanwhile, the Internet Research Task Force ([IRTF](https://irtf.org)) has focused on developing new cryptographic techniques to serve these rapidly-evolving privacy-focused activities. IRTF also fosters work on truly-global Internet access and, in a sense, serves as the IETF’s conscience through it’s work on the [human rights implications of protocol design](https://datatracker.ietf.org/rg/hrpc/about/).  


Yet, it’s valid to ask: will the Internet be more free when/if these proposals become widely-deployed standards? While there’s sound reason for hope, I see two major concerns that could significantly reduce the positive impact of this work.


The first concern is extreme pushback from the major state actors who want more control over how their citizens use the Internet.  While QUIC, TLS1.3 and ECH appear to be headed for full adoption in regions where the Internet is already nominally free, they amount to a [royal flush](https://www.poker.org/poker-hands-ranking-chart/) for the good guys in the regions where it is not. The reaction? Stop playing the game (the major state actors have already blocked QUIC).  What’s going to be the reaction when ECH makes ubiquitous domain-fronting possible?  Will that just increase the number of states participating in blocking QUIC?  It’s important to remember, state actors [have options](https://www.huawei.com/us/technology-insights/industry-insights/innovation/new-ip).


The second concern is centralization.  The Internet has gotten more centralized over time, both in the way the breadth of its content is hosted and in the number of services users visit to view that content.  Further, national gateways have seen massive consolidation in the last five years as most states reduce exposure in the name of terrorism prevention and reducing the flow of disinformation.  This centralization has worsened the [pervasive monitoring](https://datatracker.ietf.org/doc/rfc7258/) all users suffer under and has made it difficult (at best) to trust service providers with even the most benign-seeming of our personal data. Yet, the privacy solutions under development at IETF - OHAI and PPM, along with [Privacy Pass](https://datatracker.ietf.org/wg/privacypass/about/) and others - all rely on layers of new infrastructure operated by these same providers, seeming to require us to put even more trust in them.  Directionally, is that sustainable?  It’s important to remember, we users also [have options](https://permission.io/blog/web-3-0/).


During 2022, I’ll be looking more critically at how IETF addresses these concerns. IETF continues to be the most open and responsive standards organization determining the Internet’s future.  It feels like we’re reaching a point where Internet Freedom isn’t any longer a niche interest, but rather the central focus of progress for mankind in terms of our intercommunication as citizens of the planet. The best option would seem to be an IETF at the forefront of that progress.
