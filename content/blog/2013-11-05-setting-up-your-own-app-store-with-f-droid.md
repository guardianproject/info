---
id: 11811
title: Setting up your own app store with F-Droid
date: 2013-11-05T11:55:43-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=11811
permalink: /2013/11/05/setting-up-your-own-app-store-with-f-droid/
categories:
  - HowTo
tags:
  - Android
  - bazaar
  - debian
  - distribution
  - F-Droid
  - fdroid
  - free software
  - howto
  - mobile
  - open source
  - privacy
  - ubuntu
---
(_This blog post as now been cooked into an <a href="https://f-droid.org/wiki/page/Setup_an_FDroid_App_Repo" target="_blank">updated HOWTO</a>_)

The Google Play Store for Android is not available in all parts of the world, US law restricts its use in certain countries like Iran, and many countries block access to the Play Store, like China. Also, the Google Play Store tracks all user actions, reporting back to Google what apps have been installed and also run on the phone. Because of the NSA leaks, we’re seeing that governments are <a href="http://www.theguardian.com/technology/2013/oct/30/google-reports-nsa-secretly-intercepts-data-links" target="_blank">actively tapping</a> into <a href="http://www.nytimes.com/2013/10/31/technology/nsa-is-mining-google-and-yahoo-abroad.html" target="_blank">the raw data streams</a> of Google, Yahoo, and others. So that means the information the Google Play Store sends back to Google is also intercepted by the NSA (and probably other country’s agencies), and that information is shared with other governments. In other words, your activity on the Google Play Store is far from private. Lastly, the Google Play Store is not free software, unlike the core of Android itself. It is proprietary software that Google entirely controls.

<img src="https://guardianproject.info/wp-content/uploads/2013/11/your-own-app-store.png" alt="your-own-app-store" width="300" height="203" class="alignright size-full wp-image-11896" /> <a href="https://f-droid.org" title="F-Droid Home Page" target="_blank">F-Droid</a> is a wonderful, free app store for Android. It is modeled after the <a href="http://www.debian.org" title="Debian home page" target="_blank">Debian GNU/Linux</a> distro. It has its own package repositories (repos) and build servers for all the apps that are part of the official OS. Like Debian and Ubuntu, you can also setup your own repos for anyone to use. Any free software can be added to the official F-Droid repos, where they are built and signed by the F-Droid server. This can be annoying because it means that your apps in F-Droid are signed by a different key than your apps in the Google Play Store. If you host your own F-Droid repo, then people can use F-Droid to install your own builds signed by your own signing key.

This is a quick HOWTO for how to setup such a repository on a Debian or Ubuntu box. It is somewhat technical, you will use the terminal, but you don’t need to be a terminal expert to follow along. First you need a the `fdroidserver` tools and a webserver. For the webserver, here we use _nginx_ for the webserver since its lightweight, but any will do if you already have one running. The fdroidserver tools are not yet in the official Debian/Ubuntu/etc repos, so you have to add our PPA (Personal Package Archive) to get it (fingerprint: <tt>F50E ADDD 2234 F563</tt>):

```
sudo add-apt-repository ppa:guardianproject/ppa
sudo apt-get update
sudo apt-get install fdroidserver nginx
```

In the case of this HOWTO, we’re going to setup a “<a href="https://f-droid.org/manual/fdroid.html#Simple-Binary-Repository" target="_blank">Simple Binary Repository</a>” to host our official APKs. The repo will be set up in the recommended `fdroid/` subdirectory. This gives the `fdroid` tool its own directory to work in, and makes the repo URL clearly marked as an FDroid repo. Let’s give our normal user control over this subdirectory in the web root so that we don’t need to run the F-Droid tools as root (with _nginx_, the webroot is `/usr/share/nginx/www`, it is different for other webservers):

```
sudo mkdir /usr/share/nginx/www/fdroid
sudo chown -R $USER /usr/share/nginx/www/fdroid
cd /usr/share/nginx/www/fdroid
fdroid init
```

