---
title: Spearphishing for developers
author: Hans-Christoph Steiner
layout: post
categories:
  - News
tags:
  - phishing
  - security
---

I received an interesting email that points to a new direction in targeting
developers to exploit them.  This email is a reply to a message that I actually
wrote to an [email list](https://mail.gnu.org/archive/html/bug-gnulib/2012-01/msg00336.html)
in 2012, that was posted on a public thread on a public list.  It also uses the
name of a person that posted on that thread: "Paul Eggers".  Oddly, it did not
use that person's actual email from the original thread.  Especially considering
that I replied to the message to ask for more info, but got no answer.  I guess
this was just to ensure that the real "Paul Eggers" did not respond.

The focus of the message is a link to download a file.  This uses a respectable
file sharing service, _onecloud.live.com_ and it even includes a password for
the downloaded file, which seems like it builds up the look of authenticity.
The use of a password-protected ZIP also means it won't be automatically scanned
by malware and anti-virus checkers.

I wasn't able to fully unzip the file using the ZIP tools I used.  That made me
think that perhaps the password method only works in specific ZIP software
packages.  Then the password method would ensure that the ZIP is only run in ZIP
software that is vulnerable to the included exploit. And otherwise, the contents
would not be readable for further inspection.

This points to an attack method that I have not encountered before.
Spearphishing relies on building up a story so that even a careful user will
want to click the link and execute the contents.  Getting a reply to a thread is
an effective way to do that.  The contents of public lists are easily readable
and indexable, so this kind of attack can be highly automated.  Just put in a
target email, and the automation sends the target a message with context.

Here's the full email source:


```
Return-Path: <info@long.frog.tw>
Delivered-To: gphans@rodolpho.mayfirst.org
Received: from rodolpho.mayfirst.org
	by rodolpho.mayfirst.org with LMTP
	id hSGSC25fFmL8LAAAME+P1Q
	(envelope-from <info@long.frog.tw>)
	for <gphans@rodolpho.mayfirst.org>; Wed, 23 Feb 2022 11:23:10 -0500
Received: from rodolpho.mayfirst.org (localhost [127.0.0.1])
	by rodolpho.mayfirst.org (Postfix) with ESMTP id D9F313CE34
	for <hans@guardianproject.info>; Wed, 23 Feb 2022 11:23:06 -0500 (EST)
X-Spam-Checker-Version: SpamAssassin 3.4.2 (2018-09-13) on
	rodolpho.mayfirst.org
X-Spam-Level: 
X-Spam-Status: No, score=0.7 required=5.0 tests=DKIM_SIGNED,DKIM_VALID,
	HTML_MESSAGE,HTML_MIME_NO_HTML_TAG,MIME_HTML_ONLY,RCVD_IN_MSPIKE_H2,
	SPF_HELO_PASS,SPF_PASS,T_SCC_BODY_TEXT_LINE autolearn=disabled
	version=3.4.2
X-Spam-Language: en
X-Envelope-From: <info@long.frog.tw>
X-Greylist: delayed 1661 seconds by postgrey-1.36 at rodolpho; Wed, 23 Feb 2022 11:23:06 EST
Received: from mg3.eee.tw (mg3.eee.tw [103.17.10.233])
	(using TLSv1.2 with cipher AECDH-AES256-SHA (256/256 bits))
	(No client certificate requested)
	by rodolpho.mayfirst.org (Postfix) with ESMTPS id 858E03CE1E
	for <hans@guardianproject.info>; Wed, 23 Feb 2022 11:23:06 -0500 (EST)
Received: from cp21.g-dns.com (cp21.g-dns.com [103.17.8.40])
	(using TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits))
	(No client certificate requested)
	by mg3.eee.tw (Postfix) with ESMTPS id AF4F419009B3
	for <hans@guardianproject.info>; Wed, 23 Feb 2022 23:54:59 +0800 (CST)
DKIM-Filter: OpenDKIM Filter v2.11.0 mg3.eee.tw AF4F419009B3
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=mg3.eee.tw;
	s=default; t=1645631699;
	bh=MvWrTbFx4VjqxMbQ1oeJJLPDVIB1s899FwwgZkbZ1wQ=;
	h=Date:From:To:Subject:From;
	b=JwtVM6G26JoedbLznxwWCmDxeFdQK2eAjM0spiAV8JGrfqpH1+MVTJ7V+8jItocF6
	 PbzZ70Ryif/OnczcFbObjb966oc8G4HfyXFid8QzoCc2x///YtHxybz/dpv01grV+/
	 7Nu86lLukMGzGcQr2C3Lhgz9Gakdx8j2fNSoWIBw=
Received: from 104.120.6.109.rev.sfr.net ([109.6.120.104]:40052 helo=mail.long.frog.tw)
	by cp21.g-dns.com with esmtpsa  (TLS1.2) tls TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
	(Exim 4.94.2)
	(envelope-from <info@long.frog.tw>)
	id 1nMtyx-005qBz-Pz
	for hans@guardianproject.info; Wed, 23 Feb 2022 23:54:59 +0800
MIME-Version: 1.0
Date: Wed, 23 Feb 2022 07:54:58 -0800
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: 7bit
X-Priority: 3 (Normal)
From: "Paul Eggert" <info@long.frog.tw>
To: "Hans-Christoph Steiner" <hans@guardianproject.info>
Subject: Re: sys/types.h on Android includes stdint.h before defining time_t
Message-ID: <uwhaose67qs7epo7ckd62gsd8qqz0kkn@long.frog.tw>
X-YuanJhen-MailScanner-Information: Please contact the ISP for more information
X-YuanJhen-MailScanner-ID: AF4F419009B3.AB186
X-YuanJhen-MailScanner: Not scanned: please contact your Internet E-Mail Service Provider for details
X-YuanJhen-MailScanner-SpamCheck: not spam, SpamAssassin (not cached,
	score=1.79, required 6, autolearn=disabled, BAYES_60 0.80,
	DKIM_VALID -0.10, HTML_MESSAGE 0.30, HTML_MIME_NO_HTML_TAG 0.38,
	MIME_HTML_ONLY 0.42, T_SCC_BODY_TEXT_LINE -0.01)
X-YuanJhen-MailScanner-SpamScore: 1
X-YuanJhen-MailScanner-From: info@long.frog.tw
X-Virus-Scanned: ClamAV using ClamSMTP

Hi,<br />
I have not seen any reply about the receipt documentation I sent you before. Have you checked it?<br />
In case it wasn't delivered, here I upload it again:<br />
<br />
<br />
https://onedrive.live.com/download?cid=8E46FC281A596F46&amp;resid=8E46FC281A596F46%21106&amp;authkey=AOYFYKwyPe_KuGI<br />
<br />
<br />
<br />
<br />
<br />
File password: WT5667<br />
<br />
On 01/26/2012 12:14 PM, Hans-Christoph Steiner wrote:
> ./stdint.h:32:3: error: invalid preprocessing directive #@

This looks like some sort of problem in the way the patch
was applied.  Perhaps you need to re-run gnulib-tool,
or ./bootstrap, or ./autogen.sh, or whatever-it-is-with
your package, to re-import the patched gnulib from scratch.
```

**Update March 23rd, 2022**

So I never received a reply from the email I replied to, so this does not seem
to be a very sophisticated attack.  Plus now, I've received the same kind of
message again responding to the same thread.  It has a different email address
in the _From:_ field, and talks about invoices.  So it seems clear that this is
an automated mass spam operation, not so targeted.  Plus replying to a technical
thread with a message about invoices or receipts seems quite tone deaf.

Here's the full source text of this new message:

```
Return-Path: <INSERT.INTO@arbonnetruth.com>
Delivered-To: gphans@rodolpho.mayfirst.org
Received: from rodolpho.mayfirst.org
	by rodolpho.mayfirst.org with LMTP
	id SAA4IDlXO2KkcgAAME+P1Q
	(envelope-from <INSERT.INTO@arbonnetruth.com>)
	for <gphans@rodolpho.mayfirst.org>; Wed, 23 Mar 2022 13:22:01 -0400
Received: from rodolpho.mayfirst.org (localhost [127.0.0.1])
	by rodolpho.mayfirst.org (Postfix) with ESMTP id AE00E3CE3B
	for <hans@guardianproject.info>; Wed, 23 Mar 2022 13:21:59 -0400 (EDT)
X-Spam-Checker-Version: SpamAssassin 3.4.2 (2018-09-13) on
	rodolpho.mayfirst.org
X-Spam-Level: ***
X-Spam-Status: No, score=3.2 required=5.0 tests=DKIM_SIGNED,DKIM_VALID,
	DKIM_VALID_AU,DKIM_VALID_EF,HTML_MESSAGE,HTML_MIME_NO_HTML_TAG,
	MIME_HTML_ONLY,RCVD_IN_PSBL,SPF_HELO_PASS,SPF_PASS,
	T_SCC_BODY_TEXT_LINE autolearn=disabled version=3.4.2
X-Spam-Language: en
X-Envelope-From: <INSERT.INTO@arbonnetruth.com>
X-Greylist: delayed 601 seconds by postgrey-1.36 at rodolpho; Wed, 23 Mar 2022 13:21:59 EDT
Received: from arbonnetruth.com (arbonnetruth.com [93.170.123.227])
	(using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
	 key-exchange X25519 server-signature RSA-PSS (2048 bits) server-digest SHA256)
	(No client certificate requested)
	by rodolpho.mayfirst.org (Postfix) with ESMTPS id 596443CE1C
	for <hans@guardianproject.info>; Wed, 23 Mar 2022 13:21:59 -0400 (EDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; s=mail; d=arbonnetruth.com;
 h=MIME-Version:Date:Content-Type:Content-Transfer-Encoding:From:To:Subject:
 Message-ID; i=INSERT.INTO@arbonnetruth.com;
 bh=tyizJcC18eXfvncOzYHJ5lCpMuLeYzPK5gBPVLAfqRw=;
 b=O19O9I/UZQxRYOrfLzW3V+Olc/uEnUNezLzdN+XqMNb4Boj5KBxyjgsQy5h18K0uBoyNF5UKQyg8
   tqaKIYKt4PPu8K4BqLrbyXZ0UfpeTQ2oxZ7uTILWi1W+LUTz9fVGfC5lulA1q2YOlJ+Q2YNEDnFq
   +m+bHLzVQwIJX8wT04A=
MIME-Version: 1.0
Date: Wed, 23 Mar 2022 09:11:54 -0800
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: 7bit
X-Priority: 3 (Normal)
From: "Paul Eggert" <INSERT.INTO@arbonnetruth.com>
To: "Hans-Christoph Steiner" <hans@guardianproject.info>
Subject: Re: sys/types.h on Android includes stdint.h before defining time_t
Message-ID: <2lixlvd5g6qeonv0dkkyzyjbbx1foep1@arbonnetruth.com>
X-Virus-Scanned: ClamAV using ClamSMTP

Greetings,<br />
Kindly review a next invoice documentation:<br />
<br />
<br />
https://onedrive.live.com/download?cid=1D05D1D2994A703C&amp;resid=1D05D1D2994A703C%21116&amp;authkey=AALIqV8bfVVLE9E<br />
<br />
File password: MT7658<br />
<br />
On 01/26/2012 12:14 PM, Hans-Christoph Steiner wrote:
> ./stdint.h:32:3: error: invalid preprocessing directive #@

This looks like some sort of problem in the way the patch
was applied.  Perhaps you need to re-run gnulib-tool,
or ./bootstrap, or ./autogen.sh, or whatever-it-is-with
your package, to re-import the patched gnulib from scratch.

```
