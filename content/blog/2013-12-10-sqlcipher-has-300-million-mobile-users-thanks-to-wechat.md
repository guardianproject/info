---
id: 12033
title: SQLCipher has 100M+ Mobile Users (Thanks to WeChat!)
date: 2013-12-10T16:38:02-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=12033
permalink: /2013/12/10/sqlcipher-has-300-million-mobile-users-thanks-to-wechat/
categories:
  - News
---
_(Note: Originally this post had a title claiming 300 Million WeChat users… that would have included iOS and Android, and we don’t know if the WeChat iOS app also includes SQLCipher encryption or not. That said, there are 50-100M Google Play downloads of WeChat for Android, which does not include all of the users inside China)_

Through some of our own recent sluething, [Citizen Lab’s](http://citizenlab.org) research into [“Asia Chats” security](https://citizenlab.org/2013/11/asia-chats-analyzing-information-controls-privacy-asian-messaging-applications/), and now via this [detailed look at WeChat security from Emaze.com](http://blog.emaze.net/2013/09/a-look-at-wechat-security.html), it has been recently discovered that [WeChat for Android](http://www.wechat.com/) uses [SQLCipher](https://sqlcipher.net) for local data encryption in its app. We co-developed SQLCipher for Android with [Zetetic](http://zetetic.net/), and have been working to promote its adoption among Android developers who need to protect data stored locally on a device. While many people would point to Android’s Full Disk Encryption feature as a solution for that, only a small percentage of users ever enable it, and even then, once a device is unlocked, then all data is accessible by someone looking to extract it. With SQLCipher, the application can ensure its own data is encrypted, and if the app is closed, then the data is secured.

Now, as with most things WeChat, the actually implementation of SQLCipher is not that ideal, utilizing a short key, generated in part from the device’s ID, and some sort of server provided token. Still, at least they tried, and SQLCipher is considered stable enough to be used for the _**over 300 million WeChat users**_ around the world. Who knows, though, maybe the devs are on our developer list or the SQLCipher list, and we can help them improve their implementation using [CacheWord](https://github.com/guardianproject/cacheword)!

The biggest irony of this, is that I gave a lightning talk at Google IO 2013, highlighting the concern I had with the rapid growth of WeChat, and their parent company’s and country’s poor record on human rights, free speech, and generally defending their users. With the growth of WeChat beyond the borders of China, it is the first major mobile service to be exported and adopted outside of the Great Firewall, by non-Chinese users.

_My part starts at about 17:00 in, and runs for about 5 minutes…_  
  
So, for now, I raise a toast to the Android developers at Tencent/WeChat, who at least took a shot at providing local message encryption in their app, and may they continue to endeavor to defend their users privacy and security, as best as they can, considering their circumstances.

More from the [emaze-ing post](http://blog.emaze.net/2013/09/a-look-at-wechat-security.html) below…

> WeChat locally stores application data in an encrypted SQLite database  
> named “EnMicroMsg.db”. This database is located in the “MicroMsg”  
> subfolder inside the application’s data directory (typically something  
> like “/data/data/com.tencent.mm”).
> 
> The database is encrypted using SQLCipher, an open source extension for  
> SQLite that provides full database encryption. The encryption password  
> is derived from the “uin” parameter (see previous sections) combined  
> with the device identifier through a custom function. More precisely,  
> the key generation function leverages the mangle() function shown in the  
> previous Python snippet. The actual database encryption key can be  
> generated through the following pseudo-code:
> 
> password = mangle(deviceid + uin)[:7]
> 
> Here deviceid is the value returned by the Android API function  
> TelephonyManager.getDeviceId(). Follows a sample SQLCipher console  
> session that demonstrate how the EnMicroMsg.db database can be decrypted.
> 
> $ sqlcipher EnMicroMsg.db  
> sqlite> PRAGMA key = ‘b60c8e4’;  
> sqlite> PRAGMA cipher\_use\_hmac = OFF;  
> sqlite> .schema  
> CREATE TABLE conversation (unReadCount INTEGER, status INT, …  
> CREATE TABLE bottleconversation (unReadCount INTEGER, status INT, …  
> CREATE TABLE tcontact (username text PRIMARY KEY, extupdateseq long, …  
> …
> 
> It is also worth pointing out that, as the key generation algorithm  
> truncates the password to 7 hex characters, it would be not so difficult  
> for motivated attackers who are able to get the encrypted database to  
> brute force the key, even without knowing the uin or the device identifier.