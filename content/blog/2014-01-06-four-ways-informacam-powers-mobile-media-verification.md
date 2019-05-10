---
id: 12084
title: Four Ways InformaCam Powers Mobile Media Verification
date: 2014-01-06T15:14:16-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=12084
permalink: /2014/01/06/four-ways-informacam-powers-mobile-media-verification/
bigimg: [{src: "https://guardianproject.info/wp-content/uploads/2014/01/informacambanner1.jpg",}]
categories:
  - Research
tags:
  - informaCam
---
_Note: A big discussion topic of 2013 was about how hard cryptography and security is for average people, journalists and others. With that in mind, we’d like to sub-title this post “Making Mobile Crypto Easy for Eyewitnesses”, as the InformaCam software and process described below includes the full gamut of security and cryptography tools all behind a streamlined, and even attractive application user experience we are quite proud of…. _

One of the primary goals of the [InformaCam](https://guardianproject.info/informa) project (now in [public beta!](https://guardianproject.info/informa)) is to create an environment where, when it comes to photos and video captured on smartphones, people and organizations can trust what they see. Faked photos and videos, whether intended to be humorous or malicious, are all too common online, especially in times of crisis. Thus, the software that been developed works to ensure the full, complete original photo or video captured of an event, can safely reach the people who need to see it, without it first being filtered, modified, cropped, trimmed or otherwise manipulated.

There are four ways this is achieved:

  1. At point of capture, secure storage and analysis of the media file itself to begin a chain of custody, create a means of verifying media pixel values directly, and defend against tampering by malicious apps.
  2. Gather corroborating metadata points using the device’s built-in sensors to establish an environmental context.
  3. Use a secure method of transmission to a secure repository to continue chain of custody, and to defend against network surveillance, intrusion and filtering.
  4. Provide a means, using open tools, to verify media was not tampered with and to view and analyze corroborating metadata.

Let’s dig deeper into each of these links of the verification chain.

<strong style="line-height: 1.5em;">Secure Storage and Analysis</strong>

When InformaCam is activated, it begins to actively monitor the device for any new photos or videos captured by the built-in camera software. InformaCam does not support importing already captured photos or videos. It must actively detect a new photo or video is captured by the active camera software on the device. As soon as it detects a new capture, it begins the following ingest process:

  1. Import the media file into an encrypted storage system, on the device, but only accessible by the InformaCam app. This ensures the file is not modified by any other application on the device.
  2. Generate and securely store a cryptographic hash value, or checksum, of the pixels of the media file, either the single photo or collectively for all the frames of the video. Any change to the pixels of the media files (“photoshopping”, removal of frames, editing, or other modifications) would result in a change to the hash value.
  3. Delete the source photo or video from its original location on the device’s shared storage, to keep it hidden from plain view in high-risk situations. Since it has been imported to encrypted storage, this version is no longer needed, and not trustworthy, ultimately.

With this three step process we have, as near as possible to the time and place of capture, ensured we have the media file in a secure storage location, and have generated a unique hash value to verify the file against later.

The hash value, which is just a short series of hexadecimal characters, can also be immediately shared to a third-party using email, text messaging, Twitter or other public notary system. The sooner it can be in the “public record” the better, to establish that the media file existed in this exact state at this time. This concept of a notary is important, and one we seek to develop more, to ensure the notary is also a trusted, tamper-proof service.

**Corroborating Sensor Metadata**

In addition to the media file itself and the cryptographic hash, an enormous amount of additional metadata is also captured during the window of time that InformaCam is activated and monitoring for the digital media creation events. We don’t discuss all of them here, but in short, InformaCam uses [all available network, radio, motion and environmental sensors built into modern smartphones](http://developer.android.com/guide/topics/sensors/sensors_overview.html) to gather corroborating data points that can be used to establish credibility. This bundle of metadata is known as J3M, or [JSON Evidentiary Mobile Media Metadata](https://dev.guardianproject.info/projects/informacam/wiki/JSON_Mobile_Media_Metadata_(J3M)), with JSON (Javascript Object Notation) being the technical format it is stored in. When the media file is exported for verification, this data is bundled into the media file itself, and cryptographically signed and encrypted to ensure it cannot be modified or otherwise used by unauthorized third-parties.

**Secure Repository Submission**

<span style="line-height: 1.5em;">When the owner of the device running InformaCam with the media file on it decides to share it with an organization for verification and use, they can send it using InformaCam’s built-in Secure Share mechanism. This enables the media file and embedded metadata to be d</span>irectly sent to an [InformaCam Repository](https://github.com/guardianproject/InformaRepo) over a secure connection. While the connection uses the public internet, it is sent directly between the device and the repository inside of a secure, tamper proof tunnel powered by software known as [Tor](https://torproject.org). This connection is configured using an [InformaCam Trusted Definition configuration file](https://dev.guardianproject.info/projects/informacam/wiki/InformaCam_Trusted_Destination_(ICTD)) which contains the necessary network addresses and credentials.

The secure repository is expected to be run on a Linux server that is properly secured with strong access controls, firewalls, encrypted disk storage, and all other available mechanisms well known for securing desktop or server systems. It should not be placed on the public Internet, but only exposed through the Tor network connection. It should be hosted in a location that can be physically secured by the organization, as much as possible, and that could not be accessed without the organization being aware. This means that third party data centers should not be used, as access to these machines by law enforcement or malicious hackers can be accomplished without notice to the customers.

However, as long as the media hash value itself is maintained in a secure manner, possibly even printed out and stored in an offline physically secure system, the state of the media file itself can be easily verified using common tools.

<strong style="line-height: 1.5em;">Open Verification and Analysis Tools</strong>

Once the media and metadata have been received in the secure repository, the organization managing it can used the [InformaCam Analyzer and Dashboard](https://guardianproject.info/informa) software to process and verify the media file. All of the steps below are automatically done by the software, but can also be manually done by a competent, trained technician. These are the steps taken:

  1. Export the J3M corroborating metadata from the media file. It will be encrypted to the organization’s public cryptographic key, so it will first need to be decrypted, and also the signature of the data verified against the sender’s public key, which the organization previously obtained. This step is accomplished using the free and open-source [GnuPG software tools](http://gnupg.org).
  2. Run the media verification process on the photo or video file. This is accomplished using a tool in the InformaCam Analyzer software, which also includes the free and open-source [FFMPEG media engine](http://www.ffmpeg.org/) software. The cryptographic hash function is run again, this time on the server-side on not on the device, and the resulting hash value from the pixel values is displayed. This must match the hash value generated on the device, which should have been shared via private or public notary (SMS, email, Twitter, etc), and is also stored in the J3M metadata obtained in step #1.
  3. View the J3M metadata directly or import into the [InformaCam Dashboard system](https://j3m.info/submission/1110ca88837d710d9c43d49f48afce0b/) for verification. The metadata will include information such as GPS location, cellular network location, nearby bluetooth and wifi devices, compass headings, altitude, temperature and more. This data can be used to match against the time and place the media claims to be from.

**Four Ways, In Summary**

Through the four ways described above, the InformCam system works to capture and safeguard both media and metadata at all points along the way, between the device and the repository. Cryptographic functions and features provide much of the power behind this, but relying on mathematics alone does not tell the whole store. By combining the corroborating metadata and open tools for analysis, we ensure that the context of the photo or video, and the means to verify the entire package are also readily available as part of the verification process.