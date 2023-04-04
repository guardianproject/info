---
title: "IETF116 Conference Report: Friday March 31, 2023"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day Five of the [116th IETF meeting](https://www.ietf.org/how/meetings/116/) in Yokohama Japan.  For the rundown on Day Four, see my [daily report](https://guardianproject.info/2023/03/30/ietf116-conference-report-thursday-march-30-2023/).*

With a lot of focus on privacy with respect to Internet protocols, novel new cryptography schemes are an important requirement for new protocol designs.  For example, [Privacy Preserving Measurement](https://datatracker.ietf.org/wg/ppm/about/) is relying on new cryptography to support distributed aggregation of a wide range of measurements in the advertising domain as well as application telemetry.  [Privacy Pass](https://datatracker.ietf.org/wg/privacypass/about/) is relying on new cryptography to allow web browsing across the broad Internet after a single, lightweight authentication to an authority.  IETF Working Groups are encouraged to work with the [Crypto Forum Research Group](https://irtf.org/cfrg) of the Internet Research Task Force ([IRTF](https://www.ietf.org/about/groups/irtf/)) to develop, test and refine new cryptography techniques that meet defined security/privacy goals and can scale for Internet-wide use.

One area receiving a lot of attention is *signature blinding*. [Blinding](https://en.wikipedia.org/wiki/Blind_signature) is used when a message's signing party is different from the message originator (digital cash, electronic voting are examples).  There are many types of blind signature, used for different purposes.  IETF's interest is in how these algorithms work at Internet scale (Privacy Pass potentially being the most high-volume example).  No fewer than three results [[1](https://datatracker.ietf.org/meeting/116/materials/slides-116-cfrg-key-blinding-for-signature-schemes)] [[2](https://datatracker.ietf.org/meeting/116/materials/slides-116-cfrg-the-bbs-signature-scheme)] [[3](https://datatracker.ietf.org/meeting/116/materials/slides-116-cfrg-rsa-blind-signatures-with-public-metadata)] were presented on this topic.

[Verifiable Distributed Aggregation Functions](https://eprint.iacr.org/2023/130) are a key set of *multi-party computing* techniques for improving the privacy of Internet measurement - split the counting across a group of non-colluding hosts and reassemble it in a manner only the requester (and not the individual aggregators) can see. While there is consensus around the approach, there is work to be done on the algorithm details, specifically around performance and elimination of attack vectors. [PLASMA](https://datatracker.ietf.org/meeting/116/materials/slides-116-cfrg-plasma) - a new proposal for distributed aggregation - was presented along with a [deeper analysis](https://datatracker.ietf.org/meeting/116/materials/slides-116-cfrg-vdaf) of two other proposals (PRIO and POPLAR). 

There is also worry about the forthcoming era of *quantum computing* and its [impact on the cryptographic tools used today](https://scienceexchange.caltech.edu/topics/quantum-science-explained/quantum-cryptography).  The search is on for cryptographic methods that are safe *post-quantum* and, along with them, ways to migrate currently-encrypted data into the post-quantum era. Currently being discussed are *hybrid* or *composite* schemes that layer the old techniques and the new techniques.  For me, the math goes off into fairy land pretty quickly, but if *Composite Key Encapsulation Mechanisms* turns you on, there's plenty happening at IETF nowadays [[1](https://datatracker.ietf.org/doc/html/draft-ounsworth-pq-composite-kem-00)] [[2](https://datatracker.ietf.org/doc/html/draft-ietf-tls-hybrid-design)] [[3](https://datatracker.ietf.org/doc/draft-wussler-openpgp-pqc/)] [[4](https://datatracker.ietf.org/doc/draft-tjhai-ipsecme-hybrid-qske-ikev2/00/)].

It turns out, it's not just me whose eyes glaze over at the mathematics involved in much of this work.  IETF has found that IRTF's research in this area should recognize that a presentation acceptable to other mathematicians might not be too useful for protocol implementers.  With this in mind, the Crypto Forum is pulling together [a set of guidelines](https://datatracker.ietf.org/meeting/116/materials/slides-116-cfrg-guidelines-for-writing-cryptography-specifications) for writing cryptographic specifications within the IETF context. 