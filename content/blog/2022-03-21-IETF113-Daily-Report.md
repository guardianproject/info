---
title: "IETF113 Conference Report: Monday March 21, 2022"
author: David
categories:
	- Standards

tags:
   - standards development
   - IETF
   - privacy
---

It's opening day at the [113th IETF meeting](https://www.ietf.org/how/meetings/113/), the first in-person meeting in two years due to the COVID pandemic and being held in Vienna Austria. We're focusing on standards activities of importance to the Internet Freedom community.

New work is brought to the IETF via Birds-of-a-Feature sessions and also each technical area's Dispatch Working Group.  The Application area often sees the most unique and interesting ideas and this meeting was no exception.  The [Open Ethics Initiative] (https://openethics.ai/) introduced its idea for an *ethics disclosure* or [transparency protocol](https://openethics.ai/oetp/) to help promote trust among users and service providers in a way similar to nutrition labelling on foods.  Two [new](https://www.ietf.org/archive/id/draft-mahy-dispatch-immi-content-00.html) [drafts](https://www.ietf.org/archive/id/draft-mahy-dispatch-immi-mls-mime-00.html) have been written related to the format of data exchange among messaging services. I know what you're thinking: "but messaging services don't interoperate".  Exactly. These drafts are a push to get that to happen, initially in the context of the Messaging Layer Security ([MLS](https://datatracker.ietf.org/wg/mls/about/)) effort.  Along the same lines, a plea was made to liberate messaging from the confines of the encapsulating (and in some cases proprietary) protocols, to be used as first-class network transactions on their own via the [Event Streaming Open Network](https://datatracker.ietf.org/doc/draft-spinella-event-streaming-open-network/). And, the team doing Encrypted Client Hello ([ECH](https://tools.ietf.org/id/draft-ietf-tls-esni-13.html)) introduced an idea to [liberate ECH's host configuration information from the DNS](https://datatracker.ietf.org/doc/draft-farrell-tls-wkesni/) to which some folks believe it is inextricably bound.  Well, they didn't present it *quite* that way, but... Liberation was the theme of the event, it seems!

The Privacy Enhancements and Assessments Research Group ([PEARG](https://pearg.org)) had a detailed presentation on the EU's General Data Protection Regulation ([GDPR](https://gdpr.eu)) as it relates to network privacy. It's much richer than I imagined, indicating there's a lot more there in terms of enforcement in the future. The long-incubating [A Survey of Worldwide Censorship Techniques](https://datatracker.ietf.org/doc/draft-irtf-pearg-censorship/) seems to be near *last call* in its Version 5.  The difficulty of getting it published has as much to do with hesitancy around the term *censorship* as with the actual content.

The major news today, however, is that the [MASQUE Working Group](https://datatracker.ietf.org/wg/masque/documents/), whose charter is to develop mechanisms that allow configuring and concurrently running multiple proxied stream- and datagram-based flows inside an HTTPS connection, is coming to closure on [CONNECT_UDP](https://datatracker.ietf.org/doc/html/draft-ietf-masque-connect-udp) and [HTTP Datagrams](https://www.ietf.org/id/draft-ietf-masque-h3-datagram-06.html) while [CONNECT_IP](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip/) has a few more issues to sort out.  Though QUIC and HTTP/3 are the focus of this work, these changes are being defined for HTTP/2 and HTTP/1.1 as well, implying the medium-term availability of robust proxying options in the Internet's service hubs.  As we mentioned in yesterday's post, [HTTP Transport Authentication](https://www.ietf.org/archive/id/draft-schinazi-httpbis-transport-auth-05.html) is an idea for privately authenticating these flows.  We hope this work gets picked up again upon completion of these three initial efforts.

