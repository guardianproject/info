---
title: "Clean Insights: February 2021 Update on Privacy-Preserving Measurement"
author: Nathan (n8fr8)
categories:
  - Development
  - News
tags:
  - tracking
  - Tracking the Trackers
  - developers
  - metrics
  - analytics
  - sdks
---

Greetings, all. I hope this finds you healthy and well, finding ways to enjoy the season (whichever it may be). While everyday still provides new cha
llenges in the life of our team at Guardian Project, we continue to strive to be productive as productive as we can be in our professional and person
al lives.

I've just posted an updated presentation on [Clean Insights](https://cleaninsights.org), reflecting on the symposium in May, and the work we have done since then. You can see and
 share it from here:

[Watch update on YouTube](https://www.youtube.com/watch?v=vo6FI-WDLG0)

You can also listen to this update on the [Guardian Project Podcast](https://guardianproject.info/podcast/2021/clean-insights-update.html)

Thanks to [Benjamin Erhart](https://die.netzarchitekten.com/), our lead developer on Clean Insights, we've made substantial progress over the last few months on delivering our new software development kits. If you visit our Gitlab project page, you will find design documents and SDKs for Android, iOS, Javascript (both for desktop and web) and soon Python (Thanks, to Iain Learmonth for this contribution). While this work is ongoing, the code is stable, and we feel it is ready to start getting it into all of your hands, so that you can start asking all the questions we have yet to consider.

[Clean Insights on Gitlab](https://gitlab.com/cleaninsights)

Here is an example of how easy it is to implement a measurement of a specific event or a visit to certain view in your app:

[Sample code for Android integration](https://gitlab.com/cleaninsights/clean-insights-android-sdk/-/blob/master/app/src/main/java/org/cleaninsights/e
xample/Main2Activity.java#L48)

We are still relying on Matomo as our backend aggregator, analysis tool and dashboard, and it continues to work well enough for our 1.0 solution. That said, to enhance the privacy of Clean Insight-enabled clients, we've design and implemented a proxy service, the Clean Insights Matomo Proxy. The C
IMP reduces the amount of metadata and logging that Matomo can do, since it is only communicate to directly by the no-logging proxy.

[Matomo Proxy](https://gitlab.com/cleaninsights/clean-insights-matomo-proxy)

All of this software is available for you to implement and deploy on your own. We also have a public testbed and hosted service available at https://
metrics.cleaninsights.org that we can make available for anyone who isn't able to run and maintain their own instance. We can also assist you with considering the insights you want to gain, threat modeling the risks it poses to your users, and implementing the SDK into your software, be it a mobil
e app, web app, desktop app, back-end service or operating system. Our deisgn partners at Okthanks also have a variety of concepts and soon sample pr
ojects and code for implementing effective and ethical Consent UX to achieve the right kind of "opt-in".

Please reach out if you have interest in using Clean Insights. We have weekly scrum meetings, email lists and a public discussion room on the Matrix 
network. More info on these on the [Developer Page](https://cleaninsights.org/dev)


