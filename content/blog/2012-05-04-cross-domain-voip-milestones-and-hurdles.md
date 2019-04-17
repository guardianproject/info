---
id: 2079
title: 'Cross-Domain calling, or “toll-free long distance VoIP”'
date: 2012-05-04T17:34:30-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=2079
permalink: /2012/05/04/cross-domain-voip-milestones-and-hurdles/
force_ssl:
  - "1"
categories:
  - Development
  - News
tags:
  - ostn
  - peering
  - sip
  - voip
---
In a standard [OSTN configuration](https://guardianproject.info/wiki/OSTN_Compliance_Specification), the Fully Qualified Domain Name ([FQDN](http://en.wikipedia.org/wiki/FQDN)) of the server running Freeswitch is a core dependency to operate the service. For example, the domain ostel.me was first configured as a DNS record, a server was bootstrapped with ostel.me as the local hostname and a [Freeswitch cookbook](https://github.com/lazzarello/chef-twelvetone) was run using the Chef automation system. Because the domain was configured both in DNS and locally, the cookbook has enough information to automatically build an operational OSTN node.

Once the node is operational, accounts are provisioned on the node and users install the OSTel Android application on their mobile handsets. Users may place secure calls to other users within the domain ostel.me.

This week I reached a milestone. I placed a call from a user at ostel.me to a user on a second private debugging domain. Both domains were configured as an OSTN node and two handsets were registered, one on each node. This kind of cross domain calling is something that is rare in the VoIP world when compared to other communications protocols on the Internet, for example email and XMPP. This is due in part to the complexity of the SIP protocol. I’m [documenting the extended details](https://guardianproject.info/wiki/The_challenges_with_secure_cross-domain_calling) on the wiki.

I configured both servers to register to each other, establishing a two way link between them. This is called [VoIP peering](http://en.wikipedia.org/wiki/Voice_peering). The more nodes in the network, the more peering relationships must exist. For example, this picture illustrates the relationships between a fully interconnected network with four nodes, named A, B, C and D.

<div id="attachment_2082" style="width: 287px" class="wp-caption alignnone">
  <a href="https://guardianproject.info/wp-content/uploads/2012/05/full_mesh_network.png"><img aria-describedby="caption-attachment-2082" src="https://guardianproject.info/wp-content/uploads/2012/05/full_mesh_network-277x300.png" alt="Four Node Peering Network" width="277" height="300" class="size-medium wp-image-2082" srcset="https://guardianproject.info/wp-content/uploads/2012/05/full_mesh_network-277x300.png 277w, https://guardianproject.info/wp-content/uploads/2012/05/full_mesh_network.png 400w" sizes="(max-width: 277px) 100vw, 277px" /></a>
  
  <p id="caption-attachment-2082" class="wp-caption-text">
    Four Node Peering Network
  </p>
</div>

The implementation of this kind of peering network differs for each application. Once the peering configuration is completed by the operator of each node, they must also enable cross domain calling in the Freeswitch dialplan. In Freeswitch, the peers create a “gateway” to route calls to a non-local domain. When a non-local call is placed, Freeswitch will attempt to find a gateway to that domain. If it exists, it will route the call to the other server, which will in turn ring the handset belonging to the registered username.

<div id="attachment_2110" style="width: 610px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2012/05/sip-peering-situation.png"><img aria-describedby="caption-attachment-2110" src="https://guardianproject.info/wp-content/uploads/2012/05/sip-peering-situation.png" alt="Protocol flow between two domains" width="600" height="188" class="size-full wp-image-2110" srcset="https://guardianproject.info/wp-content/uploads/2012/05/sip-peering-situation.png 600w, https://guardianproject.info/wp-content/uploads/2012/05/sip-peering-situation-300x94.png 300w" sizes="(max-width: 600px) 100vw, 600px" /></a>
  
  <p id="caption-attachment-2110" class="wp-caption-text">
    Cross Domain SIP Call
  </p>
</div>

  
The user interface to place this type of call in the OSTel app is experimental due to our security requirements. In my test, the non-local domain was debug.ostel.me. To place a call from &#x62;o&#x62;@o&#x73;t&#x65;l.&#x6d;e to alice@debug&#x2e;&#x6f;&#x73;&#x74;&#x65;&#x6c;&#x2e;&#x6d;&#x65; I had to type a fully qualified [SIP URI](http://en.wikipedia.org/wiki/Uniform_resource_identifier) into the OSTel dialer interface. It looks like `sip:&#x61;l&#x69;ce&#x40;de&#x62;u&#x67;&#x2e;o&#x73;te&#x6c;.&#x6d;&#x65;;transport=tls`. The transport=tls attribute is due to the secure SIP requirement. Without that, the app will try and connect to debug.ostel.me over the insecure SIP port, which is not open on an OSTN node.

This test proved that cross domain SIP calling is possible but as I’ve shown above, there are significant hurdles on both the user and operator side. Some of these hurdles may be overcome by using a [SIP application other than Freeswitch](http://www.opensips.org/), some may be solved on the client side, [others with DNS](http://www.e164.org/). It’s great to have a secure voice service with a network of trusted peers. I’m looking forward to future research and development to remove the hurdles to create these peering agreements. Eventually we’ll all have the ability to call our friends email addresses.