---
id: 3330
title: Lower Bounds of The Narrow Bands
date: 2013-02-22T09:05:48-04:00
author: lee
layout: post
guid: https://guardianproject.info/?p=3330
permalink: /2013/02/22/lower-bounds-of-the-narrow-bands/
force_ssl:
  - "1"
categories:
  - App Reviews
  - Development
tags:
  - codec
  - ostel
  - ostn
  - voip
---
Voice is becoming a standard feature of any messaging app on mobile phones, in various forms using many different protocols. There&#8217;s the old guard, whom I will refer to as &#8220;Skype&#8221;. Some [tough](https://www.privacyinternational.org/blog/skype-please-act-like-the-responsible-global-citizen-you-claim-to-be) [questions](http://www.skypeopenletter.com/) have been thrown their way by many groups who support a free Internet. There&#8217;s Google Voice, which is not really VoIP. Apple is playing around in the hedge maze inside their walled garden with iChat. There&#8217;s also Facebook, who is rolling out [voice calling in Canada and the USA](http://techcrunch.com/2013/01/16/facebook-rolls-out-voip-calling-to-u-s-ios-messenger-users/) in their Messenger app on iOS.

None of these offerings address the callers privacy, and few document the details of their calling systems for developers. Surprisingly, none of these global VoIP carriers interoperate with each other. Why? Like most complicated problems, there is a complicated answer. I&#8217;m going to focus on codecs, which is a research subject that has been very active in the last few years.

Our friends at WhisperSystems recently did an [in depth writeup](http://whispersystems.org/blog/client-side-audio-quality/) on some challenges they had with the Speex codec when building RedPhone. RedPhone is the client application for one of a small group of secure VoIP carriers that address the challenging privacy issues around VoIP.

The Guardian Project is also one of these carriers, with a public service called [OSTel](https://ostel.me). We chose to leverage an existing open source client called [CSipSimple](https://code.google.com/p/csipsimple/). This client has a modular design, which provides a wide selection of codecs. I&#8217;m going to focus on one in particular, [named Codec2](http://codec2.org/).

[<img src="https://guardianproject.info/wp-content/uploads/2013/02/spectrogram-300x231.png" alt="spectrogram" width="300" height="231" class="aligncenter size-medium wp-image-3338" srcset="https://guardianproject.info/wp-content/uploads/2013/02/spectrogram-300x231.png 300w, https://guardianproject.info/wp-content/uploads/2013/02/spectrogram.png 560w" sizes="(max-width: 300px) 100vw, 300px" />](https://guardianproject.info/wp-content/uploads/2013/02/spectrogram.png)

Codec2 addresses a challenge in radio communications that has been around for longer than the Internet. Bandwidth. It might be appropriate to think of your cell phone as a radio to understand this example. When connected to a cellular data connection, the bandwidth is limited by the carrier&#8217;s packet switched radio technology. This may be GPRS, EDGE, 3G, 4G(LTE) to name a few lovely acronyms. If your VoIP call uses a codec that exceeds the upper bounds of this bandwidth, you start to hear side effects like dropouts or unintelligible transmission which probably will lead to a dropped call.

One way to address this problem is to shoot for the bottom. The lower bounds of the bandwidth of cellular data connections start to look a lot like more traditional radio. Shortwave radio, or HAM is the community that&#8217;s the closest to the technology behind Codec2. If a codec can be used to transmit [digitally encoded data](https://en.wikipedia.org/wiki/AMPRNet) over HAM, that means it is possible to &#8220;do VoIP&#8221; over a shortwave radio link. This opens up exciting new possibilities for secure voice over narrow bandwidth environments.

While a small part of the world enjoys plentiful wide band data connections in urban areas, coverage in many rural areas is less common. In this case shooting for the bottom of the bandwidth spectrum helps us keep our calls from dropping and our voices heard.

The [CSipSimple Codec Pack](https://play.google.com/store/apps/details?id=com.csipsimple.plugins.codecs.pack1&feature=more_from_developer#?t=W251bGwsMSwyLDEwMiwiY29tLmNzaXBzaW1wbGUucGx1Z2lucy5jb2RlY3MucGFjazEiXQ..) supports secure voice calls using Codec2 with the stable release on the [Google Play Store](https://play.google.com/store/apps/details?id=com.csipsimple&feature=more_from_developer#?t=W251bGwsMSwyLDEwMiwiY29tLmNzaXBzaW1wbGUiXQ..).