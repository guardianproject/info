---
title: "IETF119 Conference Report: Monday March 18, 2024"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*It's Opening Day of the [119th IETF meeting](https://www.ietf.org/how/meetings/119/) in Brisbane Australia.  This post commences a daily rundown of privacy and Internet Freedom activities at this IETF meeting. For the rundown on IETF119 Hackathon, see my [Hackathon report](https://guardianproject.info/2024/03/17/ietf119-hackathon-report/)*

## Dispatch

IETF meetings don't often kick off with the open dispatch but this time it happened. Dispatch sessions are meant to help specification authors find a home for their work if a home isn't obvious. There are two classes of dispatch request: 

+ Smaller items that have been spun off from mature work.  A good example is when a specification has a component that needs a formal record-type declaration.
+ New work, possibly not yet well-defined, where the authors themselves haven't a clue where it belongs. This is somewhat rarer because IETF offers several mechanisms for new work to develop interest and work its way into the formal process. 

We got some of both this time. Unfortunately, the one that needs the most work is in the latter category and brought to IETF by a privacy-focused team.  I need to write a separate post with a crisp definition of a better method for achieving success at the IETF because we can't make headway until hyptothetical participants learn from past mistakes (including my own).

## CFRG

There has a frightening amount of new cryptography coming into the IETF over the last three to five years, driving by privacy-preserving measurement, quantum computing and the endless search for better performance.  Most of it entires IETF through the Cryptography Forum Research Group. It stikes me that this space is moving very quickly and I'm concerned we're baking mistakes into Internet protocols in a way that will be hard to retrieve in the future.

## OHTTP

The Oblivious HTTP Application Intermediation (OHAI) Working Group has brought its key draft - [Oblivious HTTP](https://datatracker.ietf.org/doc/draft-ietf-ohai-ohttp/10/) to RFC status as of January 25, 2024 ([RFC9458](https://datatracker.ietf.org/doc/rfc9458/)). This was a focused effort, well-managed by the [Working Group](https://datatracker.ietf.org/wg/ohai/about/) chairs.

The Working Group remains in place to tackle future items that arise from the early deployments. Better handling of large data transactions is the first such item, giving rise to a new specification for [Chunked Oblivious HTTP Messages](https://datatracker.ietf.org/doc/draft-ietf-ohai-chunked-ohttp/). 

## Hackathon Demo

I presented the results from our interoperability testing on the [The HTTP Signature Authentication Scheme](https://datatracker.ietf.org/doc/draft-ietf-httpbis-unprompted-auth/) to the wider IETF attendee audience at the Hackathon Demo event and felt lucky to have six people show interest (the competition being free food nearby).  