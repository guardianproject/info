---
id: 13514
title: 'Build Your Own App Store: Android Media Distribution for Everyone'
date: 2017-02-22T09:45:11-04:00
author: Torsten Grote
layout: post
guid: https://guardianproject.info/?p=13514
permalink: /2017/02/22/build-your-own-app-store-android-media-distribution-for-everyone/
categories:
  - News
tags:
  - bazaar
  - distribution
  - F-Droid
  - fdroid
  - mobile
  - open source
  - security
  - signing
---
Most people get their Android apps from Google Play. It is usually the simplest and most secure option for them. But there are also many people who do not have access to Google Play. This might be due to lack of a proper internet connection or simply because Google Play is blocked within their country.

The [F-Droid](https://f-droid.org/) project already offers [tools to create independent app distribution channels for Android apps](/2015/06/02/building-a-trustworthy-app-store-that-respects-privacy/). These tools are ready for production, but require expert knowledge and the command-line to be used. Now, we want to build upon this foundation and develop curation tools that can also be used by people with little technical knowledge, thus making the app distribution technology more broadly available.

### Use-Cases {#use-cases}

The primary use-case we want to address is to circumvent app store censorship and blocking. But there are other use-cases that benefit from easy-to-setup app stores as well.

There are Android phones and tablets that do not have Google Play available, either because their manufacturer did not get a license from Google or because their owners prefer their phones Google-free.

Similar to Apple’s app store, the terms of service of Google Play exclude certain apps from being distributed and these are being removed on a regular basis. Having alternative means for distribution of apps is often the only way to bring those apps to people.

### Features {#features}

#### Core Features {#core-features}

  * Create a new app repository
  * Add new apps/media to the repository
  * Update existing apps/media to the repository
  * Update the description and metadata of apps/media
  * Remove apps/media from the repository
  * Automatic generation of repository website with QR Code (and instructions)
  * Import apps directly from other repositories

#### Optional Future Features {#optional-future-features}

  * Archive apps/media to archive repository
  * Remove installed apps/media from user’s devices
  * Provide hosted web-app with user-management (Sign-Up, Lost Password) as a service
  * Allow multiple curators to manage the same repository
  * Import apps (and their description) from Google Play
  * Check for updates from Google Play periodically and automatically import them
  * Making the repository available through the Tor network
  * Generate custom white-labelled repository app (based on F-Droid)
  * App security scanner for vulnerable libraries and Virus Total (opt-in) upload
  * App browsing and download on generated repository website

### Target Audience {#target-audience}

The main audience for this work are activists and trainers with moderate technical knowledge who need to securely distribute apps and updates to their community. This is especially a concern in countries where the official app store is blocked. Organizations like Amnesty International for example still need to enable people in those countries to securely receive their apps and updates.

The person maintaining the repository might use any operating system and in some cases might not even have a laptop/desktop computer available. They might be targeted by advanced attackers that can intercept and insert arbitrary traffic, but do not have the ability to compromise large service providers such as Amazon.

Furthermore, this work might also be used by the following groups:

  * service providers (who want own distribution and update mechanism for their apps)
  * individual software developers (who want to distribute beta releases for e.g. user-testing)
  * everybody else who needs full control of the entire distribution and update process

### Implementation Options {#implementation-options}

There are roughly four different ways, the app store curation tool could be implemented. Each has their own pro and cons as well as different implications for the usability.

#### Command-line interface {#command-line-interface}

The current app repository tools are already used via the command-line, but they require some setup and several non-intuitive commands to be executed. The goal here would be to reduce the number of required commands as much as possible and make them easy to understand and remember. This would be similar to how Letsencrypt’s Certbot simplified SSL certificate management.

Pros

  * least amount of work building directly on existing tools
  * signing key could be created and stored on local device

Cons

  * too difficult to use for people with no prior command-line experience
  * off-putting and not inviting for potential non-expert curators
  * adds little benefit to existing solution

#### Cross-Platform Desktop Application {#cross-platform-desktop-application}

A graphical user interface (GUI) could be added to the existing tools to make them easier to use. Existing UI toolkits such as Qt, Gtk or Tcl/Tk could be used for this.

Pros

  * can make use of existing python tools
  * signing key could be created and stored on local device

Cons

  * requires a desktop computer and installation procedure (possibly of dependencies as well)
  * need to maintain and support install packages for Windows and MacOS

#### Android App {#android-app}

The free software [F-Droid app](https://f-droid.org) already includes repository functionality used for direct app swapping. This could be modified to publish repositories to remote servers and extended by curation functionality. Alternatively, a new app could be developed that is dedicated to repository curation and could contrary to F-Droid even be distributed via Google Play.

Pros

  * Simple installation
  * No desktop computer required

Cons

  * Needs reimplementation of existing Python code in Java
  * Signing key stored on potentially less secure mobile device

#### Web App {#web-app}

The user interface for repository curation could be implemented as a web application that is accessed through a web browser. Low-risk curators could use a hosted instance for maximum simplicity while others could also access the interface through a local (built-in) web-server. Powerful web frameworks such as Flask or Django might be a good choice for that job.

Pros

  * Very easy to use from every device
  * Does not need installation (lower usage barrier)
  * Can make use of existing python tools
  * Makes multi-curator feature potentially easier to implement

Cons

  * In hosted mode: signing keys need to be stored permanently on a web server

### Security Considerations {#security-considerations}

#### Repository Attacks {#repository-attacks}

The technology used for app distribution needs to ensure the integrity and authenticity of apps provided in the repository. It can not prevent malicious apps from being _intentionally_ distributed, but can offer a security scanner to reduce the risk of unintentional distribution. An attack is considered successful when the content provided by the curator of the repository can be altered so that the changes propagate to users’ devices.

Malicious apps might compromise the targeted application or the entire phones (root exploit). There are two defenses against unintentional distribution of malicious apps:

<ol type="1">
  <li>
    app package signatures: clients trust the provided app signature on first installation (TOFU) and refuse updates with a different signature.
  </li>
  <li>
    repository signature: clients check signature when repository is installed and with every update. They warn and refuse operations with the repository when the signature is invalid.
  </li>
</ol>

The first defense is out of scope for this work, because app packages are signed when the app is built so that they are already signed when added to the repository. The repository curation should still not allow to publish an update that carries a different signature.

The second defense needs to be provided automatically by the curation tools. A repository signing key needs to be created and securely stored. If this key is compromised, an attacker can modify app metadata and can inject modified apps for specific or all users when they install them for the first time. Malicious updates of already installed apps are prevented by above package signature.

If the repository key is created and stored automatically by a service (see implementation option 4), the curator needs to trust the service and the hosting provider. Both need to be out of reach of attackers from the curators’ threat-model. For example, if the Guardian Project provides a repository service hosted in Amazon’s Cloud, this service should be out of reach of most attackers that have neither the ability to compromise the Guardian Project, nor Amazon. Advanced nation-state adversaries could compromise both and thus the repository. Recipients of apps need to trust their distributors/curators and their ability to keep their own system secure.

However, we can generally not protect against attackers who has the ability to directly compromise the users’ devices. All that can be done is to prevent malicious applications from being installed _via the repository_ (without knowledge of the curator). If the attacker can compromise users’ devices through other means, this defense does not matter anymore.

#### Root and Unknown Sources {#root-and-unknown-sources}

In order to get content from the provided repository onto a generic device, the user needs to install F-Droid which requires allowing the installation of apps from unknown sources. This can put the user at risk, because it makes installing malicious application very easy. Alternatively, super user privileges (root) can be used to install F-Droid’s system extension effectively trusting all apps installed via F-Droid. However, the security risks associated with super user privileges are even more severe as they can lead to compromise of the entire device.

#### Lack of Updates {#lack-of-updates}

If a repository is the user’s sole source for an application, any delay in providing updates might put the user at risk of an adversary exploiting a vulnerability in that application that would have otherwise been fixed by the missing update.

### What We Will Do {#what-we-will-do}

The main goal of the curation tools is to make creating and maintaining repositories as easy as possible for our target audience.

This rules out the command line and the desktop application, since today’s user experience expectations are no longer being fulfilled by these technologies. While a desktop application comes closer, the need for an installation procedure and for maintaining it for different operating systems makes it too difficult and error-prone compared to the two other remaining options.

Implementing the curation tools within an Android application has its merits. It comes with an easy installation procedure, provides a familiar state-of-the-art user interface and allows apps to be added directly from the curators’ device. However, some existing functionality would need to be reimplemented in Java and maintained along-side the existing Python codebase. Also the curator needs to provide an external storage location for the repository which can be a barrier for many users and needs its own documentation.

The easiest and most flexible solution is a web-application based on the existing Python tools. More advanced curators can use it on a local desktop computer with a built-in web-server just like a desktop application, only that the UI is in the browser. This usage scenario comes with the same pros and cons like the desktop application. The repository signing key for example is stored locally under the curator’s control.

But it allows for other usage scenarios as well. If installed on a trusted web-server as a service, the curation tools can also be used by curators with little technical knowledge. The curators don’t need to install anything and can use them from any device. They can even switch devices without a data migration. However, they would need to give up control over the signing key.

If time permits, the app store creator can be turned into a full repository service that allows user registrations and several repositories per user. A trusted organization such as the Guardian Project could host this as a service and provide it to an activist community. Software freedom would allow other organizations to host their own repository services as well. You can imagine the activist collective Riseup for example not only hosting its own repository of recommended apps, but also allowing its users to create and curate their own repositories.

This becomes even more interesting when people fill their repositories not only with apps, but with all sorts of files such as books, music and photos.