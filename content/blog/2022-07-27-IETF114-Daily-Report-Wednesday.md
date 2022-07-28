---
title: "IETF114 Conference Report: Wednesday July 27, 2022"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day Three of the [114th IETF meeting](https://www.ietf.org/how/meetings/114/) in Philadelphia USA. For the rundown on Day Two, see my [daily report](https://guardianproject.info/2022/07/26/ietf114-conference-report-tuesday-july-26-2022/).

Interest is starting to consolidate on the need for additional definition for serving media over the QUIC transport layer, particularly for streaming and conferencing applications.  Following an informal gathering at IETF113 in March 2022, a formal Birds of Feather session met today with a draft [charter proposal](https://datatracker.ietf.org/meeting/114/materials/slides-114-moq-moq-charter-proposal-00) and two draft documents describing the intended [use cases](https://www.ietf.org/id/draft-gruessing-moq-requirements-02.html) and a [protocol](https://www.ietf.org/id/draft-jennings-moq-quicr-proto-01.html). [Here's](https://datatracker.ietf.org/meeting/114/materials/slides-114-moq-if-time-permits-quicr-01) a more visual overview.  There was broad concensus (at this well-attended session) as to the need for this work, but a split between one camp that sought a much narrower set of use cases (not wanting to *boil the Internet* as it were) and another who wanted to *solve this problem once*. This will be addressed as the BoF leaders work towards a vote on chartering the effort.  Either way, this is substantial work ahead.  I mention this here not so much in the realm of privacy as to look towards a future where QUIC's efficiency and scalability benefits might make media-rich services available to those of lesser economic means or with mediocre connectivity.

Directly related to our interests in privacy and a free and open Internet, the MASQUE Working Group presented the status of what will be the last of its core specifications, [CONNECT-IP](https://www.ietf.org/archive/id/draft-kuehlewind-masque-connect-ip-01.html).  With implementations ready for interoperability testing, the protocol definition is being scrubbed for [burning issues](https://github.com/ietf-wg-masque/draft-ietf-masque-connect-ip/issues). Of these, some headway was made at the meeting, though all are still officially under discussion.  

Recall the challenges with actual interoperability testing with CONNECT-IP at the Hackathon last weekend (see [report](https://guardianproject.info/2022/07/24/ietf114-hackathon-report-sunday-july-24-2022/))?  With spec definition work almost complete, the Working Group's mission will also be complete and, officially, put the group in a position to disband.  But those interoperability challenges provide the next raison d'être for continuation and, with five proposals already before the group, concensus was that the group leaders should move forward with re-chartering with a new mission which - at least by concensus of those present - will focus on assuring MASQUE is deployable in real-world scenarios. With CONNECT-IP lowest in the protocol stack individual vendors and implementors face vastly different integration scenarios and, in many cases, with quite different teams who have (historically) faced divergent requirements. That said, the demand for proxying IP over QUIC is already huge, with both major mobile device vendors lining up extensive services for their platforms using the MASQUE model.  IETF's implementation-checks-definition model is well-suited to this sort of aggressive development, thankfully.
