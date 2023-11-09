---
title: "IETF116 Conference Report: Tuesday March 28, 2023"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
   - OpenSSL
---

*Day Two of the [116th IETF meeting](https://www.ietf.org/how/meetings/116/) in Yokohama Japan.  For the rundown on Day One, see my [daily report](https://guardianproject.info/2023/03/28/ietf116-conference-report-monday-march-28-2023/).*

The [OHAI Working Group](https://datatracker.ietf.org/wg/ohai/about/) has submitted the core draft of [Oblivious HTTP Application Intermediation](https://datatracker.ietf.org/doc/draft-ietf-ohai-ohttp/) to the RFC Editor for editorial finalization and publication. OHAI is designed to support *transational* uses of the HTTP protocol that seek IP address privacy (by means of a relay pair, one associated with the client and one associated with the target resource). The target resource is, thus, said to be *oblivious* to the requester's IP address.  While the initially-imagined use case for OHAI was access to the DNS service (with some in the IETF feeling DNS-over-HTTP did not go far enough to protect user privacy), the dominant  use case imagined today is *telemetry* - monitoring vendor-, application- or operating system-defined usage parameters on centralized systems. 

It's fair to ask how OHAI-capable services are to be discovered.  The OHAI Working Group is proposing to use DNS *Service Binding Records* (SVCB, defined [here](https://datatracker.ietf.org/doc/draft-ietf-dnsop-svcb-https/) and well-described [here](https://www.sobyte.net/post/2022-01/dns-svcb-https/)). TLS 1.3 Encrypted Client Hello is among the other IETF standards leveraging SVCB.  SVCB records, similar to the (also new) HTTPS records, allow a host of define multiple ways to make connection with parameterization using just the DNS lookup (as opposed to the multiple round-trip mechanism of HTTP's Alt-Svc header).  The draft - [Discovery of Oblivious Services via Service Binding Records](https://datatracker.ietf.org/doc/draft-ietf-ohai-svcb-config/) has been under Working Group discussion since IETF113 and is close to submission for last call (technical completion). 

Speaking of [TLS 1.3](https://datatracker.ietf.org/doc/rfc8446/) and Service Binding Records, Encrypted Client Hello [ECH](https://www.ietf.org/archive/id/draft-ietf-tls-esni-14.html) was, in fact, the reason SVCB records were defined. DNS lookup is the only point at which certain cryptographic information can be made available before all the connection encryption starts to happen.  Unfortunately, the SVCB draft is stuck in the RFC Editor work queue behind ECH, even though there is language in ECH that references SVCB.  The Working Group is therefore required to remove all the SVCB language from the ECH draft so that it may proceed.  This procedural detail - and accompanying delay - has important consequences: the major open source software package that requires modification before ECH can expect wide adoption (OpenSSL) is waiting for ECH to become a full-fledged RFC before the submitted pull requests will be granted.  Meanwhile there is plenty of experimentation with ECH happening on the live Internet with Mozilla/Firefox and Cloudflare running experiments.

It turns out there's an alternative (or perhaps *parallel*) proposal for TLS 1.3 - [CompactTLS](https://datatracker.ietf.org/doc/draft-ietf-tls-ctls/) - an effort begun in 2019 and now in it's eighth revision.  cTLS proposes to ```save bandwidth by trimming obsolete material, tighter encoding, a template-based specialization technique, and alternative cryptographic techniques. cTLS is not directly interoperable with TLS 1.3 or DTLS 1.3 since the over-the-wire framing is different.```  cTLS is undergoing formal analysis and implementation work proceeds, though no results are currently available.

The [HTTPbis Working Group](https://datatracker.ietf.org/wg/httpbis/charter/) formally adopted the [HTTP Unprompted Authentication](https://datatracker.ietf.org/doc/draft-ietf-httpbis-unprompted-auth/) specification in the month before IETF116.  As a reminder, Unprompted Authentication allows a server to offer authenticated services without advertising that it does so (meaning the authenticated resources can not be actively probed). A number of semantic elements are under discussion, mostly to understand how this new feature is unique among existing HTTP features (and can, or can not, be aligned with *adjacent* capabilities). An action item for IETF117 is a formal analysis of the cryptography used, with several alternatives being proposed. 
