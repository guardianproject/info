---
id: 11867
title: Issues when distributing software
date: 2013-10-31T15:51:19-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=11867
permalink: /2013/10/31/issues-when-distributing-software/
categories:
  - News
  - privacy
tags:
  - anonymity
  - bazaar
  - debian
  - encryption
  - privacy
  - security
  - tor
---
There is currently a <a href="http://lists.debian.org/debian-security/2013/10/msg00027.html" target="_blank">discussion underway on the Debian-security list</a> about adding TLS and Tor functionality to the official repositories (repos) of Debian packages that is highlighting how we need to update how we think about the risks when distributing software. Mostly, we are used to thinking about making sure that the software that the user is installing is the same exact software that has been posted for distribution. This is generally handled by signing the software package, then verifying that signature on the user’s machine. This is how it works on Mac OS X, Windows, Debian, etc. etc.

But the authenticity of a software package is not the only issue that needs to be addressed, especially these days where many companies and governments around the world are trying to track everything that anyone is doing on the internet. In order to understand why Tor and TLS would be useful here, it good to break down the various concerns (or threats if you prefer):

  1. package authenticity _(software can be modified while being downloaded)_
  2. package availability _(software security updates can be individually blocked)_
  3. repo availability _(internet services can be blocked by governments and companies)_
  4. who’s downloading what package _(currently visible to anyone who can see the network traffic, including open wifi, etc.)_

Most people distributing software are used to thinking about #1 verifying packages when thinking about the security of software distribution. #2, #3, and #4 are also important, and currently not well addressed. This is where TLS and Tor come in. Both can help prevent Man-In-The-Middle manipulations as well as reduce the amount of information that is leaked to the network. Tor can also help with #3. Since Tor is difficult to block, it is often uses to circumvent censorship. In this case a software repo could be blocked entirely, and Tor could help with gaining access to it. The Update Framework has <a href="https://github.com/theupdateframework/tuf/blob/develop/README.md" title="TUF: The Update Framework -  Security" target="_blank">a good overview of the possible attacks</a> against software repos.

So having software repos available with both TLS and Tor available as options is a very good idea. As far as I have seen, there are not any Debian repos available via a Tor Hidden Service. There are a number of official mirrors that already support TLS/HTTPS. You can find them using <a href="https://gist.github.com/eighthave/7285154" title="the script in a gist paste" target="_blank">this script:</a>

```python
#!/usr/bin/python

import urllib2
import re
import ssl
import sys

# # find generic mirrors
mirrors = urllib2.urlopen('http://www.debian.org/mirror/list')
https = []
for line in mirrors.readlines():
    m = re.match('.*<td valign="top"><a rel="nofollow" href="http(.*)">.*', line)
    if m:
        url = 'https' + m.group(1)
        print 'trying: ',
        print url,
        print '...',
        sys.stdout.flush()
        try:
            response=urllib2.urlopen(url, timeout=1)
            https.append(url)
            print 'success!'
        except urllib2.URLError as err:
            print 'fail!'
        except ssl.SSLError as err:
            print 'bad SSL!'

# print 'HTTPS apt repos:'
#for url in https:
#    print url


# # find security mirrors
mirrors = urllib2.urlopen('http://www.debian.org/mirror/list-full')
securitys = []
for line in mirrors.readlines():
    m = re.match('.*</tt><br>Security updates over HTTP: <tt><a rel="nofollow" href="http(.*)">.*/debian-security/</a>.*', line)
    if m:
        url = 'https' + m.group(1)
        print 'trying: ',
        print url,
        print '...',
        sys.stdout.flush()
        try:
            response=urllib2.urlopen(url, timeout=1)
            securitys.append(url)
            print 'success!'
        except urllib2.URLError as err:
            print 'fail!'
        except ssl.SSLError as err:
            print 'bad SSL!'

# print 'HTTPS security repos:'
# for url in securitys:
#     print url


# now find the backports mirrors
mirrors = urllib2.urlopen('http://backports-master.debian.org/Mirrors/')
backports = []
for line in mirrors.readlines():
#<td><a href="http://be.mirror.eurid.eu/debian-backports/">/debian-backports/</a>
    m = re.match('.*<td><a href="http(.*)">.*/debian-backports/</a>.*', line)
    if m:
        url = 'https' + m.group(1)
        print 'trying: ',
        print url,
        print '...',
        sys.stdout.flush()
        try:
            response=urllib2.urlopen(url, timeout=1)
            backports.append(url)
            print 'success!'
        except urllib2.URLError as err:
            print 'fail!'
        except ssl.SSLError as err:
            print 'bad SSL!'

#print 'HTTPS backports repos:'
#for url in backports:
#    print url


# now find the CD image mirrors
mirrors = urllib2.urlopen('http://www.debian.org/CD/http-ftp/')
cds = []
for line in mirrors.readlines():
# <a rel="nofollow" href="http://mirror.easyspeedy.com/debian-cd/">HTTP</a></li>
    m = re.match('.*<a rel="nofollow" href="http(:.*)">HTTP</a></li>.*', line)
    if m:
        url = 'https' + m.group(1)
        print 'trying: ',
        print url,
        print '...',
        sys.stdout.flush()
        try:
            response=urllib2.urlopen(url, timeout=1)
            cds.append(url)
            print 'success!'
        except urllib2.URLError as err:
            print 'fail!'
        except ssl.SSLError as err:
            print 'bad SSL!'

print 'HTTPS CD image repos:'
for url in cds:
    print url


# now write everything to a file
f = open('/tmp/https-debian-archives.txt', 'w')

f.write('HTTPS apt repos\n')
f.write('---------------\n')
for url in https:
    f.write(url + '\n')

f.write('\n\nHTTPS security repos\n')
f.write('---------------\n')
for url in securitys:
    f.write(url + '\n')

f.write('\n\nHTTPS backports repos\n')
f.write('--------------------\n')
for url in backports:
    f.write(url + '\n')

f.write('\n\nHTTPS CD image repos\n')
f.write('--------------------\n')
for url in cds:
    f.write(url + '\n')


f.close()
```
