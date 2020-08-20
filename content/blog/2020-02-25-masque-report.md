---
title: MASQUE Review
author: Hans-Christoph Steiner & Michael Pöhn
tags:
  - IETF
  - MASQUE
  - Pluggable Transports
  - privacy
  - QUIC
---


[MASQUE](https://datatracker.ietf.org/wg/masque/about/) is set of related IETF drafts for specifying flexible proxying built into a standard webserver.  It is meant to be deployed on a server that is serving public websites, then this connection can be reused for proxying generic connections.  It is very much a work in progress, so any of this can change.  It is currently built on top of the QUIC+HTTP/3 and HTTP/2+TLS+TCP protocols.  The website and proxy packets look the same, and all connections to the webserver will be shared and reused, regardless of whether its a web page request or proxy traffic.  Each new proxy/website request will reuse any existing connection, providing a key reduction in metadata that makes all the packets blend together from the point of view of the network observer.  For example, to prevent the network observer from corrolating requests to proxy with the outbound request to the destination, a client could first connect to the website, then some time later, connect to the proxy. 

QUIC is an Internet protocol on the verge of being standardized by the IETF, initially developed by Google.  Approximately 50% of traffic from Chrome browsers to Google sites currently use QUIC, so it already has some large scale adoption.  MASQUE is very similar to Meek and Encrypted _ClientHello_ (aka ECH or Encrypted SNI) domain fronting in how it functions, and all of them "hide in plain site" by making circumvention traffic look the same as traffic that censors are unwilling to block.  Like ESNI, MASQUE could be totally blocked in countries that deem QUIC too large a risk, e.g. China already blocks Google, so blocking the QUIC protocol right now would have very low cost to them.  So it must be rolled out and gain broad adoption before it can be an effective circumvention tool.

One use case is individuals enabling MASQUE on their personal websites, or organizations on their websites.  Another use case is to provide travelling employees with VPN access even with local networks are blocking VPNs based on the protocols (e.g. DPI to identify OpenVPN or Wireguard traffic).  Hosting providers and CDNs are not likely to to deploy MASQUE behind their main TLS certificate, as they are not willing to take the risk of getting blocked, just like with domain fronting.  MASQUE/QUIC does not change the domain fronting formula, instead, it just provides a different mechanism to leverage.

One key feature of MASQUE is a means of requiring authentication to the proxy before it gives any information back at all, including even if it exists.  It does this with a custom authentication method where the replies are defined only as `200 OK` for successful authentication or `404 Not Found` for everything else.  This is an idea that could also be used in Pluggable Transports in general.


## Relation to Pluggable Transports

The MASQUE Obsfuscation and HTTP Transport Authentication pieces of MASQUE are directly relevant to Pluggable Transports (PT), and could be included as part of the suite of standards for implementing complete PT solutions.  The non-discoverable authentication method is useful for any PT that already requires some kind of key and is served via an public network socket.   Standardizing the proxy setup and configuration makes sense to do both for MASQUE as much as PT.  Right now, there are a wide variety of proxy configurations for PT with circumvention and VPN service providers.  


## MASQUE as Onion Routing and Tor Components

There are also some efforts to expand the scope of MASQUE into a Tor replacement based on QUIC and HTTP CONNECT proxies.  This is a nice idea, but it should not distract from the core MASQUE pieces which will provide real value now.  This area of work is now represented by three drafts: HTTP Transport Authentication, MASQUE Obfuscation, and MASQUE.  Without a drastically expanded scope, MASQUE cannot replace Tor.  It can provide one key but small building block: the base mechanism for onion routing based on HTTP CONNECT and QUIC.  This could potentially allow Tor middle relay services to be implemented with a standard webserver like nginx with only a small custom plugin.  This would not change the requirement for all of the various Tor network management services.


## Sources

* https://tools.ietf.org/html/draft-ietf-quic-tls-27
* https://lists.torproject.org/pipermail/tor-dev/2018-March/013026.html
* https://davidschinazi.github.io/masque-drafts/draft-schinazi-masque.html
* https://davidschinazi.github.io/masque-drafts/draft-schinazi-masque-obfuscation.html
* https://davidschinazi.github.io/masque-drafts/draft-schinazi-httpbis-transport-auth.html
* https://mailarchive.ietf.org/arch/msg/masque/Cxh1phx6vFgn19jyANmt2YwLDqQ/
* https://datatracker.ietf.org/meeting/104/materials/slides-104-secdispatch-the-masque-protocol-draft-schinazi-masque-00
* https://guardianproject.info/2019/04/16/exploring-possibilities-of-pluggable-transports-on-android/

