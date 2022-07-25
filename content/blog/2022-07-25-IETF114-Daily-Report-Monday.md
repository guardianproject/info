---
title: "IETF114 Conference Report: Monday July 25, 2022"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Day One of the [114th IETF meeting](https://www.ietf.org/how/meetings/114/) in Philadelphia USA.*

With privacy a key consideration in new protocol design, cryptography has become a major focus of IETF activities.  The Internet Research Task Force (IRTF) has the [Crypto Forum Research Group](https://irtf.org/cfrg) where new cryptography schemes are brought forward and vetted for use in IETF protocols.  Well, *new* is a misnomer. Much of the mathematics has long been defined, at least at its core, and the work is rather being brought into the IETF context where important engineering considerations apply: use of memory (at rest or in flight), processing required, round-trips required, etc.. Of significance at this meeting, mechanisms for *blinding* a digitial signature are in high demand given the prevalence of multi-tiered approaches to privacy (that is, approaches that insert one or more proxies between entities in a transaction).  Something similar is in the works for cryptographic keys. A number of IETF protocol specifications, still in development, are in line to receive these mathematical gems including [Privacy Pass](https://datatracker.ietf.org/group/privacypass/about/), [Private Access Tokens](https://datatracker.ietf.org/doc/draft-private-access-tokens/), [Oblivious HTTP Application Intermediation](https://datatracker.ietf.org/wg/ohai/charter/) and others.  An excellent summary of the National Institute for Standards and Technology (NIST) [Post-Quantum Cryptography *contest*](https://csrc.nist.gov/publications/detail/nistir/8413/final) was also provided. The topic itself, let alone the solutions chosen, is not for the weak-kneed.

Among IETF's most difficult challenges - for those of us interested in privacy - is the massive amount of surveillance that Internet users endure in everyday life.  One problem is simply defining what *surveillance* means, in the commercial rather than law enforcement sense. Toward that end, the [Privacy Enhancements and Assessments Research Group](https://datatracker.ietf.org/rg/pearg/about/) hosted an excellent *first principles* presentation teasing out ideas around *decoupling* who we are versus what we do, and specifically architectures and design principles to increase decoupling for the purpose of preserving privacy. IETF has a new Working Group looking at [Privacy Preserving Measurement](https://datatracker.ietf.org/wg/ppm/about/) where some of the decoupling ideas are key.  While one approach to privacy preserving measurement has been presented to IETF in the past, PEARG hosted a well-considered survey presentation that looked at a number of techniques in this field at different stages of development. Not considered here: the [Clean Insights](https://cleaninsights.org) project, with which Guardian Project is associated and which was perhaps the first to take a user-consent approach, and the [Open Differential Privacy Project](https://opendp.org) which seeks to make its tools explicitly transparent for public scrutiny. 
