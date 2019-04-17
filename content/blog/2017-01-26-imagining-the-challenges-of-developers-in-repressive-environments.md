---
id: 13472
title: Imagining the challenges of developers in repressive environments
date: 2017-01-26T09:56:59-04:00
author: Seamus Tuohy
layout: post
guid: https://guardianproject.info/?p=13472
permalink: /2017/01/26/imagining-the-challenges-of-developers-in-repressive-environments/
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "477"
discourse_permalink:
  - https://talk.developersquare.net/t/imagining-the-challenges-of-developers-in-repressive-environments-draft/345
discourse_comments_count:
  - "0"
discourse_comments_raw:
  - '{"id":345,"posts_count":1,"filtered_posts_count":1,"posts":[],"participants":[{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"}]}'
discourse_last_sync:
  - "1553079858"
wpdc_sync_post_comments:
  - "0"
categories:
  - Development
  - News
  - Research
tags:
  - bazaar
  - privacy
  - security
  - usability
---
The Guardian Project team spends a lot of time thinking about users. In our work we focus on easy-to-use applications for users in high-risk scenarios. Because of this we are very focused on security. In our current work with the FDroid community to make it a secure, streamlined, and verifiable app distribution channel for high-risk environments we have started to become [more aware](https://guardianproject.info/2015/02/24/phishing-for-developers/) of the challenges and risks facing software developers who build software in high-risk environments.

There are a wealth of resources available on how to support and collaborate with high-risk users. Unsurprisingly, we could not find any guidance on how to support and collaborate with developers in repressive environments, let alone developers who are put at high-risk because of the software they develop. So, we have started conducting “user research” with developers from a range of repressive environments.

We started our user research by conducting surveys and interviews with Internet Freedom donors, developers, and CSOs about the challenges of being a, or working with, software developers in places where the internet is heavily monitored and filtered. We did this for two reasons. First, we want to make sure that the output produced is valuable to our target audience. Second, we wanted to see how this community viewed the challenges that these developers face. We are a little over ¾ done with our interviews and decided to share some initial thoughts from our interviews alongside that initial survey research.

### How to read the survey results

Each of the plots below shows how survey respondents ranked the level of challenge or negative impact specific factors had on the different phases of the development life-cycle. The survey split these rankings into categories that included the design (**Des**) and development (**Dev**) of software; deploying (**Dep**) and maintaining (**Maint**) software; and general threats (**Thrt**).

Participants were also asked to provide some basic information about their relationship to developers in repressive environments. We did this to explore the ways that experience might impact how some groups evaluate the challenges faced by developers in repressive environments. Using their answers we split the results into six groups.

**At Risk**: The type of of software development they, or those they interact with, could put either of them at risk.  
**Censor/Surv**: They are based in a place where the internet is heavily monitored filtered.  
**Not Censor/Surv**: They are not based in a place where the internet is heavily monitored filtered.  
**Collab**: They collaborate, support, or work with developers who are based in a place where the internet is heavily monitored or filtered.  
**Dev**: They develop Software  
**All**: Everyone who was surveyed.

The initial survey was not designed to create accurate comparisons between groups who were surveyed and the data visualizations do not reflect the number of participants who declined to answer specific questions. It is also important to note that we asked participants to fill out the survey based upon the regions that they work in. Because of the possible identifying nature of participants responses we did not ask them to identify what regions those were. This had led to a wide variation in many of the responses.

### Infrastructure

Infrastructure plays a critical role in technological development. Software development, distribution, and use require an interconnected world of infrastructure. Only a small portion of this infrastructure is controlled and maintained by the developer. They also rely on a range of public and private infrastructure to provides power, connectivity, and financial support.

To explore these topics we first asked about the challenge that barriers to Internet access played in the design (**Des**) and development (**Dev**) of software for developers in high-risk environments. Generally, respondents thought that it was a greater challenge for developers to design software for these environments than to conduct development in these environments.

<div id="attachment_13476" style="width: 1011px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2016/12/bandwidth.png"><img aria-describedby="caption-attachment-13476" class="wp-image-13476 size-full" src="https://guardianproject.info/wp-content/uploads/2016/12/bandwidth.png" width="1001" height="285" srcset="https://guardianproject.info/wp-content/uploads/2016/12/bandwidth.png 1001w, https://guardianproject.info/wp-content/uploads/2016/12/bandwidth-300x85.png 300w, https://guardianproject.info/wp-content/uploads/2016/12/bandwidth-768x219.png 768w" sizes="(max-width: 1001px) 100vw, 1001px" /></a>
  
  <p id="caption-attachment-13476" class="wp-caption-text">
    Internet/data bandwidth, connectivity, and/or cost
  </p>
</div>

In our interviews we have heard that barriers to internet access can make it difficult to learn how to develop software and to easily get the libraries, documentation, and support that make developing software easier. It is not a universal challenge. Access varies widely depending upon the developer’s region. When it is a barrier it is often one of the largest barriers that is faced. We were happy to find that the challenges of designing software for users in areas with barriers to Internet access is one area where there is [existing guidance](https://developers.google.com/billions/) for developers in these regions.

We also asked how a developer’s own infrastructure led to challenges when developing (**Dev**), deploying (**Dep**), and maintaining (**Maint**) software.

<div id="attachment_13477" style="width: 1011px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2016/12/dev_infra.png"><img aria-describedby="caption-attachment-13477" class="size-full wp-image-13477" src="https://guardianproject.info/wp-content/uploads/2016/12/dev_infra.png" alt="" width="1001" height="285" srcset="https://guardianproject.info/wp-content/uploads/2016/12/dev_infra.png 1001w, https://guardianproject.info/wp-content/uploads/2016/12/dev_infra-300x85.png 300w, https://guardianproject.info/wp-content/uploads/2016/12/dev_infra-768x219.png 768w" sizes="(max-width: 1001px) 100vw, 1001px" /></a>
  
  <p id="caption-attachment-13477" class="wp-caption-text">
    Developer Infrastructure (e.g Hosting, setup, security, software)
  </p>
</div>

This topic, like barriers to internet access, had widely varying responses in the Interviews depending on the region the developer was based in. Unlike internet access, where technology was the root of the challenges the responses to these questions showed that legal challenges were the root of hosting challenges. In regions where international sanctions were in place this was a greater concern in the everyday experience of developers. Data localization was another more recent legal concern that was brought up in the interviews.

Financial infrastructure and other economic challenges can impact various stages of the software lifecycle. Even FOSS developers need to make a living. To look at financial infrastructure we asked if access to payment systems was a challenge when designing (**Des**) and developing (**Dev**) software. We also asked about general challenges to monetizing and earning revenue when maintaining software and supporting users (**Maint**).

<div id="attachment_13478" style="width: 1011px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2016/12/money.png"><img aria-describedby="caption-attachment-13478" class="size-full wp-image-13478" src="https://guardianproject.info/wp-content/uploads/2016/12/money.png" alt="" width="1001" height="285" srcset="https://guardianproject.info/wp-content/uploads/2016/12/money.png 1001w, https://guardianproject.info/wp-content/uploads/2016/12/money-300x85.png 300w, https://guardianproject.info/wp-content/uploads/2016/12/money-768x219.png 768w" sizes="(max-width: 1001px) 100vw, 1001px" /></a>
  
  <p id="caption-attachment-13478" class="wp-caption-text">
    Economics (payment, monetizing, & earning revenue)
  </p>
</div>

As with many of the other questions payment and monetization challenges vary widely by region. Interviewers from areas with economic sanctions spoke of monetization as a greater challenge than any other group of interviewees. Because economic challenges vary so widely, we will hold off on discussing them in more depth until we are done with our analysis.

### Localization

Many developers face challenges far before they have to worry about their infrastructure. Not only are a majority of programming languages in English, many of the textbooks used to teach software development are in English as well. We asked our survey participants if localized software libraries, platforms, or developer documentation were a challenge for developers in high-risk environments when they were designing (**Des**), developing (**Dev**), and deploying (**Dep**) software.

<div id="attachment_13479" style="width: 1011px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2016/12/localization.png"><img aria-describedby="caption-attachment-13479" class="size-full wp-image-13479" src="https://guardianproject.info/wp-content/uploads/2016/12/localization.png" alt="" width="1001" height="285" srcset="https://guardianproject.info/wp-content/uploads/2016/12/localization.png 1001w, https://guardianproject.info/wp-content/uploads/2016/12/localization-300x85.png 300w, https://guardianproject.info/wp-content/uploads/2016/12/localization-768x219.png 768w" sizes="(max-width: 1001px) 100vw, 1001px" /></a>
  
  <p id="caption-attachment-13479" class="wp-caption-text">
    Localization of software libraries, platforms, or developer documentation
  </p>
</div>

Access to localized content was seen as a primary concern in almost every interview we have had with developers. In multiple interviews basic English language skills were even described as a requirement for any software development. Even developers with basic technical English skills spoke about the challenges of finding the appropriate tools and libraries because the descriptive documentation was difficult to skim. The lack of multi-language books, blog-posts, and forums also impedes access to best-practices and developer guidance.

### Targeted Attacks

Attacks that focus on compromising the user through counterfeit software pirated by a user are not new. But, increased secondary and local markets for apps increase the possible otherwise legitimate locations where a malicious counterfeits of apps can be uploaded. We asked questions about impact of possible malicious counterfeit versions of their software being produced on how developers their design (**Des**) and deploy (**Dep**) their software. Targeted attacks against developers can be used to compromise their otherwise legitimate software to to deliver malicious content. We also asked about the challenges related to possible backdoors in the software or developer tools they used (**Thrt**).

<div id="attachment_13480" style="width: 967px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2016/12/malicious.png"><img aria-describedby="caption-attachment-13480" class="size-full wp-image-13480" src="https://guardianproject.info/wp-content/uploads/2016/12/malicious.png" alt="" width="957" height="285" srcset="https://guardianproject.info/wp-content/uploads/2016/12/malicious.png 957w, https://guardianproject.info/wp-content/uploads/2016/12/malicious-300x89.png 300w, https://guardianproject.info/wp-content/uploads/2016/12/malicious-768x229.png 768w" sizes="(max-width: 957px) 100vw, 957px" /></a>
  
  <p id="caption-attachment-13480" class="wp-caption-text">
    Malicious & Counterfeit Software
  </p>
</div>

Only a couple of the developers we interviewed expressed concern about malicious counterfeit versions of their applications.

While targeted attacks were acknowledged by some interviewees, most described the insertion of backdoors as less likely than targeted threats that aimed at stopping the developer from continuing development. The initial survey asked about the challenge of developer account shutdown and/or seizures during development (**Dev**) and take-down requests (**Thrt**) because of content restrictions, defamation laws, copyright claims, etc.

<div id="attachment_13481" style="width: 967px" class="wp-caption aligncenter">
  <a href="https://guardianproject.info/wp-content/uploads/2016/12/takedown.png"><img aria-describedby="caption-attachment-13481" class="size-full wp-image-13481" src="https://guardianproject.info/wp-content/uploads/2016/12/takedown.png" alt="" width="957" height="285" srcset="https://guardianproject.info/wp-content/uploads/2016/12/takedown.png 957w, https://guardianproject.info/wp-content/uploads/2016/12/takedown-300x89.png 300w, https://guardianproject.info/wp-content/uploads/2016/12/takedown-768x229.png 768w" sizes="(max-width: 957px) 100vw, 957px" /></a>
  
  <p id="caption-attachment-13481" class="wp-caption-text">
    Account shutdown and/or seizures during development or software take-down requests
  </p>
</div>

The in-platform censorship we surveyed for was seen as far less a challenge in the interviews. Interviewees were far more concerned about the possibility of real-world legal censorship or harassment. When asked how developers addressed their perceived threats many of the interviewees noted that developers go beyond technological measures to protect themselves. Many also rely heavily on the strategic use of pseudonyms and other operational security measures.

### Conclusion

With our interviews nearly complete it is interesting to look back at, what seemed like, wide disagreement at the time of the survey as an indicator of how important local context is to the challenges and threats faced by developers in repressive societies. Over the next couple of months we will be building user personas that synthesize and codify our findings. We hope these personas will help other individuals and organizations working on internet freedom issues to think about how they can structure their projects to support and collaborate with developers in repressive environments in safe and productive ways.