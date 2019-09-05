---
id: 13901
title: 'Wind: Code, Libraries and Work So Far'
date: 2017-11-15T20:45:38-04:00
author: n8fr8
layout: page
guid: https://guardianproject.info/?page_id=13901
---
You can find our Github repo for the project here: <https://github.com/guardianproject/wind>

&nbsp;

We have created a tool to simulate a variety of scenarios to understand how quickly information can move through a community, based on different physical configurations, speed, distance and density. Here are a few examples:

&nbsp;

“GriffeyNet” portable WindBox:https://rawgit.com/jcushman/windviz/master/windviz.html?nodes=SimpleNode(.5,.5)|WaypointNode([[.15,.85],[.5,.7],[.85,.15],[.5,.7]],3)|SimpleNode(.2,.7)|SimpleNode(.1,.9)|SimpleNode(.3,.9)|SimpleNode(.8,.1)|SimpleNode(.7,.3)|SimpleNode(.9,.3)</p> 

</a>“Causeway”: WindChime Peer-to-Peer Communication https://rawgit.com/jcushman/windviz/master/windviz.html?nodes=WaypointNode([[.01,.2],[.99,.2],0],2.1)|WaypointNode([[.01,.4],[.99,.4],0],1.1)|WaypointNode([[.01,.6],[.99,.6],0],2.9)|WaypointNode([[.01,.8],[.99,.8],0],1.9)|WaypointNode([[.99,.1],[.01,.1],0],1.9)|WaypointNode([[.99,.3],[.01,.3],0],3.1)|WaypointNode([[.99,.5],[.01,.5],0],2.2)|WaypointNode([[.99,.7],[.01,.7],0],1.2)|WaypointNode([[.99,.9],[.01,.9],0],1.5)</p> 

</a>“Temple”: A mobile user accessing multiple WindBox static instances, sharing WindReports https://rawgit.com/jcushman/windviz/master/windviz.html?nodes=SimpleNode(.5,.5)|SimpleNode(.5,.1)|SimpleNode(.5,.9)|SimpleNode(.1,.3)|SimpleNode(.1,.7)|SimpleNode(.9,.3)|SimpleNode(.9,.7)|WaypointNode([[.5,.4],[.5,.15],[.85,.3],[.85,.7],[.5,.85],[.15,.7],[.15,.3]],4)</p> 

