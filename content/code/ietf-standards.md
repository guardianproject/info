---
title: 'IETF Standards'
date: 2026-05-18T00:00:00-04:00
author: Guardian Project
description: 'Open implementations and interoperability work for privacy-preserving Internet standards.'
menu:
  main:
    parent: code
---


Network activity is now routine raw material for profiling, advertising, surveillance, and legal demands. VPNs and older privacy proxies still help in some cases, but they centralize trust and are often treated as suspicious outside corporate networks. Guardian Project works on Internet standards so privacy features can become ordinary infrastructure. Our focus is on protocols that divide trust across multiple parties, reduce unnecessary identifying data, and still fit into the tools developers already use.

Newer IETF work moves more privacy into the protocol. A service can receive a request without learning the user's network address. A server can require proof from a client without asking for a conventional account or exposing more identity than the request needs. But a standard does not help much if the only working code is locked inside closed products. Open source developers then have to guess at behavior after the standardization work is finished. That leads to incompatible implementations, longer launches, and public-interest tools that cannot easily interoperate with commercial deployments.

## How We Participate

We try to get involved before a draft becomes an RFC. We take part in working-group discussions, attend IETF meetings, and use hackathons to test ideas against code and other implementations.

That participation includes:

- reading and commenting on drafts from an implementation point of view
- building proof-of-concept clients, relays, gateways, and servers
- testing our code against other implementations
- bringing interop failures and deployment problems back to working groups
- publishing notes and examples so other open source projects can follow the work

## Oblivious HTTP and HTTP Concealed Authentication

Alongside the ECH work, we are also working on [Oblivious HTTP][OHTTP] and [HTTP Concealed Authentication][CA]. These protocols address related but distinct problems: separating the requester from the destination, and proving client authorization without using conventional account or bearer-token patterns.

The immediate audience is application and service developers. Example uses include sensitive form submission, anonymous telemetry, access control, rate limiting, and reducing unauthenticated probing of public services.

**More on Oblivious HTTP and Concealed Authentication: [implementation details and project links](/code/ohttp-and-ca/).**

## Encrypted Client Hello

Encrypted Client Hello (ECH) is another major part of our standards work. ECH extends TLS so the server name and other early connection metadata can be encrypted during the first stage of an HTTPS connection. Plaintext SNI has long let network observers identify, profile, or block the sites people visit, even when the rest of the connection uses HTTPS.

Through the [DEfO project](https://defo.ie/), Guardian Project has worked on ECH implementation and deployment in open source software. That work has included ECH support for OpenSSL and Conscrypt, interoperability testing, and experiments with ECH-enabled clients and servers such as curl, nginx, Apache HTTP Server, lighttpd, HAProxy, and F-Droid-related Android builds.

ECH is separate from Oblivious HTTP and HTTP Concealed Authentication, but the work has the same shape: implement the privacy feature in open source components, test it against other implementations, and write down the deployment problems before they become permanent barriers.

## Related Blog Posts

- 2020-02-25: [MASQUE Review](/2020/02/25/masque-review/)
- 2021-02-10: [Clean Insights: February 2021 Update on Privacy-Preserving Measurement](/2021/02/10/clean-insights-february-2021-update-on-privacy-preserving-measurement/)
- 2021-10-18: [The IETF and Internet Freedom](/2021/10/18/the-ietf-and-internet-freedom/)
- 2021-11-24: [IETF112 - Meeting Update (November 2021)](/2021/11/24/ietf112-meeting-update-november-2021/)
- 2021-11-30: [Implementing TLS Encrypted Client Hello](/2021/11/30/implementing-tls-encrypted-client-hello/)
- 2021-12-23: [IETF: Year End Review 2021](/2021/12/23/ietf-year-end-review-2021/)
- 2022-03-20: [IETF113 Hackathon Project](/2022/03/20/ietf113-hackathon-project/)
- 2022-03-21: [IETF113 Conference Report: Monday March 21, 2022](/2022/03/21/ietf113-conference-report-monday-march-21-2022/)
- 2022-03-24: [IETF113 Conference Report: Tuesday March 22, 2022](/2022/03/24/ietf113-conference-report-tuesday-march-22-2022/)
- 2022-03-26: [IETF113 Conference Report: Wednesday March 23, 2022](/2022/03/26/ietf113-conference-report-wednesday-march-23-2022/)
- 2022-03-27: [IETF113 Conference Report: Thursday March 24, 2022](/2022/03/27/ietf113-conference-report-thursday-march-24-2022/)
- 2022-03-28: [IETF113 Conference Report: Friday March 25, 2022](/2022/03/28/ietf113-conference-report-friday-march-25-2022/)
- 2022-07-24: [IETF114 Hackathon Report: Sunday July 24, 2022](/2022/07/24/ietf114-hackathon-report-sunday-july-24-2022/)
- 2022-07-25: [IETF114 Conference Report: Monday July 25, 2022](/2022/07/25/ietf114-conference-report-monday-july-25-2022/)
- 2022-07-26: [IETF114 Conference Report: Tuesday July 26, 2022](/2022/07/26/ietf114-conference-report-tuesday-july-26-2022/)
- 2022-07-27: [IETF114 Conference Report: Wednesday July 27, 2022](/2022/07/27/ietf114-conference-report-wednesday-july-27-2022/)
- 2022-07-28: [IETF114 Conference Report: Thursday July 28, 2022](/2022/07/28/ietf114-conference-report-thursday-july-28-2022/)
- 2022-07-29: [IETF114 Conference Report: Friday July 29, 2022](/2022/07/29/ietf114-conference-report-friday-july-29-2022/)
- 2023-03-28: [IETF116 Conference Report: Monday March 27, 2023](/2023/03/28/ietf116-conference-report-monday-march-27-2023/)
- 2023-03-29: [IETF116 Conference Report: Tuesday March 28, 2023](/2023/03/29/ietf116-conference-report-tuesday-march-28-2023/)
- 2023-03-30: [IETF116 Conference Report: Wednesday March 29, 2023](/2023/03/30/ietf116-conference-report-wednesday-march-29-2023/)
- 2023-03-30: [IETF116 Conference Report: Thursday March 30, 2023](/2023/03/30/ietf116-conference-report-thursday-march-30-2023/)
- 2023-04-04: [IETF116 Conference Report: Friday March 31, 2023](/2023/04/04/ietf116-conference-report-friday-march-31-2023/)
- 2023-11-09: [DEfO - Developing ECH for OpenSSL (round two)](/2023/11/09/defo-developing-ech-for-openssl-round-two/)
- 2023-11-10: [Quick set up guide for Encrypted Client Hello (ECH)](/2023/11/10/quick-set-up-guide-for-encrypted-client-hello-ech/)
- 2024-03-17: [IETF119 Conference Report: Hackathon March 17, 2024](/2024/03/17/ietf119-conference-report-hackathon-march-17-2024/)
- 2024-03-18: [IETF119 Conference Report: Monday March 18, 2024](/2024/03/18/ietf119-conference-report-monday-march-18-2024/)
- 2025-01-10: [Using TLS ECH from Python](/2025/01/10/using-tls-ech-from-python/)

[OHTTP]: https://www.ietf.org/rfc/rfc9458.html
[CA]: https://datatracker.ietf.org/doc/rfc9729/
