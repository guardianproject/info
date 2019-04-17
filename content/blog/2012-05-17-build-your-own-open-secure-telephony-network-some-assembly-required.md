---
id: 2189
title: '<!--:en-->Build your own Open Secure Telephony Network, some assembly required<!--:-->'
date: 2012-05-17T17:13:39-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=2189
permalink: /2012/05/17/build-your-own-open-secure-telephony-network-some-assembly-required/
force_ssl:
  - "1"
categories:
  - HowTo
tags:
  - backend
  - freeswitch
  - ostn
  - sip
  - voip
  - zrtp
---
<!--:en-->The Open Secure Telephony Network is a standard that defines how to configure a VoIP softswitch with the capability to have secure two-way VoIP conversations if both parties are using the same server. The system requires both backend and frontend components, which makes OSTN is a little different than some of the other Guardian apps. Unlike Gibberbot, there are few public SIP services that support secure signalling for a mobile app to connect with. Notably 

[Tanstagi.net](https://tanstagi.net) offers free accounts. But it&#8217;s more fun to run your own.

Ready? Here&#8217;s the 12 step program.

The core server system is what provides user registration and media proxying. The reference application I used is called Freeswitch. It has a plethora of configuration options, so I chose to use a configuration management system called Chef to get everything set correctly.

  1. Bootstrap a Debian server. Right now the only supported platform for an automated installation is Debian 6 &#8220;Squeeze&#8221;. The adventerous may try to run the cookbook on another platform and do some bug fixing
  2. Install sudo, curl and git if you don&#8217;t already have them. `apt-get install sudo curl git-core`
  3. Get a static IP address. This is crucial! Your users will need a place to register from anywhere in the world
  4. Get a domain name. This is also crucial! Your users will prefer to register to a name rather than an IP address
  5. Configure a local hostname. This is a dependency for the cookbook to properly configure Freeswitch to serve your custom domain. Unfortunately, this process varies based on OS and has bizarre conventions that make no sense. Just [follow the instructions](http://serverfault.com/questions/331936/setting-the-hostname-fqdn-or-short-name) and don&#8217;t ask questions. Remember to reboot after changing the hostname
  6. Install Chef from the [opscode full stack](http://www.opscode.com/chef/install/).
  7. Download the [freeswitch cookbook](https://github.com/lazzarello/chef-twelvetone) and [execute it](https://github.com/lazzarello/chef-twelvetone/tree/master/cookbooks/freeswitch) with chef-solo
  8. Walk away and have some coffee or a beer, depending on where the sun is relative to you
  9. When the Chef run is finished, Freeswitch will be up and running. Check with `netstat -lntp` you should see freeswitch listening on TCP port 5061
 10. Create users by running `/opt/chef/embedded/bin/ruby /usr/local/freeswitch/scripts/gen_users`. Without arguments, it will print the required parameters. Run it with an offset of 1000 and as many users as you like. Copy the XML files output by the script to `/usr/local/freeswitch/conf/directory/default/` The script will also output a file with plaintext passwords so you can provision user handsets. Put this file somewhere safe and encrypted
 11. Reload the XML into Freeswitch&#8217;s memory. `/usr/local/freeswitch/bin/fs_cli -x "reloadxml"`
 12. Install [CSipSimple](http://nightlies.csipsimple.com/trunk/) and configure it to connect to your domain name with the username/password pair

If you make it through these steps, congratulations! You are now a Freeswitch operator. If you&#8217;re curious what is behind all of this and why it works, you should read about [SIP](http://en.wikipedia.org/wiki/Session_Initiation_Protocol), [ZRTP](http://en.wikipedia.org/wiki/ZRTP) and [SDP](http://en.wikipedia.org/wiki/Session_Description_Protocol). It&#8217;s also worth noting that the Chef cookbook configures the server to act as an SSL [Certificate Authority](http://en.wikipedia.org/wiki/Certificate_authority). This is used for Secure SIP. The current landscape of using commercially signed certificates in Freeswitch is far more complicated than any HTTPS web server you may have worked with.

If you&#8217;d like to get help from me or another Guardian Project hacker, you can create issues [in our tracker](https://dev.guardianproject.info/projects/ostn) and message SteeleNivenson on Freenode or OFTC in channel #guardianproject. Oh yeah, and there&#8217;s Twitter @leeazzarello.<!--:-->