---
id: 1457
title: Introducing InformaCam
date: 2012-01-20T13:58:26-04:00
author: harlo
layout: post
guid: https://guardianproject.info/?p=1457
permalink: /2012/01/20/introducing-informacam/
categories:
  - News
tags:
  - encryption
  - informaCam
  - metadata
  - obscuracam
  - pgp
  - privacy
  - securesmartcam
  - witness
---
These are interesting times, if you go by Times Magazine as an indicator. The magazine’s person of the year for 2011 was The Protester, preceded in 2010 by Facebook founder Mark Zuckerberg. Both entities partners with equal stake in freely sharing the digital content that shows the world what’s going on in it, at any time, from behind any pair of eyes.<img class="alignright size-medium wp-image-1471" alt="The Protester: Person of the Year" src="https://guardianproject.info/wp-content/uploads/2012/01/poy_cover-225x300.jpg" width="225" height="300" srcset="https://guardianproject.info/wp-content/uploads/2012/01/poy_cover-225x300.jpg 225w, https://guardianproject.info/wp-content/uploads/2012/01/poy_cover.jpg 474w" sizes="(max-width: 225px) 100vw, 225px" /> Also casting in their lot with the others is Time Magazine’s 2006 person of the year, You: the You that puts the “you” in “user-generated content;” the You whose miasma of bits, bytes, and the powerful images they express are becoming increasingly problematic. Problematic and exciting. As governments, police forces, and other power players here and abroad crack down on voices of dissent, it is only You, The Protester, armed not with a press pass, but with a smartphone and a Twitter account, who brings the rest of the world its news. You do it mainly without either the support or permission of those in power, and this makes you a very important person in the world.

The smartphone’s role in the defense of human rights has thus become ever-more clear. How can we make it clearer? Our latest project, InformaCam, tackles this issue head-on. In collaboration with <a href="http://witness.org/" target="_blank">Witness.ORG</a> and the <a href="www.ibanet.org/" target="_blank">International Bar Association</a>, we’re building a powerful tool to create iron-clad digital images and video that could, should the occasion arise, be used in courts of law to bring justice. This is no small feat&#8211; with this project we are helping create the first evidentiary standards for digital media in the social networking age. So, <a href="http://www.economist.com/node/21542748" target="_blank">there’s been a lot of excitement</a> these past few weeks about InformaCam, as well as a lot of mystery. It’s time to give the project a proper unveiling.

InformaCam is a plugin for ObscuraCam that allows the user, without much intervention on their own part, to inflate image and video with extra points of data, or metadata. The metadata includes information like the user’s current GPS coordinates, altitude, compass bearing, light meter readings, the signatures of neighboring devices, cell towers, and wifi networks; and serves to shed light on the exact circumstances and contexts under which the digital image was taken. Some users will already be familiar with ObscuraCam, which allows for capturing and digitally manipulating media. With InformaCam included, the app starts to behave almost like Adobe Photoshop or GIMP, supporting non-destructive, layer-based edits to media. This means that a version of an image can be created with any sensitive image data and metadata preserved and encrypted to trusted entities, along with a redacted version that has its metadata stripped which can be easily shared to Facebook, Twitter, Flickr, or any public service the user wishes to use.

## How InformaCam Works

<img class="alignleft size-full wp-image-1459" alt="InformaCam (1)" src="https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.18.27-PM.png" width="205" height="341" srcset="https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.18.27-PM.png 205w, https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.18.27-PM-180x300.png 180w" sizes="(max-width: 205px) 100vw, 205px" /> The workflow is similar to that of ObscuraCam, but with a few key differences. Notice that on start-up, the app triggers the on-board sensors. (Notifications in the top right corner clearly indicate the GPS and Bluetooth modules have been turned on.) This allows the app to register sensory and atmospheric data throughout the session. These “bundles” of data contain the following:

  * Current timestamp
  * Device&#8217;s identification
  * User&#8217;s public (PGP) key
  * Image Regions created in the image/video
  * Current latitude & longitude
  * Current cell ID (if available)
  * Altitude
  * Compass bearing

Whether the user is taking a picture, or editing an existing piece of media, the app registers the goings-on, and signs each bundle of data with the user’s private key. This mean that all actions taken on a piece of media (from capture to editing) are attributed to the user.

As with ObscuraCam, the user can perform image filtering and obfuscation on image regions. InformaCam also adds the “Identify” filter, which prompts the user for the subject’s name (or pseudonym) and to fill in whether or not the subject has given his or her consent to be filmed. This checklist of subject permissions can be further developed to match the needs of any organization to provide further protection to the people in front of the camera. Notice again the sensor notifications: the context surrounding each edit to the image is recorded and will be inserted into the media as metadata once the media is saved.

