---
title: "IETF116 Conference Report: Monday March 27, 2023"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - privacy-preserving measurement
   - IETF
   - privacy
---

*This post begins a daily blog, live from the 116th meeting of the [Internet Engineering Task Force](https://www.ietf.org/how/meetings/116/) in Yokohama, Japan, March 25-31, 2023.  We're focusing on standards activities of importance to the Internet Freedom community.*

Since IETF114 ([report](https://guardianproject.info/2022/07/28/ietf114-conference-report-thursday-july-28-2022/)), the [Privacy Preserving Measurement Working Group](https://datatracker.ietf.org/wg/ppm/about/) has been deliberating over two distinct proposals offering very different technical methodologies for undertaking measurement activities while respecting user privacy. [STAR](https://datatracker.ietf.org/doc/html/draft-dss-star) offers an approach called *k-anonymity* - reporting a measurement value only if *k* or more parties are also reporting the same value. This approach theoretically prevents rare values being used to single-out individuals.  Distributed Aggregation Protocol, [DAP](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/), uses an approach that distributes individual measures across a set of aggregators, none of which gets to see all the granular measurement data - the fully-aggregated total only seen by the third-party who requested it (who, in turn, gets to see none of the granular measurements).  At IETF116 we're learning about the operational experience with these technologies, with multiple implementations of both running in different testbeds.  [Performance analysis](https://datatracker.ietf.org/meeting/116/materials/slides-116-ppm-poplarstar-measurements) has also been undertaken.

Though it's very early days, it's becoming clear that both approaches have had to make operational modifications (based on privacy vulnerabilities or performance or security) that seem to *decrease* their uniqueness and call into question the need to have two approaches.  Both approaches, for example, are considering adding *differential privacy* features.  Operationally, STAR performs best when *k* is within the range 10-100 and it is being argued that such a range is insufficient for Internet-scale use cases.  Operationally, DAP can benefit from a more distributed computation model (using *helpers*) but this is offset by performance loss due to the volume of network traffic generated.  DAP is already at a performance deficit compared to STAR, partially because it handles the negative impact of malicious clients (those that purposely submit erroneous values).  Will we see a unified approach in the future?  I sense there's a long way to go here.

The concept of *web filtering* - raised initially at IETF115 - was again discussed in a side meeting hosted by the [Internet Watch Foundation](https://www.iwf.org.uk) who are focused on combating child abuse, trafficking and exploitation, a problem they say is exacerbated by the distribution of specific types of content on the Internet. IWF is raising this problem within the IETF in hope of a technical solution to finding and removing the types of content that encourage, they say, these behaviors.  This problem area strikes at the heart of the design of the Internet which, at its core, is *content-neutral*.  Perhaps more importantly, there is significant concern that tools developed to suit this particular use case could be easily adapted to induce censorship of less well-defined content and for less-altruistic purposes.  