---
id: 643
title: 'SQLCipher: Encrypted Database'
date: 2011-02-19T08:27:13-04:00
author: n8fr8
guid: https://guardianproject.info/
image: https://guardianproject.info/wp-content/uploads/2011/02/showcase.png
menu:
  main:
    parent: code
---

<img class="alignnone size-medium wp-image-1329" title="logo-sqlcipher-android" src="https://guardianproject.info/wp-content/uploads/2011/02/logo-sqlcipher-android-300x50.png" alt="" width="300" height="50" srcset="https://guardianproject.info/wp-content/uploads/2011/02/logo-sqlcipher-android-300x50.png 300w, https://guardianproject.info/wp-content/uploads/2011/02/logo-sqlcipher-android.png 522w" sizes="(max-width: 300px) 100vw, 300px" />

<div class="source-code" style="width: 30%; margin: 0 auto;">
  <a href="https://github.com/sqlcipher/android-database-sqlcipher" target="_blank" title="SQLCipher for Android">
    <i class="fa fa-github"></i> GitHub
  </a>
  -
  <a href="/tags/sqlcipher" target="_blank" title="SQLCipher blog posts">
    <i class="fa fa-rss"></i> blog posts
  </a>
</div>
<hr />

In an environment where mobile data privacy is increasingly [in the headlines](http://www.reuters.com/article/2011/05/08/us-privacy-congress-idUSTRE7471SA20110508), this project will make it easier than ever for mobile developers to properly secure their local application data, and in turn better protect the privacy of their users. The data stored by Android apps protected by this type of encryption will be less vulnerable to access by malicious apps, protected in case of device loss or theft, and highly resistant to [mobile data forensics tools](http://www.cellebrite.com/) that are increasingly used to mass copy a mobile device during [routine traffic stops](http://www.thenewspaper.com/news/34/3458.asp).

SQLCipher is a [SQLite](http://sqlite.org/) extension that provides transparent 256-bit AES encryption of database files. To date, it has been open-sourced, sponsored and maintained by [Zetetic LLC](http://zetetic.net/). In the mobile space, SQLCipher has enjoyed widespread use in Apple’s [iOS](http://sqlcipher.net/documentation/ios.html), as well as [Nokia / QT](http://www.qtcentre.org/wiki/index.php?title=Building_QSQLITE_driver_with_AES-256_encryption_support) for quite some time. Given that Android [by default](http://developer.android.com/guide/topics/data/data-storage.html#db) provides integrated support for SQLite databases, our goal was to create an almost identical API for SQLCipher, so that developers of all skill level could use it, without a steep learning curve.


## Learn More and Download

* [SQLCipher for Android](https://www.zetetic.net/sqlcipher/sqlcipher-for-android/)
* source: <https://github.com/sqlcipher/android-database-sqlcipher>


### An Illustrative Terminal Listing

A typical SQLite database in unencrypted, and visually parseable even as encoded text. The following example shows the difference between hexdumps of a standard SQLite db and one implementing SQLCipher.

> ~ sjlombardo$ hexdump -C sqlite.db  
> 00000000 53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 33 00 |SQLite format 3.|  
> &#8230;  
> 000003c0 65 74 32 74 32 03 43 52 45 41 54 45 20 54 41 42 |et2t2.CREATE TAB|  
> 000003d0 4c 45 20 74 32 28 61 2c 62 29 24 01 06 17 11 11 |LE t2(a,b)$&#8230;..|  
> &#8230;  
> 000007e0 20 74 68 65 20 73 68 6f 77 15 01 03 01 2f 01 6f | the show&#8230;./.o|  
> 000007f0 6e 65 20 66 6f 72 20 74 68 65 20 6d 6f 6e 65 79 |ne for the money|
> 
> ~ $ sqlite3 sqlcipher.db  
> sqlite> PRAGMA KEY=&#8217;test123&#8242;;  
> sqlite> CREATE TABLE t1(a,b);  
> sqlite> INSERT INTO t1(a,b) VALUES (&#8216;one for the money&#8217;, &#8216;two for the show&#8217;);  
> sqlite> .quit
> 
> ~ $ hexdump -C sqlite.db  
> 00000000 84 d1 36 18 eb b5 82 90 c4 70 0d ee 43 cb 61 87 |.?6.?..?p.?C?a.|  
> 00000010 91 42 3c cd 55 24 ab c6 c4 1d c6 67 b4 e3 96 bb |.B<!--?U$???.?g??.?| ... 00000be0  dc 77 5c 6c de c6 d3 be  43 49 48 3e f3 02 94 a9  |?w\l??ӾCIH-->?..?|
> 
>  
> 00000bf0 8e 99 ee 28 23 43 ab a4 97 cd 63 42 8a 8e 7c c6 |..?(#C??.?cB..|?|
> 
> ~ $ sqlite3 sqlcipher.db  
> sqlite> SELECT * FROM t1;  
> Error: file is encrypted or is not a database

(example courtesy of [SQLCipher](http://sqlcipher.net/design))

#### Details for Developers

We&#8217;ve packaged up a very simple SDK for any Android developer to add SQLCipher into their app with the following three steps:

  1. Add a single sqlcipher.jar and a few .so&#8217;s to the application libs directory
  2. Update the import path from _android.database.sqlite.*_ to _info.guardianproject.database.sqlite.*_ in any source files that reference it. The original android.database.Cursor can still be used unchanged.
  3. Init the database in onCreate() and pass a variable argument to the open database method with a password*:

>   * SQLiteDatabase.loadLibs(this); //first init the db libraries with the context
>   * SQLiteOpenHelper.getWritableDatabase(“thisismysecret”):

***Note:** we are working on some dialog builder helper methods for password and PIN input, password caching, and other features that we would like to standardize across all applications that use SQLCipher.

#### Compatibility

The Developer Preview implements SQLCipher v1, is compatible with Android 2.2 & 2.3, and works only within one process (you can&#8217;t pass a Cursor from a remote Service to an Activity).

#### Notepad + SQLCipher = Notepadbot

Notepadbot is a sample application pulled from the standard Android samples code and updated to use SQLCipher. You can browse the source [here](https://github.com/guardianproject/notepadbot) and download the apk [here](https://github.com/guardianproject/notepadbot/Notepadbot-0.0.1c-dev.apk/qr_code).

<p style="text-align: center;">
  <img class="alignnone" src="https://guardianproject.info/wp-content/uploads/2011/05/prompt.png" alt="" width="180" height="300" /><img class="alignnone" title="successful authentication" src="https://guardianproject.info/wp-content/uploads/2011/05/notes.png" alt="" width="180" height="300" />
</p>

#### Final Notes

It&#8217;s important to note that this project is not intended to be a distinct, long-term fork of SQLCipher. We&#8217;ve been working closely with the SQLCipher team at [Zetetic](http://zetetic.net/) and fully intent to closely maintain the project as SQLCipher evolves, re-integrating changes in upcoming releases such as [SQLCipher v2](https://github.com/sjlombardo/sqlcipher/tree/v2beta).

The Android support libraries are licensed under [Apache 2.0](https://github.com/guardianproject/android-database-sqlcipher/blob/master/LICENSE), in line with the Android OS code on which they are based. The SQLCipher code itself is licensed under a [BSD-style license from Zetetic LLC.](https://github.com/guardianproject/android-database-sqlcipher/blob/master/SQLCIPHER_LICENSE) Finally, the original SQLite code itself is in the [public domain](http://www.sqlite.org/copyright.html).

<!--:-->