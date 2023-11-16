---
title: DEfO - Developing ECH for OpenSSL (round two)
author: Stephen Farrell
categories:
  - News
tags:
  - Apache
  - Conscrypt
  - curl
  - DEfO
  - ECH
  - F-Droid
  - free software
  - HAProxy
  - IETF
  - metadata
  - nginx
  - open-source
  - OpenSSL
  - privacy
  - resilience
  - TLS

---

Encrypted ClientHello (ECH) plugs a privacy-hole in TLS, hiding previously visible details from network observers. The most important being the name of the web-site the client wishes to visit (the Server Name Indication or SNI).  This can be a major privacy leak, like when accessing a dissident news source hosted on a Content Delivery Network ([CDN](https://en.wikipedia.org/wiki/Content_delivery_network)). A visible domain name also provides a straightforward method for censors to block websites and internet services. [Tolerant Networks Limited](https://www.tolerantnetworks.com/about-us.html) and the Guardian Project successfully ran the [OTF](https://www.opentech.fund/)-funded [DEfO](https://defo.ie/) project that [developed interoperable implementations](https://guardianproject.info/2021/11/30/implementing-tls-encrypted-client-hello/) of ECH for OpenSSL, Conscrypt and, via those libraries, a range of ECH-enabled web servers and clients.  This second funded project, DEfO-2, is a timely continuation of that project from the same the team.  As needed for disambiguation, we use DEfO-1 to refer the completed project and DEfO-2 for this current project. When there’s no ambiguity, we use the DEfO acronym to cover both past and future work related to ECH for OpenSSL, related applications and other TLS stacks.

As the IETF standard for ECH completes, our key objectives are to:

* Upstream DEfO code
* Integrate ECH into more clients and servers
* Gain and document operational experience
* Submit key code for red team audits
* Publish open-source ECH provisioning tools

The key challenges we expect to face in meeting those objectives are: firstly, dealing with the OpenSSL and other upstream code bases (e.g. nginx, Apache HTTP Server) - satisfying upstream developers when dealing with complex code changes, as are involved here, has proven to be quite time and effort consuming. Secondly, it is a challenge to arrange the trials we have envisaged for DEfO-2 but doing so should help to demonstrate that web sites can easily and safely enable ECH without putting themselves at risk of interoperability failures or adverse attention from censors and without further centralising the web. Lastly, there are some remaining technical challenges not addressed in DEfO-1 (proprietary TLS ClientHello extension handling, interactions between TLS Hello Retry Request and ECH, and privacy analyses of split-mode ECH deployments) that we plan to address in DEfO-2.

The key challenges we aim to mitigate for users is the ease with which user activity can be tracked and blocked based on clear text SNI. Secondarily, our focus on web-server integrations and provisioning mechanisms for ECH addresses Internet centralisation (which itself poses potential risks for censorship) by ensuring this technology can be easily deployed without having to depend on entities such as global-scale CDNs.

The primary gaps addressed by DEfO are: the privacy-leak that is clear text SNI in TLS and secondly that nobody else has been developing an ECH implementation for OpenSSL, which is one of the most widely used TLS stacks, particularly for web servers. That situation has not changed since DEfO-1 started. Arguably filling that gap has become more pressing as some browsers now ship with ECH support.

ECH is designed to contribute to the safety of users by removing one the the main remaining aspects of the web that allows network observers to easily monitor and censor web traffic based on either client DNS queries (browsers typically only use ECH when DoH has been used) and the Server Name Indication (SNI) in the TLS handshake, which is encrypted via ECH. The eventual goal is that use of ECH becomes near ubiquitous, and that goal is very achievable for web sites that make use of a CDN. DEfO however also has a focus on ECH support in various web servers and proxies (Apache, nginx, lighttpd, HAProxy) so that users of deployments that don’t use a commercial CDN can also benefit from ECH. The result of using ECH should be that neither the DNS query nor the TLS exchange leak the name of the web server with which the browser is establishing contact, thus taking away a still-easy opportunity for monitoring and censorship.

Censors however, especially at the nation-state level, might choose to block all uses of ECH, which is something that is to be expected. The main mitigation for that envisaged is that browsers, even while not using ECH, will emit “fake” (or GREASEd) ECH values, thus increasing the costs if a censor decides to block all use of ECH. The extent to which GREASEing will be an effective mitigation for blocking all ECH will essentially
end up as a political/commercial decision for censors, browser makers, and web sites, but what we can say is that for now at least, browser makers and the larger CDNs do seem committed to making use of ECH. So we can have some hope that even the most capable censors might have to think hard before blocking all ECH. In DEfO-2 we are also planning some significant-scale trials that, if successful, should go a long way towards helping other significant web sites overcome fears related to enabling ECH. Overcoming a fear that one’s web site may be blocked if one deploys ECH will be a valuable result of DEfO-2 should our trials come to fruition as we hope.

We do see a number of usability issues for those deploying web servers that need to be addressed, and that we plan to address in DEfO-2. Our approach is to aim for the same level of usability for web server administrators as has been achieved by [_certbot_](https://certbot.eff.org/) as it interacts with Let's Encrypt or other CAs. Making it easy to enable ECH, especially for "smaller" web properties is high priority for DEfO.

The outcome for which we hope is the upstreaming of ECH into important code bases, and to have demonstrated that one can deploy ECH easily at either small or large scale. The impact we expect is that we continue to significantly contribute to the use of ECH becoming near ubiquitous.



## Timeliness

The time is now ripe for DEfO-2:

* [Firefox](https://support.mozilla.org/en-US/kb/faq-encrypted-client-hello) now supports ECH by default.
* Chrome supports ECH in [10% of stable releases](https://groups.google.com/a/chromium.org/g/blink-dev/c/KrPqrd-pO2M/m/_8Lfd5xcAwAJ) as of August 2023.
* Brave now also supports ECH, [behind the same flags](https://github.com/brave/brave-browser/issues/1851#issuecomment-1763176335) as Chromium
* These browser developments, plus the server code developed by DEfO-1, now enable us to plan real-world experiments
* Cloudflare has [beta support](https://developers.cloudflare.com/ssl/edge-certificates/ech/) for enabling ECH.
* During the run-time of DEfO-2 we expect to be in a position to run trials with significant players that could significantly assist with the goal of making use of ECH common for large web sites.
* The DEfO-2 project timeline should also cover the finalisation of the IETF specification for ECH, significant progress on ancillary specifications (e.g. for provisioning) and provide sufficient time for upstreaming of DEfO code
* DEfO-2 benefits from the same team as DEfO-1 – Tolerant Networks and the Guardian Project having co-operated successfully on DEfO-1 are looking forward to continuing that collaboration and to extending the team for DEfO-2
* HPKE, a core part of ECH, but with broader applicability, is now RFC9180 and the OpenSSL maintainers merged our DEfO code for HPKE in November 2022.

## Our development projects

The DEfO project implemented Encrypted ClientHello (ECH) support for OpenSSL and Conscrypt, carried out interoperability testing of those implementations, and also used those libraries to ECH-enable various web servers and clients. We deployed services using these web servers and the DNS infrastructure required to support automated key upated for the HTTPS RRs associated with those services. Here we provide a short overview of that work in order to help with larger scale experiments and with further development of the ECH specification.

### Libraries

As part of the DEfO project, we ECH-enabled two important TLS libraries:

* [Conscrypt](https://www.conscrypt.org/) is a Java Security Provide (a library) that provides a Java "wrapper" for the C++ language boringssl library. Conscrypt is commonly used as the TLS provider for applications running on Android devices and is thus an attractive target to allow many clients to be ECH-enabled. (We do not target browser clients in DEfO as work on ECH-enabling those is being done by browser-makers.) The authors of boringssl (Google) have added ECH support to a version of their code, and we used that to enhance Conscrypt to call the new borinssl APIs required to use ECH and to provide mechanisms for applications to default to, or signal use of, ECH.
* OpenSSL is a long-lived library providing cryptographic and TLS services that is used by many applications, including many web servers and hence is an attractive target for ECH-enabling, especially for server-side functionality. Our ECH-enabled fork of OpenSSL is here.
* We have and will continue to work with the developers of other TLS libraries (e.g. wolfSSL) to assist in ECH-enabling their code, mostly via interoperability testing.

### Clients

We ECH-enabled implemented the following TLS client applications:

* OpenSSL `s_client` - this client application comes as part of the OpenSSL build but is commonly used for testing and as an extremely simple scriptable TLS client.
* _curl_ is a widely-used command line web client that can use OpenSSL for TLS support, so we [ECH-enabled that](https://github.com/sftcd/curl/blob/ECH-experimental/docs/ECH.md).
* F-Droid is an Android client application that provides an installable catalogue of FOSS applications and that uses Conscrypt. We made an ECH-enabled build called [DEfO ECH Apps](https://f-droid.org/packages/ie.defo.ech_apps/)

### Servers

We ECH-enabled implemented the following web servers:

* The Apache HTTP Server is one of the two most commonly used web servers today, you can try our [ECH-enabled fork](https://github.com/sftcd/httpd).
* _nginx_ is the other web server in the "top two.", you can try our [ECH-enabled fork](https://github.com/sftcd/nginx).
* lighttpd is a web server that is commonly used on smaller devices such as home routers, you can try our [ECH-enabled fork](https://github.com/sftcd/lighttpd1.4).
* HAProxy is widely used as an HTTP ingress proxy and so is a good target for exploring ECH split-mode, you can try our [ECH-enabled fork](https://github.com/sftcd/haproxy).
* OpenSSL `s_server` - this example server application is part of the OpenSSL build and is commonly used for testing and experimentation.


### Test tools

Amongst the test tooling we developed are:

* Comprehensive OpenSSL make test targets for HPKE and ECH.
* [ECHInteropTest](https://github.com/defo-project/EchInteropTest) is a Java client for interoperability testing on Android.
* [_echdnsfuzz_](https://github.com/sftcd/echdnsfuzz) is a catalogue of "interesting" ECHConfigList values that could cause issues for clients combined with a service to randomly select one of those for publication in the public DNS every 30 minutes. This is a useful part of fuzz-testing an ECH-enabled client application.

## Issues Arising

We saw the following issues that could benefit from further work to ease deployment of ECH:

* For HAProxy, since DEfO-1 we have achieved support for HelloRetryRequest in ECH split-mode but have further work to do on ECH key rotation.
* There can sometimes be a lack of clarity as to which software component should be responsible for choosing to attempt real (i.e. non-GREASEd) ECH, and hence to be responsible for the additional DNS queries required to acquire an ECHConfig. For libraries like OpenSSL and boringssl it clearly only makes sense for that decision (and hence any new DNS handling code) to be outside the library. For a browser, it as clearly makes sense for that code to be in the browser application layer. With "middleware" though, such as OkHTTP or Conscrypt it can be hard to know which is the correct decision.
* The new DNS code required for handling HTTPS RRs is not too complex but the full generality of SVCB is extremely complex. Adding such complexity (and associated caching) is a major change for clients like curl that have to date only had to have a very simple model for DNS - essentially only querying A/AAAA and having almost trivial caching in the application itself.
* The client implementation of ECH is relatively complex in that it "touches" the TLS state machine in many ways, and hence requires changes in a lot of places. As well as increasing the cost of implementing this also increases the costs associated with testing and upstreaming.
* Achieving the same level of usability as ``certbot`` for web server administrators may be challenging, but is an important goal to make it easy for web server administrators to be able to easily deploy ECH.

## Conclusions

ECH is demonstrably implementable and can be deployed. We don't yet know if new issues will become apparent as larger-scale experiments are carried out, but we should find out during the run-time of DEfO-2.