Now put your APK files into `/usr/share/nginx/www/fdroid/repo` and you are ready to run the commands to build the repo (if `fdroid init` cannot find your Android SDK in `/opt/android-sdk` or `$ANDROID_HOME`, it will prompt you for the path):

```
cd /usr/share/nginx/www/fdroid
cp /path/to/*.apk /usr/share/nginx/www/fdroid/repo/
fdroid update -c
fdroid update
```

[<img src="https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3-300x75.png" alt="fdroidheader3" width="300" height="75" class="alignleft size-medium wp-image-11906" srcset="https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3-300x75.png 300w, https://guardianproject.info/wp-content/uploads/2013/11/fdroidheader3.png 720w" sizes="(max-width: 300px) 100vw, 300px" />](https://f-droid.org)Voila! Now you have a working F-Droid Repo! Add it to an F-Droid client on your Android device to test it out. That is done in the **Manage Repos** screen available from the menu. Your repo URL will be the hostname or IP address of your machine with `/fdroid/repo/` added to the end of it, i.e. `https://mysecureserver.com/fdroid/repo/` or `http://192.168.2.53/fdroid/repo/`. You can temporarily uncheck the official repos to easily see what F-Droid found in your new repo.

## Customization

You can also customize your repo by editing the config file. Be sure to use a programming text editor, like `editor /usr/share/nginx/www/fdroid/config.py`. In the config file, you can set the name of the repo, the description, the icon, paths to specific versions of the build tools, links to a related wiki, and whether to keep stats. Here’s the basic repo description block:

```
repo_url = "https://guardianproject.info/fdroid/repo"
repo_name = "My Local Repo"
repo_icon = "GP_Logo_hires.png"
repo_description = """
This is a local test repository of Hans-Christoph Steiner <&#x68;a&#x6e;s@&#x67;ua&#x72;d&#x69;&#x61;n&#x70;ro&#x6a;e&#x63;&#x74;.&#x69;nf&#x6f;>.  It is a repository of Guardian Project apps.
"""
```

To put your icon into your repo, choose a PNG image to put in your repo. The PNG goes in `/usr/share/nginx/www/fdroid/`, the file can be named whatever you want (by default its `fdroid-icon.png`). If you change the name from the default, be sure to update `repo_icon` and `archive_icon` in `/usr/share/nginx/www/fdroid/config.py`

## More Security

[<img src="https://guardianproject.info/wp-content/uploads/2010/02/apg-150x150.png" alt="apg" width="150" height="150" class="alignright size-thumbnail wp-image-1029" srcset="https://guardianproject.info/wp-content/uploads/2010/02/apg-150x150.png 150w, https://guardianproject.info/wp-content/uploads/2010/02/apg.png 256w" sizes="(max-width: 150px) 100vw, 150px" />](https://guardianproject.info/wp-content/uploads/2010/02/apg.png)Now that you have a working repo, its time to improve the security. Generating a repo in place is very easy, that is why this HOWTO started there, but it is not as secure as it should be if your repo is going to be your main distribution point. When generating the repo in place, make sure that `config.py` is not accessible via the web, since it contains passwords. If the file permissions are correct (e.g. `chmod 0600 config.py`), then `config.py` will not be readable by the webserver. But the signing keys will still be that public server. To improve this situation, generate the repo on a non-public machine like your laptop, keeping `config.py` and the keystore only on that machine, then use `fdroid server update` to publish the changes to your repo on a separate server. You just need to set `serverwebroot` in `config.py` properly, then `fdroid server update` will do the publishing via rsync over ssh. So both computers will have to have ssh and rsync installed and setup.

You can also use your own existing signing key rather than the one generated by `fdroid init`, just edit `repo_keyalias`, `keystore`, `keystorepass`, `keypass`, and `keydname` in `/usr/share/nginx/www/fdroid/config.py`

Since we like Tor and its Hidden Services for providing privacy, we also want to setup an F-Droid repository that is accessible over a Tor Hidden Service aka onion address. This will be covered in a future HOWTO.