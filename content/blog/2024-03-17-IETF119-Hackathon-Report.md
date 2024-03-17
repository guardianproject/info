---
title: "IETF119 Conference Report: Hackathon March 17, 2024"

author: David Oliver

categories:
   - Standards

tags:
   - standards development
   - IETF
   - privacy
---

*Hackathon Weekend at the [119th IETF meeting](https://www.ietf.org/how/meetings/119/) in Brisbane Australia.  This post commences a daily rundown of privacy and Internet Freedom activities at this IETF meeting.*

IETF's Hackathon, held at each face-to-face IETF meeting, is designed to encourage interoperability testing of standards under development. See this meeting's wiki page for a description of[this year's twenty-four projects](https://wiki.ietf.org/en/meeting/119/hackathon).
  
The [The HTTP Signature Authentication Scheme](https://datatracker.ietf.org/doc/draft-ietf-httpbis-unprompted-auth/) has been winding its way through the [HTTPbis Working Group](https://datatracker.ietf.org/wg/httpbis/charter/) since being adopted as a Working Group draft in July 2022. This work proposes a mechanism by which HTTP servers can offer authenticated resources without telegraphing they do so (thus resisting probing attacks).

Until very recently, Guardian Project had the [only extant implementation](https://gitlab.com/guardianproject/httpsignatureauthentation/-/tree/main/http-sigauth-java) of this specification.  It was originally demonstrated at the IETF113 (March 2022) Hackathon.  That changed in the last month with new implementations by [Google](https://github.com/google/quiche/) and [Université catholique de Louvain](https://github.com/francoismichel/http-signature-auth-go). We were able to pull together an interoperability test among these three for the Hackathon!

Interoperability proved surprisingly easy, implying that each of the authors had the same understanding of the wording of the specification, at least for this baseline test.  While we were unable to conduct a full pairwise test across the three server implementations and the three client implementations, we did get sufficient coverage to call it an early win. The testing team agreed more exercise will be necessary on the handling of the three supported HTTP versions as well as a variety of key related issues that will arise with the specification "in practice". Still this effort seems technically solid.

Potentially the most significant issue going forward is defining an approach to integrating this work into the prominent protocol stacks. Since HTTP and TLS have been in the field for more than a quarter century, their programming libraries have ossified (and narrowed) around conventional practices which does not support layer interaction in the manner necessary to support this work.  In particular, this work uses the [keying materials exporter](https://www.openssl.org/docs/man1.1.1/man3/SSL_export_keying_material.html) available at the TLS layer but not currently available in most HTTP layers where this spec needs the keying materials to create the proper HTTP authentication header.  Time will tell.
