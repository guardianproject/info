---
title: "Debian over HTTPS"
author: Hans-Christoph Steiner
categories:
  - News
tags:
  - Debian
  - metadata
  - privacy
  - TLS
---

Debian's package manager [_apt_](https://wiki.debian.org/SecureApt) has a
time-tested method of securely providing packages from the network built on
OpenPGP signatures.  Even though this signing method works well for verifying
the indexes and package files, there are new threats that have become relevant
as man-in-the-middle attacks and data mining become ever easier.  Since 2013,
_apt_ developers have supported encrypted transport methods HTTPS and Tor Onion
Service.  We have been [recommending]({{< ref 2016-07-31-howto-get-all-your-debian-packages-via-tor-onion-services >}}) [their]({{< ref 2019-01-23-use-onions-https-for-software-updates >}}) [use]({{< ref
2014-10-16-reducing-metadata-leakage-from-software-updates >}}) since [2013]({{<
ref 2013-10-31-issues-when-distributing-software >}}).

Most major mirrors already support HTTPS, and now <https://security.debian.org>
has finally joined the party.  That means it is possible to use HTTPS on all of
the official repositories.  On top of that, many Debian Developers are working
on making [HTTPS the
default](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=992692) for new
installs.


## The threats

Now is a good time to reiterate the areas of concern:

1. Package authenticity (software can be modified while being downloaded).
2. Repository availability (whole sites or specific URL paths can be selectively
   blocked by the network).
3. Package availability (software security updates can be individually blocked).
4. Who is downloading what package (currently visible to anyone who can see the
   network traffic, including open wifi, etc.).
5. Vulnerabilities in _apt_ or its signature validation (_apt_ can be
   exploited, authenticity checks can be bypassed).

The current _apt_ model with HTTP covers #1 well, but only covers #2 and #3 with
a one week window (the `Valid-Until` header sets the expiration date on the repo
metadata).  That gives attackers a short-term window where blocking and replay
attacks remain effective.  The And it does not cover #4 or #5 at all.

Using HTTPS adds a weak backup security layer for #1.  HTTPS makes it much more
difficult for certain files from a mirror to be selectively blocked or replayed,
as well as making related errors louder and earlier (e.g. #2 and #3).  Tracking
package downloads needs only simple passive listening with HTTP, but with HTTPS,
the attacker must build full indexes of package sizes, then parse the size from
TLS streams.  So HTTPS helps a little with #4.  Lastly,
[there](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-1829)
[have](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-1358)
[been](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3587)
[bugs](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-3462)
[in](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-1252)
[_apt_'s](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-0501) GPG
verification.  With HTTP, any network can inject exploits into _apt_'s
downloads.  HTTPS helps with #5 by providing a backup layer of encryption,
albeit weaker.

It is of course important to point out that HTTPS itself has flaws, and it is
not the best option out there, especially for protecting anonymity.  HTTPS is
quite easy to use for _apt_ repositories, so there is hardly any trade-off to
using it.  That is why it is the focus of this post.  If protecting privacy is
important to you, you should use the [Tor Onion Service
repositories](https://onion.debian.org), especially if #4 and #5 concern you.



## The risks of adding HTTPS

* The only security critique of using HTTPS for repositories that still makes
sense is that there might be vulnerabilities in the code that handles HTTPS,
since its a lot more complicated that HTTP.  In _apt_, HTTPS requires GnuTLS,
which is currently linked in by default.  In order to fully protect against
exploits related to the HTTPS code, the machine would need to use a custom build
of _apt_ with GnuTLS support not included.  It is possible to limit exposure of
the HTTPS implementation by setting `Acquire::AllowTLS false`.  This kind of
attack seems to be theoretical as of the time of writing, whereas there are at
least 6 CVEs related to exploiting the GPG verification.

* Using HTTPS makes using caching proxies much harder to setup.  Caching proxies
can reduce the leakage of metadata about which machine is getting which package,
so using direct HTTPS connections would therefore increase the leakage of that
kind of metadata.


## Things that can be improved

There are some additional bits of metadata that can be protected when using
HTTPS, thereby further improving the privacy protections in _apt_:

* With [TLSv1.3 Record
  Padding](https://www.gnutls.org/manual/gnutls.html#On-Record-Padding), TLS
  streams [can be
  padded](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1001335), which
  would obscure the size of the packages being downloaded from network
  observers.
* Pipelining downloads through a reused HTTPS connection makes it even more
  difficult for the network observer to track packages by size.
* The Server Name Indication (SNI) field in TLS will leak the domain name in
  plaintext.  The upcoming TLS Encrypted Client Hello standard will encrypt that.

The SNI field issue does not exist when using Tor Onion Services.  Package
sizes would still be visible to network observers when using Onion Services, so
TLS padding and pipelining would help there also.
