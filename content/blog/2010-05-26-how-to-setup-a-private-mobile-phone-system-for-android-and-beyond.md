---
id: 332
title: 'How To: Setup a Private VOIP Phone System for Android'
date: 2010-05-26T05:53:54-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=332
permalink: /2010/05/26/how-to-setup-a-private-mobile-phone-system-for-android-and-beyond/
bigimg: [{src: "/wp-content/uploads/2010/05/sipdroidcall-64x64.png",}]
categories:
  - HowTo
tags:
  - asterisk
  - sipdroid
  - voice
  - voip
---
<div>
  <div>
    <strong>MAY 2011: Learn more about our new efforts on the Open Secure Telephony Network at <a href="https://guardianproject.info/wiki/OSTN">https://guardianproject.info/wiki/OSTN</a> – we currently recommend the <a href="http://code.google.com/p/csipsimple/">CSipSimple</a> Android app instead of SIPDroid, for secure voice calls.</strong>
  </div>
  
  <div>
  </div>
  
  <div>
    Near the very top of Guardian’s open-source application suite <a href="https://guardianproject.info/apps/"><span style="color: #0000ff;"><span>wish l<span style="color: #0000ff;"><span>ist</span></span></span></span></a> is something that might seem like a no-brainer for a secure mobile device: voice. When we take into account network performance and audio fidelity requirements, as well as the International nature of Guardian’s target users (everything from average citizens to multi-national journalists or humanitarian organizations), the prospect of a truly real-time secure VOIP solution starts to reveal itself as quite the challenge. Fortunately, a number of efforts have been underway for some time on the Android platform. <strong>The following is an introduction to one such effort, and this post provides a very easy step-by-step how to enable your very own private mobile phone system.</strong>
  </div>
  
  <p>
    <span style="color: #0000ff;"><a href="https://guardianproject.info/wp-content/uploads/2010/05/sipdroidcall.png"><img class="alignleft size-full wp-image-337" title="sipdroidcall" src="https://guardianproject.info/wp-content/uploads/2010/05/sipdroidcall.png" alt="" width="145" height="241" /></a><a href="http://code.google.com/p/sipdroid/">Sipdroid</a></span> is an open-source SIP client that adds native SIP/VOIP to Android’s default dialer / contacts applications. You can find Sipdroid in the Android Market or alternatively can <a href="http://code.google.com/p/sipdroid/downloads/list"><span style="color: #0000ff;"><span>download it here</span></span></a>. SIP (<a href="https://en.wikipedia.org/wiki/Session_Initiation_Protocol"><span style="color: #0000ff;"><span>Session Initiation Protocol</span></span></a>) is the Internet standard for real-time voice and video communications. It’s a fundamental building block for many popular consumer VOIP products that you may have used – <a href="https://www.youtube.com/watch?v=1XU06zbDBBA"><span style="color: #0000ff;"><span>Vonage</span></span></a> or <a href="http://www.magicjack.com/"><span style="color: #0000ff;"><span>MagicJack</span></span></a> are two examples. Once installed and configured properly, sipdroid allows you to make & receive calls over Wifi and 3G / EDGE data connections – which is a really powerful thing! A similar solution from <a href="https://my.gizmo5.com/"><span style="color: #0000ff;"><span>Gizmo5</span></span></a> allowed many Android users to completely untangle themselves from mobile minutes and rely on a purely VOIP solution. Alas, new Gizmo signups were suspended after Google announced their <a href="http://googlevoiceblog.blogspot.com/2009/11/google-welcomes-gizmo5.html"><span style="color: #0000ff;"><span>acquisition</span></span></a> – but we should all be excited to see what they can cook up as part of the official <a href="https://www.google.com/voice"><span style="color: #0000ff;"><span>Google Voice</span></span></a> team.
  </p>
  
  <p>
    While it’s expected that SIP providers will become more <a href="http://code.google.com/p/sipdroid/wiki/NewStandbyTechnique"><span style="color: #0000ff;"><span>interoperable</span></span></a>, the simplest and most powerful solution currently available to get sipdroid running involves registering to the virtual PBX service from <a href="https://www1.pbxes.com/index_e.php"><span style="color: #0000ff;"><span>PBXes.com</span></span></a>. For the uninitiated, a PBX (Private Branch Exchange) is what establishes and manages the connections between the telephony products of a private organization (telephones, fax machines, etc.) – each of which is labeled with an ‘extension’. It also is the system through which these extensions are able to access the public telephone network (<a href="https://en.wikipedia.org/wiki/PSTN"><span style="color: #0000ff;"><span>PSTN</span></span></a>). Since the 1990s, traditional PBX solutions – usually out of reach for small businesses or individuals due to cost and complexity – have evolved to IP-based and virtual or hosted PBXes, which greatly simplify the processes of building and scaling telephony services. PBXes.com is one such ‘virtual PBX.’ Once a PBXes account is established, the account owner can create multiple extensions beneath it and easily dial between those extensions. You get 5 extensions for a free account, more for paid <a href="https://www1.pbxes.com/iptel_virtual-pbx.html"><span style="color: #0000ff;"><span>account types</span></span></a>.
  </p>
  
  <p>
    <strong>Why is this solution so interesting?</strong> If you have a relatively small group of colleagues (NGO, humanitarian workers, activists, journalists, etc.), it allows you to easily establish a private internal phone system that can be used over a data connection in lieu of the regular phone system. In our experience, the call quality is also quite good. <span>And while the following step-by-step guide will lead you through the process of setting up this simple solution, first a word of caution: t<span>his is <strong><span>not<span> a secure solution yet</span></span></strong><span>. It is a first step, however, down that road. To achieve a more secure solution, we need to enable more features, include tunneling and encrypting traffic through a Virtual Private Network (VPN) as well as integrating to a privately maintained <a href="http://www.techsteward.com/blog/dirk/?p=735"><span style="color: #0000ff;"><span><span style="color: #0000ff;"><span>A<span style="color: #0000ff;"><span>sterisk</span></span></span></span></span></span></a> phone server running with custom security settings. </span></span></span>
  </p>
  
  <p>
    <span><span><span>We are also investigating solutions that uses a public key exchange model, such as Philip Zimmermann’s <a id="s_.7" title="ZFone" href="http://zfoneproject.com/">ZFone</a>, such as the new </span><a href="http://whispersys.com/">RedPhone app just announced by WhisperSystems</a><span>.</span></span></span>
  </p>
  
  <p>
    <strong><span><span>1.</span></span></strong> <strong><span><span>Configure <span><span>extensions to <span><span>a<span><span> PBXes.com account</span></span></span></span></span></span></span></span></strong>
  </p>
  
  <p>
    <span><span>If you don’t already have a PBXes.com account, head over to <a href="http://www.pbxes.com"><span style="color: #0000ff;"><span><span><span>http://www.pbxes.com</span></span></span></span></a><span><span> and fill out the straightfo<span><span>rward account registration form for a free account.</span></span></span></span></span></span>
  </p>
  
  <p>
    <span><a href="https://guardianproject.info/wp-content/uploads/2010/05/welcome.png"><img class="alignnone size-medium wp-image-333" title="welcome" src="https://guardianproject.info/wp-content/uploads/2010/05/welcome-300x172.png" alt="" width="300" height="172" srcset="https://guardianproject.info/wp-content/uploads/2010/05/welcome-300x172.png 300w, https://guardianproject.info/wp-content/uploads/2010/05/welcome.png 615w" sizes="(max-width: 300px) 100vw, 300px" /></a></span>
  </p>
  
  <p>
     
  </p>
  
  <p>
    <span><span>Next, select ‘Extensions’ from the left-hand navigation menu, <span><span>then<span><span> choose ‘SIP’ under ‘Add an Extension.’ </span></span></span></span></span></span>
  </p>
  
  <p>
    <span> <span>Last, configure your new extension with a few critical elements. Make sure you fill out the following fields, at a minimum:</span></span>
  </p>
  
  <p>
    <a href="https://guardianproject.info/wp-content/uploads/2010/05/addSIPExtension.png"><img class="alignnone size-medium wp-image-334" title="addSIPExtension" src="https://guardianproject.info/wp-content/uploads/2010/05/addSIPExtension-300x171.png" alt="" width="300" height="171" srcset="https://guardianproject.info/wp-content/uploads/2010/05/addSIPExtension-300x171.png 300w, https://guardianproject.info/wp-content/uploads/2010/05/addSIPExtension.png 619w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  </p>
  
  <ul>
    <li>
      <ul>
        <li>
          <span><span>Extension number (e.g. 100, 101, 402, etc.)</span></span>
        </li>
        <li>
          <span><span>Display name (e.g. johndoe-100)</span></span>
        </li>
        <li>
          <span><span>Password</span></span>
        </li>
      </ul>
    </li>
  </ul>
  
  <div>
    <p>
      <span><span>After clicking ‘Submit,’ go ahead and repeat the process for as many extensions as  you’d like to set up. Each of these will be specific for a unique Android device. Don’t forget to APPLY your changes when finished by clicking the bright red bar – this ensures your changes take effect.</span></span>
    </p>
  </div>
  
  <p>
    <strong>2.</strong> <strong>Configure extensions on sipdroid</strong>
  </p>
  
  <p>
    If you don’t already have sipdroid, you can find the latest version <a href="http://code.google.com/p/sipdroid/downloads/list"><span style="color: #0000ff;"><span>here</span></span></a>, or point your barcode scanner to the following QR code:
  </p>
  
  <div>
    <a href="http://chart.apis.google.com/chart?cht=qr&chs=170x170&chl=http%3A%2F%2Fwww.androidzoom.com%2Fweb%2Findice%2FqrLink%3FappCode%3Dmaf%26dwnId%3D231933"><img class="alignnone size-full wp-image-335" title="dp82z4m_35fd9f9hgz_b" src="http://chart.apis.google.com/chart?cht=qr&chs=170x170&chl=http%3A%2F%2Fwww.androidzoom.com%2Fweb%2Findice%2FqrLink%3FappCode%3Dmaf%26dwnId%3D231933" alt="" width="170" height="170" /></a>
  </div>
  
  <div>
    <p>
      Within the Account Settings section of sipdroid, set up one of your extensions from step 1:
    </p>
  </div>
  
  <p>
    · Authorization Username and Password
  </p>
  
  <p>
    · Server: pbxes.com
  </p>
  
  <p>
    · Port: 5060
  </p>
  
  <p>
    · Protocol: TCP
  </p>
  
  <div>
    <a href="https://guardianproject.info/wp-content/uploads/2010/05/sipdroid_account.png"><img class="alignnone size-full wp-image-336" title="sipdroid_account" src="https://guardianproject.info/wp-content/uploads/2010/05/sipdroid_account.png" alt="" width="144" height="240" /></a>
  </div>
  
  <p>
    <span><span>You should see a green dot appear in your notifications tray on successful registration like so:</span></span>
  </p>
  
  <div>
    <a href="https://guardianproject.info/wp-content/uploads/2010/05/sipdroidoptions.png"><img class="alignnone size-full wp-image-338" title="sipdroidoptions" src="https://guardianproject.info/wp-content/uploads/2010/05/sipdroidoptions.png" alt="" width="145" height="241" /></a>
  </div>
  
  <p>
     
  </p>
  
  <p>
    <strong>3.</strong> <strong>Trial Run – dial between extensions</strong>
  </p>
  
  <p>
    Once you’ve set up a number of extensions within your PBX, you can easily dial between them. Simply input their extension number (e.g. 100).
  </p>
  
  <p>
    <a href="https://guardianproject.info/wp-content/uploads/2010/05/sipdroidcall.png"><img title="sipdroidcall" src="https://guardianproject.info/wp-content/uploads/2010/05/sipdroidcall.png" alt="" width="145" height="241" /></a>
  </p>
  
  <p>
     
  </p>
  
  <p>
    <strong><span><span>4.</span></span></strong> <strong><span><span>(Optional) <span><span>Configure VPN</span></span></span></span></strong>
  </p>
  
  <p>
    <span><span>As mentioned above, the solution so far isn’t a secure one. A first step in the right direction is connecting to <span><span>PBXes<span><span>’ <span><span>PPTP VPN. For those quicker on their feet, configuration instructions can be found <a href="http://mona-lilly.de/wiki/index.php/VPN"><span style="color: #0000ff;"><span><span><span>here</span></span></span></span></a><span><span>. If you’d prefer to stick with us, follow these steps:</span></span></span></span></span></span></span></span></span></span>
  </p>
  
  <p>
    <span><span><em>4a.</em> <span><span>On<span><span> your Android phone, access the ‘VPN settings’ section of Wireless & network settings.</span></span></span></span></span></span>
  </p>
  
  <p>
    <em>4b. </em>Select ‘Add VPN,’ then ‘Add PPTP VPN’
  </p>
  
  <p>
    <a href="https://guardianproject.info/wp-content/uploads/2010/05/addvpn.png"><img class="alignleft size-full wp-image-340" title="addvpn" src="https://guardianproject.info/wp-content/uploads/2010/05/addvpn.png" alt="" width="144" height="240" /></a><a href="https://guardianproject.info/wp-content/uploads/2010/05/addvpntype.png"><img class="alignleft size-full wp-image-341" title="addvpntype" src="https://guardianproject.info/wp-content/uploads/2010/05/addvpntype.png" alt="" width="144" height="240" /></a><br /> <br style="clear: both;" /><br /> <span><span><em>4c.</em> <span><span>On<span><span> your Android phone, access the ‘VPN settings’ section of Wireless & network settings.</span></span></span></span></span></span>
  </p>
  
  <ul>
    <li>
      VPN Name – your choice
    </li>
    <li>
      VPN server – www#.pbxes.com [for # see URL line after logging into PBXes on your browser]
    </li>
    <li>
      Enable encryption – We haven’t had success with enabling encryption on PBXes yet. This might be due to a sipdroid <a href="http://code.google.com/p/sipdroid/issues/detail?id=370"><span style="color: #0000ff;"><span>issue</span></span></a> or it might not. If you have success on Android 2.0 / Éclair please let us know in the comments! <span><span> Nathan reported issues with encryption using PBXes PPTP VPN as well.  -Derek Halliday 5/12/10 4:33 PM </span></span>
    </li>
    <li>
      DNS search domain – leave empty
    </li>
    <li>
      Username – <account name>-<extension no.> (e.g. guardianproj-401)
    </li>
    <li>
      Password – <extension password>
    </li>
  </ul>
  
  <p>
    <a href="https://guardianproject.info/wp-content/uploads/2010/05/add_pptp_vpn.png"><img class="size-full wp-image-342 alignnone" title="add_pptp_vpn" src="https://guardianproject.info/wp-content/uploads/2010/05/add_pptp_vpn.png" alt="" width="144" height="240" /></a>
  </p>
  
  <p>
     
  </p>
  
  <p>
    <span style="color: #000000;"><span><strong>That’s it! </strong><span>If you come across any issues or have any questions along the way, please let us know in the “Comments” below and we’ll do our best to help you out or clarify. And if you’re itching for more, here are a couple next steps. We’re not presenting a deep tutorial on these (yet), so we’d love to hear from you if you have pursued either – or even better – if you’ve used sipdroid and/or PBXes in any other creative ways!</span></span></span>
  </p>
  
  <ol>
    <li>
      <span><span>Hook your PBXes account into an external DID / VOIP number to dial out to standard phone. Think of it as the equivalent of ‘Skype Out’ for sipdroid. You can use a service such as CallCentric (<a href="http://www.callcentric.com/">http://www.callcentric.com/</a>) for this. </span></span>
    </li>
    <li>
      <span><span>You can also integrate desktop VOIP programs or other mobile device client into the same PBXes accounts. Here’s a great list of </span><a href="https://en.wikipedia.org/wiki/List_of_SIP_software#Free_and.2For_open_source_software">free, open-source SIP clients</a><span>. We personally like </span><a href="http://icanblink.com/">Blink for Mac OS</a><span>.</span></span>
    </li>
    <li>
      <span><span>If you have a privately maintained <a id="zdnk" title="Asterisk" href="https://en.wikipedia.org/wiki/Asterisk_(PBX)">Asterisk</a> or other SIP compatible-server, you can use this same approach with that box, and integrate with your own VPN server. We will be covering this in more detail with a future post, as this is a more secure solution that using a provide such as PBXes.</span></span>
    </li>
  </ol>
  
  <p>
     
  </p>
</div>