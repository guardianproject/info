---
title: "The IETF and Internet Freedom"
author: David
categories:
  - Standards
tags:
  - standards development
---

It seems useful to clarify the relationship between the near-term work of keeping the Internet open on a daily basis - work that dominates the efforts of the Internet Freedom community - and the long term work of the industry on crafting operational standards for the same network.

Those involved in Internet Freedom are typically focused on the “problems of today”, creating solutions using existing technologies offering immediate effect.  Often, it’s hard to tell if Internet standards are helping, hurting, or just in the way.  However, looking back at the (roughly) 15-year history of Internet Freedom work, it’s useful to recognize the many times we’ve said to ourselves “*Gosh, I would have done that differently if I’d had a chance to think about it*”.  

The standards bodies offer one mechanism for broad deliberation on what it means to have the opportunity of a universally-accessible Internet.  There’s a lot of time to “*think about it*”, there’s input from many stakeholders and broad involvement in getting the final document -- the standard -- written.   For several years now, members of the Internet Freedom community have been asking themselves if such a process is useful in their context.  It’s easy to imagine, for example, that if the community had spent even a small effort over fifteen years voicing its concerns over, and hopes for, Internet Freedom to the right standards bodies, there might be more … Internet freedom.   We’re testing that theory now, taking part in the activities of the [Internet Engineering Task Force](https://www.ietf.org) (IETF).

## What is the IETF?

Since 1993 the IETF has operated as the standards-development body of the Internet under the auspices of the Internet Society, an international membership-based non-profit organization.  The IETF is the formal successor to similar (but smaller) bodies - based in the United States - that participated in orchestrating and managing the deployment of the Internet after 1981, when the original research project ([ARPANet](https://en.wikipedia.org/wiki/ARPANET)) was expanded into the global scientific community.   The Internet became a fully public entity in the mid-1990s.

The IETF is organized into informal topic-based discussion groups (“birds of a feather”, BoFs) and formal “working groups”. Membership in these groups is open to the public, both for in-person and mailing-list participation.  International participation is encouraged.  The IETF operates, formally, in an inclusive manner and maintains a strict code-of-conduct for its activities that encourages “small voices” to participate.  The IETF operates in a bottom-up manner for idea development and task-creation, largely driven by these groups.  The Internet Architecture Board ([IAB](https://en.wikipedia.org/wiki/Internet_Architecture_Board)) plays a modest role in defining vision and strategy.

[Rough consensus](https://en.wikipedia.org/wiki/Rough_consensus) is the primary basis for decision making. There are no formal voting procedures. An important part of rough consensus is demonstrated interoperability among independently-developed implementations of proposed standards.  Generally speaking, as work moves from “idea” toward “standard”, the act of clarifying the idea is informed by the act of implementing it.  In the early years of the IETF, this approach was unique among standards bodies.

While the details of IETF operations have changed considerably over time, the basic mechanism remains: (1) publication of a proposed specification, (2) development of software based on the proposal, (3) review and independent testing by participants, and (4) republication as a revised proposal, a draft standard, and possible, eventually as an Internet standard. Two types of working document are available: the Internet Draft (generally speaking, the idea) and the Request for Comment (generally speaking, the standard).  It is perhaps a credit to the spirit of iterative improvement through constant testing and discussion that IETF’s completed documents are not titled “Internet Standard”.  

An allied organization within IETF is the Internet Research Task Force ([IRTF](https://irtf.org/)) that promotes longer-term research on the evolution of the Internet.  Made up largely of academic researchers, IRTF operates in a manner that brings cutting edge research into the decision-making processes of IETF activities.

## Who’s Who at IETF?

The modern IETF is composed of technical representatives from commercial vendors, academic researchers, researchers and advocates from non-profit entities and independent “concerned citizens”.   While the IETF’s modern code of conduct makes it possible for anyone to attend a meeting or mailing list and have a voice in the conversation, the IETF remains an “implementation-centric” forum.  That is, “talk is cheap” and ideas have to be implementable - or have impact on implementations - to be considered for standardization.  Thus, individuals and organizations who are successful within IETF are able to both espouse their ideas and “code them up” (or, at minimum, understand the process of coding them and the hard problems that arise from coding them).   Experience shows, however, that these criteria still allow for a broad range of meaningful participation and impact.  

IETF now has the Human Rights Protocol Considerations ([HRPC](https://datatracker.ietf.org/rg/hrpc/about/)) research group (chartered in 2017) monitoring and informing IETF working groups.  HRPC draws its mission directly from RFC 1958 (“Architectural Principles of the Internet”, 1996).  Key participants include both technical people and rights advocates.  

The Internet Architecture Board (IAB) has, as of 2019, given considerable attention to the problem of privacy (as distinct from the IETF’s successful, long-duration work on security).  The Privacy Enhancements and Assessment Research Group ([PEARG](https://datatracker.ietf.org/rg/pearg/about/)) brings important research activities on privacy to the IETF.  

## What are some memorable IETF standards?

The specifications for Internet Protocol (IP, [RFC 791](https://datatracker.ietf.org/doc/html/rfc791) in 1981), Transmission Control Protocol (TCP, [RFC 793](https://datatracker.ietf.org/doc/html/rfc793) in 1981) and Hypertext Transfer Protocol (HTTP, [RFC 1945](https://datatracker.ietf.org/doc/html/rfc1945) in 1996) are the foundation of the modern Internet.  

The most significant update to the foundational protocols is Quick UDP Internet Connections (QUIC, [RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000) in 2016), a new “hybrid” transport protocol informed by the evolved use cases impacting TCP.  

The most significant technical update, in terms of the Internet Freedom community’s interest, was Transport Layer Security Version 1.0 (TLS, [RFC 2246](https://datatracker.ietf.org/doc/html/rfc2246) in 1999) and its improved form, Version 1.1 ([RFC 4346](https://datatracker.ietf.org/doc/html/rfc4346) in 2006).  Two important “Best Current Practice” pieces impacting Internet Freedom are [RFC 7258](https://datatracker.ietf.org/doc/html/rfc7258) “Pervasive Monitoring Is An Attack” and [draft-irtf-hrpc-guidelines-10](https://datatracker.ietf.org/doc/draft-irtf-hrpc-guidelines/) “Guidelines for Human Rights Protocol and Architecture Considerations”.  These works have stimulated a significant portion of IETF's activity on privacy and Internet accessibility.

## Among the current work of IETF, what is most important to the Internet Freedom community?

* TLS 1.3 ([RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446))

The Transmission Control Protocol (TCP) was designed for long-lived connections between clients and servers.  HTTP broke that in a big way and Transport Layer Security (TLS) magnified the problem further, with the two biggest challenges being the lengthy setup (or “handshake”) phase and the negotiation of cryptographic modes and strategies, many of which quickly went out of date.  TLS 1.3 is an effort to mitigate these challenges with so-called Zero-RTT.   More importantly, TLS 1.3 fixes a few security flaws created by wrong assumptions made in earlier designs.  See below.

* [ECH / eSNI](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/) (draft)

Encrypted Client Hello (ECH/ECHo) is successor work to the earlier Encrypted Server Name Identifier (eSNI) effort.  Security requirements evolve as bad actors get smarter.  While the designers of TLS thought they’d made the transport layer “secure” (thus, the name), several omissions were quickly spotted.  Among these was the public visibility of the requested server name (the SNI).  A plan was put forward to encrypt the SNI, but quickly that too became insufficient and a plan was advanced to encrypt the entire “client hello” message - that is, all the data that exists about the attempted connection before the actual encrypted session begins.

ECH/eSNI has its opponents, of course.  TLS 1.3 is already blocked in specific geographies because of this feature.  

* DNS Security ([DoT](https://datatracker.ietf.org/doc/html/rfc7858), [DoH](https://datatracker.ietf.org/doc/html/rfc8484), [DNSSEC](https://datatracker.ietf.org/wg/dnssec/charter/), [Oblivious DNS](https://datatracker.ietf.org/doc/html/draft-pauly-dprive-oblivious-doh-04.html), Private DNS, etc)

A key benefit of the Internet over pre-existing networking techniques was the ability to address servers using human-readable names.  Old-schoolers recognize this was, in fact, a late-arriving component of the Internet protocols and, in some minds, handled in an ill-considered manner.  That skepticism has been borne out in numerous failures of the Domain Name Service (DNS) and, in more recent times, the way in which DNS has been co-opted by national authorities in certain geographies - malicious operators of the DNS can know all the servers/services you visit based solely on the server names you want resolved.

There are many schemes being advanced to improve this situation.  Private DNS abrogates the architected “hierarchy of authority” built into the original DNS (which is the part that’s been broken by malicious providers) and implies “trust Google” or “trust Cloudflare”.  DNSSEC is a collection of small, but meaningful, improvements to the DNS implementation aimed at sealing off the (many) leaks of metadata found in the original DNS design.  DNS-over-HTTP (DoH) and DNS-over-TLS (DoT) provide ways for an individual user’s web browser to select a trustworthy DNS provider (like the Private DNS providers) and ask them to do their lookups over a secure link.  ObliviousDNS could (in theory) remove even the need to have a trusted provider (though it adds the idea of a “trusted proxy”.  A further advantage with ObliviousDNS (and the other “Oblivious” proposals, and the reason for the term) is that the user’s IP address is not leaked either (the bugaboo of most other privacy schemes being proposed in standards bodies).

* [Privacy Pass](https://datatracker.ietf.org/wg/privacypass/about/)

Bots, it seems, have taken over the Internet.  Automated programs submit billions of requests to websites, probing in most cases for weaknesses or purposely attempting to flood the system.  With provision of most web content now in the hands of a tiny number of content delivery networks, those networks put up defenses in the form of “roadblocks” that only humans can cross.  This has become overbearing on some services, to the frustration of users.  One attempted solution is Privacy Pass.  The idea is to provide valid users (who’ve successfully crossed the roadblock once) with a token that can be presented on many future accesses so the roadblock is not in their way again.  A key criteria for this token, however, is that it can not be used to identify and track an individual (human) across their access to many sites served by the content delivery network.  If implemented properly, Privacy Pass could be a big win for users who don’t want their access tracked and monitored.

* Messaging Layer Security ([MLS](https://datatracker.ietf.org/wg/mls/about/))

In short, while secure messaging systems exist, the mechanisms by which they implement security for “group messaging” (greater than 2 parties) are typically divergent from standards, layered in a proprietary way on top of standards, or do not scale to large conversations.  MLS is an activity designed to improve this situation by applying the lessons (good and bad) learned with TLS.  MLS also hopes to achieve what has now been defined as a modern level of security and privacy (thanks to the Signal team who raised the bar quite high).  MLS defines both an architecture and protocol that would standardize the way privacy and security are provided, with room for future upgrade, without denying the individuality of each service and that application-level feature demands of the different user groups.

## What are the limits to IETF’s effectiveness?

We should reject the idea that “the standards process is too slow”.  IETF’s method of working dramatically speeds up the standards process while still allowing for as much disagreement and clarification as required for a standard to be considered “deliberative”.  Further, the end result of IETF standardization is not only a descriptive document, but multiple interoperable implementations of that document’s standard.  Again, that’s another big difference between IETF and the strictly “declarative” standards bodies.  With few exceptions, IETF has avoided the problems of too-early standardization based on a fad or a reaction, while still being responsive to perceived needs - be they technical or social/cultural.

There is, however, the Hammer/Nail analogy: when you’re a hammer, everything looks like a nail.  The IETF solves problems using the Internet infrastructure, even when certain problems might be better solved elsewhere, or in ways that are not infrastructural.
 
## What is the most important problem (to Internet Freedom) facing IETF today?

There appears to be broad agreement that the most important problem facing the IETF is “The Problem of Centralization”.  

Centralization initially arose in the hardware sense as the mesh of routers that connect the Internet fell into fewer and fewer hands.  This happened “innocently”, over time, and in the name of cost efficiency.  But this slow change violated one of the fundamental design strengths of the Internet’s original core architecture: resilience.  In recent times, there has been a strong tendency for nation-states to acquire tight control over the gateway routers that allow traffic into and out of their geographic area, further decreasing the resiliency of the Internet and serving as a vehicle for censorship and mass surveillance. 

This problem has been further complicated and accelerated by the development of data centers of unimagined scale and worldwide presence whose internal operations are largely opaque and filled with “middle boxes” performing specialized tasks.  Unfortunately, the presence of these “middle boxes” can slow the pace of technological change.

Lastly, and mostly unimagined at the dawn of the Internet, a small set of application software service providers has come to dominate Internet traffic and exercise an oversized amount of influence on the way users perceive the Internet or are allowed access to its resources.  

The problem of centralization is magnified at IETF due to the organization’s inherent nature of “defining the Internet”.  Its solutions are “large scale” and large scale solutions by definition fall into the hands of the largest organizations.  Thus, it can sometimes seem that the IETF has moved far from the founding principles of decentralized, decoupled, cooperative, associative solutions that characterized the original Internet.

However, sometimes it takes a pendulum-swing of the magnitude we now see to drive people to action.  And, by nature, IETF has a constantly-evolving but actively-engaged community.  The “big names” of thirty years ago have significantly less presence today.  There is hope, thus, that a new community of people who care about the problem of centralization will rise up to make their voices heard.  Indeed, there are signs this is already happening. 

Formally, the IRTF’s [Decentralized Internet Infrastructure Research Group]()https://datatracker.ietf.org/rg/dinrg/history/ was chartered in September 2017 to address the interest of infrastructure centralization.  Parallel (and in a way orthogonal) advancements in blockchain technology, distributed hash tables and decentralized cryptographic authority are creating what is effectively an “overlay network” on top of the Internet as defined by the IETF.  Colloquially, it’s being called [Web 3.0](https://www.forbes.com/sites/forbestechcouncil/2020/01/06/what-is-web-3-0/?sh=4002a4bc58df).  These activities have forced IETF to take notice. 

## What’s next in our IETF participation?

Monitoring IETF activities - bringing that knowledge to the teams doing current-term Internet Freedom work - and presenting the current-term work of the Internet Freedom community to the IETF - has begun to bear fruit in terms of synergy between the two approaches to keeping the Internet open.  Discussion, however, will probably not be enough.  

Another important way the community might participate is active (and early) involvement in the implementation of important IETF proposals.  Doing so would give the Internet Freedom community a “seat at the table” where core problems and concerns arise and where key decisions are made.   The Internet Freedom community brings extensive expertise in open source software development, a counterpoint to the mostly closed-source implementations undertaken by the IETF’s vendor organizations.  The benefits of transparency and loosely-coupled cooperation - so key to the most successful software projects that built the Internet - are difficult to overstate in this context.

Certain of these efforts are already underway - ECH, and specifically the [DEfO](https://defo.ie) project, is an example - and the impact this is having on key pieces of “infrastructural” open source software (the Apache web server, the OpenSSL security layer, for example) is important.  Keeping open source software current and “in tune” with developing standards may be the best way to “square the circle” of Internet freedom work -- assuring that solutions to the problems and challenges of today lead to the creation of a better Internet for the future.
