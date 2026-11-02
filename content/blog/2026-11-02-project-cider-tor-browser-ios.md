---
title: "Brewing Onion Cider: Bringing a full Tor Browser to iOS"
date: 2026-11-02
author: Guardian Project Team
categories:
  - News
  - Onions
tags:
  - tor
  - tor browser
  - ios
  - onion browser
  - orbot
  - gecko
  - mozilla
  - dma
  - privacy
  - circumvention
  - censorship
images: ["/images/onioncidervinegar.jpeg"]
---

*Announcing Project 'Cider': Our plan to support the existing Tor on iOS ecosystem, while bringing Tor Browser to iOS.*

![Fermenting Onions in Apple Cider Vinegar](/images/onioncidervinegar.jpeg)
<small>*Credit: Daily Knowledge*</small>

In September of 2026, some of the Guardian Project team met, mostly in-person, in Lisbon, after the wonderful Global Gathering 2026 event, to discuss our strategic plan to bring [Tor Browser](https://www.torproject.org/) to Apple iOS devices. This work is supported by the funds we so gratefully received through the crowdfunding support from [Funding the Commons and Tor Project earlier this year](https://blog.torproject.org/funding-internet-freedom-together/). While we understand the technical work ahead, the regulatory and policy environment we are operating in is a bit more murky.

Thanks to [new policy doors](https://developer.apple.com/support/apps-in-the-eu/) opened by the [European Union Digital Markets Act (DMA)](https://digital-markets-act.ec.europa.eu/index_en), Apple must now [allow third-party browser engines on iOS](https://developer.apple.com/support/alternative-browser-engines/). The question is, do we really want to keep playing Apple's games, and support their path of "malicious compliance"? It may not be ideal, but this is the way to reach mainstream iPhone users in Europe, and now Japan as well, who only know how to get apps through the official Apple channels. That said, maybe instead we should support the growing [AltStore](https://altstore.io/) sideloading user base, and break free from App Store censorship and limitations? Would that path better support users in China, Iran, Russia and elsewhere, who already face app store censorship and limitations?

Building on over ten years of work developing and shipping [Onion Browser](https://onionbrowser.com) and [Orbot for iOS](https://orbot.app), as well as being the original team who brought Tor Browser to Android ([Orfox!](https://blog.torproject.org/tor-heart-orbot-and-orfox/)), we are well positioned to tackle these questions and the technical work ahead. Our goal is simple: deliver a genuine Tor Browser experience powered by Mozilla's Firefox Gecko engine on iOS, with all of the improvements and patches from the Tor Project team, and our own experience with Onion Browser. By giving iOS users real browser engine choices beyond WebKit, we're making it easier than ever to enjoy strong privacy, reliable anti-censorship and circumvention capabilities, all within the trust and security that Apple devices are known for.

## One Year Roadmap Plan

Even with the uncertainty about which is the best path forward, we did put together a one year roadmap for this project, giving structure upon which we can make forward progress.

### Q1 (October 2026)

* Continue to maintain and update Onion Browser and Orbot on iOS
* Share our announcement and public plans about bringing full Tor Browser to iOS
* Dig into tech challenges and research key questions to weigh our options
  * The open route: [Reynard Browser for iOS](https://github.com/minh-ton/reynard-browser)
  * The Apple route: Gecko via iOS BrowserEngineKit through the [EU DMA and Japan alternative browser engine programs](https://developer.apple.com/support/alternative-browser-engines/)
* Kick off a risk/threat analysis on Apple as a platform and distributor for this work
* Set up a rough one year budget based on our initial goals and the funds we have raised/received
* Look into user numbers and country breakdowns for Onion Browser to guide our strategy
* Meet with Tor and Mozilla to talk through our ideas and share them at the October 2026 Tor Project meeting (already done!)

### Q2 (January 2027)

* Get more involved with Tor Project / Tor Browser meetings and collaboration
* Map out the Onion Browser threat model and refresh user guidance and understanding
* Show off demos and prototypes running Gecko for iOS / Reynard Browser + Tor
* Plan out Orbot iOS continued R&D (split tunneling, per-app routing, and funding ideas)
* Pick our main path for Tor Browser for iOS (TBi): Apple official store distribution in the EU/Japan, or open alternative setups (Reynard, AltStore, etc.)
* Upgrade and improve the Onion Browser website (getting planning under way)

### Q3 (April 2027)

* Tor Browser for iOS: launch the initial Alpha release via TestFlight and sideloading
* Onion Browser website: roll out a fresh, localized site design
* Help users pick the right browser for them (Onion Browser vs. TBi)
* Team up with Tor UX to analyze the user experience when bringing Tor Browser for Android to iOS
* Chat with Tor Project to align and get approval on TBi branding
* Send out new grant applications and project proposals
* Explore Apple-friendly ways to fund the project through donations and sustainability options

### Q4 (July 2027)

* Formulate a friendly guide to help users transition from Onion Browser to TBi smoothly
* Figure out launch plans, whether that's a beta or a full public debut
* Continue to work on securing long-term funding to keep Onions on Apples and TBi thriving

## More Ideas and Possibilities Ahead

Beyond the clear core work above, we have many more ideas to tackle and take on, hopefully with additional support, volunteers, partners, and funding to assist us. Below is a brain dump of everything else we discussed at the "Lisbon Meeting" in September 2026.

At our core, we will keep shipping and maintaining the apps we offer today, Orbot and Onion Browser, while expanding to ship the new Tor Browser for iOS through EU and Japan app stores, when and if it is ready to go that way. We will also have a great launch party, and everyone is invited! We want to prove that community-driven, crowdsourced projects can yield awesome breakthrough software within complicated ecosystems.

We will continue to strengthen our partnership with Tor Project, especially around the idea of using the Tor Browser naming and trademark for an iOS app. The name has power and meaning, and we specifically chose a different name for Onion Browser, because it is not the full Tor Browser. We also seek to gain active support from Mozilla for Gecko on iOS as an officially supported component, and to showcase our work at developer events like MozFest and Mozilla developer meetings.

We seek to continue building social media and community awareness about all the options for Tor on iOS, from Orbot and OnionShare, to Onion Browser, and other partner apps in the iOS ecosystem. We are also excited about spinning off the Snowflake-powered ["Kindness Mode"](/2025/11/13/kindness-mode-help-people-connect-to-tor-on-world-kindness-day/) feature into a standalone iOS app, to get more adoption from people who want to help others connect to Tor, but who are not interested in the Orbot VPN app. Our efforts to ensure our tech is accessible to all will also continue to grow, and if we are limited to shipping Tor Browser for iOS in Europe and Japan only, we will reach out to high-risk communities in those places to help them adopt it and benefit from what it can provide.

We will continue to focus on fundraising, from in-app donation subscriptions and sponsorships, to crowdfunding opportunities, and grants through foundations and funds supporting free and open-source privacy-focused work. This includes EU-focused digital resilience and internet freedom grants to keep this work thriving.

We will continue to work with advocacy groups and efforts to push Apple to be more open, beyond just Europe and Japan, and to fully, authentically implement the DMA and similar regulations. We want to encourage and push Apple to enable third-party browser engine support worldwide, thanks to user demand we can demonstrate.

## And so…

There is a lot of exciting and complex work and decisions ahead that we are excited to take on and make progress on. We have the product, design and technical team to do it, and can't wait to see you at the launch party in a year, however it may end up! [Reach out to us](https://guardianproject.info/contact/) if you are interested in learning more, collaborating or contributing.
