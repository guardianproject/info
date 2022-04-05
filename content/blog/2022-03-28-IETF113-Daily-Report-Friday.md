---
title: "IETF113 Conference Report: Friday March 25, 2022"

author: David

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

Final day of the 113th IETF meeting, in Vienna Austria. 

The IETF is looking to make a clear contribution to the problem of hyper-aggressive measurement of user activities on the Internet and the many misuses thereof.  To do so, the IETF recognizes that some measurement is important but that many desirable measurements require data most people consider sensitive.  It also recognizes that aggregated measurements often provide the most value, rather than individual ones.  Yet, today, parties interested in measurement need to collect and store individual records in order to aggregate them, exposing themselves to potential violations of their privacy agreements with users (or governments) and to theft of that data by outsiders.  Instead, IETF is looking at ways this aggregation can be managed in ways that protect user privacy while still providing much of the statistical power needed.  The [Privacy Preserving Measurement Working Group](https://datatracker.ietf.org/group/ppm/about/) has formed.

The IETF's effort centers around new cryptographic techniques that allow an intermediary aggregation service to aggregate measurements in a variety of ways *without* learning the individual values themselves, then passing that aggregated information along to *collectors* (organizations that use the measurements).  The protocol design will include mechanisms for:

- Safe submission of individual measurements by the client (potentially including proof of validity)
- Verification of such validity proofs at the *aggregator* when provided by the client
- Computation of aggregates at the *aggregator*
- Reporting of results to the *collector* without leaking the individual measurements

The Working Group is chartered to deliver one or more protocols that can accommodate multiple privacy-preserving algorithms as necessary.  Two such algorithms are already under consideration - one based on [Prio](https://educatedguesswork.org/posts/ppm-prio/) ([Draft](https://datatracker.ietf.org/doc/draft-gpew-priv-ppm/)), the other based on [STAR](https://www.ietf.org/staging/draft-dss-star-00.html). The protocol(s) will be designed to limit abuse by both clients and servers (aggregation servers, collector servers), including exposure of individual user measurements and denial of service attacks. 

While this work has the character of *seeming* appropriate and necessary, there are many aspects to consider - just in the protocol design, let alone the social and policy implications - that caused attendees to say, to the effect, "*I'm leaving here more confused than when I entered*".  The unique trust model implied, the increased centralization implied, the completeness of the approach (that is, how much measurement it subsumes), the alignment with laws and agreements already in place, the pragmatics around what organizations can run such a service - these are questions yet unaddressed.  But at least now IETF has a solid stake in the ground from which to move forward.  




   
   
   
   
   

