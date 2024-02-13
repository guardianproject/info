---
title: Improving website resilience with LibResilient and IPFS
author: uniq
categories:
  - News
tags:
  - censorship
  - censorship circumvention
  - circumvention
  - filecoin
  - free software
  - IPFS
  - open source
  - resilience

---

We're always looking for techniques to make services more resilient to all
sorts of issues. That's why we took special interest in
[LibResilient](https://resilient.is/) and mapped out it's capabilities.  It's a
JavaScript library for decentralized content delivery in web-browsers and
markets itself as easy to deploy to any website. We've looked at LibResilient
primarily in the context of static websites.  While it should work with dynamic
websites too, that was out of focus for us.

Under the hood LibResilient uses [Web
Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API).
Technically it's a piece of JavaScript that websites can install into the
browsers of their visitors.  I like to compare it to cookies, except that it's
not just data but actually a program for manipulating your network request. The
main purpose of Web Workers is to enable web apps to optimize their network
connections. Web Workers are pretty low-level API.

LibResilient delivers implementations for common use-cases on top of Web
Workers in the form of plug-ins.  We've looked at the 3 most basic of those
plug-ins.

* _fetch plugin_ - routes network requests directly to the web-server as if
  LibResilient wasn't present.
* _cache plugin_ - stores HTML, JavaScript, images and other files inside
  the browsers local storage
* _alt-fetch plugin_ - allows to configure a list of website mirrors and tries
  to fetch files from there

These enable us to keep a website online and even update it if the main
web-server running that site has an outage.  It's key that visitors must have
managed to load the website at least once before.  Only than can LibResilient
work it's magic and install itself and the list of site mirrors into the users
browser.  This solution doesn't work for first time visitors, during the period
of an outage.

Of course this requires to run website mirrors. Static websites really shine in
this regard, because they are very easy to mirror and static web-space is quite
inexpensive these days.

We also looked into using IPFS Gateways as mirrors.  To accomplish this we had
to first add and pin websites to IPFS.  Next we had to publish the pinned copy
of the site to IPNS.  Then we could use the IPNS-key-fingerprint to use every
public IPFS gateway as mirror.  However, public gateways tend to require quite
long to answer requests, which is bad for LibResilient because it uses
relatively short timeouts to fail-over between mirrors.  So to get some sense
of reliability, paid IPFS gateways guaranteed to pin your website are a more
stable choice.

# Publishing LibResilient to IPFS

This is a for publishing a static LibResilient enabled website to IPFS.

## requirements

You will need VPS, or some other kind of tiny but always online server to make
your data available on IPFS. This guide assumes that your server is running some
flavor of GNU/Linux. It also assumes that you are familiar with the concept of
static websites and that your site is already hosted on the internet.

Mind that IPFS can be very slow, if you run into timeouts don't give up. Just
wait a few minutes and give it a few more retries, it will work eventually.

## Install IPFS

This short snipped will install `kubo` the official IPFS binary build on your
server:

```bash
wget https://dist.ipfs.tech/kubo/v0.18.1/kubo_v0.18.1_linux-amd64.tar.gz
echo "15d42b47b8529edda3e8e2d6fe6c14958d939c4efd07dea02e204743e05216f3 kubo_v0.18.1_linux-amd64.tar.gz" \
    | sha256sum --check
tar -xzf kubo_v0.18.1_linux-amd64.tar.gz
mv kubo/ipfs /usr/local/bin/ipfs
rm -rf kubo kubo_v0.18.1_linux-amd64.tar.gz
```

Setup kubo daemon to always run in background as systemd service. (Note: this
is tested for Debian and might require different steps on other GNU/Linux
distributions.)


```bash
adduser ipfs --gecos '' --disabled-password
su ipfs -c '/usr/local/bin/ipfs init --profile server'

cat << EOF > /etc/systemd/system/ipfs-daemon.service
[Unit]
Description=IPFS Daemon

[Service]
Restart=always
User=ipfs
group=ipfs
WorkingDirectory=/home/ipfs
ExecStart=/usr/local/bin/ipfs daemon

[Install]
WantedBy=default.target
EOF

systemctl enable ipfs-daemon.service
systemctl start ipfs-daemon.service
```

Tip: If you're behind a firewall or NAT make sure to open ports 4001/tcp and
4001/udp so IPFS can connect to the internet.

### Publish site to IPFS

Next we'll publish the website to IPFS. You'll need to copy your static website
to the IPFS server. For this guide we'll assume there's a copy of your website
at `/home/ipfs/website`.

```bash
ipfs add -r /home/ipfs/website"
```

The last line of the output of this command should look something like this:

```
added QmcoZGQZnaGGdcv3zWf1pdcpMQXuXz74tUy7veWdxCiPck website
```

Copy the CID and pin it. Pinning means that your IPFS daemon will never
automatically delete these files to free up memeory.

```bash
ipfs pin add QmcoZGQZnaGGdcv3zWf1pdcpMQXuXz74tUy7veWdxCiPck
```

Now it's time to make make it available via IPNS. So we need to generate an
IPNS key. This key will serve as address for accessing the website using IPFS.
It also serves as key for publishing updates to your website.

NOTE: all commands in this section are to be executed by `ipfs` user.

```bash
ipfs key gen --type=rsa --size=2048 example-site
```

This is how you can list your keys:

```bash
ipfs key list -l
```

the relevant output should look something like this:

```
k2k4r8ls72x686fmm2s0px4plejbHkhOm9uuzrxwedsaag1w72ene5rw     example-site
```

The hash of the key, on the left side is going to be the IPNS name of your
website. It's a fixed name that doesn't change even when you update your site.

```bash
ipfs name publish --key=example-site QmcoZGQZnaGGdcv3zWf1pdcpMQXuXz74tUy7veWdxCiPck 
```

When your IPFS node is working and could connect to some peers, your site
should now be accessible using IPNS. Although publishing may take several
minutes. There are so-called [public
gateways](https://ipfs.github.io/public-gateway-checker/) which allow users to
access IPFS and IPNS content using http. E.g.:
https://cloudflare-ipfs.com/ipns/k51qzi5uqu5dlfqyi5ofzusx23myrrfzxlbzjho4nso0nq28lueo1994l0uwzw

You can also use `ipfs` to check if the files got ingested correctly. E.g.:

```bash
ipfs ls /ipns/k51qzi5uqu5dlfqyi5ofzusx23myrrfzxlbzjho4nso0nq28lueo1994l0uwzw
ipfs cat /ipns/k51qzi5uqu5dlfqyi5ofzusx23myrrfzxlbzjho4nso0nq28lueo1994l0uwzw/index.html
```

### Update LibResilient config to include IPNS link

Now that your site is available on IPNS you can finally add it to your
LibResilient `config.json`. You can actually add as many gateways as you'd
like with LibResilient's `alt-fetch` plugin. Here's a simple example where we
added two gateways:

```json
{
  "plugins": [{
    "name": "fetch"
  }, {
    "name": "alt-fetch",
    "endpoints": [
      "https://cloudflare-ipfs.com/ipns/k51qzi5uqu5dlfqyi5ofzusx23myrrfzxlbzjho4nso0nq28lueo1994l0uwzw",
      "https://ipfs.io/ipns/k51qzi5uqu5dlfqyi5ofzusx23myrrfzxlbzjho4nso0nq28lueo1994l0uwzw",
    ]
  }],
  "loggedComponents": ["service-worker", "fetch", "alt-fetch"]
}
```

NOTE: We have to use IPNS, because as you can see we need write the IPFS
address to a file which itself is part of the website. With IPNS updating the
site also won't require changing `config.json` for every update.

When you've made your pick of IPFS gateways and added them to your
`config.json` you can publish it to your web-server.

### Publish updated site to IPFS

Now you also need to publish the change to IPFS. Again start by copying the
site to your IPFS server. We again assume the updated copy of your static
website is located at `/home/ipfs/website`.

Next we can unpin the old version of the website. (Tip: you can list pinned
files and directories with: `ipfs pin ls` pinned directories will be marked as
`recursive`)

```bash
ipfs unpin QmcoZGQZnaGGdcv3zWf1pdcpMQXuXz74tUy7veWdxCiPck
```

Then we can add the updated site to IPFS and publish it to IPNS again.

```bash
ipfs add -r /home/ipfs/website"
ipfs name publish --key=example-site QmcoZrn004DGdRvuZWf1pdcpMQXuXghjCUy7ve5Og45dNU 
```

You can repeat this step whenever you want to publish an updated version of
your static website.
