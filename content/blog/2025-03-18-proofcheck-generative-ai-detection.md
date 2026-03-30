---
title: "Generative AI Detection in ProofCheck"
date: 2025-03-18
author: ProofMode
tags:
  - proofmode
  - proofcheck
  - ai-detection
  - c2pa
---

*Reposted from [proofmode.org](https://proofmode.org/blog/proofcheckai)*

ProofCheck is our free and open-source, multi-purpose "Swiss Army Knife" tool for image, video, and audio metadata inspection. It can work with the "Proof Pack" bundle zip files that are produced by our ProofMode camera app, and it can also inspect any multimedia file you try to throw at it. It will look for metadata formats like EXIF, C2PA, IPTC, and more, and validate ProofMode PGP signatures, OpenTimestamp notarization, and other cryptographic signatures. All of this happens locally in your browser, without any uploads to a server, ensuring privacy of your media and metadata is maintained.

Recently, we also added a specific capability looking for any sign or fingerprint of generative AI activity in media files. To do this, we combine a series of logic inspecting filenames, the EXIF data, as well as any of the create, open, or edit attestations in the C2PA manifest.

While we understand that metadata and watermarks can be stripped, we feel that this free, open, and private utility for inspecting media metadata, with additional enhancements for analysis of "Gen AI Fingerprints" can still be very useful to researchers, journalists, and the general public. In the future, we are also exploring adding in additional capabilities for deeper analysis and inspection at the pixel data level, in order to be able to discover more indicators of media provenance even when there is no metadata present.
