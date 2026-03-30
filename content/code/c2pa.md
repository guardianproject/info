---
title: 'Proofmode and C2PA'
date: 2024-01-01T00:00:00-04:00
author: n8fr8
menu:
  main:
    parent: code
---

**Defending Reality with Code**

[Proofmode](https://proofmode.org) is a technology platform designed to authenticate and verify digital media, developed collaboratively by Guardian Project, WITNESS, and Okthanks since 2013. It provides tools for adding signed [C2PA](https://c2pa.org/) actions, claims, and attestations to media files.

## Core Products

- **Capture** - A mobile camera application with built-in provenance tracking
- **Verify** - Inspect and analyze multimedia metadata
- **Identify** - Device verification and attestation signing services
- **Connect** - Secure communication with media provenance preservation
- **Enhance** - AI safety through provenance and authentication workflows

## Developer Integration

Proofmode provides mobile SDKs for Android and iOS, enabling developers to integrate media authentication and provenance into their own apps. C2PA support is available through:

- **C2PA 1.x** via SimpleC2PA, built on the C2PA Rust library
- **C2PA 2.x** (beta) through official mobile SDKs developed with Adobe
- Tools for generating private keys and self-signed certificates on-device
- Legacy libProofMode libraries for custom integration

The technology serves journalists, humanitarian organizations, businesses, and individuals needing to verify media authenticity or establish verifiable proof chains.

**Learn more at [proofmode.org/build](https://proofmode.org/build)**
