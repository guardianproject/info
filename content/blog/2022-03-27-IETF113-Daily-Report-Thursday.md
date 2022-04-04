---
title: IETF113 Conference Report: Thursday March 24, 2022

author: David

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

Day four of the 113th IETF meeting, in Vienna Austria. 

[Privacy Pass](https://datatracker.ietf.org/group/privacypass/about/) - originating at Cloudflare in 2017 as a solution to user frustration with CAPTCHA - has been in full swing as an IETF activity since mid-2020.  Privacy Pass allows a client to solve some form of validity check (a CAPTCHA, a puzzle, a user-pass authentication) to then receive some number of tokens to be used at websites accepting Privacy Pass, thus eliminating the need to do a CAPTCHA at each site.  Sites hosted on large CDNs like Cloudflare benefit (Cloudflare provides the service for them) and users get a more convenient experience.  Users accessing the Internet through Tor are even more positively affected since they are most prone to CAPTCHA.  Privacy Pass is now in Version 3 and working to support a multi-issuer environment to provide another uplift to the user experience (tokens can be validated across issuers).  Just prior to this IETF meeting, a standardized mechanism for exchanging Privacy Pass tokens was adopted by the Working Group - [The Privacy Pass HTTP Authentication Scheme](https://datatracker.ietf.org/doc/draft-ietf-privacypass-auth-scheme/). Both request and response mechanisms are provided so that use of (or demand for) the token can be either server- or client-initiated. Going forward, it will be interesting to see if Privacy Pass benefits mostly the web browsing environment or finds its way into applications using HTTP as a substrate for richer styles of interaction.  

It's important to point out that Privacy Pass, in practice, requires relatively-centralized infrastructure (issuers, who grant and redeem tokens).  In fact, the mathematics behind the multi-issuer capability in Version 3 requires that the number of issuers is limited to avoid users being de-anonymized too easily.  A more complete discussion of centralization and Privacy Pass is available [here](https://datatracker.ietf.org/doc/html/draft-mcfadden-pp-centralization-problem-01).  IETF members have, for some years now, expressed concern about increasing centralization - not only of Internet hardware (which the work of IETF can not in practice impact) but also of the  protocol designs themselves. The Internet Architecture Board has, during its recent Open Meetings, taken on the weight of this discussion, providing a forum for both studies of, and individual views on, the topic.  A formal statement from the group, though, has been harder to achieve.  As an alternative, individual voices have been encouraged, the most recent being former IAB member [Mark Nottingham](https://datatracker.ietf.org/person/Mark%20Nottingham) who has produced [*Centralization and Internet Standards*](https://datatracker.ietf.org/doc/draft-nottingham-avoiding-internet-centralization/) that tries to define the problem in ways that can eventually be addressed within the IETF.  

Though it seems like very early days here, I'm encouraged both that discussions are vocal and pubic, and that more *human-centric* voices are now present at IETF who have been working *within the system* to provide tools and guidelines that can inform protocol design in ways that maybe, just maybe, will pull us back from the edge.


