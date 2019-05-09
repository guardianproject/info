---
id: 3205
title: report on IOCipher beta dev sprint
date: 2013-01-31T19:45:44-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=3205
permalink: /2013/01/31/report-on-iocipher-beta-dev-sprint/
bigimg: [{src: "http://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg",}]
categories:
  - Development
tags:
  - android
  - encryption
  - iocipher
  - libsqlfs
  - open-source
  - psst
  - sqlcipher
---
We are just wrapping up an intensive dev sprint on [IOCipher](https://guardianproject.info/code/iocipher/) in order to get the first real beta release out, and it has been a wonderfully productive session on many levels! Before we started this, we had a proof-of-concept project that was crashy and ridiculously slow. We’re talking crashes every 100 or so transactions and 9 minutes to write 2 megs. Abel and I were plodding thru the bugs, trying to find the motivation to dive into the hard problems in the guts of some of the more arcane parts of the code. Aaron Huttner of <a href="http://gryphn.co/" target="_blank">Gryphn</a> found IOCipher while developing their <a href="https://play.google.com/store/apps/details?id=com.Gryphn.mms&hl=en" title="Gryphn Secure Text Messaging in the Google Play store" target="_blank">Gryphn Secure Text Messaging</a> and thought it was a remarkable easy way to add encrypted storage of files, and it worked quickly for him, so he included it his app before we had even announced an alpha release (thanks again for the vote of confidence!).

Aaron worked through a lot of the bugs with us, providing good bug reports and real, working test cases in code. What more could we ask for? We made progress on them slowly but surely. Gryphn then decided they needed IOCipher to work for them ASAP so they could put out a real release. They approached us about funding a development sprint and we thought it was a great idea. This also allowed us to bring in Stephen Lombardo and Nick Parker of <a href="http://zetetic.net/" target="_blank">Zetetic</a> to apply their <a href="http://sqlcipher.net/" target="_blank">SQLCipher</a> and SQLite expertise. Our very own David Oliver put together the deal, and off we went. So we put our heads down and focused everything on getting IOCipher to be a real file system.

To begin with, we focused on the core of IOCipher, <a href="https://github.com/guardianproject/libsqlfs" target="_blank">libsqlfs</a>, since we could run that on GNU/Linux, greatly speeding up the testing cycle. It started out with about 3 full days of Abel and I running `fsx` (File System eXersizer) tests of all shapes and sizes on libsqlfs mounts to try to pin down the crashes. It seemed like we were swimming in mountains of test results that vaguely pointed somewhere. We had some vague leads, but were excited to find that memory-mapped writes were far and away the most common crash. Since IOCipher does not use mapped writes at all, we could safely ignore those crashes for now. Turns out that using libsqlfs as a FUSE mount for our test platform has produced this one red herring.

One thing we knew all along is that both reads and writes were really slow, so Zetetic started with that. We all had the idea that the block sizes should all be aligned, and that should likely speed things up. This means Java stream readers and writers, writes in our Posix-style JNI layer, and the page size of the SQLite database. Zetetic did some testing and found that using 8k block sizes throughout produces some dramatic speed increases, here are some ballpark figures for doing a 2MB write with no contention:

  * ~710 seconds: default 256 byte blocks and no buffering, one SQLite transaction per block
  * ~65 seconds: wrapping all the 8192 write calls for each 256 byte block in a single SQLite transaction
  * ~20 seconds: same as above with the IOCipher FileOutputStream wrapped in a BufferedOutputStream
  * ~5 seconds: increase internal IOCipher block size to 4k
  * ~10 seconds: 8k sqlfs block size, 8k sqlite page size, and 8k BufferedOutputStream buffer, one SQLite transaction per block
  * ~1 second: same as above, all blocks written in a single SQLite transaction

Ok, now we had something you could actually use. Pretty slow still, but no longer ridiculous. Through much reading of code and testing, we figured out that there is one spot of the code that assumed it would always be able to read from the database. Under heavy load, this was not possible, especially when you have 9 minute blocking write operations. So the next step was to figure out all of the locking and make sure that was working right. The libsqlfs code from 2006 had the remnants of three separate locking mechanisms in it, SQLite locking, pthread locking, and a delay-retry timeout mechanism. Zetetic dove into updating libsqlfs to replace all that and use all of the modern SQLite tricks like `sqlite3_busy_timeout()` to replace the delay-retry logic, <a href="https://www.sqlite.org/lockingv3.html" target="_blank">v3.0 locks</a> and v3.7 <a href="https://www.sqlite.org/draft/wal.html" target="_blank">Write-Ahead-Logging</a> which gave libsqlfs a huge improvement in read/write concurrency, and putting libsqlfs and IOCipher reasonable performance in the realm of other encrypted file systems. I’ll let Stephen explain it:

> First, we changed the transaction command in begin_transaction to use “begin immediate”. This seeks an immediate reserved lock on the database, but does not exclusively lock it. This reduces unresolvable contention for write locks that would normally occur with deferred transactions, and is less restrictive than an exclusive lock, since it will continue to allow shared locks for reading.
> 
> It is extremely important that we prevent write operations from failing to execute due to busy timeouts, even if another process/thread has the database locked. Even using WAL, it is still possible for a command to be blocked during attempted concurrent write operations. This causes the write operation to fail leading to corruption. While libsqlfs has some “delay()” code that provides rudimentary busy handling, it is only in use for a small number of operations leaving other critical calls unprotected. Therefore, our second change was to register SQLite’s internal busy handler with a relatively high timeout (currently 10 seconds, but open for discussion) via sqlite3\_busy\_timeout. This provides protection for all operations in libsqlfs, reducing the likelihood that a write operation would fail outright, though it may be delayed. 
> 
> Finally, we enabled WAL mode to speed up write operations and further improve concurrency between readers and writers. Note that WAL mode only fsync()s on checkpoint operations, so it may be possible to enable NORMAL synchronous mode with lower overhead than the standard journal mode (we didn’t change this yet).
> 
> With these changes in place, three concurrent fsx processes running in parallel on a single fuse mount produced no errors in a 24hr test run. The tests also shows improved performance on read and writes. In light of these results, we’d like to get your feedback on these changes, and request that you run your own tests in the multi-threaded Android application to see if they resolve the problems that were reported. 

This was the final kicker. Who would of thought we could again get performance improvements of an order of magnitude twice in a single dev sprint. Now we have a encrypted filesystem that is stable and with reasonable performance that is really easy to use. And since that means that there is only very short chunks of time where everything is blocked (no more 9 minute writes), the crashes have basically vanished under real world loads. We have run super heavy file system tests over hundreds of thousands of operations without data corruption or crashes. We know that there is the theoretical potential for crashes in certain operations under super heavy load. We aim to address that in upcoming releases. And in conclusion, I’ll quote Aaron since he summarized what we are trying to achieve when we make developer tools:

> Between <a href="http://sqlcipher.net/sqlcipher-for-android/" target="_blank">SQLCipher-for-Android</a> and <a href="https://guardianproject.info/code/iocipher/" target="_blank">IOCipher</a> I don’t think it could get any easier to implement cryptography on Android, hopefully people pick up on this.

So grab the code now from git, if you’re ready to dive in! Or for the more patient, we’re developing tutorials to go along with the beta release that is coming any day now.