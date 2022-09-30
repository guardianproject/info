---
title: "The Search for Ethical Apps: Let's start with governments"
author: Hans-Christoph Steiner
categories:
  - News
tags:
  - Android
  - apkeep
  - EFF
  - Exodus Privacy
  - F-Droid
  - ITUJ
  - LfDI-BW
  - metadata
  - mobilsicher
  - NGI0-discovery
  - NLnet
  - Pithus
  - privacy
  - TechLore Plexus
  - The Search for Ethical Apps
  - tracking
  - Tracking-the-Trackers

---

Governments across the world are moving services to mobile apps.  The vast majority of these apps are only available in the Google Play store or in the Apple App store.  Installing apps from these services requires users to agree to their terms of service.  This means governments require their citizens to sign opaque and privacy invading contracts with foreign Big Tech in order to use digital services.  This feeds ever more into Big Tech data control, filtering, and information bubbles.  There are some exceptions here, like China has multiple app stores that are popular.  Chinese Big Tech also require restrictive terms of service agreements.  Additionally, many of apps are developed by the same firms that are tied into the surveillance capitalism ecosystem.  So they include features that track the end users. The governments are not demanding data transparency, and these firms have not been delivering it.

In Austria, there is a clear example: the [_Handy Signatur_](https://www.a-trust.at/en/Handy-Signatur/) app.  Public health insurance providers require this app for people to access their accounts online. Since COVID-19 countermeasures forced schools into online-mode, many public schools have been requiring education apps for students, parents and teachers to connect with and interact with the school. People with the that app can also sign petitions and download vaccination certificates those without have to do much more work.

Mobile phone users want to know about what apps are doing with their personal data. Citizens around the world gaining consciousness about these issues.  In order to build public pressure, a critical mass must be aware of these problems. To learn, they must first discover how widespread and entrenched this problem is.  We received funding from [NLnet]](https://nlnet.nl/project/EthicalApps/) to work on this key area.  This project integrates existing tools and builds a "software kit" to make it easy to generate data about the apps governments require.  This data will be simple to index so that it citizens and search it and discover the terms their governments are requiring them to take to access e-government services.

Journalists are just starting to report on this large and growing problem.  One of the few stories in the European media came recently in the Dutch media: "[_Overheid dwingt burger in de richting van Google en Apple_](https://fd.nl/economie-politiek/1383007/overheid-dwingt-burger-in-de-richting-van-google-en-apple)" (The authorities force citizens towards Google and Apple).  On top of transparency, governments should also ensure that the apps they make and use are available without privacy concerns or corporate control, and that they are not feeding data to companies that control search algorithms and limit user autonomy.

This first step is to make a repository with the apps related to government services.  This then provides a template for others to do the same in other countries.  Next steps are include pushing organizations and companies to do the same, for example school and banking apps; getting more country repositories and perhaps an EU repository; an helping governments, organizations, and companies set up good distribution options.  Governments should also list F-Droid as an option for getting the apps whenever they mention Google Play and Apple App Store.  And when governments go [all](https://f-droid.org/packages/de.bwl.lfdi.app/) [the way](https://www.baden-wuerttemberg.datenschutz.de/lfdi-bw-app-f-droid/), they should be lauded. 🎉

We work partners to make this come to life:

* F-Droid provides all the tools for securely publishing and managing app repositories.  F-Droid's community app [review](https://gitlab.com/fdroid/rfp/-/issues) [process](https://gitlab.com/fdroid/fdroiddata/-/merge_requests) gives us a template to build upon for reviewing all apps in an open way.  F-Droid provides another option that does not lock anyone into any service. There are no terms of service, or even [user accounts](https://f-droid.org/2022/02/28/no-user-accounts-by-design.html) to sign up for.  And F-Droid provides a decentralized app distribution ecosystem where anyone can publish their own apps via their own repositories.  If the app is free software, it can be included in the main [f-droid.org](https://f-droid.org) repository.  Millions of users have installed F-Droid themselves, and companies like Fairphone have shipped devices with F-Droid pre-installed.  Anyone can freely install F-Droid on any Android device.  So F-Droid provides app distribution without being locked into any service, unlike Google Play.
*  ITUJ's [mobilsicher](https://mobilsicher.de/) project will provide the user facing service for Germany. Their new repository will serve both as an app distribution provider, and as an example of how other organizations can do the same.  Their impressive [app-check](https://git.app-check.org/app-check) review [platform](https://appcheck.mobilsicher.de/) is a complete stack for human reviewers to do dynamic analysis, and the database they have built up will be integrated into the review process.
* [Exodus Privacy](https://exodus-privacy.eu.org/) focuses on tracking embedded in Android apps.  It works based on users requesting apps be reviewed.  It is an important source for this project since it is narrowly focused on detecting and reporting tracking in any Android app.
* EFF created and maintains [_apkeep_](https://github.com/EFForg/apkeep), the essential tool for getting the actual app files to inspect when the source code is not available.
* [Pithus](https://beta.pithus.org/about/) is a mobile threat intelligence platform for activists, journalists, NGOs, researchers that is a entirely open platform supported and maintained by the community.
* [Techlore Plexus](https://github.com/techlore/plexus) is a catalog of Android apps that have been reviewed in terms of compatibility with Google-free devices.  For example, they list whether an app requires Google Play Services to run.

Of course, this is not the complete solution for [ethical apps](https://www.ethicsinapps.eu/).  This is a stepping stone towards the end goal of "[Public](https://publiccode.eu/) [Money](https://www.eff.org/deeplinks/2017/10/public-money-public-code-show-your-support-free-software-europe), [Public](https://publiccode.asia/) [Code](https://blog.okfn.org/2017/09/20/public-money-public-code/)".  This project will push governments down that road by outlining easier steps to take as they move towards free software: making apps available for public audit, allowing users to install apps without agreeing to any terms of service, etc.  It enables users of free platforms like CalyxOS, LineageOS, Murena, etc. to get access to public services via their mobile devices.  It gives users with Google Play devices the option to disable Google Play, because they can get the apps they need via F-Droid.



## The shape of the work

Here is the general idea of what this project will do, as outlined in the funding propsal:

### 1. Low maintenance repositories

Launch an F-Droid app repository for a pre-curated set of apps that includes direct download links.  Ongoing software maintenance is covered since it will be integrated into F-Droid's core offering.  App updates, verification, and hosting for the Austria repository are all covered indefinitely by existing Guardian Project/F-Droid efforts.   Once complete, other launches will require only a website and a launch campaign.

* Integrate APK download tools like EFF's _apkeep_, _gplaycli_, etc. into _issuebot_
* Build existing automation scripts into user tools
* Link repo publishing with _issuebot_ posts in GitLab project


#### 2. Ongoing Review

Build a public facing app review site based on existing F-Droid methods and software.  This would clearly show the technical factors that go into the review process.  Chosen contributors can submit and review apps there, the public can watch.  This needs some software development and a GitLab instance (could be free hosting on gitlab.com).

* Integrate review tools from collaborators
* Sync tracking lib data with Exodus Privacy's public database
* Create canonical F-Droid database of proprietary libraries
* Build out data publishing system, so all extracted data is navigable by scripts


#### 3. Community Review

Expand software tooling to allow submission and review to more contributors.  Stage 2 should be running smoothly before opening it up to the public. On top of software development, this needs staff or committed volunteer time spent on managing the community.

* user research on how people think about data extracted from apps
* UX design for _issuebot_ to represent extracted data in GitLab tracker posts
* document tools so community manager can effectively curate user interactions


#### 4. Launch for new Organization

Launch a campaign for other countries and perhaps EU-wide in partnership with civil society organizations and governments.  This could happen after any of the previous stages, e.g. we could help one government setup a "pre-curated" website and another organization with a "community review" setup.


### Total Budget: 48,000€

(_We're a little late in publishing this post, the project runs from April through September 2022_).





