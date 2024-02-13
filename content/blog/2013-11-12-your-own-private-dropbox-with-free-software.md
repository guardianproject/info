---
id: 11924
title: Your own private dropbox with free software
date: 2013-11-12T12:50:23-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=11924
permalink: /2013/11/12/your-own-private-dropbox-with-free-software/
categories:
  - HowTo
  - Research
tags:
  - anonymity
  - desktop
  - encryption
  - git
  - open source
  - privacy
  - sparkleshare
  - ssh
  - tor
  - usability
---
There are lots of file storage and sharing software packages out there that make it easy for a group of people to share files. Dropbox is perhaps the most well known of the group, it provides an easy way for a group of people to share files. The downside of Dropbox is that it is not a private service, just like any cloud-based service. Dropbox has total access to your files that you store there. That means its likely that the NSA and its collaborators do too.

Dropbox also knows where the computers are that are accessing their service because they can see the IP address of the incoming connections. To help with this, it is possible to use use Dropbox over Tor, thankfully they have provided proxy settings.

For our shared files, we use <a href="http://sparkleshare.org/" target="_blank">SparkleShare</a>. It provides an experience very similar to Dropbox: you have a SparkleShare folder that is synced up with the service, and in turn any other users who are also linked up to it. Once its setup, it is as easy to use as Dropbox, but setting it up takes a bit more work than Dropbox. It builds upon two software packages well known for security and reliability: `git` and `ssh`, and works with Tor Hidden Services. It runs on Windows, Mac OS X, and GNU/Linux, and there is an <a href="https://github.com/NewProggie/SparkleShare-Android" target="_blank">Android client</a> in the works.[<img src="https://guardianproject.info/wp-content/uploads/2013/11/sparkleshare-onion.png" alt="sparkleshare-onion" width="312" height="342" class="alignright size-full wp-image-11936" srcset="https://guardianproject.info/wp-content/uploads/2013/11/sparkleshare-onion.png 312w, https://guardianproject.info/wp-content/uploads/2013/11/sparkleshare-onion-273x300.png 273w" sizes="(max-width: 312px) 100vw, 312px" />](https://guardianproject.info/wp-content/uploads/2013/11/sparkleshare-onion.png)

You can use any git service as the server for SparkleShare, including github, bitbucket, <a href="https://gitorious.org/" target="_blank">gitorious</a>, etc. But these have the same issues as putting your files on Dropbox: that service has complete access to your files. For extra protection, SparkleShare <a href="https://github.com/hbons/SparkleShare/wiki/Client-Side-Encryption" target="_blank">can encrypt the files on the client-side</a>, have encrypted shared folders with SparkleShare, so that the server does not have access to the files. For the last piece of setting up a private SparkleShare, you need a computer that you can `ssh` to, and has `git` and Tor on it. This computer could even be an old Android device running <a href="https://guardianproject.info/code/lildebi/" target="_blank">Lil’ Debi</a>, it only needs enough disk space for your SparkleShare files and a steady network connection. Running it on your own computer means it can use a Tor Hidden Service, and that all of the metadata related to who is editing what files remains private.

To start, setup a Tor Hidden Service to the sshd port. You can read all about that process in the <a href="https://www.torproject.org/docs/tor-hidden-service.html" target="_blank">Tor instructions</a>, but basically, you need to add something like this to the `torrc` configuration file:

<pre>HiddenServiceDir /var/lib/tor/ssh_hidden_service/
HiddenServicePort 22 127.0.0.1:22
</pre>

Then restart tor, and it will generate two files in `/var/lib/tor/ssh_hidden_service/`, open the file called `hostname` to see your new .onion address. We’re going to use `fakefakefakefake.onion` as our made-up one for this HOWTO. That is the address you will use in SparkleShare as the server address.

Next `ssh` needs to be setup to use Tor to access the .onion address of the Tor Hidden Service. To do that we need the wonderful Netcat tool (`nc`). On Debian/Ubuntu, run `sudo apt-get install netcat-openbsd` to get it, its included with Mac OS X by default. Now edit your SSH config file, its usually in `~/.ssh/config`, and add this section:

<pre>Host *.onion
     Compression yes
     ProxyCommand nc -X 5 -x 127.0.0.1:9050 %h %p
</pre>

For Windows, you need to use `connect` proxy, which is thankfully included in SparkleShare. You can optionally use `connect` instead of Netcat/`nc` on Mac OS X (`fink install connect` or `brew install connect`) and GNU/Linux (e.g. `apt-get install connect-proxy` or `yum install connect-proxy`). Instead of the snippet above, use this snippet in `~/.ssh/config` to use `connect`:

<pre>Host *.onion
     Compression yes
     ProxyCommand connect -5 -S 127.0.0.1:9050 %h %p
</pre>

Now its time to set up the git repo on the server that will be the conduit for sharing files between the different users. Basically, all you need to do is create a new folder, then make it a “bare” git repo (you can read <a href="http://git-scm.com/book/en/Git-on-the-Server-Setting-Up-the-Server" target="_blank">all about it in the git book</a>):

<pre>ssh g&#x69;t&#x40;&#x66;a&#x6b;e&#x66;&#x61;k&#x65;f&#x61;&#x6b;e&#x66;a&#x6b;&#x65;.&#x6f;n&#x69;&#x6f;n
mkdir /home/git/MyPrivateShare
cd /home/git/MyPrivateShare
git init --bare
</pre>

For sshing to the git, we set up a single account called `git`, then to grant access, we add the SSH key (SparkleShare calls this the _Client ID_) to the `git` account’s `~/.ssh/authorized_keys` file.

Now everything should be ready to start adding clients! In SparkleShare, go to Add Hosted Project…, choose On my own server, then enter your username and .onion address (_ssh:&#x2f;&#x2f;&#x67;&#x69;t@fak&#x65;&#x66;&#x61;&#x6b;efake&#x66;&#x61;&#x6b;&#x65;.onio&#x6e;_) in **Address** and the path to the git repo (_/home/git/MyPrivateShare_) in **Remote Path**:

[<img src="https://guardianproject.info/wp-content/uploads/2013/11/Screenshot-SparkleShare-Setup.png" alt="SparkleShare Setup" width="686" height="427" class="alignnone size-full wp-image-11945" srcset="https://guardianproject.info/wp-content/uploads/2013/11/Screenshot-SparkleShare-Setup.png 686w, https://guardianproject.info/wp-content/uploads/2013/11/Screenshot-SparkleShare-Setup-300x186.png 300w" sizes="(max-width: 686px) 100vw, 686px" />](https://guardianproject.info/wp-content/uploads/2013/11/Screenshot-SparkleShare-Setup.png)

Now the client will download the entire git repository from the server, and you’ll then have a working shared dropbox! If there are a lot of files in it, then the first sync can take a long time before any files show up. This is because git first downloads the entire history first, then it checks out the files. After that initial setup, then the new files show up quite quickly.

So this SparkleShare setup keeps your files on computers that you control, it prevents information and metadata from being leaked to the network while people are using this SparkleShare setup. When using Client Side Encryption, even less data is leaked. The server cannot access the content of the files at all since they are encrypted. The the server in this case would only be able to see the network traffic, and which ssh key was used to access the server. If everyone accessing this setup used the same user account (i.e. `git`) and ssh key, then the server would not even know which user is making the changes. This is about as private as you could hope for in a shared dropbox folder.

One last nice feature of this setup is that git server does not need a domain name, static IP or even a public IP, it just needs a working internet connection. As long as it can connect to Tor, then the Hidden Service will work. So if this private dropbox is for extra sensitive stuff, it could be stashed anywhere it can get power and wifi.