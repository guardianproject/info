---
id: 2478
title: Threats and Usability of Secure Voice
date: 2012-07-10T12:48:18-04:00
author: patch
layout: post
guid: https://guardianproject.info/?p=2478
permalink: /2012/07/10/threats-and-usability-of-secure-voice/
image: http://guardianproject.info/wp-content/uploads/2012/07/whitdiff.jpg
categories:
  - News
tags:
  - audit
  - encryption
  - ostel
  - ostn
  - voip
  - zrtp
---
In my [previous post](https://guardianproject.info/2012/07/05/a-network-analysis-of-encrypted-voice-over-ostn/) I found that end-to-end encryption with OSTN is both effective and usable. There are two important things the user must be aware of when using OSTN. They must confirm with each phone call that the encryption icon is present and  they must correctly complete SAS verification dialog boxes. So on a basic level, encrypted voice just works. But, what does this all mean? This post looks at the threats to security and usability of encrypted ZRTP phone calls in CSipSimple.

**Usable Security**  
Crypto wizards have created and refined algorithms that bring strong encryption to the everyday user. Yet, more often then not, security is compromised through user error. This is a usability problem. Information security is abstract and the practicalities of the real world demand that encryption software &#8216;just works&#8217; for the average user. It is more dangerous for a user to be unaware of a loss of encryption then that they fail to get it working. Government P25 handheld radios were found to have such poor usability for encryption that a [research team](http://www.crypto.com/blog/p25) found many government agents accidentally transmitting sensitive information in the clear. ZRTP and CSipSimple&#8217;s implementation fair much better however.

<div id="attachment_2606" style="width: 283px" class="wp-caption alignleft">
  <a href="https://guardianproject.info/wp-content/uploads/2012/07/whitdiff.jpg"><img aria-describedby="caption-attachment-2606" class="wp-image-2606 " title="whitdiff" src="https://guardianproject.info/wp-content/uploads/2012/07/whitdiff-300x244.jpg" alt="Whit Diffie" width="273" height="222" srcset="https://guardianproject.info/wp-content/uploads/2012/07/whitdiff-300x244.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/07/whitdiff.jpg 528w" sizes="(max-width: 273px) 100vw, 273px" /></a>
  
  <p id="caption-attachment-2606" class="wp-caption-text">
    Whitfield Diffie is pioneer of modern cryptography
  </p>
</div>

<div id="attachment_2612" style="width: 250px" class="wp-caption alignright">
  <a href="https://guardianproject.info/wp-content/uploads/2012/07/gandalf22.jpg"><img aria-describedby="caption-attachment-2612" class=" wp-image-2612" title="gandalf" src="https://guardianproject.info/wp-content/uploads/2012/07/gandalf22-300x283.jpg" alt="Gandalf" width="240" height="226" srcset="https://guardianproject.info/wp-content/uploads/2012/07/gandalf22-300x283.jpg 300w, https://guardianproject.info/wp-content/uploads/2012/07/gandalf22.jpg 546w" sizes="(max-width: 240px) 100vw, 240px" /></a>
  
  <p id="caption-attachment-2612" class="wp-caption-text">
    Whit and Gandalf fight evil with magic abilities gained by pouring through dusty tomes full of obscure symbols. (Borrowed from this excellent <a href="http://www.subspacefield.org/security/math_rules_cyberspace_20120421/math_rules_cyberspace_20120421.pdf">Math Rules Cyberspace</a> presentation)
  </p>
</div>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

Although not required for the average user, its good to have a basic background of cryptography. This is not an full introduction, but it will provide some background on ZRTP and the importance of authentication.

**ZRTP, Authentication, PKI**  
Most usability issues with encrypted communications deals with Public-Key-Infrastructure or PKI. Public Key Infrastructure is how we verify the identity of each participant in a communication channel. Verifying the identity of the other party is important to prevent [Man-In-The-Middle-Attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). These attacks allow an attacker the opportunity to eavesdrop. PKI is a crucial point to understand in almost all encryption schemes. It inherently effects how the encrypted communication medium will be used.

Basically, to use encryption, both users must exchange secret keys without transmitting them in the clear. This is a bootstrapping problem, exchanging keys safely requires both users to already have exchanged keys! Public key cryptography has solved the problem of needing to secretly exchange keys in advance. Rather, a user can exchange public keys that don&#8217;t require secrecy. These keys can be published to the world. The issue is then whether or not the public key is **authentic**. How does one user know that they received the right public key and not the public key of an attacker attempting a MITM attack?

Different communities have different approaches to PKI. Smaller distributed technical communities have long relied on the web-of-trust model supported by [PGP](http://en.wikipedia.org/wiki/Pretty_Good_Privacy). This was the first widely available open-source software that provided strong cryptography to everyone. It was created by Phil Zimmerman who also created ZRTP to encrypt voice.  Its work flow, while fine for some, has precluded its widespread adoption outside of the tech community.

Websites rely on a Certificate Authorities to make encryption transparent for the user.  It does not require the user to make manual trust decisions and &#8216;just works&#8217;. However, it never obtained the goal of strong end-to-end encryption the way PGP has because it relies on the trust of centralized authorities that have proven time and time again to not be trustworthy. The future of SSL is a heavily researched area. For some approaches to this issue I&#8217;d personally suggest looking into [DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions), [Convergence](http://blog.thoughtcrime.org/ssl-and-the-future-of-authenticity), and this [talk](http://events.ccc.de/congress/2010/Fahrplan/events/4295.en.html) from Dan J. Bernstein, a cryptographer and professor at the University of Illinois. [This talk](https://www.youtube.com/watch?feature=player_embedded&v=Z7Wl2FW2TcA) by Moxie Marlinspike at Blackhat 2011 is great, it introduces Convergence and provides an interesting dialogue on the SSL issue.

Modern cryptographic protocols such as OTR(instant messaging) and ZRTP(voice) have come a long way in providing easy to use end-to-end encryption. They are open standards that strike a great balance between usability and security. They both have adopted to the TOFU POP model (Trust on First Use- Persistence of Pseudonym).  This is similar to what SSH does: when you first connect to the server you are asked if you want to save and trust the server&#8217;s public key. ZRTP takes it a step farther and **verifies** the other party&#8217;s identity on first use.  A commitment protocol is used that requires the users to discuss whether they both are viewing the same string of text in a dialog box. This guarantees that the person you hear on the other end of the phone is the actual person your talking to.

This is great because by saving the public key and trusting it an attacker can no longer pretend to represent someone else&#8217;s key. This relies on the first conversation not being actively attacked. The commitment protocol strengthens this by making sure that the first time you trust a key, you actually have a way to verify it. This solves the issue of MITM attacks!

If all this doesn&#8217;t make sense, that is OK, you don&#8217;t actually have to understand cryptography to use OSTN. You just need to understand what it provides you (Confidentiality!). More information about authentication and verification was written in a great [post by Hans](https://guardianproject.info/2012/03/19/on-verifying-identity-using-cryptography/). Guardian also has a great research project called [PSST](https://guardianproject.info/wiki/PSST) that is actively solving verification problems like this across multiple platforms and communication schemes.

Below are the threats to the current ZRTP implementation in CSipSimple from both the user&#8217;s perspective and attacker&#8217;s perspective.

**User Threats**  
ZRTP is great in this regard. It is one of the most user friendly ways to enable verified end-to-end encryption. This said, there are two concepts that a user should understand:

  * **Verification:** The first time you call someone with ZRTP a dialog box is displayed that asks both users to confirm that they see the same SAS (Short Authentication String). Once confirmed this identity will persist within your OSTN account and when you call the same person this dialog will not appear. If your conversation is not verified it is possible that the call is susceptible to a certain kind of attack (MITM) that allows someone to listen to your phone call. As seen in the pictures above it is easy to tell if your phone call is encrypted but not if it is verified. It is up to the user to make sure they pay attention to the SAS dialog at the beginning of a conversation. Key&#8217;s are remembered after first verification so lack of a SAS box indicates the user&#8217;s have both hit OK on a previous SAS box.
  * **Opportunistic Encryption: **This means that encryption is only attempted, but not forced. If you have encryption on, but you happen to talk to a friend who has managed to turn it off, then your call will silently remain unencrypted.  Since encryption can not be forced, a user must not  expect to be encrypted but rather check their phone at the beginning of every call to be sure. This is how opportunistic encryption should work, but it would be easy for a user to assume otherwise. Don&#8217;t do it!

**Adversarial Threats**  
Currently, I see two opportunities for attackers that are related to the same two usability concerns listed above.

  * **MITM: **I mentioned before that unverified conversations are susceptible to eavesdropping. This is solved by verifying each conversation by sharing a 4 letter code before starting a conversation. You must actually cancel or ignore the SAS dialog for this to happen. Don&#8217;t!
  * **Force clear-voice communication:** Opportunistic encryption presents a more interesting problem. It is possible for someone to selectively block a ZRTP negotiation packets. This would force two users to start a conversation in clear-voice despite both setting their accounts to use ZRTP. It would be obvious to the user if they check for the lock icon, but friends who frequently communicate with OSTN might forget to check each time. This could be prevented by having a setting to force encryption. In this case the call would simply fail. In Wireshark, I was clearly able to distinguish the ZRTP negotiation packets. An attacker who can filter your traffic on the application layer can perform this attack. ISPs, Governments, and adversaries on your LAN may reasonably be in a position to do this.

The MITM attack can be mitigated with verification. The selective blocking of ZRTP packets can not be avoided (because ZRTP can&#8217;t stop censorship) but the consequences can be mitigated by paying attention to when your calls are encrypted.

**Improving ZRTP usability  
**  
Given the threats listed above, I see a couple things that would increase usability and prevent accidental misunderstandings by the user.

  * **Forced ZRTP Encryption**: ZRTP in CSipSimple has two modes: off or opportunistic. I would propose changing these options to **ZRTP Off, Attempt ZRTP**, and **Force ZRTP**. Force ZRTP would provide a huge security benefit to accounts in CSipSimple that you would always expect to use encryption with.OSTN would of course be the ideal example here.

<div id="attachment_2621" style="width: 310px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2012/07/zrtpoptions.png"><img aria-describedby="caption-attachment-2621" class="size-medium wp-image-2621" title="zrtpoptions" src="https://guardianproject.info/wp-content/uploads/2012/07/zrtpoptions-300x240.png" alt="" width="300" height="240" srcset="https://guardianproject.info/wp-content/uploads/2012/07/zrtpoptions-300x240.png 300w, https://guardianproject.info/wp-content/uploads/2012/07/zrtpoptions.png 447w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-2621" class="wp-caption-text">
    Current ZRTP options in CSipSimple
  </p>
</div>

  * **Verification Status:** Currently you can tell when your conversation is ZRTP encrypted by the lock icon. This is great because this allows the user to avoid problems with opportunistic encryption or a downgrade attack. It would make sense to allow the user to see whether their call has also been authenticated correctly. Feedback might encourage users to continue to correctly use the SAS function.

<div id="attachment_2622" style="width: 310px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2012/07/lockicon.png"><img aria-describedby="caption-attachment-2622" class="size-medium wp-image-2622" title="lockicon" src="https://guardianproject.info/wp-content/uploads/2012/07/lockicon-300x298.png" alt="" width="300" height="298" srcset="https://guardianproject.info/wp-content/uploads/2012/07/lockicon-300x298.png 300w, https://guardianproject.info/wp-content/uploads/2012/07/lockicon-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2012/07/lockicon.png 350w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-2622" class="wp-caption-text">
    This means your OSTN call is encrypted. It would be useful if it displayed the verification status of the caller as well.
  </p>
</div>

  * **Verification Options: **Currently when verifying an identity the user is displayed with the SAS. They have the option to press &#8216;OK&#8217; or &#8216;Cancel&#8217;. Cancel effectively ignores this step, OK means that the SAS has been verified. This is non-intuitive. I would propose simply having three options: **Verify, Ignore, Reject. **The current function of OK is mapped to Verify, Cancel is mapped to Ignore, and Reject ends the phone conversation in situations in which the SAS doesn&#8217;t match.

<div id="attachment_2623" style="width: 310px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2012/07/sasbox.png"><img aria-describedby="caption-attachment-2623" class="size-medium wp-image-2623" title="sasbox" src="https://guardianproject.info/wp-content/uploads/2012/07/sasbox-300x199.png" alt="" width="300" height="199" srcset="https://guardianproject.info/wp-content/uploads/2012/07/sasbox-300x199.png 300w, https://guardianproject.info/wp-content/uploads/2012/07/sasbox.png 447w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-2623" class="wp-caption-text">
    Suggested improvement would present &#8220;Verify, Ignore, and Reject&#8221; as options to the user
  </p>
</div>

**Wrapping up**  
It should be noted that I pick on CSipSimple over the other clients because it is both great software and the recommended client to use with OSTN. It is still considered experimental software and requires the nightly release for OSTN support. Other clients may suffer from these ZRTP usability issues as well. The good thing is that by simply implementing a working ZRTP client you should have most of the protocol benefits thanks to its simple and elegant design. The recommendations I make here should applicable across all ZRTP implementations. A future comparison of of these implementations may be in order.

&nbsp;

&nbsp;