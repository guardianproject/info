---
id: 1784
title: User scenarios to guide our crypto development
date: 2012-04-14T20:16:03-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=1784
permalink: /2012/04/14/user-scenarios-to-guide-our-crypto-development/
categories:
  - Development
tags:
  - anonymity
  - encryption
  - openpgp
  - otr
  - privacy
  - psst
  - usability
  - user scenarios
  - user stories
---
At Guardian Project, we find user-centered development to be essential to producing useful software that addresses real world needs. To drive this, we work with user stories and scenarios as part of the process of developing software. One particular development focus is the <a href="https://guardianproject.info/wiki/PSST" title="Portable Shared Security Token" target="_blank">Portable Shared Security Token (PSST)</a> project, which aims to make it easy to use encryption across both mobile and desktop computers, as well as keep the stores of cryptographic identities (i.e. trusted keys, certificates, etc) in sync between devices.

This post outlines some initial user scenarios that PSST aims to address. We believe them to be common enough so that our solutions will be readily applicable to real world people now. They are a small subset of all of the types of users that we feel can ultimately benefit from the PSST core research, so these user stories provide a starting place for honing the tools for the needs of actual working organizations. These stories also discuss how the software could be used in these situations. The software as described mostly exists, but not all details are currently implemented or even fully vetted as secure practices.

We are very eager for feedback, comments, and criticism on any aspect of these scenarios, from whether they are plausible to whether the user interactions described are built upon realistic expectations of actual members of organizations like the ones described here.

**The Small Cabal**

[<img src="https://guardianproject.info/wp-content/uploads/2012/04/activists-meeting.jpg" alt="" width="300" height="224" class="alignright size-full wp-image-1799" />](https://guardianproject.info/wp-content/uploads/2012/04/activists-meeting.jpg)There is a small group of people that needs to communicate as securely and anonymously as possible. They all meet up in person. They generate keys, and individually sign each person’s key and get that person’s signature on their own key. These are local-only unpublishable signatures. No one uploads their keys to any other server or device. They each generate a revocation certificate and hook it up to their panic button app. Once the panic button is hit, the phone broadcasts the revocation certificate to the pre-determined list of people.

**Diffuse Activist Organization**

An activist organization has members spread out all over their country, with concentrations in certain areas, and a handful abroad. They are working in a country that aggressively tracks communications, but encryption is not banned nor aggressively tracked. Since there are many members and they are widely spread, very few of the members have met the whole membership. Many members often meet up in person at various places around the country, and some people also travel to regional and national meet-ups. The central forum for the whole group is on the internet, and there are many big group discussions and announcements that happen on internet forums.

Each member has a cryptographic key that represents their online identity, which they post to the public keyservers. They generate and store a revocation certificate to upload to the keyservers in case of a compromised key or computer. They do not post any signatures to the key servers so that the social graph information remains private. Whenever they meet another person that they trust, they sign each others’ keys and swap all signature data using direct peer-to-peer communication.

When interacting with members who they only know on the internet, they check whether they have a cryptographic trust path to each others’ keys, and if not, they establish the first step of trust via OTR by doing key verification via question/answer, shared secret or manual fingerprint validation over a trusted channel, like the phone. When they hit there panic button the post the revocation certificate to the keyserver. Each member’s computer/phone automatically checks the public keyservers for revocations hourly, and marks any revoked key as invalid as soon as it receives a revocation certificate.

**Multinational Organization**

[<img src="https://guardianproject.info/wp-content/uploads/2012/04/orgmtg.jpg" alt="" width="300" height="158" class="alignleft size-full wp-image-1800" />](https://guardianproject.info/wp-content/uploads/2012/04/orgmtg.jpg)An organization has many members in a number of different countries. Some of the governments are supportive of the organization’s goals, while some of the governments are strongly hostile and are actively seeking out local members. Many members work in countries where there is little chance of active tracking and monitoring of their use of encryption, while others work in high risk environments from time to time. Certain local contacts and members work in aggressively monitored countries where use of encryption is a flag for the secret police.

The public figures of the organization in safe countries have a public trust profile that is freely downloadable. They use the public OpenPGP infrastructure and publicly share all public signatures. These members also have private, unpublishable signatures related to the members in high risk situations. Operatives in high risk situations use only unpublishable local signatures and the whole collection of signatures is stored in an encrypted form. There devices only contact keyservers via anonymized connections like Tor or VPNs.

When members are signing each other’s keys, the signatures are always sent to the key owner via encrypted email. The signer can then mark the signature as private or public, or their software can be set to always mark all keys as private and unpublishable. When the key owner receives the emailed signature, she can then decide how to manage the signatures: either privately import the signature to their keyring, where it will be stored in an unpublishable format; or publicly import the signature into their keyring and sync it via the public PGP servers. If the signer emailed a private signature to the key owner, then the key management software will automatically make it a private signature.

**Improvised movement organized via social software**

[<img src="https://guardianproject.info/wp-content/uploads/2012/04/Tahrir_Square_during_8_February_2011-300x225.jpg" alt="" width="300" height="225" class="alignright size-medium wp-image-1791" srcset="https://guardianproject.info/wp-content/uploads/2012/04/Tahrir_Square_during_8_February_2011-300x225.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/04/Tahrir_Square_during_8_February_2011-1024x768.jpg 1024w, https://guardianproject.info/wp-content/uploads/2012/04/Tahrir_Square_during_8_February_2011.jpg 1600w" sizes="(max-width: 300px) 100vw, 300px" />](http://en.wikipedia.org/wiki/File:Tahrir_Square_during_8_February_2011.jpg)People from all over a region join a popular movement to help organize protests, distribute media, spread information, etc. Many join in groups of friends or family, but overall the group is not socially well connected together. The common cause is the central binding of the group. In their communications, they want to avoid keyword filtering and communications tracking, as well as try to hinder infiltration and the injection of misinformation. They need to communicate and exchange media with some level of trust. Since the group wants as many members as possible, the infrastructure must be relatively open and public. 

Users who do not have any shared history will trust each other’s keys on first contact, and rely on the continued validation against the initial mark of trust (known as TOFU/POP or Trust On First Use/Persistence of Pseudonym). Once users build up some context with each other, they can deepen the cryptographic trust by using OTR question/answer or shared secret authentication. Users publicly share their TOFU/POP and OTR marks of trust on public exchanges so that people can build up public trust in their cryptographic identity.

**Foreign Journalist, Diplomat, Business Person, etc.**

This user is working in a place with active monitoring, tracking and filtering. She has strong links to institutions outside of the country that can help in case of trouble. She has clear outsider status so is able to use encryption and anonymizing software without a large risk of persecution. She wants to keep her communications private in the face of active monitoring.

Standard public cryptography tools cover most of this situation, but they must be made easier to use, and work on mobile devices. If this user needs encrypted exchanges with locals at high risk of monitoring, local unpublishable signatures can be used in those situations.