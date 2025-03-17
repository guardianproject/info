---
title: "7ASecurity Completes Security Audit of Círculo"
author: n8fr8
categories:
  - News
tags:
  - audit 
  - free software
  - open source
  - privacy
  - matrix
  - synapse
  - article19
  - otf
  - opentechfund
---

Over the last six months, we’ve been working with [7ASecurity](https://7asecurity.com/) through support from the [Open Technology Fund’s Security Safety Audits](https://www.opentech.fund/impact/security-safety-audits/), to complete an audit of our [Círculo project](https://encirculo.org).  The public report on that is [now available](https://www.opentech.fund/security-safety-audits/circulo-security-audit/).

If you don’t know about Circulo, this is a physical check-in safety app we have developed, alongside Article 19’s Mexico City team, for a number of years, focused on providing secure location sharing and urgent notifications within small trusted groups, for people under threat of physical violence. The free and open-source [code we have developed](https://gitlab.com/circuloapp) includes iOS and Android mobile apps, as well as server infrastructure, largely based on the [Matrix Protocol](https://matrix.org/), including the mobile software development kits (SDKs), [MegaOLM encryption](https://matrix.org/docs/matrix-concepts/end-to-end-encryption/), and [Synapse Server](https://github.com/element-hq/synapse). You can read about the last round of work we completed on Circulo, including design, development, and community building, in a [public report released in November](https://guardianproject.info/releases/CirculoFinalReport20232024.pdf). 

The primary summary from the audit is as follows: “Overall, the auditors found that the app defended itself well against a broad range of attack vectors.”. We are happy with that assessment, though a number of issues were found, both in our mobile app code and in our infrastructure. While some of them were difficult to address, we have done our best to fix or mitigate to the extent we are able. More detail on that below.

As the report states: 
*Of the nine vulnerabilities identified one was flagged as “high-risk,” and seven were considered “medium-risk”*.

The one high-risk vulnerability discovered was summarized as “Android & iOS apps are vulnerable to DoS attacks via DNS spoofing”. This means that while the Círculo app was using TLS to encrypt the network encryption, as well as to authenticate the domain it connects to, it was not using any special method for ensuring the IP address provided by the DNS lookup was secure. Instead, Círculo relies on the mobile OS to provide secure DNS options for the user to enable, or on the user themselves adopting a third-party secure DNS tool. 

The primary harm from this high-risk vulnerability is that if someone was targeted in this way, they would not be able to access or share or see check-in and location updates from Círculo. No private information would be compromised. While we take app and service blocking and censorship seriously, we know there are many ways to avoid it, including third-party VPN apps like our own Orbot.

As one method of remediating this vulnerability, we were able to build in support on Círculo Android for DNS-over-HTTPS (DoH), currently with support for Cloudflare, but in the future, as a configurable option as well. You can see the [code commit on gitlab](https://gitlab.com/circuloapp/circulo-keanu-android/-/commit/955c5a3198a9fbfd887ee3fa57b3f331373e9127). 

Most of the other medium and lower issues we resolved last year and already included in public app releases. You can view all the open tickets responding to the medium and lower issues in the report on our [public bug tracker](https://gitlab.com/groups/circuloapp/-/milestones/19#tab-issues). 

You will notice there are still open issues in the tracker, which we continue to consider how to implement. These are marked as “enhancements” as we see them as providing additional security beyond our established threat model. They also require significant changes in the core Matrix SDK which we rely upon, and that is shared with other Matrix-based applications such as Element. 

On the infrastructure side, 7ASecurity was very helpful in pointing out many ways to harden our deployment by taking advantage of additional security configurations and options available through Amazon Web Services.

There are two open issues related to our production server infrastructure. 

“Synapse Admin API exposed to the internet”: The Admin API is utilized by our system moderators to handle emergency requests from authenticated users and partners to delete or disable accounts and rooms, if they have lost access to them due to extreme circumstances (device taken, lost, destroyed, or had to delete the app due to physical threat concern).

“Data leaks in Nginx and CloudWatch logs”: The Synapse logging detail level is capturing too much data clearly. This was useful during staging deployment and development, but needs to be reduced. No personal information is leaked, only tokens and ids of rooms.

These are both issues we are working to address by requiring additional network authentication to access the Admin API, and by reducing the log detail that we are storing. We also ensure our existing admin accounts and authentication credentials are stored securely in multi-factor password managers.

One important aspect of Círculo to point out, is that anyone can run their own server, to fully control the stack and infrastructure. It is a complete standard Matrix Synapse deployment. You can also pay a third-party hosting provider to host your own private Matrix server instance. While we are happy to offer a default community service, we believe in open, decentralized, and federated systems, along with data sovereignty.

In summary, Círculo’s security and usability is constantly improving, with security audits from organizations like 7ASecurity and support from OTF, being a critical part to that progress. If you have any questions or concerns, please reach out to us at the Guardian Project help desk at [mailto:support@guardianproject.info](support@guardianproject.info). 
