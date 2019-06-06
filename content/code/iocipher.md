---
id: 2871
title: 'IOCipher: Virtual Encrypted Disks'
date: 2012-10-04T00:39:12-04:00
author: mark
guid: https://guardianproject.info/?page_id=2871
image: https://guardianproject.info/wp-content/uploads/2013/02/288491653_a9b6251477.jpg
menu:
  main:
    parent: code
---
<img class="alignleft size-thumbnail wp-image-3079" alt="alberti cipher disk" src="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg" width="150" height="150" srcset="https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2012/10/alberti_cipher_disk.jpg 245w" sizes="(max-width: 150px) 100vw, 150px" />

{{< source-code name="IOCipher" >}}

IOCipher provides a virtual encrypted disk for Android apps without requiring the device to be rooted. It uses a clone of the standard `java.io` API for working with files, so developers already know how to use it. Only password handling, and opening the virtual disk are what stand between the developer and working encrypted file storage. It is based on and <a href="http://sqlcipher.net/" target="_blank">SQLCipher</a>, and designed to work with <a href="https://github.com/guardianproject/IOCipher" target="_blank">CacheWord</a> for handling the keys and passwords.

IOCipher is ultimately based on transactions in SQLite, which means that it does not require being mounted in the normal sense. There is no open state once a transaction is complete. Each read or write operation is a self-contained SQLite transaction, so if the file system is forcably quit, SQLite&#8217;s transactions prevent the whole file system from being corrupted. This is important in Android since an `Activity` or `Service` can be killed at any moment without warning.

IOCipher is a cousin to <a href="https://www.zetetic.net/sqlcipher/sqlcipher-for-android/" target="_blank">SQLCipher-for-Android</a> since it is also based on SQLCipher and uses the same approach of repurposing an API that developers already know well. It is built on top of <a title="libsqlfs git repo" href="https://github.com/guardianproject/libsqlfs" target="_blank">libsqlfs</a>, a filesystem implemented in SQL that exposes a FUSE API.

## Features

  * Secure transparent app-level **virtual encrypted disk**
  * **No root** required
  * Only **three new methods** to learn: `VirtualFileSystem.get()`, `VirtualFileSystem.mount(dbFile, password)`, and `VirtualFileSystem.unmount()`
  * Supports Android versions **2.3 and above**
  * Licensed under the **LGPL v3+**

## Adding IOCipher to your App

If you are using gradle, then add this to your project:

<pre>compile 'info.guardianproject.iocipher:IOCipherStandalone:0.4',</pre>

Here are the things you need to do in your code to make it use IOCipher encrypted storage for all of your app&#8217;s file storage:

  1. manage the password using Cacheword or whatever works for you
  2. get the VFS singleton using `VirtualFileSystem.get()`
  3. on first run, create the container file with a password using `VirtualFileSystem.createNewContainer(dbFile, password)`
  4. mount the container file with a password using `VirtualFileSystem.mount(dbFile, password)`
  5. replace the relevant `java.io` import statements with `info.guardianproject.iocipher`, e.g.: 
    <pre>import info.guardianproject.iocipher.File;
import info.guardianproject.iocipher.FileOutputStream;
import info.guardianproject.iocipher.FileReader;
import info.guardianproject.iocipher.IOCipherFileChannel;
import info.guardianproject.iocipher.VirtualFileSystem;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
</pre>

For more detailed examples, see <a href="https://github.com/guardianproject/IOCipherExample" target="_blank">IOCipherExample</a>, <a href="https://github.com/guardianproject/IOCipherThreadTest" target="_blank">IOCipherThreadTest</a>, and <a href="https://github.com/guardianproject/IOCipherTests" target="_blank">IOCipherTests</a>. To start from scratch, follow <a href="https://www.zetetic.net/sqlcipher/sqlcipher-for-android/" title="SQLCipher for Android Application Integration" target="_blank">the instructions on starting with SQLCipher-for-Android</a>, then download IOCipher and add it to the `libs/` folder of that new project.

## Downloads

Here you can get the complete IOCipher jar and native library files, ready to drop right into your project (for MIPS, you need to build from source):

  * [IOCipher-v0.4.zip](/releases/IOCipher-v0.4.zip) 
      * [detached GPG signature](/releases/IOCipher-v0.4.zip.asc)

If you are interested in experimenting with the underlying <a href="http://fuse.sourceforge.net/" title="Filesystem in Userspace" target="_blank">FUSE</a> library, you can download the **optional** `libsqlfs` source tarball:

  * [libsqlfs-1.3.2.tar.bz2](/releases/libsqlfs-1.3.2.tar.bz2) 
      * [detached GPG signature](/releases/libsqlfs-1.3.2.tar.bz2.sig)

## Source Code Repositories

  * all you need for your project: <https://github.com/guardianproject/IOCipher>

### optional:

  * the test suite: <https://github.com/guardianproject/IOCipherTests>
  * a simple example file manager app: <https://github.com/guardianproject/IOCipherExample>
  * a very simple test app: <https://github.com/guardianproject/IOCipherThreadTest>
  * the core: <https://github.com/guardianproject/libsqlfs>

## Usage notes

  * only one active mount per-app is supported
  * single thread/sequential access is the preferred way of using IOCipher
  * multi-threaded access possible (_potentially unstable under extremely high write load_)
  * VFS now has beginTransaction and completeTransaction to optimize performance
  * parts of java.io not currently supported: vectored I/O, memory-mapped files

## Reporting Bugs

Please report any bugs or issues that you have with this library! We want to hear from you. Help us improve this software by filing bug reports about any problem that you encounter. Feature requests and patches are also welcome!

  * [<img src="https://guardianproject.info/wp-content/uploads/2011/02/reportbug-150x150.jpg" alt="report bug" width="150" height="150" class="size-thumbnail wp-image-12362" srcset="https://guardianproject.info/wp-content/uploads/2011/02/reportbug-150x150.jpg 150w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug-100x100.jpg 100w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug-200x200.jpg 200w, https://guardianproject.info/wp-content/uploads/2011/02/reportbug.jpg 225w" sizes="(max-width: 150px) 100vw, 150px" /> <strong style="font-size: 200%">Report a Bug or Issue</strong>](https://dev.guardianproject.info/projects/iocipher/issues/new)

## Known Issues

  * files cannot currently be larger than 4GB (<a href="https://dev.guardianproject.info/issues/3624" target="_blank">#3624</a>)
  * no users, groups, or permissions implemented
  * crashes possible under _extremely_ heavy, concurrent load (<a href="https://dev.guardianproject.info/issues/522" target="_blank">#522</a>)
  * <a title="existing IOCipher issues" href="https://dev.guardianproject.info/projects/iocipher/issues" target="_blank">View all open issues</a>