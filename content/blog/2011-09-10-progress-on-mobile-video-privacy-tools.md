---
id: 1259
title: Progress on Mobile Video Privacy Tools
date: 2011-09-10T04:36:11-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=1259
permalink: /2011/09/10/progress-on-mobile-video-privacy-tools/
categories:
  - Development
tags:
  - ffmpeg
  - obscuracam
  - open source
  - openvideo
  - ovc11
  - privacy
  - securesmartcam
  - witness
---
_If you are  a developer you may just want to skip all the prose below, and just jump over to Github to find our new [FFMPEG on Android project](https://github.com/guardianproject/android-ffmpeg){.vt-p} and build system. You can also check out our [SSCVideoProto Project](https://github.com/guardianproject/SSCVideoProto){.vt-p} to understand how we are using it to redact faces and other identifying areas of HD video right on the Android phone itself. For more context, read on…_

Last October at the Open Video Conference 2010, the idea of a camera application that could be designed to understand the needs and requirements of the human rights community was born. During a [hackday hosted with WITNESS](https://blog.witness.org/2010/10/ovc2010-opensubtitles/){.vt-p}, we proved that is was possible to take a feature like “Face Detection” which is built into the Android operating system, and turn it into a capability that could be used to protect people, by blurring, pixelating or removing faces that unintentionally appeared in a video filmed on a mobile phone. In the last year, through our partnership with [WITNESS Labs](https://www.witness.org/cameras-everywhere/witness-labs), we have built on that concept, designing, developing and releasing apps and source code which move the state of the art in mobile video privacy and anonymity capabilities forward.

Here is a short video of [where we were a year ago](https://blog.witness.org/2010/10/ovc2010-opensubtitles/){.vt-p}.



The idea was that using a combination of approaches, we might be able to take the human rights video workflow, and ideas of consent and intent, that [WITNESS has developed for over twenty years](https://www.witness.org/training){.vt-p}, and encode that into best practices and features in a software application. This was the catalyst for the launch of our joint [Secure Smart Cam Project](https://github.com/guardianproject/securesmartcam/wiki){.vt-p}, which just a three months ago resulted in the [launch of our first public app](https://guardianproject.info/2011/06/23/announcing-obscuracam-v1-enhance-your-visual-privacy/){.vt-p}, [ObscuraCam v1](https://guardianproject.info/2011/06/23/announcing-obscuracam-v1-enhance-your-visual-privacy/){.vt-p}. Available in the Android Market, this app allows a user to quickly process a still photo taken on an Android smartphone, empowering them to remove unwanted identifying visual elements (faces, logos, signs, places) and remove unwanted digital metadata attached to the photo (GPS data, camera make and model, timestamps, etc). The app assists the user in this process by using Android’s built-in face detection technology to automatically identify and pixelize faces found in photos.

[<img class="alignnone" alt="" src="https://guardianproject.info/wp-content/uploads/2011/06/02_autodetect.png" width="560" height="336" />](https://guardianproject.info/2011/06/23/announcing-obscuracam-v1-enhance-your-visual-privacy/){.vt-p}

We continue to develop ObscuraCam in order to add new features, filters and privacy-enhancing capabilities. In addition, we exploring the “Informa” mode of this application, which uses the same technologies developed to assist in removing information, and instead uses them to add layers of extra verification, subject consent and intent tracking, and full media encryption. The idea is that in many cases people want to use visual media as evidence, or at least as reliable sources for journalistic use, and the more data that can be securely and safely captured and associated with a mediafile, the better. This is still in the research and design phase, but we expect to have some concepts of this ready for public play in the next few months.

While ObscuraCam is exciting, it only supports photos at this time. This is a fundamental issue, because WITNESS is a human-rights video organization, and the type of compelling content people are creating on their mobile phones are moving pictures not still. A year out from when the idea was first prototyped, I am happy to say that we have addresses the major challenges necessary to achieve mobile video processing of high-resolution video on the Android phone itself. The prototype last year was faking it in a sense, as it couldn’t actual record anything, and just showed the idea that you could detect faces. Our new [SSCVideoProto project](https://github.com/guardianproject/sscvideoproto){.vt-p}, utilizes the open-source [FFMPEG video processing library](https://github.com/guardianproject/android-ffmpeg){.vt-p}, to redact regions from recorded video files. Below is a short video that demonstrates the current state of the work.



In summary, this means we can now remove, pixelize or otherwise modify any identifying content in a high-resolution video recorded on a mobile phone, before that video is uploaded to YouTube, Facebook or elsewhere. Faces can be removed, screens blacked out or any other element that shouldn’t be shown, as it would increase some risk to the subjects of the video. Beyond redaction, we can now process any video, using open-source software, on an Android phone, including trimming, splitting, adjusting color, balance, brightness or any other common ffmpeg feature.

_Thanks to Shawn, Andrew and Hans for the collective work on getting us to this milestone_

[FFMPEG on Android project](https://github.com/guardianproject/android-ffmpeg){.vt-p}  
[SSCVideoProto Project](https://github.com/guardianproject/SSCVideoProto){.vt-p}