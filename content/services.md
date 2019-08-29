---
id: 13442
title: Services
date: 2016-11-14T23:58:19-04:00
author: n8fr8
guid: https://guardianproject.info/?page_id=13442
image: https://guardianproject.info/wp-content/uploads/2015/06/5399436072_d9bcbbab50_b.jpg
menu:
  main:
    parent: about
---
We offer services for-hire for a variety of work related to our mission, projects and code-base.

We have deployed fully secure service infrastructures for mobile devices, from client to server, using open protocols and standards, such as XMPP+OMEMO and SIP+ZRTP. We utilize and promote the adoption of public, transparent collaborative development processes, built on Git (Gitlab, Github), Continuous Integration (Travis, Gitlab-CI), test driven development practices, and public communications channels like mailing lists and secure group messaging.

We build software with modularity in mind, utilizing Gradle (Android), CocoaPods (iOS), NPM and other systems, to build upon, or create if needed, reusable, testable, reproducible code libraries. Finally, we offer usability testing, quality assurance, and release acceptance processes, to ensure we are effectively delivering upon the desired enhancements and product roadmap.

## Engagement Team

Our team is made of product leads, software developers, user experience designers, and user advocates who have been working in mobile application and platform development for over twenty years. For the past nine years, as Guardian Project, we have focused equally on developing our own technology, while fostering deep partnerships with human rights and activists organizations in need of our services. This includes engaging deeply with partners’ staff to uplift their knowledge and skill set to be able to support their technical programs long term. We have also worked to incubate mobile support for keyprivacy technologies such as Tor, GnuPG, OTR, SQLCipher and Debian, where interest in emerging platforms directly within the communities themselves was nascent.

  * Engagement Manager: Works with client to define needs, scope, milestones and schedule  
    Solution Architect: Works with all parties to design the solution specification and specific tickets
  * Mobile Developer: Implementations features, enhancements, bug fixes for mobile software, working in concert and constant review with client and entire team
  * Systems Developer (SysAdmin, DevOps): Implementations server/infrastructure features, configurations, images, scripts, as well as security controls, access protocol, etc.
  * Quality Assurance / Testing: Tracks progress by development teams, provide QA feedback, and handles acceptance testing for all features, enhancements, bug fixes

## Menu of Services

Some examples of work we do for hire include:

**Integration of secure data and media storage into a mobile app**

Assist the application’s development team to define (architect) how application data and media can be stored safely.  Two mechanisms exist: SQL database storage (using API that closely mimics SQL) and file system (using API that matches the existing file system API).  Development team will require assistance with acquiring the libraries and integrating them into their build environment. Development team will likely need assistance with debug methodologies, management of encryption keys, safe error logging and reporting.

**Integration of Secure Messaging features into mobile app**

Integrate secure messaging and notification features into a mobile app, using Signal protocol through OMEMO, XMPP open protocol messaging, and XMPP Cloud Notify (ChatSecure Push). Implement system for adding and communicating with contacts through a pseudonymous identity, not tied to real names, phone number or email. Optionally implement communication through censorship and surveillance resistant transports such as Tor or Pluggable Transports.

**Integration of PanicKit into an Android mobile app**

Assist the application’s development team in handling “panic” signals from a Panic trigger application, thus allowing the developer’s app to support emergency data delete, app hiding, SOS message alerts. Also, optionally, integrate Panic trigger capabilities into their app, to support unique methods for trigger (hardware, location, motion).  Development team will require assistance with acquiring the libraries and integrating them into their build environment.

**Kit-out a set of Android phones for delivery to a project team**

The task here is to define a special configuration of security and operational software to be delivered on a specific type of Android device likely based on Copperhead (or other secure OS) such that all team members have a unified base experience and secure environment.  These devices would all be “backed” by a unique (predefined) custom F-Droid software distribution that would, in daily operation, keep the on-board software up to date.

**Set up a secure and private XMPP communication endpoint for an organization or project team**

The task here is to set up a secure, XMPP Infrastructure, Ansible-scripted for maintenance and upgrade, with minimal logging, for production use by the organization or team.  The configuration would be production tested, scalable and distributable (to multiple geographics, IP ranges, or domains) depending on organization size and needs.

**Establish a Pluggable Transport service for a defined user group on behalf of a single organization**

The task here is to setup, configure and provide maintenance for a defined and specific circumvention service (e.g., Meek, ShadowSocks, Wireguard) to be offered by an organization for a specific community of users.   The configuration would be production tested and scalable.

**Mobile application and system threat modeling**

The task here is to work with an application (or system/service) development team to understand the types of internal and external threats that could impact them, then architect solutions for combating those threats (to be ultimately implemented in software, procedures or training) by the application or system team.