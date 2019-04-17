---
id: 14042
title: Use Onions/HTTPS for software updates
date: 2019-01-23T06:35:40-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=14042
permalink: /2019/01/23/use-onions-https-for-software-updates/
categories:
  - News
tags:
  - debian
  - security
  - updates
---
There is a new <a href="https://lists.debian.org/debian-security-announce/2019/msg00010.html" target="_blank">vulnerability in Debian&#8217;s apt</a> that allows anything that can Man-in-the-Middle (MITM) your traffic to get root on your Debian/Ubuntu/etc boxes. Using encrypted connections for downloading updates, like HTTPS or Tor Onion Services, reduces this vulnerability to requiring root on the mirror server in order to exploit it. That is a drastic reduction in exposure. We have been pushing for this [since 2014](https://guardianproject.info/2014/10/16/reducing-metadata-leakage-from-software-updates/), and <a href="https://onion.debian.org" target="_blank">Debian</a>, <a href="https://ftp.fau.de" target="_blank">mirror</a> <a href="https://mirrors.kernel.org" target="_blank">operators</a>, and others in the ecosystem have taken some big steps towards making this the standard. This should finally put to rest the idea that plain <a href="https://whydoesaptnotusehttps.com/" target="_blank">HTTP is enough</a> for software updates with signed metadata.

To this end, we have always supported <a href="https://f-droid.org/docs/Security_Model/" target="_blank">F-Droid&#8217;s practice</a> of requiring HTTPS connections to f-droid.org and mirrors, even though the signed metadata file is the essential mechanism for providing security.

## Using encrypted connections on your server

Over the years, we have been honing our `apt` sources setup to use encrypted connections as much as possible, while getting updates as fast as possible. The hard part of this is that the <a href="http://security.debian.org" target="_blank">official Debian security server</a> only provides HTTP. There are mirrors of that that are available over HTTPS, but they can receive updates hours or days later. The best fix for this would be for Debian to provide an HTTPS connection to `security.debian.org`. There are still things in the `apt` source configuration that can help. There are three levels we use:

  1. only Tor Onion Services for all updates, this means always encrypted and over Tor, but can mean that updates are delayed, for example if Tor traffic is blocked.
  2. First try Tor Onion, then try HTTPS. This provides a backup connection method in case Tor is not working, for whatever reason, but still could get updates slower than the official security source
  3. First try Tor Onion, then try HTTPS, then try HTTP. But HTTP is only enabled for `security.debian.org`

You can see an example of the final option by looking at <a href="https://gitlab.com/fdroid/fdroid-cfarm-bootstrap/commit/24389018a164e110e7204f2b2c62a7b81863cdd4" target="_blank">F-Droid&#8217;s compile farm server config</a>.

## Fixing your boxes

`@abelxluck` aka `@abeluck` put out an <a href="https://gist.github.com/abeluck/67525909a17403060cd1722b53d57d00" target="_blank">Ansible Playbook</a> to do this update. Here is a quick script for securely updating on Debian/stretch/amd64 based on the <a href="https://lists.debian.org/debian-security-announce/2019/msg00010.html" target="_blank">info published</a> on the debian-security list:  
`<br />
#!/bin/sh -ex`

`apt -o Acquire::http::AllowRedirect=false update || true<br />
apt -o Acquire::http::AllowRedirect=false upgrade --download-only || true`

`cd /var/cache/apt/archives`

`test -e apt-dbgsym_1.4.9_amd64.deb && \<br />
echo "1da507155c7b1ad140739c62fdacceaf5b5ee3765b1a00c3a3527d9d82a8d533  apt-dbgsym_1.4.9_amd64.deb" | sha256sum -c`

`test -e apt-transport-https-dbgsym_1.4.9_amd64.deb && \<br />
echo "59f3e1c91664fe3b47048794560ebe9c41f1eeccbdd95f7715282f8cbe449060  apt-transport-https-dbgsym_1.4.9_amd64.deb" | sha256sum -c`

`test -e apt-transport-https_1.4.9_amd64.deb && \<br />
echo "c8c4366d1912ff8223615891397a78b44f313b0a2f15a970a82abe48460490cb  apt-transport-https_1.4.9_amd64.deb" | sha256sum -c`

`test -e apt-utils-dbgsym_1.4.9_amd64.deb && \<br />
echo "e3e157c291b05b2899a545331c7597ab36ca04e02cd9010562b9985b76af60db  apt-utils-dbgsym_1.4.9_amd64.deb" | sha256sum -c`

`test -e apt-utils_1.4.9_amd64.deb && \<br />
echo "fb227d1c4615197a6263e7312851ac3601d946221cfd85f20427a15ab9658d15  apt-utils_1.4.9_amd64.deb" | sha256sum -c`

`test -e apt_1.4.9_amd64.deb && \<br />
echo "dddf4ff686845b82c6c778a70f1f607d0bb9f8aa43f2fb7983db4ff1a55f5fae  apt_1.4.9_amd64.deb" | sha256sum -c`

`test -e libapt-inst2.0-dbgsym_1.4.9_amd64.deb && \<br />
echo "0e66db1f74827f06c55ac36cc961e932cd0a9a6efab91b7d1159658bab5f533e  libapt-inst2.0-dbgsym_1.4.9_amd64.deb" | sha256sum -c`

`test -e libapt-inst2.0_1.4.9_amd64.deb && \<br />
echo "a099c57d20b3e55d224433b7a1ee972f6fdb79911322882d6e6f6a383862a57d  libapt-inst2.0_1.4.9_amd64.deb" | sha256sum -c</p>
<p>test -e libapt-pkg-dev_1.4.9_amd64.deb && \<br />
echo "cfb0a03ecd22aba066d97e75d4d00d791c7a3aceb2e5ec4fbee7176389717404  libapt-pkg-dev_1.4.9_amd64.deb" | sha256sum -c</p>
<p>test -e libapt-pkg5.0-dbgsym_1.4.9_amd64.deb && \<br />
echo "cdb03ddd57934e773a579a89f32f11567710a39d6ac289e73efb20e8825874d1  libapt-pkg5.0-dbgsym_1.4.9_amd64.deb" | sha256sum -c</p>
<p>test -e libapt-pkg5.0_1.4.9_amd64.deb && \<br />
echo "03281e3d1382826d5989c12c77a9b27f5f752b0f6aa28b524a2df193f7296e0b  libapt-pkg5.0_1.4.9_amd64.deb" | sha256sum -c</p>
<p>````````````````````apt -o Acquire::http::AllowRedirect=false upgrade<br />
`