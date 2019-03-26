---
id: 13629
title: Tracking usage without tracking people
date: 2017-06-08T10:58:53-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=13629
permalink: /2017/06/08/tracking-usage-without-tracking-people/
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "540"
discourse_permalink:
  - https://talk.developersquare.net/t/tracking-usage-without-tracking-people/391
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":391,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553110305"
wpdc_sync_post_comments:
  - "0"
categories:
  - HowTo
  - News
  - privacy
  - Research
tags:
  - bazaar
  - data
  - fdroid
  - metadata
  - privacy
  - tor
  - tracking
---
One thing that has become very clear over the past years is that there is a lot of value in data about people. Of course, the most well known examples these days are advertising and spy agencies, but tracking data is useful for many more things. For example, when trying to build software that is intuitive and easy to use, having real data about how people are using the software can make a massive difference when developers and designers are working on improving their software. Even in the case of advertisers, they mostly do not care exactly who you are, they want to know what you are interested in so that they can more effectively promote things to you.

From the beginning Guardian Project has focused on privacy, and worked to practice what we preach in our own software. For example, we have entirely disabled Apache web logs on our website for the past couple of years, so that we would not even have access to that rich data. We felt that we could not even store that data without fear of violating people&#8217;s privacy, let alone working with it.

Things have changed in the past few years, and there are now a number of well tested techniques for tracking how people are using software without actually tracking who they are. It is now possible to keep some usage data while feeling safe that no one who might get that data could use it to identify individuals. One good example of this is the <a href="https://metrics.torproject.org/" target="_blank">Tor Project&#8217;s tracking data</a>. They provide a wide variety of tracking data to follow how Tor is being used, and how well the Tor network is operating.

So we believe that it is now possible to responsibly track usage without violating anyone&#8217;s privacy. One piece of work along these lines is the new <a href="https://github.com/cleaninsights/cleaninsights-android-sdk" target="_blank">Clean Insights Android SDK</a>. Nathan is leading the development of that effort. And this blog post announces another new development that we are starting: tracking usage data from F-Droid app repositories. 

[<img src="https://guardianproject.info/wp-content/uploads/2017/06/bycountry-300x133.png" alt="tracking by country" width="300" height="133" class="aligncenter size-medium wp-image-13632" srcset="https://guardianproject.info/wp-content/uploads/2017/06/bycountry-300x133.png 300w, https://guardianproject.info/wp-content/uploads/2017/06/bycountry.png 747w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2017/06/bycountry.png)

To start with, the Apache web logs for this site will be configured to store, but only information that is not fine-grained enough to identify people:

  * only the date is stored, not the time or time zone
  * Referer, IP Addresses, User Agent are never stored
  * country is stored by looking up the IP Address in the _geoip_ database

Normally, a log entries look like:

<pre>189.4.73.81 testy.at.or.at - [08/Jun/2017:13:55:46 +0200] "GET /fdroid/repo/index-v1.jar HTTP/1.1" 200 147950 "-" "F-Droid"
119.29.81.134 199.119.112.126 - [08/Jun/2017:14:46:48 -0400] "GET /fdroid/repo/index-v1.jar HTTP/1.1" 200 147950 "http://testy.at.or.at/fdroid/repo/index-v1.jar" "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)"
</pre>

This stripped version looks like:

<pre>0.0.0.0 - - [08/Jun/2017:00:00:00 +0000] "GET /fdroid/repo/index-v1.jar HTTP/1.1" 200 147950 "-" "-" AT
0.0.0.0 - - [08/Jun/2017:00:00:00 +0000] "GET /fdroid/repo/index-v1.jar HTTP/1.1" 200 147950 "-" "-" ZH
</pre>

Since the raw data is processed by the webserver, the extra information will be discarded and never written to disk. Only the sanitized usage tracking information is ever stored. This is based on Tor Project&#8217;s <a href="https://gitweb.torproject.org/webstats.git/tree/src/sanitize.py" target="_blank">web tracking</a>. It is possible to do this with _Apache_, _lighttpd_, _nginx_, and probably other webservers. For _Apache_, _mod_geoip_ needs to be installed, then only a single line is needed to configure this private logging mode:

<pre>LogFormat "0.0.0.0 - %u %{[%d/%b/%Y:00:00:00 %z]}t \"%r\" %>s %b \"%{Referer}i\" \"-\" %{GEOIP_COUNTRY_CODE}e" privacy+geo
CustomLog ${APACHE_LOG_DIR}/access.log privacy+geo
</pre>

Now, we hope that we can work towards providing value from tracking data, without violating anyone&#8217;s privacy. Indeed, we are still prioritizing privacy over any value derived from tracking data. So anyone else who also wants to go follow this route needs to be fully aware that any tracking must be very carefully done, since it can easily result in inadvertent leaks. Do not take this as a stamp of approval on any tracking activity!