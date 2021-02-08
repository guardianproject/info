---
title: Easy translation workflows and the risks of translating in the cloud
author: Hans-Christoph Steiner
categories:
  - Development
tags:
  - Hugo
  - Jekyll
  - Linguine
  - localization
  - poedit
  - privacy
  - tracking
  - translation
  - Weblate
  - Wordpress
---


Crowdsourced translation has opened up software and websites to whole
new languages, regions, and uses.  Making translating easier has
brought in more contributors, and deploying those languages requires
less work.  A number of providers now offer "live", integrated
translation, speeding up the process of delivering translated
websites. On the surface, this looks like a big win.  Unfortunately,
the way such services have been implemented opens up a big can of
worms.  Third parties must be trusted with user data.  The translators
cannot work without being tracked. Displaying the translation requires
JavaScript.  The security profile is more complicated and harder to
defend.

For projects with elevated security and privacy requirements, these
are deal breakers.  Translators can get in trouble for working on
publishing software or translating censorship circumvention
documentation.  Minority languages are suppressed in many places
around the world, even publicly working in some languages can get
people into trouble.

We have been working for many years now to help make software and
website translation easier, more accessible, and more efficient.  We
also balance that with privacy and security concerns.  This post
outlines how to balance all those concerns.


## Live, integrated translation systems

Using this new class of translation services means that the
translations are not shipped with the website or app, but instead
dynamically downloaded and delivered.  These translation services
require that third party code is integrated into the website or app to
deliver the translations.  All of the regular
[privacy](https://browserleaks.com/) and
[security](https://owasp.org/www-project-top-ten/) concerns of dynamic
web services apply here.

For example, Transifex Live is based around
[JavaScript](https://docs.transifex.com/live/installing-the-JavaScript-snippet),
it uses JavaScript to dynamically load the translated strings from the
Transifex CDN hosted on Amazon AWS.  They also provide an iFrame
option, which has its own [security
concerns](https://stackoverflow.com/a/9428051).  Crowdin provides
"[in-context
localization](https://support.crowdin.com/in-context-localization/)"
which lets translators see the translations live in the website as
they are working.  This is a huge benefit to the translators, but it
has all the same issues as Transifex Live.  Their code must run in
your site.  They use other providers like Amazon to provide their own
service.  All of these third-parties have to be trusted to provide
security and privacy.  On top of that, Crowdin and Transifex are
monolithic, proprietary offerings, it is not possible run your own
instance.  Like many cloud-based services, it is all-or-nothing:
accept all the tracking, the privacy concerns, and security issues, or
do not use such a service

Lastly, the data from the translation contributors must be considered.
These live services provide the translators a direct channel to feed
data into the website.  A malicious translator could feed an exploit
to the website using this channel.  Such a setup relies entirely on
any automated checks that the translation platform provides.  These
checks are optional, and often disabled by default.  Also, attackers
regularly find ways around even the best checkers and sanitizers, like
Mozilla [Bleach](https://github.com/mozilla/bleach) or Ruby
[loofah](https://github.com/flavorjones/loofah).

For all these reasons, projects like
[SecureDrop](https://weblate.securedrop.org/) and
[Tails](https://translate.tails.boum.org/) self-host Weblate to
provide crowdsourced translation..


## Static sites with live previews

Static sites built with tools like Jekyll and Hugo offer big benefits
in terms of privacy, security, and cost of operation.  But they
generally require more technical skills to operate, and have
restricted possibilities in terms of dynamic interaction.  There is a
lot that still can be done, and things are improving fast.  The dream
of live localization and in-context translation workflows without
privacy and security concerns is within reach.

Live display of translations is not possible with a fully static site.
Live translation requires front end JavaScript or a dynamic backend
server.  The vast majority of web tracking and security
vulnerabilities come from JavaScript, sites that serve high risk
communities should use static sites that work without JavaScript
enabled.

Translation updates can be highly [automated]({{< ref
"2020-04-23-figuring-out-crowdsourced-translation-of-websites/index.md"
>}}) with a static site.  This means new translations can be reviewed
and deployed within minutes.

Jekyll and Hugo can also provide live previews while editing the
source pages and translations. Unfortunately, using these features
requires base level familiarity with technical things like working in
the terminal.  When Jekyll or Hugo is installed locally on the
translators computer, `jekyll serve` and `hugo serve` generate the
whole website on the fly, and the browser will automatically refresh
the page with each change.


## Wordpress, Translation, and Static Sites

Wordpress remains a popular option for running websites, especially
for small and non-technical organizations.  It provides intuitive
editing and publishing tools combined with a wide array of attractive
templates to build on.  It is free software that can be self-hosted,
and it can even be used as a static site generator.  Even with the
rise of Jekyll, Hugo, and so many other static site generators,
Wordpress remains a [good
option](https://www.brianshim.com/webtricks/wordpress-static-site-generator/)
for small organizations with privacy and security concerns, given that
it is used with the [static HTML output
plugin](https://wordpress.org/plugins/static-html-output-plugin/).
The one missing piece is crowdsourced translation that fits in with
all that.

[Poedit](https://poedit.net/) provides an alternate approach that is
self-hosted and free software, but is not entirely a typical
crowdsourced translation workflow.  It is an editor app that runs
locally on the translator's own machine.  It supports translating
Wordpress directly via its API.  Then the results are included when
Wordpress generates the static HTML output.

Using self-hosted Weblate, the full website and translation workflow
can be as private as needed.  The static HTML output can be fed
[directly to
Weblate](https://docs.weblate.org/en/latest/formats.html#html-files)
or [use _po4a_]({{< ref
"2020-04-23-figuring-out-crowdsourced-translation-of-websites/index.md#translation-setup-with-po4a"
>}}) to set up an automated workflow that is tailored to your needs.

If self-hosting the translation platform is not a requirement, then
Crowdin and Transifex are options for translating the static HTML that
comes from Wordpress.  It is important to consider that both of these
will send data to many different companies, so they cannot be
considered private.  Using Crowdin sends data to Amazon, Google, and
Sentry.  Using Transifex sends data to Amazon, ChurnZero, Google,
jsDelivr, New Relic, Sentry, Stripe, Adobe (Typekit), and VWO.  Both
can potentially also send data to Facebook, GitHub, GitLab, LinkedIn,
and Twitter since those can be used for signing in.

Two good patterns for setting up the languages are the hosting each
language on a subdomain like how wikipedia does it; or, use path
segments for each language.  With GitHub Pages and GitLab Pages, each
language can be a project, then each language will be deployed to a
sub-directory, e.g.:

* https://mysite.gitlab.io/en comes from https://gitlab.com/mysite/en
* the main site is the language chooser, e.g.
  https://mysite.gitlab.io comes from https://gitlab.com/mysite/mysite.gitlab.io

One idea further improve the Wordpress workflow is to combine the
[Transifex Wordpress Plugin](https://www.transifex.com/integrations/wordpress-multilingual-plugin/)
with the
[Wordpress Static HTML Output Plugin](https://wordpress.org/plugins/static-html-output-plugin/
to customize and streamline the whole process.  This could work with
Crowdin, Transifex, and Weblate, since they all provide APIs to
integrate with.
