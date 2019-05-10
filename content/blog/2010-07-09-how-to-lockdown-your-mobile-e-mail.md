---
id: 383
title: 'How To: Lockdown Your Mobile E-Mail'
date: 2010-07-09T11:00:25-04:00
author: Derek
layout: post
guid: https://guardianproject.info/?p=383
permalink: /2010/07/09/how-to-lockdown-your-mobile-e-mail/
bigimg: [{src: "https://guardianproject.info/wp-content/uploads/2010/07/k9_view_decrypt-64x64.png",}]
categories:
  - App Reviews
  - HowTo
  - News
tags:
  - android
  - apg
  - encryption
  - openkeychain
  - openpgp
  - pgp
---
**Update 2015-04-27**: _We now recommend <a href="http://www.openkeychain.org/" target="_blank">OpenKeychain</a> over APG, the app described in this blog post. The set up is drastically easier, so you probably don’t even need this HOWTO anymore. Start by downloading K-9 and <a href="http://www.openkeychain.org/" target="_blank">OpenKeychain</a>, then go into OpenKeychain and start the config there._

Over the past few years it’s become [increasingly popular](http://www.youtube.com/watch?v=Gm8NdNy4wOM) to sound the call that ‘[email is dead](http://www.pcmag.com/article2/0,2817,2343209,00.asp "dead"){#y8a0}.’ And while many complementary forms of synchronous and asynchronous communication – from IM to social networking – have evolved since email first came on the scene, it’s hard to see email suddenly disappearing from its role as the most important way organizations communicate. I expect to be scooting around on my [hoverboard](http://en.wikipedia.org/wiki/Hoverboard) by the time email goes the way of the dinosaur.

Unfortunately, many of the protocols involved in sending and receiving e-mail are not considered secure – in the sense that they are vulnerable to eavesdropping. Simple Mail Transport Protocol (SMTP) – the Internet standard for e-mail transmission across IP networks  most commonly used by client applications for sending messages to a mail server for relaying – is typically implemented without any type of transport encryption. Internet Message Access Protocol (IMAP) and Post Office Protocol (POP) suffer from the same eavesdropping issues as SMTP when implemented without transport encryption. Even when SMTP is implemented with transport encryption it does not, by default, require the authentication of e-mail message senders. As a result, mail servers cannot be sure that the senders of messages are really who they claim to be. And even though POP and IMAP require users to authenticate, messages are sent and delivered using SMTP.

The result is a situation where the _recipient_ of an e-mail message can be positively identified but the _sender_ cannot. Along with the eavesdropping concerns mentioned at the top of the paragraph, this is an alarming state of affairs. Imagine if the same were true of snail mail – there would be rioting in the streets! Fortunately there has been a lot of great work done to combat these fears – the main issue being that the problem itself is  still one  that is often ignored or not fully understood by the layperson. As secure solutions for mobile platforms gain momentum, we’re hoping to change things.

Enter [OpenPGP](http://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP), an IETF standard for encryption and decryption of data. The version of OpenPGP that exists today is the evolution of PGP, which was created in 1991 as a means for secure BBSs communication and message storage (it ironically also stands for “Pretty Good Privacy”). Why do you need PGP? In the words of its inventory, Phil Zimmerman: “[It empowers people to take their privacy into their own hands](http://www.spectacle.org/795/byzim.html).” How it works is a whole other story – one too complex for the purposes of this posting – but we’ll do our  best to scrape the surface quickly. Disclaimer: The following is meant solely as an introduction. There are many people out there who are experts in these topics, and we welcome any and all comments – especially if we misstate or misrepresent anything!

PGP uses a serial combination of hashing, data compression, symmetric-key cryptography, and, finally, public-key cryptography. From the user’s perspective, it creates two [cryptographic keys](http://en.wikipedia.org/wiki/Cryptographic_key) to encrypt and decrypt data. The first of these two is called the [Public Key](http://en.wikipedia.org/wiki/Public-key) – which can be freely shared with anyone the user wishes and is used by others to encrypt data so that it can be decrypted by **only the intended recipient**. The second key is the Private Key, which should be kept as private and safe as possible. It is used to decrypt data that has been encrypted using a specific Public Key. As long as the Private Key is kept secret, only the owner is  able to decrypt data that has been encrypted with a Public Key. One problem with older methods of encryption was the relative ease with which codes could be broken. With increasingly powerful computers that are able to crack codes via pure ‘brute force,’ encoding methods must be incredibly complex to stand up. To combat this, PGP uses a key that is astronomically large,  meaning that the security of PGP encryption lies entirely with the key as opposed to keeping the method for key generation a secret. In fact, the methods that PGP encryption uses are known and widely documented. In addition, the size of keys can be increased whenever necessary to stay one step ahead of technological advances. And for the time being, each of the algorithms in current use by PGP is not known to have cryptanalytic weaknesses.

So how secure does this make your information? Italian Police, the [FBI](http://www.pcworld.com/article/110841/pgp_encryption_proves_powerful.html), and [British police](http://www.theregister.co.uk/2007/11/14/ripa_encryption_key_notice/) have been unable to crack its security and have resorted to demanding private keys. It’s been likened as “the closest you’re likely to get to military-grade encryption” by cryptographer [Bruce Schneier](http://en.wikipedia.org/wiki/Bruce_Schneier). Short answer: pretty darn good, as long as you guard your private key wisely.

You’ve probably guessed by now that the reason for this posting is to show you how to effectively use OpenPGP to secure your mobile email. And while we would’ve loved to just jump right into the tutorial, there are a few more things you should know first. [Android Privacy Guard](http://code.google.com/p/android-privacy-guard/ "Android Privacy Guard"){#udlg} (or APG for short), is a first step at bringing [OpenPGP](http://en.wikipedia.org/wiki/Pretty_Good_Privacy "PGP"){#qtjc} to the Android platform, letting you manage OpenPGP keys directly from your Android phone – and use them to encrypt, sign and decrypt emails and files. [Very recently](http://groups.google.com/group/k-9-mail/browse_thread/thread/921051bc0a61ed0b/d6085b925805ebf2?lnk=raot) the teams behind APG and the popular, open-source Android email client [K-9 Mail](http://code.google.com/p/k9mail/) have joined forces in a limited edition [team-up](http://en.wikipedia.org/wiki/Marvel_Team-Up) to create a beta version of K-9 that plays nice with APG quite seamlessly. We’ve been using it as our default email solution at Guardian for weeks now and want to share it with you!

**Note:** Currently APG only supports importing and deleting keys – not generating them – so you’ve got to use a desktop implementation of OpenPGP (such as [GNU Privacy Guard](http://www.gnupg.org/ "GNU Privacy Guard"){#vrm_}) to actually generate your keypair if you don’t already have one. A number of front-end applications and libraries are available to perform this task. If you already have a keypair set up, you should skip the first step.

<p style="padding-left: 30px;">
  <strong>1. Download and Install GnuPG Generate an OpenPGP keypair</strong>
</p>

<p style="padding-left: 30px;">
  Install GnuPG  <a href="http://www.gnupg.org/download.html">here</a>. There are binaries available for <a href="http://www.gnupg.org/download/supported_systems.en.html">whatever OS flavor</a> you prefer, and since they do a great job of making documentation and <a href="http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html">How-To Guides</a> available, we’ll skip the part where we reinvent the wheel.
</p>

<p style="padding-left: 30px;">
  <strong>2. Generate and export your keypair</strong>
</p>

<p style="padding-left: 30px;">
  Follow the instructions <a href="http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto-3.html#ss3.1">here</a> to create a new keypair. <a href="http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto-3.html#ss3.2">Export</a> your public and private keys (re-direct from stdout to a file) and stick that file on your Android device’s SD card. Usually it’s best to create a new folder /APG to keep things organized, especially if your SD card is a mess like ours 🙂
</p>

<p style="padding-left: 30px;">
  <strong>3. Download APG and import your keys</strong>
</p>

<p style="padding-left: 30px;">
  <strong> </strong>If you don’t already have it, download Android Privacy Guard from its repository <a href="http://code.google.com/p/android-privacy-guard/downloads/list">here</a> or point your barcode scanner to the QR code below. You can also find it on the Market if you prefer.
</p>

<p style="padding-left: 30px;">
  <span style="line-height: 1px; font-size: 13.2px;"> </span>
</p>

<p style="padding-left: 30px; text-align: center;">
  <a href="https://guardianproject.info/wp-content/uploads/2010/06/qrcode_apg.png"><img class="size-full wp-image-385 aligncenter" title="qrcode_apg" src="https://guardianproject.info/wp-content/uploads/2010/06/qrcode_apg.png" alt="" width="120" height="120" srcset="https://guardianproject.info/wp-content/uploads/2010/06/qrcode_apg.png 120w, https://guardianproject.info/wp-content/uploads/2010/06/qrcode_apg-64x64.png 64w" sizes="(max-width: 120px) 100vw, 120px" /></a>
</p>

<p style="padding-left: 30px;">
  Fire up APG and select ‘Manage Public Keys’ from the menu:
</p>

<p style="padding-left: 30px; text-align: center;">
  <a href="https://guardianproject.info/wp-content/uploads/2010/06/apg_menu1.png"><img class="size-medium wp-image-390 aligncenter" title="apg_menu" src="https://guardianproject.info/wp-content/uploads/2010/06/apg_menu1-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/06/apg_menu1-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/06/apg_menu1.png 480w" sizes="(max-width: 180px) 100vw, 180px" /></a>
</p>

<p style="padding-left: 30px; text-align: center;">
  <p style="padding-left: 30px;">
    From the ‘Manage Public Keys’ screen, select ‘Import Keys’:
  </p>
  
  <p style="padding-left: 30px; text-align: center;">
    <a href="https://guardianproject.info/wp-content/uploads/2010/06/apg_manage_public_keys_blur.png"><img class="size-medium wp-image-391 aligncenter" title="apg_manage_public_keys_blur" src="https://guardianproject.info/wp-content/uploads/2010/06/apg_manage_public_keys_blur-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/06/apg_manage_public_keys_blur-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/06/apg_manage_public_keys_blur.png 480w" sizes="(max-width: 180px) 100vw, 180px" /></a>
  </p>
  
  <p style="padding-left: 30px;">
    <p style="padding-left: 30px;">
      From the popup dialog, select the public key that you’ve transferred to your SD card. It’s helpful to use a file browser program like Astro File Manager if you don’t already have it installed:
    </p>
    
    <p style="padding-left: 30px; text-align: center;">
      <span style="line-height: 8px;"><a href="https://guardianproject.info/wp-content/uploads/2010/06/apg_import_keys_blur.png"><img class="size-medium wp-image-392 aligncenter" title="apg_import_keys_blur" src="https://guardianproject.info/wp-content/uploads/2010/06/apg_import_keys_blur-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/06/apg_import_keys_blur-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/06/apg_import_keys_blur.png 480w" sizes="(max-width: 180px) 100vw, 180px" /></a></span>
    </p>
    
    <p style="padding-left: 30px;">
      <p style="padding-left: 30px;">
        Once your public key(s) are successfully imported, return to the main APG menu, select ‘Manage Secret Keys’ and repeat the steps above for your Private Key.
      </p>
      
      <p style="padding-left: 30px;">
        <strong>4. Download and Configure K-9 Mail</strong>
      </p>
      
      <p style="padding-left: 30px;">
        Download the latest version of K-9 mail featuring APG integration. You can find it on the Downloads page <a href="http://code.google.com/p/k9mail/downloads/list">here</a> or, again, point your barcode scanner to the QR Code below. Whatever floats your boat.
      </p>
      
      <p style="padding-left: 30px; text-align: center;">
        <img class="aligncenter" src="http://chart.apis.google.com/chart?chs=150x150&cht=qr&chl=http://k9mail.googlecode.com/files/k9-apg-2900-beta.apk&chld=L|1&choe=UTF-8" alt="" width="125" height="125" />
      </p>
      
      <p style="padding-left: 30px;">
        Set up your email account by entering your email address and password, then give it a name.
      </p>
      
      <p style="padding-left: 30px;">
        <a href="https://guardianproject.info/wp-content/uploads/2010/07/k9_setup1.png"><img class="aligncenter size-medium wp-image-451" title="k9_setup" src="https://guardianproject.info/wp-content/uploads/2010/07/k9_setup1-168x300.png" alt="" width="168" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/07/k9_setup1-168x300.png 168w, https://guardianproject.info/wp-content/uploads/2010/07/k9_setup1-84x150.png 84w, https://guardianproject.info/wp-content/uploads/2010/07/k9_setup1.png 480w" sizes="(max-width: 168px) 100vw, 168px" /></a>
      </p>
      
      <p style="padding-left: 30px;">
        <p style="padding-left: 30px; text-align: center;">
          <img class="aligncenter" title="k9_almost_done" src="https://guardianproject.info/wp-content/uploads/2010/07/k9_almost_done-168x300.png" alt="" width="168" height="300" />
        </p>
        
        <p style="padding-left: 30px;">
          For more popular accounts such as gmail, Yahoo!, etc., K-9 will automatically detect the correct configuration. For more complex accounts such as Exchange, please check out the K-9 wiki page <a href="http://code.google.com/p/k9mail/w/list">here</a>.
        </p>
        
        <p style="padding-left: 30px;">
          <strong>5. Send and Receive Encrypted Email!</strong>
        </p>
        
        <p style="padding-left: 30px;">
          Thanks to the integration effort by the teams at APG and K-9, actually using secure mobile email becomes easy. The compose screen features a prominent checkbox and button that allow you to sign and encrypt your outbound messages, respectively.
        </p>
        
        <p style="padding-left: 30px;">
          <a href="https://guardianproject.info/wp-content/uploads/2010/07/k9_compose.png"><img class="aligncenter size-medium wp-image-453" title="k9_compose" src="https://guardianproject.info/wp-content/uploads/2010/07/k9_compose-168x300.png" alt="" width="168" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/07/k9_compose-168x300.png 168w, https://guardianproject.info/wp-content/uploads/2010/07/k9_compose-84x150.png 84w, https://guardianproject.info/wp-content/uploads/2010/07/k9_compose.png 480w" sizes="(max-width: 168px) 100vw, 168px" /></a>
        </p>
        
        <p style="padding-left: 30px;">
          Decrypting messages with your private key is even easier and is literally a 1-touch experience:
        </p>
        
        <p style="padding-left: 30px;">
          <a href="https://guardianproject.info/wp-content/uploads/2010/07/k9_almost_done.png"></a><a href="https://guardianproject.info/wp-content/uploads/2010/07/k9_view_decrypt.png"><img class="aligncenter size-medium wp-image-455" title="k9_view_decrypt" src="https://guardianproject.info/wp-content/uploads/2010/07/k9_view_decrypt-180x300.png" alt="" width="180" height="300" srcset="https://guardianproject.info/wp-content/uploads/2010/07/k9_view_decrypt-180x300.png 180w, https://guardianproject.info/wp-content/uploads/2010/07/k9_view_decrypt-90x150.png 90w, https://guardianproject.info/wp-content/uploads/2010/07/k9_view_decrypt.png 480w" sizes="(max-width: 180px) 100vw, 180px" /></a>
        </p>
        
        <p style="padding-left: 30px;">
          <strong>Enjoy! </strong>As always, please post all questions, concerns, and jokes (only good ones please) in the Comments section. We’re very excited about the powerful combination that these two apps bring and we’d love to hear from you!
        </p>
        
        <p style="padding-left: 30px;">
          If you find any issues with APG, please report them <a href="http://code.google.com/p/android-privacy-guard/issues/list">here</a>:
        </p>
        
        <p style="padding-left: 30px;">
          <span style="line-height: 13px;"><span style="line-height: 16px;">Likewise, report issues with K-9 <a href="http://code.google.com/p/k9mail/issues/list">here</a>. </span></span>
        </p>