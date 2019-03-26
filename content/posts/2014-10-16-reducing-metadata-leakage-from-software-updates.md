---
id: 12695
title: Reducing metadata leakage from software updates
date: 2014-10-16T12:48:04-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=12695
permalink: /2014/10/16/reducing-metadata-leakage-from-software-updates/
spacious_page_layout:
  - default_layout
has_been_saved:
  - "1"
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "426"
discourse_permalink:
  - https://talk.developersquare.net/t/reducing-metadata-leakage-from-software-updates/306
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":306,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553030246"
wpdc_sync_post_comments:
  - "0"
wpdc_publishing_response:
  - error
categories:
  - News
tags:
  - anonymity
  - bazaar
  - debian
  - encryption
  - gnu/linux
  - howto
  - https
  - linux
  - ssl
  - tails
  - tor
  - ubuntu
---
**Update**: now you can [do this with Tor Onion Services](https://guardianproject.info/2016/07/31/howto-get-all-your-debian-packages-via-tor-onion-services/)

[<img src="https://guardianproject.info/wp-content/uploads/2014/10/leakage-300x199.png" alt="leakage" width="300" height="199" class="alignright size-medium wp-image-12699" srcset="https://guardianproject.info/wp-content/uploads/2014/10/leakage-300x199.png 300w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-100x66.png 100w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-150x99.png 150w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-200x132.png 200w, https://guardianproject.info/wp-content/uploads/2014/10/leakage.png 410w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2014/10/leakage.png)Many software update systems use code signing to ensure that only the correct software is downloaded and installed, and to prevent the code from being altered. This is an effective way to prevent the code from being modified, and because of that, software update systems often use plain, unencrypted HTTP connections for downloading code updates. That means that the metadata of what packages a machine has installed is available in plain text for any network observer, from someone sitting on the same public WiFi as you, to state actors with full network observation capabilities.

That means that potentially private information is leaking. That private information could be which packages you have installed and which versions. That information can help an attacker figure out the best way to break into the target machine. Also, a unique fingerprint can be generated based on which packages a machine has installed, and that could help de-anonymize traffic that goes over Tor or other anonymity tool.

For people who use `apt-get` in Debian, Ubuntu or any related GNU/Linux distro, there is a lot of metadata leaked to the internet when `apt-get` contacts Debian repositories using a standard configuration. Mostly, that is because by default, the connections are unencrypted (http, ftp, rsync). The integrity of the package itself is not reason enough to use HTTPS since the GPG signing is much more reliable for that task. Here is how I break it down:

  1. package authenticity  
    (_software can be modified while being downloaded_)
  2. repo availability  
    ( _whole sites or specific URL paths can be selectively blocked by governments and companies_)
  3. package availability  
    (_software security updates can be individually blocked_)
  4. who’s downloading what package (_currently visible to anyone who can see the  
    network traffic, including open wifi, etc._)

The current apt model covers #1 well, but only covers #2 and #3 with a two week window (the expiration date on the repo metadata). And it does not cover #4 at all. Using HTTPS for apt repos is a simple way to improve the security of all 4. It adds a weak backup security layer for #1, it makes it much more difficult for a portion of a large internet mirror to be seletively blocked (e.g. #2 and #3). For example, if you use HTTPS to mirrors.kernel.org, everything has to be blocked to block Debian repos or packages. And pipelining downloads through a reused HTTPS connection makes it very difficult for the network observer to track metadata about packages, #4).[<img src="https://guardianproject.info/wp-content/uploads/2014/10/leakage-control-150x150.jpg" alt="leakage control" width="150" height="150" class="alignright size-thumbnail wp-image-12701" srcset="https://guardianproject.info/wp-content/uploads/2014/10/leakage-control-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-control-100x100.jpg 100w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-control-200x200.jpg 200w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-control.jpg 300w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2014/10/leakage-control.jpg)

Luckily, there are some relatively easy steps that greatly reduce the amount of metadata that is leaked: using HTTPS connections to the mirrors and running those connections through Tor. Setting `apt-get` to pipeline as many transactions into a given HTTPS session is also useful, but currently only supported for HTTP and not HTTPS. Even though HTTPS/TLS has security weaknesses, it is a lot better than nothing, and can help provide real world protection. The downside is that it is not common for Debian machines to connect to apt mirrors using HTTPS, so that potentially marks the install as a machine worth targeting. There are more and more HTTPS mirrors, and more interest in using them, so I think in time, that will only lessen as a concern. Here are the HTTPS mirrors that I have had good luck with:

  * mirrors.ece.ubc.ca
  * mirrors.kernel.org
  * mirror.cse.unsw.edu.au
  * spout.ussg.indiana.edu

On that note, here is the config that I have been using on a number of Debian-deriv machines, and it has been working well. It requires `apt-transport-https`, and <a href="http://ubuntuguide.org/wiki/Tor#Privoxy" target="_blank"><code>privoxy</code> setup as an HTTP proxy for Tor</a>.

<pre>$ cat /etc/apt/apt.conf.d/99force-tor
# force everything through privoxy HTTP proxy to tor
Acquire::ftp::Proxy "http://127.0.0.1:8118";
Acquire::http::Proxy "http://127.0.0.1:8118";
Acquire::https::Proxy "http://127.0.0.1:8118";

# don't use SSL, its insecure, only use TLS
Acquire::https::SslForceVersion "TLSv1";
</pre>

I have found about 10 official Debian mirrors that have reliable HTTPS. Then I have a <a href="https://gist.github.com/eighthave/7285154" target="_blank">script that finds all of them</a>, but many have self-signed certs and other issues. A number of the HTTPS mirrors also mirror the &#8220;security&#8221; archive, but I recommend that the `http` URL to the official `security.debian.org` repo is still included to make sure that security updates are promptly available.

I also have a test security repo running that is only available via an .onion address. I hope to encourage people to run official mirrors on a Tor Hidden Service, then HTTPS is not needed. Note that `apt-transport-tor` is not required if a tor proxy is setup. To try mine, add it to your `sources.list` (and make sure `apt-get` is somehow using Tor). The order is important, that determines the priority of where `apt-get` will get the package from is all other variables are the same.

<pre>deb http://dju2peblv7upfz3q.onion/debian-security/ wheezy/updates main
deb http://security.debian.org/ wheezy/updates main
</pre>

**Update**: Use the official <a href="https://onion.debian.org/" target="_blank">Debian Tor Onion Services</a> now, <tt>dju2peblv7upfz3q.onion</tt> is deprecated and will be shut down!

### A specific example: TAILS

[<img src="https://guardianproject.info/wp-content/uploads/2014/10/Tails-150x150.png" alt="Tails" width="150" height="150" class="alignleft size-thumbnail wp-image-12711" srcset="https://guardianproject.info/wp-content/uploads/2014/10/Tails-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2014/10/Tails-100x100.png 100w, https://guardianproject.info/wp-content/uploads/2014/10/Tails-200x200.png 200w, https://guardianproject.info/wp-content/uploads/2014/10/Tails.png 256w" sizes="(max-width: 150px) 100vw, 150px" />](https://tails.boum.org/)<a href="https://tails.boum.org/" target="_blank">TAILS</a> is an operating system that aims to be as private and anonymous as possible to enable, and has allowed <a href="https://freedom.press/blog/2014/04/help-support-little-known-privacy-tool-has-been-critical-journalists-reporting-nsa" target="_blank">journalists</a> like <a href="https://www.wired.com/2014/10/laura-poitras-crypto-tools-made-snowden-film-possible/" target="_blank">Laura Poitras</a> to work without leaking information despite being targeted by some very skilled and highly resourced organizations. TAILS mostly works as a &#8220;live CD&#8221;, meaning the whole operating system is downloaded as a single &#8220;image&#8221; file, then either burned to a CD/DVD, or to a USB thumb drive. Updates work the same way. But TAILS has an optional feature to use the Debian package system to install and persist packages that are not included by default. TAILS does not use the default set of mirrors that a standard Debian install uses, it is set up by default with a range of possible Debian package sources, including the current stable version (called wheezy), the versions in testing, and packages backported to the stable version. That means that when this feature is used, TAILS fetches the metadata for all of those sections of Debian (stable/wheezy, testing, wheezy-backports, unstable).

Given all of the proven fingerprinting approaches, like using the font list from the browser, I think its a safe assumption that the apt-get metadata will also provide similar fingerprinting opportunities. For basic TAILS use, this is all avoided since updates are done via ISO images. But once a user installs packages via `apt-get`, that changes since TAILS then goes out onto the internet to fetch all of the repo metadata. That goes over Tor since TAILS forces all network traffic over Tor, so that helps break the link between the machine downloading the updates and those that can see that machines internet traffic.

It seems quite likely that the set of mirrors and the order in which they are run will provide a way to identify the system as TAILS. As for identifying individual machines, `apt-get` sends a lot of metadata, like language that the system is using, which packages need updates, etc. On top of the set of mirrors used, there is potentially enough metadata there to fingerprint the individual machine.

One open question is how the `apt-get` downloads map to different Tor circuits. If all of the traffic from a given `apt-get` session goes over a single Tor circuit, then the exit node, the mirror server, and any network observer that can see the traffic between those two can use that as the fingerprint.

To expand on this, if TAILS fetched all of its apt sources (wheezy, backports, testing, etc) via HTTPS from the same mirror (e.g. mirrors.kernel.org), then the exit node and network observer could not really distinguish the distro the machine making the connection was running since mirrors.kernel.org hosts many distro mirrors. There are two key parts here: using HTTPS to encrypt the data, and using HTTP pipelining so that network connections are reused for multiple downloads, rather than the default behavior of making a new HTTPS for each individual download. This setup would also prevent the custom pattern of apt sources from being distinguished since it would just show as downloading some series of files, and those files could be packages, package metadata, perl modules, source tarballs, etc.