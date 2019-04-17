---
id: 13924
title: 'Haven: Building the Most Secure Baby Monitor Ever?'
date: 2017-12-22T09:07:00-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=13924
permalink: /2017/12/22/haven-building-the-most-secure-baby-monitor-ever/
publish_post_category:
  - "6"
publish_to_discourse:
  - "0"
update_discourse_topic:
  - "0"
discourse_post_id:
  - "583"
discourse_topic_id:
  - "412"
discourse_permalink:
  - https://talk.developersquare.net/t/haven-building-the-most-secure-baby-monitor-ever/412
discourse_comments_count:
  - "2"
discourse_comments_raw:
  - '{"id":412,"posts_count":3,"filtered_posts_count":3,"posts":[],"participants":[{"id":274,"username":"Loxmyth","avatar_template":"https://avatars.discourse.org/v2/letter/l/4bbf92/{size}.png"},{"id":282,"username":"Pentiummania","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/pentiummania/{size}/340_1.png"},{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553111199"
wpdc_sync_post_comments:
  - "0"
image: http://guardianproject.info/wp-content/uploads/2017/12/Haven_app.jpg
categories:
  - Development
  - New Release
tags:
  - encryption
  - IoT
  - privacy
  - smart camera
  - surveillance
---
About eight months ago, friends at the [Freedom of the Press Foundation](https://freedom.press/) reached out to us, to see if we were interested in prototyping an idea they had been batting around. They knew that from projects like [CameraV](https://guardianproject.info/apps/camerav) and [ProofMode](https://guardianproject.info/2017/02/24/combating-fake-news-with-a-smartphone-proof-mode/), that we knew how to tap into the sensors on smartphones to do interesting things. They also knew we could connect devices together using encrypted messaging and onion routing, through our work on [ChatSecure](https://chatsecure.org) and Tor ([Orbot!](https://guardianproject.info/apps/orbot)). They also knew of our deep interest in bringing ideas to life that can solve real problems faced by people out on the front lines (both at home and abroad), who often are more in danger from physical threats, than digital. They had a concept that would bring all of these things together, and just wanted to see if it was even possible. We were game, and well, here we are today, announcing a real working public beta, and a new open-source project, that we are extremely excited about.

**IT’S NOT JUST A PHONE**

At some point soon, we should stop calling the smartphones that over two billion people carry with them everyday and everywhere, phones at all. These devices have powerful processors with multiple cores, at gigahertz speeds, and gigabytes of RAM and storage. They have at least two cameras, now often three, arrays of microphones to capture sound near and far, and high definition, hyper sensitive touch screens for controlling them. They contain multiple radios and signal processors, that allow you to make crystal clear calls to someone on the other side of the planet, live stream 4K video, and download a game all at once. Most importantly, for the work we are announcing today, they contain an amazing variety of sensors, that can measure gravity, motion, air pressure, ambient light, temperature, and your precise location on the planet. I don’t think Alexander Graham Bell ever imagined a telephone doing all of these things. Once you step back from thinking of these devices as phones, and instead as powerful general purpose portable computing platforms, a world of possibilities and potential uses opens up wide. Even better, many people have an old second-hand, last generation device lying around, ready to be transformed into a computing platform much more powerful than a Raspberry Pi or some generic Internet of Shoddy (!) Things platform.

**A SAFE ROOM IN YOUR POCKET**

This re-imagining of a smartphone as something more, is what inspired the development of [Haven](https://guardianproject.github.io/haven/), a new open-source project and mobile app we are announcing today, built in partnership with Freedom of the Press Foundation. The concept of [Haven](https://guardianproject.github.io/haven/), as imagined by Micah F. Lee and Edward Snowden, is based on the notion that any smartphone could be turned into a personal, portable security device, to watch for unexpected intrusions into physical spaces.

<div class="arve-wrapper" data-mode="normal" data-provider="youtube" id="arve-Fr0wEsISRUw" style="max-width:945px;" itemscope itemtype="http://schema.org/VideoObject">
  <div class="arve-embed-container" style="padding-bottom:56.250000%">
  </div>
</div>

They call it a “safe room” in your pocket, or way to defeat “evil maid” attacks, that lets you know when you’ve been targeted by a “black bag” operation. I also like to think that through Haven, we have unexpectedly created the most powerful, secure and private baby monitor system ever. By tapping into the sensors and processing power on these devices with custom software, a system could feel the vibrations of someone walking, detect the shine of a flashlight, hear the sound of a door opening (or a child crying), or see someone entering into the view of a camera. All of these “intruder alerts” are recorded on the device, so that the victim can have evidence of their unwanted guest. Even better, they can receive real-time secure and private notifications, with images and sound, as it happens, and take appropriate actions.

**YOU ARE THE WATCHER  
** 

An important design goal of Haven, is to not require the user to share data with any third-party, or to have centralized infrastructure. It was clear that some might see Haven as a surveillance device (or “self” sous-veillance), which, regardless of who is in control of it, can be problematic and a vulnerability. Thus, it was a fundamental tenet to not require people to give up privacy, in order to gain security. The person we aim to help must have complete control of the system, the sensors and the captured data and media. In addition, the device must not simply record a stream of video, audio and sensors, hoover-ing up all things. Only when configurable sensor thresholds are crossed, is any data recorded permanently in the log. All of the processing and analysis of the sensor data happens locally on the device, and is only stored locally, and not in a cloud. The device itself can be protected by a strong password and disk encryption, to stop intruders from meddling or accessing any data.

**SIGNAL’D AND ONION’D**

If the intruders chooses to destroy or make off with a Haven device, thats fine. The every act of vandalism and theft is detected in progress, and the owner of the device is notified in real-time. All photos and audio can be sent remotely via notifications, ensuring the evidence is safe. Haven does currently support optional plaintext SMS notifications. This does leak some data to the mobile operator or anyone who can access your text messages, that you are using Haven.

<p style="text-align: center;">
  <a href="https://guardianproject.github.io/haven/docs/preso/" target="_blank" rel="noopener"><img class="aligncenter wp-image-13927 size-large" src="https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-11-1024x576.jpg" alt="" width="945" height="532" srcset="https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-11-1024x576.jpg 1024w, https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-11-300x169.jpg 300w, https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-11-768x432.jpg 768w, https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-11.jpg 1500w" sizes="(max-width: 945px) 100vw, 945px" /></a><em>Click to view our <a href="https://guardianproject.github.io/haven/docs/preso/" target="_blank" rel="noopener">online presentation on Haven</a></em>
</p>

 

We provided SMS support because we wanted Haven to be used in parts of the world where mobile internet access isn’t available, is too expensive, or is heavily censored. The notification message sent over SMS provide minimal information to an attacker. Better than SMS, however, is the integrated support for sending fully end-to-end encrypted notifications, with photo and audio attachments, over Signal. This method allows you to use a device without a SIM card, or in airplane mode, since Signal utilizes the internet for communication, not the mobile operator network. Haven also includes support for Tor’s Onion Services, through integration with Orbot, the Tor app for Android. This allows you to activate a web service on your device, and make it accessible via a “.onion” address, which you can access from any Tor-enabled browser, like Tor Browser, Orfox or Onion Browser. This provides a surveillance-free, end-to-end encrypted channel between you and your device, through which you can access all data stored in Haven, past and present.

**INTERNET OF SHODDY THINGS**

At this point, you might be saying to yourself “Wait, did these paranoid privacy hackers just building a surveillance camera? Are they trying to sell me on some kind of IoT crap?”. While we didn’t set out to try to address the insane amount of vulnerabilities, insecurities, and fundamental flaws that most most commercial home security devices have, we do admit that our work on Haven crosses over into that problem space. We knew that journalists, activists and others were not interested in setting up cameras and microphones watching themselves 24/7, streaming to the cloud, as a solution to their threat. We also knew, as discussed before, that linking any solution to a centralized cloud service that asked you to trust them, also didn’t make sense.

[<img class="aligncenter size-large wp-image-13929" src="https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-07-1024x576.jpg" alt="" width="945" height="532" srcset="https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-07-1024x576.jpg 1024w, https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-07-300x169.jpg 300w, https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-07-768x432.jpg 768w, https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-07.jpg 1500w" sizes="(max-width: 945px) 100vw, 945px" />](https://guardianproject.info/wp-content/uploads/2017/12/havenpreso-07.jpg)

What we’ve built then could be seen as a competitor to commercial solutions, except for a few key points. First, it is freely licensed, and open-source, enabling anyone to audit it, improve it, remix it, and use as they see fit. It runs on any hardware that can support the Android operating system back to version 4.1. This includes not just smartphones, but also tablets, Raspberry Pi’s, TV set top boxes and sticks, and the emerging Android Things platform. This makes it portable, battery powered, and able to run on devices that are readily available for very little money, anywhere in the world. It takes advantage of many more sensors than a typical home security product, and can easily be expanded to support more. Most importantly, all network communications can be encrypted using other open-source gold standards such as Signal and Tor. You can receive notifications from and access in real-time your Haven device anywhere in the world, completely privately, without any third-party even knowing you are doing so. This addresses the primary threat of remote network intruders, device botnets, and legal actions, as well. The goal is for someone to be able to use Haven, without anyone knowing they are.

With these innovations, we have set the bar for what a personal security device should be, and do. We know that many people this holiday season will be setting up new cameras around the house, on their front door, in their car… pretty much everywhere, and letting a third-party tap into all of that content. We think that Haven shows a better way, that provides just as much, if not more, peace of mind.

**THE ROAD AHEAD AND YOU!**

Today, we are announcing our public beta, and beginning to promote the open-source project. Haven was originally built upon our previous work with CameraV and ProofMode, as well as a project called SecurIt from developer Marco Ziccardi (<https://github.com/mziccard>), which is how we went from an idea to a pretty cool app in about eight months. The team at Guardian Project, has been doing the bulk of the work up to this point, but as with all of our projects, we look to expand our contributions to the community. If you are interested in this project, for your own use, as an activist, or as a developer, designer or hardware hacker, we need your help. Here’s a quick set of things to do to join:

* Check out the [Github issues](https://github.com/guardianproject/haven/issues) and the [Prototype Project board,](https://github.com/guardianproject/haven/projects) pick some things to work on or provide feedback on  
* Come talk with us at the Guardian Project through our points of contact: <https://guardianproject.info/contact>  
* Test Haven out on your hardware and let us know if you find any issues (see [havenapp.org](http://havenapp.org) for links)  
* Share your user stories, personas, threats and more, to ensure we are keeping your needs in mind  
* Donate (Bitcoin accepted!) to support our ongoing efforts: <https://freedom.press/donate-support-haven-open-source-project/>

Thanks for reading this far, and being interested in our ongoing work, to ensure people are empowered by mobile technology, and not endangered by it. Happy Holidays, and remember: keep watch, stay safe!

 