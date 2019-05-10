---
id: 488
title: 'Orbot Update: New Setup Wizard at Startup'
date: 2010-07-29T17:17:08-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=488
permalink: /2010/07/29/orbot-update-new-setup-wizard-at-startup/
categories:
  - Development
tags:
  - android
  - anonymity
  - open-source
  - orbot
  - proxy
  - tor
  - usability
  - ux
---
We’ve been working away at the 0.0.9 release of [Orbot](https://guardianproject.info/apps/orbot) over the last few months, and have put a decent amount of effort into usability. Specifically, we hoped to better communicate to users what it means to run Tor on your Android phone. In addition, we wanted to clearly lay out how the various configuration options help to improve your mobile web anonymity and ability to circumvent web filters and tracking by your mobile service provider.

The screenshots below are what you see the first time you install and run Orbot, and also whenever you open the “Help” menu. One important thing to point out is that Orbot can run with or without root, and our setup UI responds to having the capability or not accordingly.

Ultimately our goal is to provide a useful bootstrap experience for novice and advanced users alike. We welcome your feedback.

<div id='gallery-3' class='gallery galleryid-488 gallery-columns-3 gallery-size-thumbnail'>
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-1.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-1-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-489" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-1-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-1-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-489'>
      permissions… we actually will only be asking for INTERNET – so don’t mind the “phone status” permission
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-2.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-2-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-490" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-2-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-2-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-490'>
      Your basic install screen
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-3.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-3-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-491" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-3-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-3-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-491'>
      A friendly welcome
    </dd>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-4.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-4-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-492" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-4-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-4-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-492'>
      About Orbot!
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-5.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-5-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-493" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-5-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-5-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-493'>
      we ask nicely to get root permissions, if possible
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-7.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-7-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-495" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-7-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-7-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-495'>
      if the user doesn’t have root, we make sure they understand the implications
    </dd>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-8.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-8-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-496" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-8-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-8-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-496'>
      Offer direct downloads of Orbot/Tor enabled apps
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.5.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.5-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-497" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.5-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.5-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-497'>
      (Root only) choose whether to “Torify All” or choose app by app
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.6.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.6-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-498" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.6-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.6-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-498'>
      (Root only) Select to send all network traffic through Tor
    </dd>
  </dl>
  
  <br style="clear: both" />
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.7.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.7-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-499" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.7-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.7-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-499'>
      (Root only) Select which apps you want to route through Tor
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-9.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-500" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-9-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-9-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-500'>
      This is the final step
    </dd>
  </dl>
  
  <dl class='gallery-item'>
    <dt class='gallery-icon portrait'>
      <a href='https://guardianproject.info/wp-content/uploads/2010/07/orbot-10.png'><img width="150" height="150" src="https://guardianproject.info/wp-content/uploads/2010/07/orbot-10-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" aria-describedby="gallery-3-501" srcset="https://guardianproject.info/wp-content/uploads/2010/07/orbot-10-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/07/orbot-10-64x64.png 64w" sizes="(max-width: 150px) 100vw, 150px" /></a>
    </dt>
    
    <dd class='wp-caption-text gallery-caption' id='gallery-3-501'>
      We’ve got root!
    </dd>
  </dl>
  
  <br style="clear: both" />
</div>