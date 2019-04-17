---
id: 12868
title: Phishing for developers
date: 2015-02-24T04:41:29-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12868
permalink: /2015/02/24/phishing-for-developers/
spacious_page_layout:
  - default_layout
categories:
  - News
tags:
  - 2-Step Verification
  - bazaar
  - Google Authenticator
  - phishing
  - security
  - two-factor authentication
---
I recently received a very interesting phishing email directed at developers with apps in Google Play. One open question is, how targeted it was: did anyone else get this?

[<img src="https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing.jpg" alt="320px-Trawling_Drawing" width="320" height="240" class="alignright size-full wp-image-12873" srcset="https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing.jpg 320w, https://guardianproject.info/wp-content/uploads/2015/02/320px-Trawling_Drawing-300x225.jpg 300w" sizes="(max-width: 320px) 100vw, 320px" />](https://en.wikipedia.org/wiki/File:Trawling_Drawing.jpg)  
It turns out that Google has been recently stepping up enforcement of certain terms, so it looks like some people are taking advantage of that. It is a pretty sophisticated or manually targeted phishing email since they got the name of the app, email address, and project name all correct. The one detail that gives it away is that the `From:` address uses the fake domain, even though it would have been possible to send the email using the actual Google account in the `From:` field. But this likely would have triggered spam and malware detection algorithms. So they took a subtly different approach by using a real Google address in the `Reply-To:`. But they were clever enough to use the same sub-domain, `gooogle.com.de`, in the From: address as in the phishing link `accounts.gooogle.com.de`, following a Google pattern of subdomains. They also included other real Google links for support and as a &#8220;follow up&#8221; URL.

When I received this, I didn&#8217;t notice the clickable link in the email since I never view HTML email. I forwarded it on to our internal email list where others figured out it was fake. In the HTML version of the email, it has this link from the fake domain `accounts.gooogle.com.de`:

<pre>&lt;p&gt;&lt;b&gt;Your application will be removed&lt;/b&gt; if you do not sign in to the &lt;a
href="http://accounts.gooogle.com.de/ServiceLogin?service=androiddeveloper&passive=1209600&continue=https://play.google.com/apps/publish/&followup=https://play.google.com/apps/publish/&type=3days&pkg=org.torproject.android"&gt;Developer
Console&lt;/a&gt;
</pre>

This attacker might have been targeting anyone who would fall for the trick, without really caring what kind of app it was. For any accounts that the attacker got access to, they would be able to change the description text, home page, email address, etc. transparently without raising any particular warning signs. The attacker could place a recommendation in the app descriptions to also install another app, and that app would be the attacker&#8217;s malware.

The attacker could not upload their own updates to an existing app, because Google Play checks uploaded APKs to make sure that the signing keys match the APKs that are already there. The attacker could create a whole new app in that developer&#8217;s account, and hope to gain installs since it would be related. Google Play has a standard view to show users apps by the same developer, for example.

**Two-factor authentication and beyond**

If a developer fell for this phishing attack, but had the forethought to have set up <a href="https://support.google.com/accounts/answer/180744" target="_blank">Google 2-Step Verification</a>, then even if the phisher got the username and password, they would be unable to log into that account since they would not have access to the two-factor SMS or <a href="https://support.google.com/accounts/answer/1066447" target="_blank">Google Authenticator</a> message. All developer accounts on Google Play should be required to use Google 2-Step Verification. Set it up **now**, if you have not already!

We also need to consider the kinds of sophisticated attacks from large state actors that are leaking out to the public. Indeed, many of these attacks are also available for any government to <a href="https://netzpolitik.org/2014/gamma-finfisher-hacked-40-gb-of-internal-documents-and-source-code-of-government-malware-published/" target="_blank">purchase from companies like Finfisher</a>. And it is only a matter of time before these techniques are widespread and easier, following the rule of &#8220;attacks never get worse; they only get better&#8221;. This phishing website could also contain malicious Javascript that installs malware that can both log all key strokes in search of passwords, as well as search for known secret caches like Java keystores for Android signing keys, and browser cookies that allow the user to skip two-factor authentication, like the <a href="https://support.google.com/accounts/answer/2544838" target="_blank">cookie from Google&#8217;s two-step authentication</a>.

One takeaway here: developers should **never** keep or use their APK signing keys on a machine that they also use to read email and browse the web.

**Full source of the email**

Here is the full source of the original email that I received, for those who might be interested in digging deeper. Another detail you can see there is that the email was not sent using Google infrastructure at all.

<pre>Return-Path: &lt;n&#x6f;&#x72;e&#x70;&#x6c;y&#x2d;&#x64;e&#x76;&#x65;l&#x6f;&#x70;e&#x72;&#x2d;g&#x6f;&#x6f;g&#x6c;&#x65;p&#x6c;&#x61;y&#x40;&#x67;o&#x6f;&#x6f;g&#108;&#x65;.&#99;&#x6f;m&#46;&#x64;e&gt;
X-Spam-Checker-Version: SpamAssassin 3.3.2 (2011-06-06) on
	rodolpho.mayfirst.org
X-Spam-Level: *
X-Spam-Status: No, score=1.3 required=5.0 tests=HTML_MESSAGE,RDNS_NONE
	autolearn=disabled version=3.3.2
X-Original-To: &#115;&#x75;p&#x70;o&#x72;t&#x40;g&#117;&#x61;&#114;&#x64;i&#x61;n&#x70;r&#111;&#x6a;&#101;&#x63;t&#x2e;i&#x6e;f&#x6f;
Delivered-To: gph&#97;&#110;&#x73;&#x40;&#x72;&#x6f;&#x64;olp&#104;&#111;&#x2e;&#x6d;&#x61;&#x79;&#x66;irs&#116;&#46;&#x6f;&#x72;&#x67;
Received: from rodolpho.mayfirst.org (localhost [127.0.0.1])
	by rodolpho.mayfirst.org (Postfix) with ESMTP id 4CFCD5E3D
	for &lt;&#x73;&#x75;&#x70;&#112;&#111;rt&#64;&#x67;&#x75;&#x61;&#x72;&#100;ian&#x70;&#x72;&#x6f;&#x6a;&#101;ct.&#x69;&#x6e;&#x66;&#x6f;&gt;; Fri, 20 Feb 2015 04:30:50 -0500 (EST)
X-Greylist: delayed 543 seconds by postgrey-1.34 at rodolpho; Fri, 20 Feb 2015
04:30:49 EST
Received: from astra1695.startdedicated.com (unknown [85.25.194.40])
	by rodolpho.mayfirst.org (Postfix) with ESMTP id D74C83CD84
	for &lt;su&#112;&#x70;&#x6f;&#x72;t&#64;&#103;&#x75;&#x61;&#x72;di&#97;&#x6e;&#x70;&#x72;oje&#99;&#x74;&#x2e;&#x69;nf&#111;&gt;; Fri, 20 Feb 2015 04:30:48 -0500 (EST)
Received: from gooogle.com.de (astra1695 [85.25.194.40])
	by astra1695.startdedicated.com (Postfix) with ESMTPA id 209D57C0918
	for &lt;s&#117;&#x70;&#x70;or&#x74;&#x40;gu&#97;&#x72;&#x64;i&#97;&#x6e;&#x70;ro&#x6a;&#x65;ct&#46;&#x69;&#x6e;f&#111;&gt;; Fri, 20 Feb 2015 10:21:32 +0100 (CET)
Date: Fri, 20 Feb 2015 09:21:32 +0000
To: The Tor Project &lt;&#x73;u&#x70;p&#x6f;&#114;t&#x40;g&#x75;&#97;r&#x64;i&#x61;&#110;p&#x72;o&#x6a;e&#x63;&#x74;.&#x69;n&#x66;&#111;&gt;
From: Google Play Developer Support &lt;&#110;&#x6f;r&#x65;p&#x6c;y&#x2d;d&#101;&#x76;&#101;&#x6c;o&#x70;e&#x72;-&#103;&#x6f;&#111;&#x67;l&#x65;p&#x6c;a&#x79;&#64;&#103;&#x6f;&#111;&#x6f;g&#x6c;e&#x2e;c&#111;&#x6d;&#46;&#x64;e&gt;
Reply-To: Google Play Developer Support &lt;nore&#112;&#108;&#x79;&#x2d;&#x64;&#x65;&#x76;&#x65;loper&#45;&#103;&#x6f;&#x6f;&#x67;&#x6c;&#x65;&#x70;lay&#64;&#103;&#111;&#x6f;&#x67;&#x6c;&#x65;&#x2e;&#x63;om&gt;
Subject: 7-Day Notification of Google Play Developer Term Violation
Message-ID: &lt;7f&#55;&#x32;&#x35;&#x34;&#x30;08&#55;&#99;&#x38;&#x31;&#x66;fe2&#101;&#x61;&#x64;&#x35;604&#50;&#x35;&#x64;&#x30;d47&#55;&#x40;&#x67;&#x6f;oog&#108;&#x65;&#x2e;&#x63;om.&#100;&#x65;&gt;
X-Priority: 3
X-Mailer: PHPMailer 5.2.9 (https://github.com/PHPMailer/PHPMailer/)
MIME-Version: 1.0
Content-Type: multipart/alternative;
	boundary="b1_7f72540087c81ffe2ead560425d0d477"
Content-Transfer-Encoding: 8bit
X-Virus-Scanned: ClamAV using ClamSMTP

--b1_7f72540087c81ffe2ead560425d0d477
Content-Type: text/plain; charset=us-ascii

Hello Google Play Developer,
This is a notification that your application, Orbot: Proxy with Tor, with
package ID org.torproject.android, is currently in violation of our developer
terms.
REASON FOR WARNING: Violation of the spam provisions of the Content Policy.
Please refer to the spam policy help article for more information.
Do not use irrelevant, misleading, or excessive keywords in apps descriptions,
titles, or metadata.
Please refer to the keyword spam policy help article for more information.
Your application will be removed if you do not sign in to the Developer
Console and make modifications to your application's description to bring it
into compliance within 7 days of the issuance of this notification.If you have
additional applications in your catalog, please also review them for
compliance. Note that any remaining applications found to be in violation will
be removed from the Google Play Store.
Please also consult the Policy and Best Practices and the Developer
Distribution Agreement as you bring your applications into compliance. You can
also review this Google Play Help Center article for more information on this
warning.
All violations are tracked. Serious or repeated violations of any nature will
result in the termination of your developer account, and investigation and
possible termination of related Google accounts.
Regards,
Google Play Team
1600 Amphitheatre Parkway
Mountain View, CA 94043


--b1_7f72540087c81ffe2ead560425d0d477
Content-Type: text/html; charset=us-ascii

&lt;p&gt;Hello Google Play Developer,&lt;/p&gt;
&lt;p&gt;This is a notification that your application, &lt;b&gt;Orbot: Proxy with Tor&lt;/b&gt;,
with package ID &lt;b&gt;org.torproject.android&lt;/b&gt;, is currently in violation of
our developer terms.&lt;br /&gt;
&lt;b&gt;REASON FOR WARNING&lt;/b&gt;: Violation of the spam provisions of the Content
Policy. Please refer to the spam policy help article for more information.&lt;/p&gt;
&lt;p&gt;Do not use irrelevant, misleading, or excessive keywords in apps
descriptions, titles, or metadata.&lt;br /&gt;
Please refer to the keyword spam policy help article for more information.&lt;/p&gt;
&lt;p&gt;&lt;b&gt;Your application will be removed&lt;/b&gt; if you do not sign in to the &lt;a
href="http://accounts.gooogle.com.de/ServiceLogin?service=androiddeveloper&passive=1209600&continue=https://play.google.com/apps/publish/&followup=https://play.google.com/apps/publish/&type=3days&pkg=org.torproject.android"&gt;Developer
Console&lt;/a&gt; and make modifications to your application&#x27;s description to
bring it into compliance within &lt;b&gt;7 days&lt;/b&gt; of the issuance of this
notification.&lt;br&gt;If you have additional applications in your catalog, please
also review them for compliance. Note that any remaining applications found to
be in violation will be removed from the Google Play Store.&lt;/p&gt;
&lt;p&gt;Please also consult the &lt;a
href="https://support.google.com/googleplay/android-developer/#topic=2364761"&gt;Policy
and Best Practices&lt;/a&gt; and the &lt;a
href="https://play.google.com/about/developer-distribution-agreement.html"&gt;Developer
Distribution Agreement&lt;/a&gt; as you bring your applications into compliance. You
can also review this Google Play Help Center article for more information on
this warning.&lt;br /&gt;
All violations are tracked. Serious or repeated violations of any nature will
result in the termination of your developer account, and investigation and
possible termination of related Google accounts.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br&gt;
Google Play Team&lt;br&gt;
1600 Amphitheatre Parkway&lt;br&gt;
Mountain View, CA 94043&lt;/p&gt;



--b1_7f72540087c81ffe2ead560425d0d477--
</pre>