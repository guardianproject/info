---
title: "IETF116 Conference Report: Wednesday March 29, 2023"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day Three of the [116th IETF meeting](https://www.ietf.org/how/meetings/116/) in Yokohama Japan.  For the rundown on Day Two, see my [daily report](https://guardianproject.info/2023/03/29/ietf116-conference-report-tuesday-march-29-2023/).*

The long-running work on [MASQUE](https://datatracker.ietf.org/wg/masque/about/) - proxying all network-layer datatypes over QUIC (HTTP/3) - is nearing completion, with the specification for [Proxying IP in HTTP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip/) in IESG review.  With these components in place, the [original MASQUE concept](https://datatracker.ietf.org/doc/draft-schinazi-masque-proxy/) - a non-probable relay for client traffic providing privacy guarantees - has been revived, now defined within the new framework and leveraging [HTTP Unprompted Authentication](https://www.ietf.org/archive/id/draft-ietf-httpbis-unprompted-auth-02.html).

Privacy-preserving measurement is much on the minds of IETF attendees as the [Privacy Preserving Measurement Working Group](https://datatracker.ietf.org/wg/ppm/about/) continues to make progress.  Two new concepts were debuted in the Privacy Enhancements and Assessments Research Group [PEARG](https://datatracker.ietf.org/rg/pearg/about/) meeting: [Secure Partitioning Protocols](https://datatracker.ietf.org/meeting/116/materials/slides-116-pearg-secure-partitioning-protocols) and [Interoperable Private Attribution](https://datatracker.ietf.org/meeting/116/materials/slides-116-pearg-ipa). Partitioning is new work looking at how multi-party statistical aggregation can be efficiently accomplished with improved privacy guarantees and is applicable to the on-going work on the Distributed Aggregation Protocol [DAP](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/).  [Private attribution](https://datatracker.ietf.org/meeting/116/materials/slides-116-pearg-ipa) measures events that occur in different contexts to the same person (shown an ad, then bought the product, for example).  As a sort of counterpoint, PEARG attendees also heard about the design decisions made in the development of a [privacy-preserving contact tracing application](https://datatracker.ietf.org/meeting/116/materials/slides-116-pearg-dp3t-deploying-decentralized-privacy-preserving-contact-tracing) rolled out during the recent COVID-19 pandemic. Perhaps the defining characteristic of the design of this app was *purpose limitation* - building out features that specifically *can not* be used for any other purpose (such is the wide-spread fear of these applications being used as the infrastructure of a much more broader system of social control).