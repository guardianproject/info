---
title: Scanning apps, off the record
author: Hans-Christoph Steiner
categories:
  - News
tags:
  - Android
  - F-Droid
  - GitLab
  - issuebot
  - metadata
  - privacy
  - The Search for Ethical Apps
  - Tracking the Trackers

---

Smart phones have brought us so many wonderful capabilities.  They let people around the world access vast realms of information.  They let app developers solve problems large and small in a way most relevent to their local context.  They are personal computers for the world.  They also have given surveillance capitalism an unprecedented reach into everyone's lives. Repressive governments use them in ways that the East German Stasi secret police could only have dreamed of.  And as promising as artificial intelligence is, it is also threatening humanity.  People around the world are pushing back.  This public interest work requires technical inspection of apps.  There are organizations highlighting algorithmic transparency and calling out surveillance capitalism.  Journalists are linking apps into key stories about the misdeeds of powerful companies.  Activists are exposing the hidden machinations of their governments.  All of these people require technical skills to see what a given app is going.

It turns out that a lot of the technical bits required to do these kinds of investigations can be automated.  When combined with good user experience design, many of the barriers to entry can be removed.  This allows more people to get involved, and for many of these problems to be crowdsourced even.  This is the central focus of our project Tracking the Trackers.  We have just completed the third round of work to bring the initial automation to a more accessible user experience.

We have discussed these workflows with a number of organizations doing this kind of work to learn about their processes, and how they might be improved.  And we want to hear from more.  There is a lot of potential to pool limited resources to build up a shared, free software resource that is greater than the sum of its parts.  And there are many complementary projects:

