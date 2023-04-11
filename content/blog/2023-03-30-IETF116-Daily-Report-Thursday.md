---
title: "IETF116 Conference Report: Thursday March 30, 2023"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day Four of the [116th IETF meeting](https://www.ietf.org/how/meetings/116/) in Yokohama Japan.  For the rundown on Day Three, see my [daily report](https://guardianproject.info/2023/03/30/ietf116-conference-report-wednesday-march-29-2023/).*

The IETF is getting serious about interoperability among messaging services ([this](https://www.eff.org/deeplinks/2022/04/eu-digital-markets-acts-interoperability-rule-addresses-important-need-raises) might have had something to do with it).  The charter for the Messaging Layer Security Working Group (MLS) specifically *excluded* interoperability, though the group organized a draft that addressed the basic concepts that would allow MLS-compatible systems to federate. In early 2023, a new Working Group - More Instant Messaging Interoperability ([MIMI](https://datatracker.ietf.org/group/mimi/about/)) - was chartered to expand on the MLS federation work.  Given IETF's relatively long and somewhat checkered history with messaging, the Working Group's charter included this reminder to itself:

```
Numerous prior attempts have been made to address messaging interoperability, including the IETF's extensive prior work on XMPP, SIP/SIMPLE, and their related messaging formats. The MIMI working group will draw lessons from these prior attempts, seek to avoid re-hashing old debates, and will focus on the minimal standards suite necessary to facilitate interoperability given the feature set of modern messaging applications.
```

Thus, its remit had some strict limits:

```
The More Instant Messaging Interoperability (MIMI) working group will specify the minimal set of mechanisms required to make modern Internet messaging services interoperable. 
```

...*minimum* being the operative word. So, what's *in scope*?

- messaging interoperability
- user discovery
- messaging content format
- (an appropriate) MLS profile
- message delivery service and transport mechanisms
- establishment of end-to-end cryptographic identity
- identifier naming conventions

Specifically *out of scope* are:

- metadata processing to manage spam and abuse
- interoperable mechanisms for group administration or moderation across systems
- extensions to the MLS protocol (if needed, requirements will be referred to the MLS working group or other relevant working groups in the security area)
- definition of completely new identity formats or protocols
- extensions to SIP, SDP, MSRP, or WebRTC
- development of anti-spam or anti-abuse algorithms
- *oracle* or look-up services that reveal the list of messaging services associated with a given user identity without the user's permission

This being the first formal meeting after group charter, discussions are still at the stage where defining what *in scope* means is still open, as are the most basic tenets of the technical mechanisms to implement the required features.  Grab your popcorn!