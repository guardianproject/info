---
title: "Serving Websites Privately Over Tor Onion Services (From Your Laptop!)"

author: Shanzay, Summer Intern

categories:
   - Onions
   
tags:
   - privacy
   - circumvention
   - censorship
   - tor

---

In this day and age when our data is consistently being tracked and profited off of, sharing information safely and securely is difficult. However, that does not necessarily mean that all network services are subject to such scrutiny. Users now have the ability to combine the security of HTTPS with the privacy benefits of Tor Browser and share information through Tor’s anonymous network services – [Onion Services](https://community.torproject.org/onion-services/). By using an onion service, users can hide their location while active, connect to other Tor users, and retain their privacy throughout. But to do so, one needs to know how to set up an Onion Service. 

While the following instructions are specific to a Mac, with minor differences this can be applied to other devices and systems. 

## Step 1 → Download and Set Up the Tor Service

While there are multiple ways to download and set up tor, the simplest is to follow the instructions at https://torproject.org/download/ that goes along with the operating system you are using. 

For further information, you can follow the Tor installation guide: https://community.torproject.org/onion-services/setup/install/

Once you have successfully downloaded tor, to check if tor is running you can either open the browser and establish connection or use commands to check its success:
```
/opt/homebrew/bin/brew services start tor
/opt/homebrew/bin/brew services stop tor
```
Please note, in this step you are running the tor service on your machine to host the onion server. In later steps, we will be using the Tor Browser app to view the site remotely. 


## Step 2 → Download and Set Up a Web Server (Optional during Development, but required for Production)

In order to set up a website or some content for a client to access, we need to set up a local web server. A web server is the computer software and underlying hardware that communicates with a web browser using HTTP to distribute web pages to the client who requested it, with local web server examples including Apache and Nginx. The reason for this is that when it comes to the finished product, you can copy the fields into the apache web directory and that would be your web server 

However, for websites that we are building on npm, as npm has its own built in web server for development, it has its own local host web server ready. Hence, we can just point our hidden service web server at that, for testing and development. Once we arrive at production, we will use the apache or another web server to host our local service.

To install these web servers on MacOS can be difficult, so specifically for this operating system, it is best to install (or update) the homebrew package, which will then allow you to run the following command:
```
/opt/homebrew/bin/brew install apache
```

If you have having trouble choosing a local web server or downloading it, a useful guidance tool is: https://www.javatpoint.com/how-to-install-apache-on-mac

The default location where web servers run is on https://localhost:80. Hence, once you have downloaded the web server software, to check if it is working, open your browser and go to https://localhost:80. If you have successfully downloaded the web server software, you will be notified of this success. 

For further steps, or multiple uses you may need to start or stop the web server software which can be done using the following commands:
```
sudo apachectl start
sudo apachectl stop
```


## Step 3 → Modify your Tor Configuration File 

In order to create the onion service link, you must mody the the tor configuration file (torrc) by adding the following lines and save the changes:
```
HiddenServiceDir /var/lib/tor/my_website/
HiddenServicePort 80 127.0.0.1:80
```

The HiddenServiceDir line is to inform tor of where to save the onion v3 service link, hence you must modify this line to point to a file whose permissions include both readable and writable. 
The HiddenServicePort line is informing Tor of the port people visiting your Onion Service will be using, which is currently set as localhost. 

While the torrc file is saved in different places depending on the operating system being used, for MacOS, the file can be found at this filepath:
```
 /Library/”Application Support”/TorBrowser-Data/Tor/ 
```


## Step 4 → Create the Hidden Service Folder (Optional)

While this step is not necessary, doing this reduces the chance of problems later on. 

Once you have modified your tor configuration file, you should create the HiddenServiceDir directory where Tor will create the hostname file, which will contain your new onion v3 service address. For MacOS, this file should be created in the tor folder which can be found with this file path:
```
HiddenServiceDir /opt/homebrew/etc/tor/
```

The folder should be given the permissions to allow tor to read and write to it, which can be done by calling:
```
filename chmod 700 
```


## Step 5 → Restart Tor and Check for the Onion Service Link

Once you have restarted Tor, it should have created the file hostname with the new onion v3 service in the directory which you pointed it to with the HiddenServiceDir line in your torrc.
If it has not, potential areas to check for faults are:
- The HiddenServiceDir directory’s file permissions
- If Tor was properly restarted 
- The torrc file modifications and if there are any incorrect file paths or mistakes 
- The log files which you can find using https://support.torproject.org/#Logs


## Step 6 → Test Your Onion Service 

If you have successfully acquired your onion service link, you can then run it on Tor and it should direct you to the page which has been initially configured on apache (the same page we saw at localhost:80). If not, potential problems could include:
- Your web server software is no longer running and needs to be started 
- The page is found at a different port 
- One important thing to remember is that once you have gotten your onion address, a new one will not be generated, this is your permanent link whose content can be manipulated. 


## Step 7 → Build the File/Web Page Being Used

Once your onion service link is up and running, it is now time to display on it the html files you intend to share. To do so, if the files are a Node app or a progressive web app, and not a static html page or website, it is important to build the code first by running: 
```
npm run build 
```

A potential problem could be that when you run a web service, especially a Node app or a progessive web app, it renders links for the domain it thinks it is at, not the one you intend it to be at. For a typical static website it wouldn't matter because it is a static set of pages; however, when using a live node application, it's helpful to know what the public address is. 

To fix this problem, to your code you should add the following line which points directly to your new onion service address, like the example here:
```
public:’2xx7phs7hw5fduqulcrthkmfaesxbsy5om5xpkpsn4y54mnbj4b6ekd.onion’
```
 

## Step 8 → Run the File and Test your Onion Service  

1- For this step, there are two potential methods depending on the type of content you intend to display on your Onion Service. For html documents or simple websites, the simplest method to run the file is to copy it into the folder which localhost:80 (or whichever port you are using) is connected to. For MacOS, the folder can be found at:
```
/Library/WebServer/Documents
```

To copy, the command to run is:
```
sudo cp /path/from /path/to
```

Once that is done, simply restart your Tor browser, head to your new onion service address and your html file can be found there. 


2- To run a Node app or progress website, first the file needs to be running on your local server. To do so, one tip is to specify the port you intend to run it on, especially other ports that are running other websites or html content. For that, run the following command (changing it to point to the port you are using):
```
npm run service – –port 4000
```

To connect to this npm web server on port 4000 instead of apache, we need to modify the onion service configuration in the torrc:

```
HiddenServicePort 80 127.0.0.1:4000
```

## Accessing the Onion site

Once the website is running on localhost at the port you have specified, restart your Tor service. Then, navigate to your new onion service address where your website is now live for all the people you have shared your secure link with. You can use any Tor-enabled browser, such as [Tor Browser for Desktops](https://www.torproject.org/download/), [Tor Browser for Android](https://www.torproject.org/download/), or [Onion Browser for iOS](https://onionbrowser.com) devices. You can also use a Tor-enabled vpn like [Orbot for Android and iOS](https://orbot.app), to allow any browser, like Chrome or Brave, to access an onion address.










