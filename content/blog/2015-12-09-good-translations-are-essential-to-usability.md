---
id: 13114
title: Good translations are essential to usability
date: 2015-12-09T17:20:15-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13114
permalink: /2015/12/09/good-translations-are-essential-to-usability/
discourse_post_id:
  - "287"
discourse_permalink:
  - https://talk.developersquare.net/t/good-translations-are-essential-to-usability/175
catchresponsive-layout-option:
  - default
catchresponsive-header-image:
  - default
catchresponsive-featured-image:
  - default
publish_to_discourse:
  - "1"
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":175,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553060057"
wpdc_sync_post_comments:
  - "0"
image: http://guardianproject.info/wp-content/uploads/2015/12/Rosetta-Stone.jpg
categories:
  - News
tags:
  - i18n
  - localization
  - OTF Localization Lab
  - translation
  - usability
---
[<img src="https://guardianproject.info/wp-content/uploads/2015/12/Rosetta-Stone-230x300.jpg" alt="Rosetta Stone" width="230" height="300" class="alignright size-medium wp-image-13155" srcset="https://guardianproject.info/wp-content/uploads/2015/12/Rosetta-Stone-230x300.jpg 230w, https://guardianproject.info/wp-content/uploads/2015/12/Rosetta-Stone-786x1024.jpg 786w, https://guardianproject.info/wp-content/uploads/2015/12/Rosetta-Stone.jpg 1164w" sizes="(max-width: 230px) 100vw, 230px" />](https://guardianproject.info/wp-content/uploads/2015/12/Rosetta-Stone.jpg)All too often, translation of an app are treated as an afterthought. It is not something that the app developers see, since they create the software in languages that work best for them. So the software looks complete to the developers. But for anyone using the software in a different language, translation is essential in order for the app to be useful. If you can’t understand the words that you see in the app’s interface, it is going to be difficult or impossible to use that app.

The part of this question that is still open is how best to manage translating software. From the point of view of the app’s developer, it is not possible to check all of the translations since no one speaks <a href="https://www.transifex.com/otf/orbot/" target="_blank">that many languages</a> fluently. Many of our apps are translated into 30 or more languages, represented by both pictograms and more than 10 alphabets. No one could read all of those writing systems, let alone understand all the words written in them. So inevitably, developers must trust many other people to do accurate translations, and to not slip in false or misleading information.

We receive substantial translations from random internet users who come along and contribute their time into translating our apps. We aim to make that process as easy as possible by posting clean source files to Transifex, the web service we currently use. We also work a lot with the <a href="https://www.transifex.com/otf" target="_blank">OTF Translation Hub</a>, which organizes the chaos of all those apps and contributors into regular events and completed translations. Organized community contributions work very well for building up baseline translations and keeping polished translations updated when the software changes. It is both a valuable and cost-effective resource, and I think its a model that can be emulated for other collections of software.

Nevertheless, for certain target languages like Tibetan or Belarusian, community contributions are rare. We get lots of contributions for many languages, like French, German, and Spanish, but other languages, like Arabic, Chinese, Persian, and Burmese get very few contributions from volunteers. Also, in order to get completed, polished translations, it is necessary to pay translators so they can devote a solid, concentrated chunk of time on making sure the whole translation works. This person can then spend time thinking about the finer points which can have a large impact on the user experience: the tone and feeling of the language, whether it is funny, serious, cute, matter of fact, etc.

So really, in order to deliver software that is translated into many languages, opening up the source files to get as many contributions as possible will get a lot of work done. But cultivating relationships with translators to oversee the whole process is essential in order to have the translations match the quality of the software.