* EFF's [apktool](https://github.com/EFForg/apkeep) - tool for downloading Android apps from various sources
* F-Droid [_issuebot_](https://f-droid.org/2020/12/21/announcing-issuebot.html) - automatically review apps via GitLab issues and merge requests
* [GitLab CI](https://about.gitlab.com/topics/ci-cd/) - server-less processing tied to issue trackers and merge requests
* [MobilSicher AppCheck](https://git.app-check.org/app-check) - dynamic analysis for finding personal data leaks in apps
* [PiRouge](https://pts-project.org/) - mobile forensic and network traffic analysis platform
* [Pithus](https://beta.pithus.org/about/) - mobile threat intelligence platform for activists, journalists, NGOs, researchers

## Putting it all together

We have developed a stack to integrate as many tools that are relevant into a single, productive user experience.  Detailed inspection of apps is a process that must be tracked, so the focus is on issue trackers and merge requests.  Each app is tracked as an issue.  A person opens up a new issue, adding what they know about the app, including links to it in an app store, the Application ID, links to any source code, etc.  Then _issuebot_ kicks in and downloads the app and any source code it can find.  Once successful, it will launch various analysis processed on what it downloaded.  Those results are then compiled into a report which is posted to the issue tracker for the human reviewers.  The bot leaves its mark using a GitLab label called `fdroid-bot`.  If someone found more files to download and would like _issuebot_ to run again, they just remove the `fdroid-bot` label and _issuebot_ will try the whole process again.

It runs a number of different scans and processes to check:

* Inspect apps from F-Droid, Google Play, APKPure, Huawei App Gallery, and GitHub Releases.
* Get the source code
* Build the app from source
* Find the license of the source code
* Extract info about libraries, classes, domain names, URLs, permissions, services, etc.
* Apply signature collections
* What kinds of [Anti-Features](https://f-droid.org/docs/Anti-Features) an app has, e.g. tracking, ads, non-free dependencies, known vulnerabilities, etc.
* Whether all the dependencies are also free software

Using this process, the F-Droid community reviews all apps for [Anti-Features](https://f-droid.org/docs/Anti-Features/) before accepting them into the <f-droid.org> collection.  For some years now, F-Droid have reviewed new apps and updates via merge requests with _issuebot_.  It automatically checks issues on the [Requests for Packaging](https://gitlab.com/fdroid/rfp/-/issues) tracker, this is the starting point of the process of adding new apps to the collection.  The collection is then maintained via merge requests on the [_fdroiddata_](https://gitlab.com/fdroid/fdroiddata/-/merge_requests) project.  There are hundreds of reviews there to browse through, an some [scans](https://gitlab.com/fdroid/rfp/-/issues/2224#note_1118052837) that are more interesting.

We believe this same workflow fits well to many processes for inspecting apps.  GitLab provides the core workflow that fits how many researchers and organizations are already doing this work:

* Detailed inspection happens over time, over multiple work sessions.
* Multiple people are involved in the process.
* Work can happen asynchronously across time zones and organizations.
* Public GitLab also opens up crowdsourcing opportunities

We have setup a instance of this setup for public interest organizations and investigators to use.  This is called the "Off The Record" tracker.  Access is available on request, send an email to <support@guardianproject.info> to make the request.  Additionally, the whole stack is free software.  Organizations are free to run it as they need to, with any privacy requirements that might need.  That also makes it cheap to host this software, so that it can be affordably provided as a service to people working in the public interest.  It can be self-hosted with any GitLab "Community Edition" instance with CI/CD Runners, and also runs on the gratis <https://gitlab.com/> hosting.    It does touch some proprietary services, but only via public APIs so that the functionality is included in the stack.

One new development is the creation a standard pattern for managing profiles for collections of signatures to detect Anti-Features in Android apps.  F-Droid [SUSS](https://gitlab.com/fdroid/suss) (Suspicious or Unwanted Software Signatures) is the first live project, with F-Droid's `scanner` tool using it. Before this round of work began, there were multiple silos where related activities were happening.  F-Droid scans for non-free software, Mobil Sicher detects when apps transmit personal data, Exodus Privacy find for tracking software, and IzzySoft looks for Anti-Features of all kinds.  We hope that standardizing data formats and workflows will make contribution and shared maintenance easier, as well as making it easy for organizations to maintain their own collections of signatures they want to detect.  YARA serves as template for this effort. It began at one malware company, and is now used by a [wide variety](https://virustotal.github.io/yara/#who-s-using-yara) of organizations. YARA has become the standard tool for writing malware signatures for desktop platforms.  Unfortunately, it is [not well structured](https://github.com/VirusTotal/yara/issues/1145) to work for scanning Android apps or source code, but it can serve as a inspiration and model.

## Appendix

### A) Know the local laws on software inspection.

In many places, just the act of inspecting software can get you in trouble with local governments or companies.  This could be anything from [unclear laws](https://www.vidstromlabs.com/blog/the-legal-boundaries-of-reverse-engineering-in-the-eu/) [regarding](https://www.eff.org/issues/coders/reverse-engineering-faq) [reverse engineering](https://www.twobirds.com/en/insights/2020/germany/vertraglicher-ausschluss-von-reverse-engineering) to overreach from law enforcement.  Running the inspection in private means the app reviewers are much less exposed unwarranted or unjust interference.  Anyone doing software inspection should familiarize themselves with local laws and regulation that affect it.

The biggest challenges that remain for making software inspection commonplace are around how organizations and governments apply this software.  Any organization that wants to start working on auditing software in the public interest will need:

* Legal guidelines for getting any required permissions before downloading apps to review.
* A home organization for this repository that has a public mission aligned with these goals.
* Legal representation to handle any issues that arise, and to push back against illegitimate requests.

### B) What, no iOS?

We recognize that it is also important to inspect iOS apps.  Compared to Android, the Apple mobile ecosystem is smaller and much more closed and restrictive.  Therefore, it is much more more difficult to inspect.  The application executable binary in the `.ipa` file is [encrypted](https://stackoverflow.com/questions/5784169/does-apple-modify-ios-application-executables-on-apps-submitted-to-the-app-store/5784332#5784332) which prevents examination of the binary.  The only way to get the actual `.app` files is to have a jailbroken iOS device, then manually install them on the device.    Only then can they be extracted and inspected.

(_This work was funded by NLnet as [The Search for Ethical Apps](https://nlnet.nl/project/EthicalApps/) under the umbrella of [Guardian Project](https://guardianproject.info/2022/09/01/the-search-for-ethical-apps-lets-start-with-governments/)'s [Tracking the Trackers](https://guardianproject.info/tags/tracking-the-trackers/) effort._)
