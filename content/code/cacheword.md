---
id: 12672
title: 'CacheWord: Passphrase Caching and Management'
date: 2014-09-26T21:44:19-04:00
author: Hans-Christoph Steiner
layout: page
guid: https://guardianproject.info/?page_id=12672
spacious_page_layout:
  - default_layout
catchresponsive-layout-option:
  - default
catchresponsive-header-image:
  - default
catchresponsive-featured-image:
  - default
publish_to_discourse:
  - "0"
publish_post_category:
  - "5"
---
CacheWord is an Android library project for passphrase caching and management.  
It helps app developers securely generate, store, and access secrets derived  
from a user&#8217;s passphrase. It is designed to work easily with [IOCipher](/code/iocipher) and <a href="https://www.zetetic.net/sqlcipher/open-source" target="_blank">SQLCipher-for-Android</a>, but it can be used any time an app needs to manage a password. Broadly speaking this library assists developers with two related problems:

  1. Secrets Management: how the secret key material for your app is generated, stored, and accessed
  2. Passphrase Caching: store the passphrase in memory to avoid constantly prompting the user

CacheWord manages key derivation, verification, persistence, passphrase resetting, and caching secret key material in memory.

### Features

  * Strong key derivation (PBKDF2)
  * Dynamic KDF iteration count based on CPU speed
  * Secure secret storage (AES-256 GCM)
  * Persistent notification: informs the user the app data is unlocked
  * Configurable timeout: after a specified time of inactivity the app locks itself
  * Manual clearing: the user can forcibly lock the application

## Downloads

To add Cacheword to your gradle project:

<pre>compile 'info.guardianproject.cacheword:cachewordlib:0.1.1'</pre>

Here you can get the complete CacheWord jar and native library files, ready to drop right into your project:

  * [cachewordlib-0.1.1.jar](https://guardianproject.info/releases/cachewordlib-0.1.1.jar) 
      * [detached gpg signature](https://guardianproject.info/releases/cachewordlib-0.1.1.jar.asc)

## Source Code Repository

  * library, helpers, tests, and sample project: <https://github.com/guardianproject/cacheword></ul>