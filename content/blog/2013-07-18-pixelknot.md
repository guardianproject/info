---
id: 11496
title: 'Our Newest App: PixelKnot'
date: 2013-07-18T13:14:49-04:00
author: mark
layout: post
guid: https://guardianproject.info/?p=11496
permalink: /2013/07/18/pixelknot/
image: http://guardianproject.info/wp-content/uploads/2013/07/pic_femmir.jpg
categories:
  - New Release
  - News
tags:
  - images
  - privacy
  - securesmartcam
  - security
  - sharing
  - steganography
---
Have you ever hidden in plain sight? Worn camouflage in the woods or an invisibility cloak in a narrow crooked alley? It’s really hard to do properly. We’re hoping that all changes with PixelKnot.

PixelKnot is an app for hiding secret messages in pictures.  Sort of like invisible ink on the back of a painting, updated to the present.  The ancient art known as steganography, now updated for the 21st century and requiring a more rigorous set of safety standards.

The idea is to let anyone, anywhere share a secret with a friend. To most people, all they see is a picture. But to the right person, they know that someone has left them a message in that picture using PixelKnot. And they can find the message by opening that same picture in PixelKnot. Some people will even add a password to add another layer of protection to make sure that the message only ends up with the right person. And even if the message is detected, it’s also encrypted, making it that much harder to decode.

While hiding in plain sight using the app is easy, the app itself isn’t.  To define it, we’ve established the Guardian Project steganography standard. The approach of using steganography has some known limitations, but to be secure and reliable, for us the steganographed image must:

  1. Have the original image appear, to the trained human eye, unedited.
  2. Have the bytes of the image appear, to a trained analyst, undistorted so much so as to arouse suspicion.
  3. Have the complete message be recoverable no matter how it is transmitted.

As recent media stories have shown, large scale analysis is becoming a reality with increasing speed. Our standard seeks to ensure that our pictures, and the messages inside, can’t be plucked out like a needle in a haystack.  Another issue is that a lot of social media sites shrink and distort images that users upload.  This breaks our cipher since it’s technically a different image than what the User uploaded.  We’re fixing it so that it’s not a problem.  Already it works across Flickr, Tumblr and Google+,  with Facebook in the pipeline.

To build the steganography into the app, we used the <a title="f5 steganography" href="https://code.google.com/p/f5-steganography/" target="_blank">F5 algorithm</a>, which is resistant to visual and statistical attacks. Yet it still offers a large steganographic capacity, by using matrix encoding to improve the efficiency of embedding. F5 uses permutative straddling to uniformly spread out the changes over the whole steganogram, which helps us maintain the standards mentioned above that keep the messages from being detected.

How safe is safe, you might be wondering? We’ve been running tests on images created by PixelKnot using <a title="Stegdetect" href="http://www.outguess.org/detection.php" target="_blank">Stegdetect</a>, an automated tool for detecting steganographic content in images. It’s capable of detecting several different steganographic methods to embed hidden information in JPEG images. We trimmed it down to target f5 specifically. The results have been promising, though not 100%.

One goal we had while building the app was to transform the user experience of security and to see how easy and fun we could make the sharing of hidden messages.  The app starts by deciphering an image if there is text hidden inside already. If not,  it chooses enciphering, asking whether to take a photo or use one from a gallery. Why add unnecessary prompts asking users what they want to do, when there’s only one thing to do? A user can only move forward through the flow of the experience. In this way, we’re trying to increase security through a guided experience. If done properly and transparently, giving the user less options for navigation mean less ways to fail.

Is hiding messages in pictures the best way to spread secrets so that only the right person hears it? We don’t know.  At times in history, it’s been the only option, like between kings. At other times, it’s merely been used for fun, like scavenger hunts. For PixelKnot, we wanted to make something that could work in both scenarios o. But it’s up to users to decide.

We hope to share stories of people using PixelKnot in fun new ways.  If you have a idea or experience, please share it with us. We’d also like to add more features to PixelKnot that make strides both in security and in design, so your feedback is important– what would you most like to see? Until then, happy knotting!

Learn more about the app on [our site](https://guardianproject.info/apps/pixelknot/ "pixelknot"), or get it directly <a title="Pixelknot on Google Play" href="https://play.google.com/store/apps/details?id=info.guardianproject.pixelknot" target="_blank">from Google Play</a>.