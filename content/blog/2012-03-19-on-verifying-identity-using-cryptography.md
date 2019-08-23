---
id: 1670
title: On Verifying Identity Using Cryptography
date: 2012-03-19T11:27:51-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=1670
permalink: /2012/03/19/on-verifying-identity-using-cryptography/
categories:
  - Development
tags:
  - crypto
  - https
  - identity
  - openpgp
  - otr
  - psst
  - signing
  - ssh
---
[<img src="https://guardianproject.info/wp-content/uploads/2012/03/identity-150x150.gif" alt="" width="150" height="150" class="alignleft size-thumbnail wp-image-1684" />](https://guardianproject.info/wp-content/uploads/2012/03/identity.gif)One of the most important uses of cryptography these days is verifying the identity of the other side of a digital conversation. That conversation could be between two people using OTR-encrypted IM, a web browser showing a bank website, a Debian Developer uploading a package to the Debian build server, an ssh client logging into an ssh server, and on and on. In all of these cases, cryptography is used to ensure that the software is indeed receiving replies from the expected entity. This happens by checking the current cryptographic key against one that is known to be correct. That is essential to the whole process. If you see the key for the first time, you have no way of knowing whether that is indeed the key you are expecting because there is no point of reference.

In order for this validation of identity to work, there needs to be a method of verifying any given key and making it a reference. There are many ideas about how to do this: 

  * a trusted list of central certificate authorities like in HTTPS
  * key-signing parties where people validate and sign each other’s keys in person, like used with the OpenPGP Web of Trust
  * “trust on first use” (aka “Persistence of Pseudonym”), where you save the key the first time you see it, and then use that as a reference (this is the way most people use SSH)
  * fingerprint verification, where the two people wanting to communicate cryptographically use another channel to manually check each other’s key fingerprints, like a phone call (this is used a lot in OTR and OpenPGP)
  * the Socialist Millionaires’ Protocol (SMP), which is a combination of user-generated question/answer pairs with a cryptographic technique that lets each side confirm whether the other answered the question correctly without divulging any information (this was recently added to OTR and is implemented in Pidgin, Gibberbot, and maybe a couple other programs)
  * a manually confirmed shared secret like a short password (ZRTP uses this when starting secure phone calls)
  * whitelists of fingerprints of widely used keys (aka <a href="http://www.imperialviolet.org/2011/05/04/pinning.html" target="_blank">public key pinning</a>) (this was recently added to Chrome in the wake of the HTTPS certificate authority failures)

[<img src="https://guardianproject.info/wp-content/uploads/2012/03/fingerprint-150x150.jpg" alt="" width="150" height="150" class="alignright size-thumbnail wp-image-1686" />](https://guardianproject.info/wp-content/uploads/2012/03/fingerprint.jpg)Each of these techniques has its advantages and disadvantages, but generally the higher level of verification provided means the more work to do the process. Most people don’t need the high level of verification provided by OpenPGP key signing parties, but maybe if it was fun and much easier to do, then a lot more people would do it. “Trust on first use” is really easy to use and implement, and has been working pretty well for a lot of people who use SSH and OTR. But it has big shortcomings in environments where the state or other central authority that provides the internet infrastructure wants to spy on its users. HTTPS has proven to be quite easy to use, but it has also <a href="https://www.eff.org/deeplinks/2011/08/iranian-man-middle-attack-against-google" target="_blank">proven</a> to be <a href="http://www.theregister.co.uk/2011/08/29/fraudulent_google_ssl_certificate/" target="_blank">quite</a> <a href="https://arstechnica.com//security/news/2011/03/how-the-comodo-certificate-fraud-calls-ca-trust-into-question.ars" title="How the Comodo certificate fraud calls CA trust into question" target="_blank">breakable</a>.

Currently, each of these techniques described above is used as the sole means of verification, then the level of verification is represented as “verified” or “not verified”. This is definitely the way that HTTPS and SSH handle it. OTR is a bit different, it has 3 states of verification: “new key”, “unverified key” i.e. trusted on first use, or “verified”, and good OTR chat apps will represent these three states in the UI. Then OpenPGP is perhaps the opposite extreme: it provides both chains of verification signatures via the Web of Trust but also user-set “trust levels” from 0 to 255 for any given key.

Perhaps an answer is to cryptographically link up these different ways of verification and represent key verification as a continuum. Then when the possibility of linking in “trust on first use” and other techniques was there, people could gradually build up cryptographic trust as they needed it. Starting with “I have seen this key before”, then on to “I have gotten them to verify their OTR key with an SMP question/answer”, then to “I have an OpenPGP trust path to them”, to “I have met them in person and manually verified their key and identity”.

To go into technical detail as an example, GnuPG supports RSA, DSA, ECDSA, El Gamal, and other key types as subkeys for an OpenPGP key. Those core algorithms core basically all of the most common uses of cryptography, including HTTPS, SSH, OTR, and OpenPGP. The link between an OpenPGP key and its subkeys is perhaps the strongest link for verification that exists, so if a given person includes their OTR key, for example, into their OpenPGP key, that provides a strong cryptographic link between them, and one that is easily publicly sharable via the OpenPGP public keyservers. When two people verify their OTR keys using the SMP question/answer, this verification could then extend to their OpenPGP keys if their OTR keys were subkeys. (<a href="http://web.monkeysphere.info" target="_blank">The Monkeysphere Project</a> is one such implementation of this idea, using OpenPGP keys for SSH and HTTPS). 

[<img src="https://guardianproject.info/wp-content/uploads/2012/03/verified-150x150.jpg" alt="" width="150" height="150" class="alignleft size-thumbnail wp-image-1685" />](https://guardianproject.info/wp-content/uploads/2012/03/verified.jpg)Then the last piece of this puzzle is how to represent all of this complexity to the users. The essential part is to stop representing trust as binary yes/no. A one-dimensional continuum provides a lot more info and is a very commonly understood concept in computers (think progress bars). The hard part of this question is ranking the various techniques in how much progress they provide towards the goal of solid identity verification.

For this round of the <a href="https://guardianproject.info/wiki/PSST" title="Portable Shared Security Tokens" target="_blank">PSST Project</a>, we have focused on first allowing people to easily move around their OTR identities, then worked on testing out the idea of linking in all identity keys into an OpenPGP key. From what we have seen so far, we believe this is not only feasible but will provide a solid platform for linking together all these verification techniques and identity keys. And on top of that, with diligent attention to user experience and testing, it should be possible to create user interfaces that make navigating all of this a common, daily task for most computer users.