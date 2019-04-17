---
id: 3941
title: Carrier Grade, Verizon and the NSA
date: 2013-06-12T06:38:46-04:00
author: lee
layout: post
guid: http://guardianproject.info/?p=3941
permalink: /2013/06/12/carrier-grade-verizon-and-the-nsa/
force_ssl:
  - "1"
categories:
  - News
  - Research
tags:
  - metadata
  - ostel
  - ostn
  - voice
  - voip
---
[<img class="size-medium wp-image-4188 alignleft" alt="PHONE_BOLT" src="https://guardianproject.info/wp-content/uploads/2013/06/PHONE_BOLT-268x300.png" width="268" height="300" srcset="https://guardianproject.info/wp-content/uploads/2013/06/PHONE_BOLT-268x300.png 268w, https://guardianproject.info/wp-content/uploads/2013/06/PHONE_BOLT.png 514w" sizes="(max-width: 268px) 100vw, 268px" />](https://guardianproject.info/wp-content/uploads/2013/06/PHONE_BOLT.png)

Last week Glenn Greenwald at The Guardian broke the news that [Verizon has been providing the NSA with metadata](http://www.guardian.co.uk/world/2013/jun/06/nsa-phone-records-verizon-court-order) about all of the calls over a subsidiary’s network. This subsidiary is called [Verizon Business Network Services](http://investing.businessweek.com/research/stocks/private/snapshot.asp?privcapId=4259068). It is a privately held company that “owns, operates, monitors, and maintains data and Internet networks in North America, Europe, Asia, Latin America, Australia, Japan, and Africa. The company provides converged communication solutions, such as local and long-distance voice, messaging, and Internet access services.” It is likely this company owns equipment that holds caller detail records for millions of customers. The order used [section 215 of The Patriot Act](http://www.aclu.org/free-speech-national-security-technology-and-liberty/reform-patriot-act-section-215), which allows the FBI to order any person or entity to turn over “any tangible things,” so long as the FBI “specif[ies]” that the order is “for an authorized investigation . . . to protect against international terrorism or clandestine intelligence activities.” The “tangible things” could have been the physical servers or hard disks that store the logged details.

[The Guardian Project](https://guardianproject.info/) operates a voice service called [ostel.co](https://ostel.co/). This service offers secure calling and only logs metadata required for the service to operate, [no more, no less](https://ostel.co/privacy). We’ve redefined what carrier grade means. Our service offers the same reliability and quality as global carriers. It goes further by including security and privacy as core features. This is something Verizon does not offer you. Ostel.co runs a full stack composed of open source software, which gives you the choice to install and operate your own service.

Metadata is information about information. Every call you make over a carrier’s network can carry metadata about your account ID, your caller ID, the duration of the call, the time it was placed and the caller ID of the person you called, even the location of your cellular radio. Information about your calls can be as important as the calls themselves. In many cases they are more important than the content of the calls since they don’t fall under laws requiring a warrant to intercept. Indexing and searching all customers metadata is much faster than tapping and listening in on the same customer’s calls.

Jane Mayer at The New Yorker gives a good example of [what a service provider can learn from your metadata](http://www.newyorker.com/online/blogs/newsdesk/2013/06/verizon-nsa-metadata-surveillance-problem.html?mbid=gnep). “Personal phone calls can also reveal sensitive medical information: “You can see a call to a gynecologist, and then a call to an oncologist, and then a call to close family members.”” Metadata from one source can also be [correlated with metadata from other sources](http://www.technologyreview.com/view/515811/correlation-is-main-concern-over-data-verizon-gives-nsa/), like web searches and credit card purchases. Tom Simonite at the MIT Technology Review writes that Facebook “uses obfuscated versions of its members’ phone numbers and e-mail addresses to connect its data with information that data-broker Datalogix gathers from loyalty card schemes, with the result that it is now possible for companies to connect a person’s activity on Facebook, and the ads they see, with what they buy in physical stores.”

Carriers operate servers that record metadata through a common software practice called logging. Each request your computer software makes to an online service can optionally log all the metadata the application can get its hands on. It is the carrier’s responsibility to define their logging policy, like what is recorded and how long it is retained. This information rarely leaves the privacy of the carrier’s internal operational documents so don’t expect to get many clear answers from them.

While the NSA debacle proves that global telecommunications carriers log everything and keep it around for a very long time, what if you don’t want this information about your behavior logged? Unfortunately, no carrier offers any kind of “opt out” process at this low of a level. To be fair, this information has many purposes. Caller detail records are required to bill customers on per-minute calling plans. It’s unreasonable to expect a carrier to flat out disable logging, though carriers never state that they share your logs with law enforcement without probable cause of a crime. But that is exactly what Verizon did.

In addition to [ostel.co](https://ostel.co), there are two other independent carriers that put your privacy first. [Whisper Systems operates a proprietary secure voice service](https://www.whispersystems.org/) with an open source client called RedPhone. It integrates nicely with Android mobile devices, though it requires a SIM card with a phone number in select countries to sign up for an account. With a little luck in the wrong hands a phone number could disclose more information about you than your social security number. WhisperSys doesn’t publish their logging policy online.

[Silent Circle offers secure voice service](https://silentcircle.com/) for iPhone and Android. They are a subscription service and all client and server software is proprietary. They publish [an exceptionally detailed logging policy on their website](https://silentcircle.com/web/privacy/), which includes how many law enforcement requests for information they have received twice a year.

Ostel.co does not log personal call details to disk, and we can’t disclose information we don’t have. IP addresses, user IDs and referrers are common points of metadata that are used to find patterns about user behavior. When the ostel.co server software requires this information to be stored, it is stored only in memory. When the system is rebooted or shut down, the information is gone forever.

Our service is under active development. It is currently in public beta status and new features like custom aliases, third party authentication services and federated calling are on the roadmap. The beta service will always be free.

For the curious, what follows is a detailed description of the logging implementation of ostel.co.

Caller Details Records are recorded with no identifying information. Attributes stored to disk include timestamp, duration, call state and bandwidth consumed. These pieces of metadata allow us to report on usage without identifying each user. When a monthly report is generated, the metadata is deleted.

The SIP server logs IP addresses of online users. This is a requirement for the SIP protocol to locate each end of the call. The contact information is logged to RAM, including the username, source IP address and source port of the registered client application. When the server is shut down or restarted, this information is erased.

The SIP server only logs debugging information to disk, which does not include any of the SIP information.

Audio data is passed through the server to work around limitations in two-way audio connectivity for common home networks. After a ZRTP key agreement, this audio is encrypted. The server cannot decrypt a call between two users, nor does the server control any of the parameters of the call. This makes calls over ostel.co function in a peer-to-peer mode similar to Skype’s “supernode” feature but without any backdoors.

No IP addresses are logged for any web requests. This is a simple configuration change for the reverse proxy and required a patch to the core source code of the application server framework.

The server stores each user’s email address, SIP username, encrypted password and account management data like when the user profile was created/updated and password reset information if the user chooses to use that feature.