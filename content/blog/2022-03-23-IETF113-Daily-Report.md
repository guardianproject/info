---
title: IETF113 Conference Report: Wednesday March 23, 2022

author: David

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

Day three of the 113th IETF meeting, in Vienna Austria.  


Messaging Layer Security ([MLS](https://datatracker.ietf.org/wg/mls/about/)) is (finally) closing in on [Last Call](https://www.ietf.org/about/glossary/?query=wglc) at protocol Draft 14 and architecture Draft 7 (which will be taken forward together). Sometimes referred to as the *TLS for messaging systems*, Messaging Layer Security creates a uniform secure group discussion protocol, scalable to very large groups and providing similarly uniform security guarantees across providers. The near completion of the architecture and protocol drafts, and commencement of interoperability testing has prompted the Working Group to dust off the [Federation draft](https://datatracker.ietf.org/doc/html/draft-ietf-mls-federation) as the next object of their affection.  Will I be able to connect my [Wire](https://wire.com/en/) client to the [Facebook Messenger](https://www.messenger.com/) server? Don't hold your breath, but in the meantime you'll be able to enjoy the manifest benefits of secure group chat (with security guarantees as high as the industry knows how to produce) on your own network.

Oblivious HTTP Application Intermediation ([OHAI](https://datatracker.ietf.org/wg/ohai/charter/)) is another in the suite of new designs aimed at reducing misuse of the client's IP address.  OHAI is complementary to [MASQUE](https://datatracker.ietf.org/wg/masque/about/) - the former focused on *transactional* service protocols like DNS and [OCSP](https://datatracker.ietf.org/doc/rfc8954/) queries, the latter on fully bi-directional interactive exchanges.  Like MASQUE, proxies are involved (between requester and request destination) and in both cases the client (user) has to trust the proxy.  However, in the case of bad-actor clients, it is imagined that the proxy will want to communicate on a side channel with its counterpart to stop things like reply attacks or other mischief via *shadow banning*.  This, however, raises the spectre of collusion among the intermediaries - something OHAI was initially defined to avoid.  There seems to be significant effort remaining on this proposal.

As mentioned in the prior post, the Human Rights Protocol Considerations([HRPC](https://sandbox-ng.ietf.org/group/hrpc/documents/)) Research Group considered a new Individual Contribution on [Regional Internet Blocking Considerations](https://datatracker.ietf.org/doc/draft-giuliano-blocking-considerations/). While the current geopolitical environment was the impetus for this work, the content isn't specific to a particular event. Rather, it catalogs - for policy makers - the technical mechanisms available to *withdraw* geographic areas from connection to the global network, effectively *de-mystifying* the concept.  Also via HRPC, the IETF got its first look at the idea of *content provenance* in the work of the [Coalition for Content Provenance and Authenticity](https://c2pa.org) and their efforts to create [specifications](https://c2pa.org/specifications/specifications/1.0/specs/C2PA_Specification.html) around this idea.  Guardian Project's pioneering [ProofMode](https://proofmode.org/about) work got a shout out!  Of special importance here, and perhaps more significance to IETF than the *data at rest* work of the specification itself, are its generally-applicable definitions in the area of *Harms Modelling*, readapted from work by [Microsoft](https://docs.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/harms-modeling/). This concept is core to HRPC's research mission as defined in [rfc8280](https://datatracker.ietf.org/doc/html/rfc8280) and this is the most rigor I've seen in defining the concept in ways that can have protocol impact. 

 
