---
id: 13379
title: 'HOWTO: get all your Debian packages via Tor Onion Services'
date: 2016-07-31T17:28:57-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13379
permalink: /2016/07/31/howto-get-all-your-debian-packages-via-tor-onion-services/
has_been_saved:
  - "1"
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "425"
discourse_permalink:
  - https://talk.developersquare.net/t/howto-get-all-your-debian-packages-via-tor-onion-services/305
discourse_comments_count:
  - "1"
discourse_comments_raw:
  - '{"id":305,"posts_count":2,"filtered_posts_count":2,"posts":[],"participants":[{"id":218,"username":"tmp","avatar_template":"https://avatars.discourse.org/v2/letter/t/e47774/{size}.png"},{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553095845"
wpdc_sync_post_comments:
  - "0"
categories:
  - anonymity
  - HowTo
  - privacy
  - Research
  - tor
tags:
  - anonymity
  - debian
  - howto
  - metadata
  - privacy
  - security
  - tor
  - tor hidden service
  - tor onion service
---
[<img src="https://guardianproject.info/wp-content/uploads/2014/10/leakage-300x199.png" alt="leakage" width="300" height="199" class="alignright size-medium wp-image-12699" srcset="https://guardianproject.info/wp-content/uploads/2014/10/leakage-300x199.png 300w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-100x66.png 100w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-150x99.png 150w, https://guardianproject.info/wp-content/uploads/2014/10/leakage-200x132.png 200w, https://guardianproject.info/wp-content/uploads/2014/10/leakage.png 410w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2014/10/leakage.png)Following up on <a href="https://guardianproject.info/2014/10/16/reducing-metadata-leakage-from-software-updates/" target="_blank">some privacy leaks that we looked into a while back</a>, there are now official Debian <a href="https://onion.debian.org" target="_blank">Tor Onion Services</a> for getting software packages and security updates, thanks to the Debian Sys Admin team. This is important for high risk use cases like TAILS covers, but also it is useful to make it more difficult to do some kinds of targeted attacks against high-security servers. The default Debian and Ubuntu package servers use plain HTTP with unencrypted connections. That means anyone with access to the network streams could both monitor and fingerprint traffic. When an request for a security update is spotted, an attacker knows that machine is vulnerable to an exploit, and could reliably exploit it before the security update is applied.

Using <a href="https://labs.riseup.net/code/issues/8143" target="_blank">HTTPS to get security updates</a> improves this situation a lot, but by measuring the size of data transfers, it is still possible to <a href="http://www0.cs.ucl.ac.uk/staff/G.Danezis/papers/TLSanon.pdf" target="_blank">track which files are being downloaded</a>. A Tor Onion Service provides end-to-end encryption like the HTTPS connection. It also mixes up the traffic with lots of other traffic, so its not easy to see what traffic goes together. That makes it a lot harder for a network observer to tell when a security update is being downloaded. Additionally, using a Tor Onion Service forces the traffic over Tor, so that the Debian mirror server cannot see which server is requesting the updates. That helps prevent targeted attacks.

There are other benefits as well, besides just for the person running the high security server in this example, especially if all of the traffic is coming over Tor. When updates are delivered over Tor, then that means the Debian mirror operators have less to worry about because they are handling less metadata that might have privacy concerns. It means that when law enforcement requests logs from the mirror operators, the mirror operators can more easily hand over anything they have since the mirror operator knows that there is not private information in the logs. Reducing the legal risks and privacy concerns makes it easier to run mirrors, and that helps internet services work better.

One disadvantage of this approach as it now stands is that your server will get updates from the same mirror every time. There is only a single Tor Onion Service for the main archive. An alternate approach using the combination of Tor and http://httpredir.debian.org/ as the package source means that your server will get updates from a different mirror each time Tor changes its exit node (I believe that’s every 10 minutes or so).

**How can you set up your Debian machine to get updates over Tor?**

[<img src="https://guardianproject.info/wp-content/uploads/2016/07/tor-logo-2011_11-300x173.jpg" alt="debian and tor" width="300" height="173" class="alignright size-medium wp-image-13395" srcset="https://guardianproject.info/wp-content/uploads/2016/07/tor-logo-2011_11-300x173.jpg 300w, https://guardianproject.info/wp-content/uploads/2016/07/tor-logo-2011_11-768x444.jpg 768w, https://guardianproject.info/wp-content/uploads/2016/07/tor-logo-2011_11.jpg 800w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2016/07/tor-logo-2011_11.jpg)Right now, the best way to set up a Debian machine to force traffic over Tor is to use <a href="https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy" target="_blank">transparent proxying</a> via \`iptables\` rules. If you have that setup, then you can add the onion addresses as Debian apt sources as if they are any other HTTP Debian mirror. Another option is to install \`apt-transport-tor\` like TAILS does, then you can use <a href="http://people.skolelinux.org/pere/blog/Always_download_Debian_packages_using_Tor___the_simple_recipe.html" target="_blank">special syntax to add the Tor Onion Services</a>. And another way is to install an HTTP proxy like \`privoxy\` and enable apt HTTP proxy support as <a href="https://guardianproject.info/2014/10/16/reducing-metadata-leakage-from-software-updates/" target="_blank">I described before</a>. The \`apt-transport-tor\` and \`privoxy\` approaches both have the downside of having to trust an added piece of software, whereas the transparent proxy technique uses what is already present in the Linux kernel. I’ve been using the \`privoxy\` method since that is what I got working in 2014 and it has been working reliably on multiple servers since then. Also, I need \`privoxy\` installed for another application anyway.

Here’s how to set up the apt sources to get packages and updates via Tor Onion Services without delaying security updates. First, remove \`/etc/apt/sources.list\` and \`/etc/apt/sources.list.d/*.list\` to start with a clean slate. Next add \`/etc/apt/sources.list.d/00.vwakviie2ienjx6t.onion.list\` to get the main Debian repositories:

`</p>
<pre>
deb http://vwakviie2ienjx6t.onion/debian/ jessie main
deb-src http://vwakviie2ienjx6t.onion/debian/ jessie main

# aka volatile
deb http://vwakviie2ienjx6t.onion/debian/ jessie-updates main
deb-src http://vwakviie2ienjx6t.onion/debian/ jessie-updates main

deb http://vwakviie2ienjx6t.onion/debian jessie-backports main
deb-src http://vwakviie2ienjx6t.onion/debian/ jessie-backports main
</pre>
<p>`

Next add the new Tor Onion Service for the security update repository at \`/etc/apt/sources.list.d/00.sgvtcaew4bxjd7ln.onion.list\`:

`</p>
<pre>
deb http://sgvtcaew4bxjd7ln.onion/ jessie/updates main
</pre>
<p>`

Then last, include the normal HTTP security.debian.org archive to ensure that your server gets the latest security updates, even if the <a href="https://onion.debian.org/" target="_blank">Onion Service mirror</a> is behind or there is some other issue related to Tor. This goes in \`/etc/apt/sources.list.d/99.security.debian.org.list\` to ensure that it is always the last repository that is tried, and apt loads files from /etc/apt/source.list.d/ in alphabetical order, so it’ll always try to get the security updates from the Onion Service before falling back to the HTTP source as a last resort.

`</p>
<pre>
deb http://security.debian.org/ jessie/updates main
</pre>
<p>`

I also run an unofficial mirror of the security updates on http://dju2peblv7upfz3q.onion/debian if you want to add another backup, i.e. \`/etc/apt/sources.list.d/00.dju2peblv7upfz3q.onion.list\`:

`</p>
<pre>
deb http://dju2peblv7upfz3q.onion/debian-security/ jessie/updates main
</pre>
<p>`