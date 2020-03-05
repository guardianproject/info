---
title: Improving Crowdsourced Translation of Long Form Text
author: Hans-Christoph Steiner
categories:
  - News
tags:
  - markdown
  - i18n
  - localization
  - localization lab
  - weblate
  - hugo
  - jekyll
  - linguine
  - translation
  - free software
---

We are happy to announce the start of work on another step in
improving crowdsourced localization, funded by the ISC Project.  This
is the second part of our ongoing "Linguine" collaboration to move
crowdsourced translation to privacy-respecting free software.

Crowdsourced translation has proven enormously successful getting apps
and website software translated into many languages.  Using tools like
Weblate or Transifex, developers can quite easily incorporate
translated app strings into their mobile apps and websites.  Any kinds
of text that is easily broken down into phrases and sentences will fit
easily into the crowdsourced workflow.  Localization Lab enables a
wide range of volunteers to contribute to the most important projects
in a wide array of languages.

For long form text, from blogs to documentation, large technical
hurdles prevent the same fluid workflow.  One clear example: Tor
Browser is available in 25 languages, but the documentation is still
largely just in English.  The standard workflow is to first complete
the English version, then submit that to translators, then wait for a
complete translation.  For the regular, small changes that come with
maintaining documentation, that workflow makes the update cycle heavy
and slow.

Few webmasters can review translations. Tools like Weblate establish a
review process, then developers need only to run an automatic import
to get approved translations from trusted translators.

The ideal workflow starts with the traditional method of translating
in one complete unit, but now, that work can easily be shared by
multiple contributors.  Whenever the original documents are updated,
those translations can then be maintained via the crowdsourcing.  Even
for organizations which directly cover their own translation needs,
like a blogger who writes in both English and Tibetan, the workflow
provided by tools like Weblate makes managing many small changes to
documents drastically easier.

While blog posts generally do not need frequent updates, a smooth path
to crowdsourced translations means, given the same effort, a larger
audience can be reached since the information will be available in
more languages.

## How we are doing this

There are already many key building blocks in place:

* Weblate and Transifex already have basic support for directly translating long form text
* _po4a_ provides good format conversion between _Markdown_ and other text formats
* _Markdown_ is a widely adopted mark-up format for documentation and blog posts
* Weblate already supports validating _Markdown_
* _po4a_ integration with Jekyll
* Static Site Generators like Jekyll and Hugo have existing methods of supporting localization

What needs doing is fixing lots of little issues here and there to
complete the whole workflow.  For example:

* Code blocks are quite common in technical documentation, and they often contain texts that should not be translated, e.g. the words from a programming language.  _po4a_ can be made to automatically recognize these blocks, and mark them as "do not translate" using standard tags, which Weblate communicates to translators.
* Most translators do not have strong technical skills, so specialized syntax like _Markdown_ or configuration examples need to be validated to ensure that the translator did not inadvertently break something with a typo.  There are existing methods and tools for validating a wide variety of markup, code, and configuration formats.  These will be integrated into the translation review process to ensure that translations will not break the website layout or generation.
* When using translation sites that do not have good support for long form text, _po4a_ can be integrated via "plugins" to static site generators like Jekyll or Hugo.
* Not all workflows allow for transparent integration, for example, Hugo to Weblate.  In these cases, there needs to be some “glue” tools to make it work.  We will produce and distribute tools for gluing together some common setups to work smoothly with Weblate and/or Transifex.

Since this project is about getting lots of pieces to integrate nicely, all the code generated will be included in all the relevant projects.  That is also where we will be looking for feedback, so file issues with [Weblate](https://github.com/WeblateOrg/weblate/issues/), [_f-droid.org_](https://gitlab.com/fdroid/fdroid-website/issues), [_guardianproject.info_](https://gitlab.com/guardianproject/info/issues), etc. and we will track them there!
