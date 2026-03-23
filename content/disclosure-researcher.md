---
id: 11675
title: Researcher Disclosure Policy
date: 2026-03-23T12:47:19-04:00
author: n8fr8
guid: https://guardianproject.info/disclosure-researcher/
menu:
  main:
    parent: contact
---

Guardian Project regularly conducts security research, audits, and penetration testing on behalf of partners and the broader open-source community. When we discover vulnerabilities in the software, infrastructure, or services of others, we follow a coordinated disclosure process grounded in [OWASP best practices](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html) and our commitment to improving security for all users.

This policy describes how we handle vulnerabilities we find in **other organizations' projects**. For reporting vulnerabilities in **our** projects, please see our [Responsible Disclosure Policy](/disclosure/).

## Scope

This policy applies when Guardian Project team members, in the course of their work, discover security vulnerabilities in:

- Open-source software projects maintained by other organizations or individuals
- Third-party services or infrastructure used by our projects or partners
- Software or systems we are engaged to audit or test under a formal agreement
- Any system where a vulnerability poses a meaningful risk to user safety or privacy

## Our Disclosure Process

We follow a coordinated disclosure model. Our goal is to ensure vulnerabilities are fixed and users are protected before technical details become public.

### 1. Initial Discovery and Verification

When we identify a potential vulnerability, we will:

- Verify the issue is reproducible and confirm it represents a genuine security risk
- Assess the severity and potential impact, using [CVSS](https://www.first.org/cvss/) or an equivalent framework where appropriate
- Document the vulnerability thoroughly, including steps to reproduce, proof-of-concept code, and affected versions
- Ensure we have not accessed, modified, or stored any user data beyond what is minimally necessary to confirm the issue

### 2. Identifying the Right Contact

Before making a report, we will make a good-faith effort to identify the appropriate security contact by checking:

- The organization's `/.well-known/security.txt` file
- Bug bounty program pages (e.g., on HackerOne, Bugcrowd, or huntr.dev)
- Dedicated security reporting addresses (e.g., `security@`)
- GitHub Security Advisories for open-source projects
- The project's documentation or contact pages

If we cannot identify a direct security contact, we will request one through general communication channels without disclosing vulnerability details. For organizations that are particularly difficult to reach, we may contact a relevant national or sector CERT for assistance.

### 3. Private Disclosure to the Vendor

We will privately report the vulnerability to the affected organization, including:

- A clear, non-threatening description of the vulnerability written for a broad technical audience
- Step-by-step reproduction instructions
- Proof-of-concept code, HTTP requests/responses, screenshots, or other evidence as appropriate, with any personal or sensitive data redacted
- An assessment of the severity and potential impact
- Recommended mitigations or fixes, where we are able to provide them
- Our proposed disclosure timeline (see below)

**We strongly prefer encrypted communication for vulnerability reports.** We will use PGP, Signal, or whatever secure channel the organization provides.

### 4. Coordination Period

After initial contact, we will:

- Work collaboratively with the vendor to understand the issue and develop a fix
- Provide retesting assistance if requested
- Allow reasonable time for the organization to triage, develop, and deploy a patch
- Maintain confidentiality during the coordination period
- Follow up professionally if we do not receive a timely response

### 5. Public Disclosure

Once the vulnerability is resolved, or after the disclosure deadline has passed, we may publish an advisory (see **Disclosure Timeline** and **Publishing** below).

## Disclosure Timeline

We follow a **90-day disclosure deadline** from the date of our initial report, consistent with widely accepted industry practice. This means:

- **Day 0**: We send our initial private report to the vendor.
- **Within 3 business days**: We expect acknowledgment of receipt.
- **Within 90 days**: We expect the vendor to develop and release a fix.
- **After 90 days**: We reserve the right to publish details of the vulnerability.

We will adjust this timeline in the following circumstances:

- **Critical vulnerabilities actively being exploited**: We may shorten the timeline significantly and work with the vendor on an emergency basis.
- **Vendor requests a reasonable extension**: If the vendor is actively working on a fix and communicates clearly, we will consider granting additional time.
- **Vendor is unresponsive**: If we receive no acknowledgment within 30 days despite repeated good-faith contact attempts, we may proceed with disclosure at our discretion.
- **Formal audit engagements**: Timelines may be governed by the terms of the engagement agreement.

## Handling Unresponsive Vendors

If an organization does not respond to our reports despite repeated contact attempts, we will consider the following options on a case-by-case basis:

- **Escalation to a CERT**: We may report the vulnerability to a relevant national or sector CERT, who can assist in coordinating with the vendor.
- **Reporting to regulators**: Where the vulnerability poses a significant risk to user safety and the vendor remains unresponsive, we may report to appropriate regulatory bodies.
- **Limited public disclosure**: We may publish a limited advisory describing the risk and available mitigations without providing full exploitation details, to help affected users protect themselves.

We will not pursue public disclosure solely out of frustration. Our decisions will always prioritize user safety and the public interest.

## Publishing

When we publish a vulnerability disclosure, it will typically include:

- A high-level summary of the vulnerability and its impact
- The affected software, versions, and components
- Technical details sufficient for defenders to assess their exposure
- Patched versions and available mitigations or workarounds
- A timeline of discovery, reporting, and resolution
- Links to the vendor's advisory, CVE identifiers, or patch notes
- Credit to any collaborating researchers, with their permission

### Proof-of-Concept Code

We will use careful judgment when deciding whether to publish proof-of-concept code. We will consider:

- Whether a patch has been widely deployed
- Whether the vulnerability can be reverse-engineered from the patch itself
- The potential for the proof-of-concept to be used for harm versus its value for defenders and educators
- Any agreements made with the vendor regarding publication

### Bug Bounty Programs

When a vulnerability falls within the scope of a bug bounty program, we will follow the program's rules regarding disclosure and publication timelines. Any bounty payments received will be handled in accordance with applicable tax and legal requirements. We do not condition our disclosure on payment.

## Legal and Ethical Commitments

In all of our security research and disclosure activities, we commit to:

- **Complying with applicable laws** in all relevant jurisdictions
- **Acting in good faith** to improve security, not to cause harm or seek undue advantage
- **Minimizing impact** by limiting testing to what is necessary to confirm a vulnerability
- **Respecting privacy** by never accessing, exfiltrating, or storing user data beyond the minimum needed to demonstrate an issue
- **Never demanding payment** in exchange for withholding vulnerability details
- **Maintaining professionalism** in all communications, even when met with hostility or indifference
- **Protecting sources** when we receive vulnerability information from third parties

## Formal Engagements

When we conduct security audits or penetration tests under a formal agreement, the terms of that agreement take precedence over this general policy. However, we will always advocate for timely disclosure and user protection in the scope and terms of any engagement we accept.

## Questions

If you are a vendor or maintainer who has received a vulnerability report from us and have questions about this policy or our process, please reach out to us via any method on our [Contact page](/contact/).

If you are a fellow researcher who would like to coordinate on a disclosure, we welcome collaboration — please contact us as well.
