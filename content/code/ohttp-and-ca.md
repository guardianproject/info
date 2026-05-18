---
title: 'Oblivious HTTP and HTTP Concealed Authentication'
date: 2026-05-18T00:00:00-04:00
author: Guardian Project
description: 'Guardian Project implementations for OHTTP, relays, gateways, and concealed HTTP authentication.'
menu:
  main:
    parent: code
---

Guardian Project works on privacy that can fit into ordinary apps, not only specialist privacy tools. [OHTTP][OHTTP] and [HTTP Concealed Authentication][CA] let an app limit what a service, relay, or observer can learn from routine network traffic. A crash report, form submission, update check, or access check should not automatically become another tracking point.

We care about these protocols because they move privacy into shared Internet plumbing. Open source projects should be able to inspect the code, run their own services, test interoperability, and ship these protections without depending on a private vendor's closed stack.

Oblivious HTTP and HTTP Concealed Authentication solve different problems in the HTTP stack. OHTTP separates the client's network address from the request. Concealed Authentication lets a client prove it holds a key without falling back to cookies, bearer tokens, or an account login.

This implementation work is part of our [IETF standards work](/code/ietf-standards/), including working-group discussion, IETF meetings, hackathons, and interoperability testing.

## Oblivious HTTP

[Oblivious HTTP][OHTTP] (RFC 9458) routes an encrypted HTTP request through separate network roles. A relay can see where the request came from, but it cannot read the request. A gateway can process the protected request, but it does not see the client's network address. This split makes OHTTP useful when a service needs data from a client but does not need to know who that client is.

That model fits privacy-preserving telemetry, crash reporting, software update checks, and sensitive data submission to government or commercial services. It gives developers a standards-based alternative to one-off privacy proxy designs.

Our OHTTP work is organized as a small stack:

- [`ohttp-gp`](https://gitlab.com/guardianproject/developer-libraries/ohttp-gp) is reusable OHTTP C++ library. It implements the client and gateway operations described by RFC 9458 and is designed to fit into Chromium-derived networking code.
- [`cog`](https://gitlab.com/guardianproject/developer-libraries/cog) is the client integration. It brings OHTTP support into an Envoy/Cronet-based networking stack so mobile, desktop, and Chromium-based clients can use it through familiar network APIs.
- [`pog`](https://gitlab.com/guardianproject/developer-libraries/pog) is a Go OHTTP relay. It forwards encapsulated OHTTP messages from clients to a configured gateway without needing access to their contents.
- [`gog`](https://gitlab.com/guardianproject/developer-libraries/gog) is a C++ OHTTP gateway. It handles OHTTP decapsulation, forwards requests to a target service, re-encapsulates responses, and publishes the key configuration clients need.

Together these projects cover the pieces needed to run OHTTP end to end: client integration, relay, gateway, and reusable protocol code.

## HTTP Concealed Authentication

[HTTP Concealed Authentication][CA] (RFC 9729) lets a client prove it controls a key as part of an HTTPS request. The proof is bound to the TLS connection, which makes it useful for access control patterns where a server needs a signal from the client without relying on conventional cookies, bearer tokens, or account login flows.

That makes it useful for services that need to rate limit access, authorize clients, or reduce automated probing before exposing more of an application. It can also support systems where the server needs a stable authorization check but does not need a broader user identity.

Our related implementation work includes:

- [`http-concealed-auth`](https://gitlab.com/guardianproject/developer-libraries/http-concealed-auth), with Java client and server code, an nginx module, and an interoperability server configuration.

## Developer Goals

We are building these projects for application and service developers who need privacy-preserving code they can inspect, modify, and test. The standards should be easy to adopt in open source software, easy to compare across independent implementations, and practical enough to ship.

Related posts from our blog:

- 2021: [IETF112 - Meeting Update (November 2021)](/2021/11/24/ietf112-meeting-update-november-2021/)
- 2022: [IETF114 Conference Report: Tuesday July 26, 2022](/2022/07/26/ietf114-conference-report-tuesday-july-26-2022/)
- 2023: [IETF116 Conference Report: Tuesday March 28, 2023](/2023/03/29/ietf116-conference-report-tuesday-march-28-2023/)
- 2024: [IETF119 Conference Report: Hackathon March 17, 2024](/2024/03/17/ietf119-conference-report-hackathon-march-17-2024/)
- 2024: [IETF119 Conference Report: Monday March 18, 2024](/2024/03/18/ietf119-conference-report-monday-march-18-2024/)

[OHTTP]: https://www.ietf.org/rfc/rfc9458.html
[CA]: https://datatracker.ietf.org/doc/rfc9729/
