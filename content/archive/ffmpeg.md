---
id: 3030
title: 'FFMPEG: Media Privacy Framework'
date: 2013-01-02T12:43:43-04:00
author: mark
layout: page
guid: https://guardianproject.info/?page_id=3030
menu:
  main:
    parent: archive
aliases:
  - code/ffmpeg
---

<a title="ffmpeg" href="http://ffmpeg.org/" target="_blank">ffmpeg</a> is a popular, widespread framework for transcoding and filtering digital videos. On Android, it has a simple Java API. Our version includes filters for redaction and pixelization of video and audio, which we hope will become standard features for any app that supports on device video processing.

It has been essential to our apps ObscuraCam, InformaCam, and Murrow/StoryMaker. We are working to make it dead simple for developers to build their own apps on it. We are also extending it to provide a full framework for audio and image redaction, metadata management, and encryption of sensitive parts of the media. This will make it easy for media app developers to build in privacy to their own apps.

You can find our code at <a title="Android FFMPEG on Github" href="https://github.com/guardianproject/android-ffmpeg" target="_blank">https://github.com/guardianproject/android-ffmpeg</a>