</a>And of course the original lots of random people approach: [https://rawgit.com/jcushman/windviz/master/windviz.html?nodes=RandomNode()|RandomNode()|RandomNode()|RandomNode()|RandomNode()|RandomNode()|RandomNode()|RandomNode()|RandomNode()|RandomNode()](https://rawgit.com/jcushman/windviz/master/windviz.html?nodes=RandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode()%7CRandomNode())

You can play with our javascript simulation tool in real-time here: <https://jsfiddle.net/2L0ffqfL/3/>

* * *

<span style="font-weight: 400;">It is important to clearly point out that our entire approach to this effort is to incrementally improve upon existing efforts, while also focusing on developing the new integration glue necessary to provide a smooth, usable and practical to deploy experience. We are not inventing a new stack or protocol from scratch, or envisioning a utopian silo in which our systems solves all of the potential problems end-to-end. The issue that we see is that there are many potential components, protocols or software libraries that exist today, but that they have not been unified into a cohesive, usable experience that promotes easy deployment, bootstrapping and adoption. Work in the past by others has also run out of “fuel”, both human and financial, and there was no focus on sustainability or maintenance of the project with a long term view.  We seek to address these by building upon a large body of excellent work that needs to be weaved together in a new way, and extended to provide a cohesive solution for the off-grid disaster scenario. We will do this primarily through partnership, collaboration and leadership.</span>

&nbsp;

<span style="font-weight: 400;">There are also still a significant amount of complex engineering tasks to complete. While we our proud of our community and user-centered work, it would not matter if we could not fulfill that promise with our ability to solve technical problems and ship usable applications. Our existing work on nearby communication features and code libraries has been significant over the last few years. We deeply understand the potential and limitations of technologies like Bluetooth LE, Wifi P2P, Wifi Hotspots, Beacons and more. Our ability to delivery systems that are both usable, and also include advanced security and privacy features, is also critical to any system that is targeted at vulnerable user populations. Finding a way to both promote widespread adoption of a new alternative network topology and applications, while also providing privacy and security capabilities within, is one of the key problems to solve.</span>

&nbsp;

<span style="font-weight: 400;">Within our Wind prototype, we propose to design and implement a system that includes the following components:</span><span style="font-weight: 400;"></p> 

<p>
  </span>
</p>

<ul>
  <li style="font-weight: 400;">
    <b>Wind Chime:</b><span style="font-weight: 400;"> A delay-tolerant peer-to-peer protocol, and core apps such as messaging and mapping that support it, to enable the flow of messages, knowledge and data within and between users and communities.</span><span style="font-weight: 400;"> 
    
    <p>
      </span></li> 
      
      <li style="font-weight: 400;">
        <b>Wind Store:</b><span style="font-weight: 400;"> A decentralized software and content distribution system built upon the Debian repository model, but made available through usable mobile app and web user experiences.</span><span style="font-weight: 400;"> 
        
        <p>
          </span></li> 
          
          <li style="font-weight: 400;">
            <b>Wind Box:</b><span style="font-weight: 400;"> Physical infrastructure nodes built from common routers and lower-power computing platforms, that provide gathering points for providing services, sharing content and discovering other users.</span><span style="font-weight: 400;"> 
            
            <p>
              </span></li> 
              
              <li style="font-weight: 400;">
                <b>Wind Report:</b><span style="font-weight: 400;"> An eyewitness testimony and verifiable multimedia evidence capture system, that allows anyone to gather and report on recovery and relief efforts, interviews refugees and victims, and capture incidents of corruption and abuse of power.</span>
              </li></ul> 
              
              <p>
                <b><br /> </b><b>Wind Chime</b><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;">Chime is a delay-tolerant peer-to-peer protocol, and core apps such as messaging and mapping that support it, to enable the flow of messages, knowledge and data within and between users and communities.</span><span style="font-weight: 400;"></p> 
                
                <p>
                  </span>
                </p>
                
                <ul>
                  <li style="font-weight: 400;">
                    <span style="font-weight: 400;">Discovery</span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;">Chime provides a way for users and applications to be aware of their proximity to services and users. This is achieved through a combination of existing broadcast and discovery technologies in Bluetooth and Wifi, emerging specifications like AltBeacon, and new Wind-oriented approaches sharing GPS place and time data between nodes in motion.</span>
                  </li>
                </ul>
                
                <p>
                  &nbsp;
                </p>
                
                <p>
                  <span style="font-weight: 400;">The AltBeacon specification defines the format of the advertisement message that Bluetooth Low Energy proximity beacons broadcast. The AltBeacon specification is intended to create an open, competitive market for proximity beacon implementations. The AltBeacon specification is free for all to implement, with no royalty or fees. AltBeacon does not favor one vendor over another for any reason other than the technical standards compliance of a vendor's implementation.</span>
                </p>
                
                <p>
                  &nbsp;
                </p>
                
                <ul>
                  <li style="font-weight: 400;">
                    <span style="font-weight: 400;">Sharing</span>
                  </li>
                </ul>
                
                <p>
                  &nbsp;
                </p>
                
                <p>
                  <span style="font-weight: 400;">Built on our current LibNearbyShare Android library, the Sharing features of Chime simplifies the discovery of other devices currently nearby, and enables a secure channel for transferring a set of data or media to them. It attempts to unify all possible nearby network technologies under a simple, clean interface that any developer can implement without too much trouble or overhead. This library does not require any Internet connection, cloud service, or other centralized method for discovering peers. All detection is done purely using the signals being broadcast by devices themselves. It unifies access to Bluetooth, WiFi LAN/NSD sharing, and Wifi P2P Sharing. We are also investigating adding additional methods for discovery and sharing, including audio-based discovery using ultrasonic and audible tones, QR code bootstrapping, WiFi Hotspot auto-setup, NFC and more.</span>
                </p>
                
                <p>
                  <span style="font-weight: 400;"></p> 
                  
                  <p>
                    </span>
                  </p>
                  
                  <ul>
                    <li style="font-weight: 400;">
                      <span style="font-weight: 400;">Messaging Protocol</span>
                    </li>
                  </ul>
                  
                  <p>
                    &nbsp;
                  </p>
                  
                  <p>
                    <span style="font-weight: 400;">Wind Chime also offers delay-tolerant peer-to-peer messaging support through the Murmur (formerly known as “Rangzen” protocol). Messages are spread directly from one device to another (forming a delay-tolerant peer-to-peer network) without user intervention using Bluetooth and WiFi Direct. The more devices the faster the message spreads and if no device is around, the message is queued in the feed to be sent later. Users control their anonymity and decide what information to share. Lastly, Connection Scores help users filter spam messages and Restricted Messages limit the audience to their friends. It is also:</span><span style="font-weight: 400;"></p> 
                    
                    <p>
                      </span>
                    </p>
                    
                    <ul>
                      <li style="font-weight: 400;">
                        <span style="font-weight: 400;">Infrastructure Independent: A mobile mesh that easily scales without compromising users’ safety</span>
                      </li>
                      <li style="font-weight: 400;">
                        <span style="font-weight: 400;">Trustworthy: Leveraging social connections to resist attack and infiltration</span>
                      </li>
                      <li style="font-weight: 400;">
                        <span style="font-weight: 400;">Private: Providing strong anonymity guarantees to users to preserve their privacy</span><span style="font-weight: 400;"> 
                        
                        <p>
                          </span></li> </ul> 
                          
                          <p>
                            <span style="font-weight: 400;">Murmur was implemented originally by the Denovo Group, following the tenets laid down in the UC Berkeley EECS research paper called “Rangzen: Circumventing Government-Imposed Communication Blackouts”: </span><a href="https://www2.eecs.berkeley.edu/Pubs/TechRpts/2013/EECS-2013-128.pdf"><span style="font-weight: 400;">https://www2.eecs.berkeley.edu/Pubs/TechRpts/2013/EECS-2013-128.pdf</span></a>
                          </p>
                          
                          <p>
                            &nbsp;
                          </p>
                          
                          <ul>
                            <li style="font-weight: 400;">
                              <span style="font-weight: 400;">Core Applications</span>
                            </li>
                          </ul>
                          
                          <p>
                            &nbsp;
                          </p>
                          
                          <p>
                            <span style="font-weight: 400;">The Wind prototype will feature number of Chime-enabled apps, including a mobile messaging app, a mapping application, a news app, and the updated Wind Store (F-Droid) and Wind Report (Proofmode) apps. All of these apps will be optimized for offline and off-grid use, and make the users aware of opportunities to share, collaborate and connect with users, services and resources around them.</span>
                          </p>
                          
                          <p>
                            &nbsp;
                          </p>
                          
                          <p>
                            <span style="font-weight: 400;"><br /> </span><b>Wind Store</b>
                          </p>
                          
                          <p>
                            &nbsp;
                          </p>
                          
                          <p>
                            <span style="font-weight: 400;">Store is decentralized software and content distribution system similar to the Debian repository model, but made available through a mobile app and distributor toolkit. It is built upon our work on the F-Droid open-source project. For an off-grid or disaster scenario, designing systems to both distribute and keep software updated is a critical linchpin for both onboarding and security of the entire system. Wind Store will be powered by F-Droid, enhanced with support for Chime, and fully tested to work in off-grid scenarios with Wind Box hosted repositories. Chime supports will also improve the capability of the F-Droid Nearby “App Swap” feature, that allows any devices to become an app store themselves, offering any app or content to nearby friends over Bluetooth or Wifi.</span>
                          </p>
                          
                          <p>
                            <span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;">The F-Droid.org site offers a repository of FOSS apps, along with an Android client to perform installations and updates, and news, reviews and other features covering all things Android and software-freedom related. It is an installable catalogue of FOSS (Free and Open Source Software) applications for the Android platform. The client makes it easy to browse, install, and keep track of updates on your device.</span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;">With the Repomaker tool of F-Droid, everyone can create their own repo. So whether you are a musician who wants to publish their music or a developer who wants to serve nightly builds of their app, you are free to create your own repo and share it with other people independently of F-Droid.org. In the past, creating a repo has been difficult because you had to have knowledge on the command line, needed to edit text files to edit your packages’ store details and had to paste screenshots in a special system of directories to have them served well inside the F-Droid app. This all got easier now: with Repomaker, you are able to create your own repo and do not need to have any special knowledge to do so.</span>
                          </p>
                          
                          <p>
                            <span style="font-weight: 400;"></p> 
                            
                            <p>
                              </span>
                            </p>
                            
                            <p>
                              <b>Wind Box</b>
                            </p>
                            
                            <p>
                              <span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;">Wind Boxe provides physical infrastructure nodes built from common routers and lower-power computing platforms, that provide gathering points for providing services, sharing content and discovering other users. The Box component will be built primarily upon the excellent LibraryBox system, but expanded to support the Chime protocol for improved nearby discovery and messaging, as well as Store, for hosting software and content repositories.</span>
                            </p>
                            
                            <p>
                              &nbsp;
                            </p>
                            
                            <p>
                              <span style="font-weight: 400;">LibraryBox (</span><a href="http://librarybox.us/"><span style="font-weight: 400;">http://librarybox.us/</span></a><span style="font-weight: 400;">) is an open source, portable digital file distribution tool based on inexpensive hardware that enables delivery of educational, healthcare, and other vital information to individuals off the grid. LibraryBox v2.0 is a combination of a router (a variety of hardware will work), USB drive, and software that, when combined, give you a small, low powered webserver. The webserver acts like a captive portal, and delivers files that are stored on the USB drive. To use LibraryBox, you simply connect to the wifi SSID "LibraryBox" and launch a browser. Attempting to visit any webpage will push you to the LibraryBox homepage on the device, which has information about the project, and links on the menu for downloads. You can browse the contents of the Shared folder, and download any files you'd like.</span>
                            </p>
                            
                            <p>
                              &nbsp;
                            </p>
                            
                            <p>
                              <span style="font-weight: 400;">At our Wind Farm event hosted in 2015, we initially experimented with deploying F-Droid app repositories on a mid-range LibraryBox. In 2016, we deployed multiple LibraryBox with digital security training content and app repositories at a large cultural gathering in India with 100,000 attendees. The devices were displayed prominently with QR Codes, “tap to use” NFC Stickers, and others information about how to bootstrap into the system. Once the user was connected once to the unique Wifi SSD used by our LibraryBox, they would then auto-connect to another other similarly configured Box deployed at these events. At Wind Farm, we deploy a number of boxes throughout the Harvard campus, and enabled content uploading so that users could submit photos, videos recording and other reports of our simulation event, as it was occurring.</span>
                            </p>
                            
                            <p>
                              &nbsp;
                            </p>
                            
                            <p>
                              <span style="font-weight: 400;">In both cases, these were powered by a large external battery capable of running for one to multiple days. Power usage is dependent upon the number of users of the system, and the amount of data stored and transferred from the device. Multiple batteries could also be paired with generators or solar capture to extend the availability. </span>
                            </p>
                            
                            <p>
                              &nbsp;
                            </p>
                            
                            <p>
                              <span style="font-weight: 400;">The portability of a Box can vary depending upon the size and capacity of the box itself, the batteries it is using, and the way in which power is generated for it. LibraryBox are often both carried in people’s backpacks for opportunistic sharing in meetings, conferences, cafes, subways and so on, but they are also installed in permanent locations like libraries, schools and lobbies. We also see great possibilities in hosting Boxes in buses, trains and trucks that have a regular, predictable path between towns, cities and other regions. These can act as a backbone of content, synchronized between any Chime-enable Box or app, as they encounter each other. The flexibility of the Box approach, and the work with what you have mentality, make it an appropriate and useful component within our prototype for the off-grid challenge.</span>
                            </p>
                            
                            <p>
                              &nbsp;
                            </p>
                            
                            <p>
                              <b>Wind Report</b><b></p> 
                              
                              <p>
                                </b>
                              </p>
                              
                              <p>
                                <span style="font-weight: 400;">Report provides an eyewitness testimony and verifiable multimedia evidence capture system, that allows anyone to gather and report on recovery and relief efforts, interviews refugees and victims, and capture incidents of corruption and abuse of power</span>
                              </p>
                              
                              <p>
                                &nbsp;
                              </p>
                              
                              <p>
                                <span style="font-weight: 400;">We have been working for many years with our partners at WITNESS, a leading human rights media training and advocacy organization, to figure out how best to turn smartphone cameras into tools of empowerment for activists. We have also contributed to Benetech’s Martus platform, the leading human rights reporting and data gathering tool. While it is often enough to use the visual pixels you capture to create awareness or pressure on an issue, sometimes you want those pixels to actually be treated as evidence. This means, you want people to trust what they see, to know it hasn’t been tampered with, and to believe that it came from the time, place and person you say it came from.</span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;"><br /> </span><span style="font-weight: 400;">Proofmode is a light, minimal “reboot” of our more heavyweight, verified media app, CameraV. Our aim was to create a lightweight (< 3MB!), almost invisible utility (minimal battery impact!), that you can run all of the time on your phone (no annoying notifications or popups), that automatically adds extra digital proof data to all photos and videos you take. This data can then be easily shared, when you really need it, through a “Share Proof” share action, to anyone you choose over email or a messaging app, or uploaded to a cloud service or reporting platform.</span>
                              </p>
                              
                              <p>
                                &nbsp;
                              </p>
                              
                              <p>
                                <span style="font-weight: 400;">Wind Report would integrate our work on the ProofMode app and service with Wind Chime and Wind Box. Adding Chime capability will allow evidence to be notarized and shared between many people in an area, without require any network infrastructure. Wind Box will be expanded to support the submission of Report generated evidence, building in chain-of-custody features, as well as a workflow for aggregating and delivering the reports to the necessary authorities and organizations.</span>
                              </p>
                              
                              <p>
                                &nbsp;
                              </p>
                              
                              <p>
                                <span style="font-weight: 400;">We believe these are the kinds of applications that are essential to not only Wind succeeding from a technical and product perspective, but for the community themselves to have the support and services needed for relief, recovery and healing.</span>
                              </p>
                              
                              <p>
                                &nbsp;
                              </p>
                              
                              <p>
                                <b>Access, Reach and Capacity</b><b></p> 
                                
                                <p>
                                  </b>
                                </p>
                                
                                <p>
                                  <span style="font-weight: 400;">A Windy network or application can operate at many different scales. In some cases, people in a rural community may find value in accessing a shared WindBox hosted at their relief center that has been brought from the city. On it might be news and entertainment, that they can download and store on their own personal devices. There may only be 10 people a time using it, with perhaps a few hundred throughout the day. Thus, at this scale, we are talking about helping hundreds of people, through one Wind deployment, in a static physical location.</span>
                                </p>
                                
                                <p>
                                  &nbsp;
                                </p>
                                
                                <p>
                                  <span style="font-weight: 400;">When you begin to consider larger instances of WindBox, or multiple boxen, combined with apps and devices that speak WindChime, and can share apps and content through WindStores, the potential scale of users connecting and benefiting from the windy network increases dramatically. A medium to large portable WindBox can host communication, serve content, and provide software to a few hundred simultaneous users. Each of those users can then continue on their way, with the content and communications they have exchanged with the WindBox. Through WindChime, they will continue to discover others around them, on the bus, in the square, at the hospital, in line for services, that they can exchange knowledge with. Some of these people they might know, and some they may be connected through interest in a topic or some other shared connection. In this collective scenario, where you have multiple large WindBox in motion, each connecting to hundreds of users, who then each connect to ten to a hundred users around them as they move through their town or city, the reach and impact grow exponentially.</span>
                                </p>
                                
                                <p>
                                  &nbsp;
                                </p>