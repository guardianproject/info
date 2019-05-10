---
id: 2387
title: Orbot Data Tax (Updated!)
date: 2012-06-20T13:05:53-04:00
author: patch
layout: post
guid: https://guardianproject.info/?p=2387
permalink: /2012/06/20/orbot-data-tax/
bigimg: [{src: "/wp-content/uploads/2010/05/toron-64x64.png",}]
categories:
  - News
---
**Update (6/26/12): I Found Orbot to have lower idle usage then previously recorded. The post now reflects the new statistics. The previous stats were based on idle usage at 92 bytes/s**

There have been many inquiries about the cost of Orbot’s data usage. I ran five different tests to record the types of data tax a user might encounter. Heavy usage of Orbot combined with a low monthly data allotment could be an issue.

Below is the compiled data for 4 different use cases:

<table align="center">
  <tr>
    <th colspan="2" align="center" valign="middle">
      Test Scenario
    </th>
    
    <th>
      Data Usage
    </th>
    
    <th>
      Overhead
    </th>
  </tr>
  
  <tr>
    <th rowspan="4" valign="middle">
      Web Traffic
    </th>
  </tr>
  
  <tr>
    <th>
      Without Orbot
    </th>
    
    <td>
      2.35 MiB
    </td>
    
    <td>
      —
    </td>
  </tr>
  
  <tr>
    <th>
      With Orbot
    </th>
    
    <td>
      3.44 MiB
    </td>
    
    <td>
      46%
    </td>
  </tr>
  
  <tr>
    <th>
      Orweb
    </th>
    
    <td>
      3.26 MiB
    </td>
    
    <td>
      38%
    </td>
  </tr>
  
  <tr>
    <th rowspan="3" valign="middle">
      Bulk Download
    </th>
  </tr>
  
  <tr>
    <th>
      With Orbot
    </th>
    
    <td>
      17.82 MiB
    </td>
    
    <td>
      15%
    </td>
  </tr>
  
  <tr>
    <th>
      Without Orbot
    </th>
    
    <td>
      15.49 MiB
    </td>
    
    <td>
      —
    </td>
  </tr>
  
  <tr>
    <th rowspan="3" colspan="2" valign="middle">
      Idle
    </th>
    
    <td>
      65 Bytes/s
    </td>
    
    <td rowspan="3">
      —
    </td>
  </tr>
  
  <tr>
    <td>
      228 KiB/hour
    </td>
  </tr>
  
  <tr>
    <td>
      160 MiB/month
    </td>
  </tr>
  
  <tr>
    <th colspan="2" valign="middle">
      Client Start/Stop
    </th>
    
    <td>
      37.8 KiB
    </td>
    
    <td>
      —
    </td>
  </tr>
</table>

**Test Scenarios**

The test cases were fairly straight forward. I used Droidwall to limit traffic on my phone to Orbot or the desired application and then recorded data.

  * **Web Browsing:** Browsed five common websites (guardianproject.info, boingboing.net, facebook.com, slashdot.org, twitter.com) with Orbot/Orweb and javascript OFF, the default browser with Orbot running as a transparent proxy, and just the default browser by itself
  * **Idle:** Started Orbot and began recording on Idle for ~10 minutes. The traffic graph clearly shows a small data spike approximately every minute.
  * **Bulk Download:** Downloaded a 5 MB file with the download manager 3 times both with Orbot’s transparent proxy and without
  * **Client Stop/Start:** Recorded traffic incurred by starting and stopping Orbot

**Contextualizing the Data**

This data suggests that Orbot could incur between  15 and 46 percent of additional data usage plus about 227 MiB of data a month for those that run Orbot 24/7. This tradeoff may significant to some, but it really depends on your data usage.

I have calculated how much data you could use for 3 different plans if you used Orbot for ALL your traffic. This means running it 24/7 over your data network AND using the transparent proxy to enforce all your applications to go through Orbot. This table represents the most extreme use case.

<table align="center">
  <tr>
    <th rowspan="3" align="center">
      Monthly Plan
    </th>
    
    <th colspan="2" align="center">
      Usable Data
    </th>
    
    <th colspan="2" align="center">
      Orbot Data Tax
    </th>
  </tr>
  
  <tr>
    <th>
      At 15%
    </th>
    
    <th>
      At 46%
    </th>
    
    <th>
      At 15%
    </th>
    
    <th>
      At 46%
    </th>
  </tr>
  
  <tr>
    <th>
      5 GiB
    </th>
    
    <td>
      4.21 GiB
    </td>
    
    <td>
      3.31 GiB
    </td>
    
    <td>
      16%
    </td>
    
    <td>
      34%
    </td>
  </tr>
  
  <tr>
    <th>
      1 GiB
    </th>
    
    <td>
      751 MiB
    </td>
    
    <td>
      588 MiB
    </td>
    
    <td>
      27%
    </td>
    
    <td>
      43%
    </td>
  </tr>
  
  <tr>
    <th>
      500 MiB
    </th>
    
    <td>
      295 MiB
    </td>
    
    <td>
      233 MiB
    </td>
    
    <td>
      41%
    </td>
    
    <td>
      53%
    </td>
  </tr>
</table>

**Reducing Data Cost**

These numbers may be high for some, but they represent very heavy usage of Orbot. If a user only wishes to use Orbot for a specific set of apps that have proxy support, there is no reason to leave Orbot running 24/7. Twitter is a great example of this because it caches its data asynchronously and would only need Orbot turned on to gather new tweets or search. If the application’s proxy is on but Orbot is off it will simply not be able to update rather then updating outside the Tor network.

> **Warning: **Turning off Orbot to save data will also remove the transparent proxy rules. This means applications relying on the transparent proxy rules as opposed to proxy support (Twitter) will be free to broadcast data outside Orbot if you have not taken other precautions.

**Note: ** (Updated 6/26/12) I previously mentioned that Droidwall may have some issues in blocking certain outbound data. I filed a bug with the author and it turned out to be my mistake in recording the traffic. So, ignore my previous statement, Droidwall would be great application to enforce outbound traffic rules during periods in which Orbot is turned off.