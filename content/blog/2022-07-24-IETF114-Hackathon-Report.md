---
title: "IETF114 Hackathon Report: Sunday July 24, 2022"

author: David

categories:
   - Standards

tags:
   - MASQUE
   - standards development
   - IETF
   - privacy
---

*This post begins a daily blog, live from the 114th meeting of the [Internet Engineering Task Force](https://www.ietf.org/how/meetings/114/) in Philadelpha Pennsylvania USA, July 23-29, 2022 (in-person meetings having restarted in March 2022 after the COVID pandemic abated). We're focusing on standards activities of importance to the Internet Freedom community.*

The [Hackathon](https://www.ietf.org/how/runningcode/hackathons/114-hackathon/) event kicks off each IETF event, with projects that run the gamut from early implementations of just-emerging specifications to full multi-vendor interoperability testing of nearly-mature protocols. At this event, I sat in on the [MASQUE](https://datatracker.ietf.org/wg/masque/about/) team's effort to commence work on the new [CONNECT-IP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip/) specification. With the recent completion of two key specifications -  [CONNECT-UDP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp/) and [H3 Datagrams](https://datatracker.ietf.org/doc/draft-ietf-masque-h3-datagram/) - MASQUE has become IETF's solution for proxying all types of network traffic over QUIC and HTTP/3, including VPN and other privacy-focused scenarios. CONNECT-IP will complete the trio.  But this initial effort didn't go well.  Google and Ericcson (co-authors on the spec) had brought teams who, indeed, implemented the key protocol elements of CONNECT-IP live and in-the-moment but were both stymied setting up testbeds that could deliver raw IP packets for routing by this new code. Wait, you might say, aren't these network engineers?  True, but it was mostly the practicalities that got in the way - only laptops as test machines, working from the open source [QUICHE](https://github.com/google/quiche) repository on a machine that also hosts an environment for building production code, even deciding what sort of packets could be used for testing and where to route them. These are the frustrations of a first-ever effort.  

Other teams had much better luck even if they are not specifically focused on privacy.  Fourteen vendors worked together on the first interoperabiltiy test of *Low Loss Low Latency Scalable Throughput*, [L4S](https://www.ietf.org/archive/id/draft-ietf-tsvwg-l4s-arch-12.html), an ambitious effort that was ultimately successful (that is, both at functioning at all and producing excellent results). Another team working on the Drone Remote ID Protocol [DRIP](https://datatracker.ietf.org/wg/drip/about/) were also successful - despite the lack of hackable drones or access to the key server software this protocol will eventually have to interoperate with -- and produced the first working demonstration of DRIP's session registration protocol (which, it happens, involves almost all aspects of the proposed standard).  These two projects will surely be the hits of the upcoming Hackdemo Happy Hour!

With the Hackathon complete, IETF turns to the serious business of creating new specifications.  This week's meeting will see working sessions on [Oblivious HTTP Application Intermediation](https://datatracker.ietf.org/group/ohai/about/), [Privacy Pass](https://datatracker.ietf.org/wg/privacypass/about/), [Messaging Layer Security](https://datatracker.ietf.org/wg/mls/charter/) and [Privacy Preserving Measurement](https://datatracker.ietf.org/wg/ppm/about/) in addition to emerging ideas from the Internet Research Task Force's [Privacy Enhancements and Assessments Research Group](https://datatracker.ietf.org/doc/charter-irtf-pearg/).  And MASQUE, where we'll have some explaining to do about our Hackathon gaff.