When the user saves the image or video, a dialog appears prompting her to choose one or more “trusted destinations.” This could be an organization, a news outlet, or any friend whose PGP key is known to you. A copy of the unredacted, data-rich image will be created and encrypted to those parties. At the same time, a redacted and data-stripped version is made available to share with anyone, anywhere.

<table>
  <tr>
    <td width="201">
      <img class="alignnone size-full wp-image-1461" alt="InformaCam (2)" src="https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.21.07-PM.png" width="201" height="332" srcset="https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.21.07-PM.png 201w, https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.21.07-PM-181x300.png 181w" sizes="(max-width: 201px) 100vw, 201px" />
    </td>
    
    <td width="197">
      <img class="alignnone size-full wp-image-1462" alt="InformaCam (3)" src="https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.21.21-PM.png" width="197" height="330" srcset="https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.21.21-PM.png 197w, https://guardianproject.info/wp-content/uploads/2012/01/Screen-shot-2012-01-20-at-1.21.21-PM-179x300.png 179w" sizes="(max-width: 197px) 100vw, 197px" />
    </td>
  </tr>
  
  <tr>
    <td>
      <i>Using the InformaCam &#8220;Identify&#8221; filter.</i>
    </td>
    
    <td>
      <i>Select a Trusted Destination for your encrypted media.</i>
    </td>
  </tr>
</table>

## The Informa Metadata Schematic

The metadata is organized in four categories: intent, consent, geneaology, and data. Here’s a rundown of what these categories mean.

### Intent

This expresses information about the media’s creator, and the rules governing how this particular media object can be shared, and to whom.

### Consent

This bucket of information regards the subjects contained in the image. Each subject is identified (by a name or pseudonym selected by the user) along with their stated preferences regarding treatment of their likeness. For example, if Bobby insists that he wants his face to be fully redacted (rather than blurred) this preference should be registered in metadata.

### Genealogy

This information regards chain-of-custody, and represents how the media was acquired, and if a particular image or video is a duplicate of another.

### Data

This category includes all standard metadata (timestamp, acquired sensory data, location and movement data) that have been collected during the lifetime of the image, from the moment it was opened to the instant it was saved.

A sample metadata bundle for an image taken with InformaCam looks like this in JSON notation:

`<br />
{<br />
"data":{<br />
"device":{<br />
"bluetoothInformation":{<br />
"selfOrNeighbor":-1,<br />
"deviceBTAddress":"00:25:36:79:EC:6C",<br />
"deviceBTName":"nexxxie"<br />
},<br />
"imei":"363289131048142"<br />
},<br />
"sourceType":101,<br />
"imageRegions":[<br />
{<br />
"regionDimensions":{<br />
"height":256,<br />
"width":256.00006103515625<br />
},<br />
"regionCoordinates":{<br />
"left":527.705078125,<br />
"top":196.15255737304688<br />
},<br />
"obfuscationType":"Identify",<br />
"location":{<br />
"locationType":11,<br />
"locationData":{<br />
"gpsCoords":"[40.7085011,-73.9668647]",<br />
"cellId":"36789325"<br />
}<br />
},<br />
"captureTimestamp":{<br />
"timestamp":1326216508313,<br />
"timestampType":7<br />
},<br />
"subject":{<br />
"consentGiven":"general_consent",<br />
"informedConsentGiven":true,<br />
"subjectName":"Harlo!"<br />
},<br />
"unredactedRegion":"I@4070cf30"<br />
}<br />
],<br />
"imageHash":"f18e7510faaad0d942db68b5c75f219a",<br />
},<br />
"geneaology":{<br />
"dateAcquired":0,<br />
"localMediaPath":"\/mnt\/sdcard\/DCIM\/Camera\/1326216520426.jpg",<br />
"dateCreated":1326216527629<br />
},<br />
"intent":{<br />
"owner":{<br />
"ownershipType":25,<br />
"ownerKey":"MY-IDENTITY-IS-HERE"<br />
},<br />
"securityLevel":1,<br />
"intendedDestination":"[\"&#x68;&#97;r&#x6c;&#x6f;.h&#x6f;&#x6c;me&#x73;&#64;g&#x6d;&#x61;&#105;l&#x2e;&#x63;om\"]"<br />
}<br />
` 

## Your Help

InformaCam is a work-in-process, and we’d love help from the community in fleshing out our metadata specification, especially in adding new items to the consent checklist. Feel free to contact us with any suggestions/comments, or just leave some helpful tips in the comments below.