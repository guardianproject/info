---
id: 11674
title: Responsible Disclosure Policy
date: 2026-03-23T12:47:19-04:00
author: n8fr8
guid: https://guardianproject.info/disclosure/
menu:
  main:
    parent: contact
---

Guardian Project is committed to the security and privacy of our users. We welcome and appreciate security researchers who help us identify vulnerabilities in our projects. This policy outlines how to report security issues and what you can expect from us in return.

## Scope

This policy covers security vulnerabilities found in:

- Any software project developed or maintained by Guardian Project, including but not limited to Orbot, ObscuraCam, Haven, ProofMode, and all libraries and tools published under the [Guardian Project GitHub organization](https://github.com/guardianproject)
- Projects we actively contribute to, where we can coordinate disclosure with the upstream maintainers
- The Guardian Project website and any internet-facing infrastructure we operate

### Out of Scope

The following are **not** covered by this policy:

- Third-party applications or services not developed or maintained by Guardian Project
- General security best practices or hardening suggestions without a demonstrated proof-of-concept
- Social engineering attacks against Guardian Project contributors or users
- Physical attacks against Guardian Project infrastructure
- Denial-of-service attacks
- Spam or social engineering via our communication channels
- Vulnerabilities in dependencies where a patch has been publicly available for less than 30 days
- Clickjacking on pages with no sensitive actions
- Missing HTTP security headers that do not lead to a directly exploitable vulnerability

## How to Report a Vulnerability

**We strongly encourage encrypted or secure communication for vulnerability reports.**

You may report security vulnerabilities through any of the following channels:

- **Email**: [support@guardianproject.info](mailto:support@guardianproject.info) — We recommend encrypting your report using PGP. Our director's PGP key is available on [keybase.io/n8fr8](https://keybase.io/n8fr8) or [pgp.mit.edu](https://pgp.mit.edu/pks/lookup?op=get&search=0xA801183E69B37AA9).
- **Signal**: [+447886176827](https://signal.me/#p/+447886176827)
- **Other methods**: Any contact method listed on our [Contact page](/contact/)

For vulnerabilities in projects hosted on GitHub, you may also use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) to report privately through the relevant repository.

### What to Include in Your Report

Please provide as much of the following information as possible:

- A description of the vulnerability and its potential impact
- The affected project, version, and/or component
- Step-by-step instructions to reproduce the issue
- Any proof-of-concept code, screenshots, or logs
- Your suggested severity rating (e.g., using CVSS)
- Recommendations for remediation, if any

Please submit one vulnerability per report unless multiple issues are closely related.

## What to Expect From Us

- **Acknowledgment**: We will acknowledge receipt of your report within **3 business days**.
- **Assessment**: We will investigate and assess the vulnerability, keeping you informed of our progress.
- **Resolution timeline**: We aim to develop and release a fix within **90 days** of a confirmed vulnerability, depending on complexity. For critical issues, we will work to release a fix as quickly as possible.
- **Coordination**: We will coordinate with you on disclosure timing. If the vulnerability affects an upstream project we contribute to, we will work with those maintainers as well.
- **Credit**: We will publicly credit you for the discovery (unless you prefer to remain anonymous) when we publish a security advisory or release notes for the fix.

## Rules of Engagement

When conducting security research on Guardian Project software, we ask that you:

- **Act in good faith** and work to avoid privacy violations, data destruction, and disruption to our services or users
- **Only interact with accounts you own** or have explicit permission to test
- **Do not exfiltrate data** beyond what is minimally necessary to demonstrate a vulnerability
- **Stop and report** if you encounter user data during testing — do not access, modify, or store it
- **Do not publicly disclose** the vulnerability before we have had a reasonable opportunity to address it and have coordinated a disclosure timeline with you
- **Do not exploit** the vulnerability beyond what is necessary to confirm its existence
- **Do not perform** denial-of-service attacks, social engineering, phishing, or physical security attacks
- **Comply with all applicable laws** in your jurisdiction while conducting research

## Safe Harbor

Guardian Project supports security research conducted under this policy. If you make a good-faith effort to comply with this policy during your research, we will:

- Consider your research to be authorized and will not pursue legal action against you
- Work with you to understand and resolve the issue promptly
- Not file a complaint with law enforcement for activities conducted in accordance with this policy

If legal action is initiated by a third party against you for research conducted in compliance with this policy, we will make it known that your actions were authorized under our responsible disclosure program.

This safe harbor applies only to legal claims under the control of Guardian Project and does not bind independent third parties.

## Public Disclosure

We believe in transparency. Once a vulnerability is resolved, we will:

- Publish a security advisory describing the vulnerability and its fix
- Credit the reporter, with their permission
- Request a CVE identifier for significant vulnerabilities, when applicable

We ask researchers to allow us a reasonable period (typically 90 days) to address vulnerabilities before any public disclosure. If we are unable to resolve an issue within that timeframe, we will work with you to agree on an appropriate disclosure date.

## Questions

If you have questions about this policy or are unsure whether your research falls within scope, please reach out to us via any method on our [Contact page](/contact/) before beginning your research.

Thank you for helping keep Guardian Project and our users safe.

