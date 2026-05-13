---
title: "Why Free, Libre and Open-Source Software is Essential for Internet Freedom"
date: 2026-05-12
author: Guardian Project Team
categories:
  - Thoughts 
tags:
  - free software
  - open source
  - floss
  - privacy
  - security
  - internet freedom
  - transparency
images: ["/images/default-social.jpg"]
---

Free, libre and open-source software (FLOSS) is a core value of Guardian Project's work, not a stylistic preference or a marketing line. Everything we produce, write, and create is meant to be accessible, transparent, and auditable. That commitment rests on a fundamental conviction: defending privacy and security in a human rights context using proprietary, commercial software is antithetical to the mission. You cannot ask people to trust their lives, their reporting, or their organizing to tools they are not allowed to inspect.

## Kerckhoffs's Principle and the Limits of Obscurity

When deciding what to publish, we follow [Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle), originally formulated in 1883 in the context of designing military ciphers. The principle holds that a system should remain secure even if everything about it, except the secret key, is public knowledge. The American mathematician Claude Shannon later restated it more plainly: *the enemy knows the system*.

That framing shapes how we treat our work. Designs, documentation, and code are all publishable by default. Configurations are publishable too, except where they relate specifically to a client's data, in which case our obligation to client confidentiality takes precedence. Secrets like API tokens and cryptographic keys are, of course, never published, and we maintain an inventory of the relevant secrets associated with any deployment.

A circumvention strategy that assumes the opponent knows what we're doing and *still* can't stop it is more robust than one that depends on the opponent not looking too closely. An open-source application may give an attacker a slight initial advantage in finding exploits, but sophisticated adversaries are already very good at reverse engineering closed software to a point where they can find exploitable patterns. The same visibility that helps them helps friendly researchers, too, who can report vulnerabilities to us before they are weaponized. "Security through obscurity" remains as questionable a strategy as ever. [NIST SP 800-123](https://csrc.nist.gov/publications/detail/sp/800-123/final) specifically recommends that "system security should not depend on the secrecy of the implementation or its components."

History has been unkind to closed-source cryptosystems. A long list of telecommunications and digital rights management cryptosystems built on secrecy have ultimately been broken in public: components of GSM, GEO-Mobile Radio Interface encryption, GPRS encryption, a number of RFID encryption schemes, and most recently Terrestrial Trunked Radio (TETRA). The pattern is consistent: obscurity buys time, not security.

## Working Openly in a Distributed Community

Because we choose to work openly, secrets present a particular structural difficulty for us. Guardian Project employees and contractors are bound to respect confidentiality by their contracts, but our community is much larger than our payroll. It includes people who work for Guardian Project, people who work for other companies and organizations, and people who work for no one in particular. That diversity is one of our greatest strengths, but it also means we cannot bind a significant portion of the community with an NDA. Any restriction on information sharing under NDA is necessarily limited to the subset of our community that we employ, which hampers our ability to incorporate that information into our standard processes. Working in the open is not just a value; it is a practical match for the way our community is actually structured.

The open approach pays off in the work itself. It invites contributions from a global community of security researchers, computer scientists, and censorship measurement specialists. Academics scrutinize our cryptography, suggest protocol improvements, and identify vulnerabilities we might have missed. They publish papers that advance the entire field, and we fold their findings back into our codebase. This virtuous cycle produces tools stronger than any closed-source alternative could plausibly become.

## Adaptability and Continuity

Publishing open-source code and open designs also enables others to adapt and improve our tools for their local contexts without needing our permission or coordination. A developer in a region we have never considered can fork the repository, modify protocols to evade their specific regional restrictions, and deploy it for their users. That kind of leverage is impossible with a closed product, no matter how well-intentioned the vendor.

Funding for internet freedom work is unpredictable. Grant cycles end. Priorities shift. Political winds blow against the work and then with it again. If a funding gap forces us to halt development on a tool, open source ensures continuity remains possible. Other nonprofits, academic institutions, or volunteer collectives can pick up where we left off, apply security patches, and keep services running for the users who depend on them. Open source is, among other things, an insurance policy against our own organizational mortality.

## Auditing Ourselves Before Adversaries Do

The threat landscape is changing. We are entering a period in which tools that write complex exploits will become publicly available and widely used. The main defense is to have already run those tools against our own code, as a routine part of the development process, before an adversary does. We should be using automated machine analysis — "AI" in some cases — to find weaknesses, vulnerabilities, and exploits in our code and live applications, regardless of whether they are open or closed source. We already use some cloud-based vulnerability and code scanning tools, and because our code is open, we can also benefit from a wide range of pro bono and community auditing tools and services that would not be accessible to a closed project.

## The Clarity in Transarency

A free and open internet cannot be defended by closed and opaque software. The people most in need of privacy and security tools are precisely those least able to take a vendor's word for it. They need to be able to verify, fork, audit, translate, and outlive any single organization that ships code on their behalf. That is what FLOSS makes possible, and it is why we treat it as a baseline commitment rather than an implementation detail.
