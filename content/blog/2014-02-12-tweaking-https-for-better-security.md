---
id: 12251
title: Tweaking HTTPS for Better Security
date: 2014-02-12T19:14:59-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12251
permalink: /2014/02/12/tweaking-https-for-better-security/
categories:
  - News
tags:
  - bazaar
  - encryption
  - howto
  - https
  - security
  - ssl
  - tls
---
The HTTPS protocol is based on TLS and SSL, which are standard ways to negotiate encrypted connections. There is a lot of complexity in the protocols and lots of config options, but luckily most of the config options can be ignored since the defaults are fine. But there are some things worth tweaking to ensure that as many connections as possible are using reliable encryption ciphers while providing [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy). A connection with forward secrecy provides protection to past transactions even if the server&#8217;s HTTPS private key/certificate is stolen or compromised. This protects your users from large scale network observers that can store all traffic for later decryption, like governments, ISPs, telecoms, etc. From the server operator&#8217;s point of view, it means less risk of leaking users&#8217; data, since even if the server is compromised, past network traffic will probably not be able to be encrypted.

In my situation, I was using our development site, <a href="https://dev.guardianproject.info" target="_blank">https://dev.guardianproject.info</a>, as my test bed, it is Apache 2.2 and openssl 1.0.1 running on Ubuntu/precise 12.04 Long-Term Support, so that means that some of the options are more limited since this is an older release. On Debian, Ubuntu and other Debian-derivatives, you&#8217;ll only need to edit `/etc/apache2/mods-available/ssl.conf`. There are more paranoid resources <a href="https://community.qualys.com/blogs/securitylabs/2013/08/05/configuring-apache-nginx-and-openssl-for-forward-secrecy" target="_blank">for perfectly configuring your TLS</a>, but we&#8217;re not ready to drop support for old browsers that only support SSLv3, and not TLS at all. So I went with this line to enable SSLv3 and TLSv1.0 and newer:  
`<br />
SSLProtocol all -SSLv2<br />
` 

With TLS connections, the client and the server each present a list of encryption ciphers that represent the ciphers they each support in order of preference. This enables the client and server to choose a cipher that both support. Normally, the client&#8217;s list takes precedence over the server&#8217;s, but with many browsers that can be changed. Unfortunately it seems that Microsoft Internet Explorer (IE) ignores this and always uses the client&#8217;s preference first. Here&#8217;s how to make Apache request that the server preferences are preferred:  
`<br />
SSLHonorCipherOrder on<br />
` 

Next up is tweaking the server&#8217;s preference list to put ciphers that enable forward secrecy first (don&#8217;t worry if you don&#8217;t understand the next stuff about my rationale, my aim is to walk thru the process). This is done in most web servers using openssl-style cipher lists. I started out with <a href="https://wiki.mozilla.org/Security/Server_Side_TLS" target="_blank">what Mozilla recommends</a>, then pared down the list to remove AES-256 ciphers, since AES-128 is widely regarded to be faster, quite strong, and perhaps <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#Prioritization_logic" target="_blank">more resistant to timing attacks than AES-256</a>. I also chose to remove RC4-based ciphers, since <a href="https://wiki.mozilla.org/Security/Server_Side_TLS#RC4_weaknesses" target="_blank">RC4 might already be broken</a>, and will only get worse with time. RC4 has historically been used to mitigate the &#8220;BEAST&#8221; attack, but that is <a href="https://community.qualys.com/blogs/securitylabs/2013/09/10/is-beast-still-a-threat" target="_blank">mostly happening in the clients now</a>. So with that I ended up with this cipher list (should be all one line in your config file):  
`<br />
SSLCipherSuite "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-CAMELLIA128-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:CAMELLIA128-SHA:DES-CBC3-SHA"<br />
` 

One thing to make sure is that all of these ciphers are supported on your system. You can get the list of supported ciphers from `openssl ciphers`. I used this command line to get them in a nice, alphabetized list:  
`<br />
openssl ciphers | sed 's,:,\n,g' | sort<br />
` 

Lastly, we want to set the <a href="https://www.owasp.org/index.php/HTTP_Strict_Transport_Security" target="_blank">HSTS</a> header to tell the browser to always use HTTPS. To enforce this, a header is added to the collection of HTTP headers delivered when connecting to the HTTPS site. This header tells the client browser to always connect to the current domain using HTTPS. It includes an expiration date (aka `max-age`) after which, the client browser will again allow HTTP connections to that domain. The server might then again redirect the HTTP connection to HTTPS, and again the client will get the HSTS header, and use only HTTPS until the expiration date comes again. To include this header in your Apache server, add this line:  
`<br />
Header add Strict-Transport-Security "max-age=15768000;includeSubDomains"<br />
` 

Now you can check the results of your work with Qualys&#8217; handy SSL Test. You can see the result of my efforts here: <a href="https://www.ssllabs.com/ssltest/analyze.html?d=dev.guardianproject.info" target="_blank">https://www.ssllabs.com/ssltest/analyze.html?d=dev.guardianproject.info</a>. **A-** is not bad. I tried for a good long while to get IE to use FS (Forward Secrecy) ciphers, but failed. IE does not respect the server-side cipher preferences. My guess is that the only way to get IE to use FS ciphers is to make a custom cipher list that does not include anything but FS ciphers and serve that only to IE. I know it is possible to do because <a href="https://www.ssllabs.com/ssltest/analyze.html?d=bitbucket.com&#038;s=131.103.20.172" target="_blank">bitbucket.com got an <strong>A+</strong> for doing it</a>. For a quick way to check out the cipher lists and HSTS header, look at <a href="https://github.com/iSECPartners/sslyze" target="_blank">iSEC Partner&#8217;s sslyze</a>.

This is only a quick overview of the process to outline the general concepts. To find out more I recommend reading the source articles for this post, including specific directions for nginx and lighttpd:

  * Mozilla&#8217;s <a href="https://wiki.mozilla.org/Security/Server_Side_TLS" target="_blank">Server-side TLS</a>
  * Qualys&#8217; <a href="https://community.qualys.com/blogs/securitylabs/2013/08/05/configuring-apache-nginx-and-openssl-for-forward-secrecy" target="_blank">Configuring Apache, Nginx, and OpenSSL for Forward Secrecy</a>
  * Qualys&#8217; <a href="https://community.qualys.com/blogs/securitylabs/2013/09/10/is-beast-still-a-threat" target="_blank">Is BEAST Still a Threat?</a>
  * <a href="https://www.owasp.org/index.php/HTTP_Strict_Transport_Security" target="_blank">HTTP Strict Transport Security</a>