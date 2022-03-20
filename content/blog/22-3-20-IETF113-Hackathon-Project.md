---

title: IETF113 Hackathon Project

author: David

categories:

   - Standards

tags:

   - standards development

   - IETF

   - privacy

---

*This post begins a daily blog, live from IETF113 in Vienna Austria, March 19-25, 2022 (first in-person meeting after six remote-only meetings during the COVID pandemic).*

The [Hackathon](https://www.ietf.org/how/runningcode/hackathons/113-hackathon/) event kicks off IETF and, at this meeting,  we picked up work originally done by one of our teammates implementing version 5 of [Internet Draft HTTP Transport Authentication](https://www.ietf.org/archive/id/draft-schinazi-httpbis-transport-auth-05.html). *_HTTP Transport Authentication* _is designed to authenticate such protocol flows in a manner that does not reveal any information to an attacker during failure cases.  Therefore, applications using *_HTTP Transport Authentication*_ are resistant to active probing by network adversaries. 

We got the original code running in Google Conscrypt (TLS for Java/Android), verified its function (as defined in the Internet Draft) and created a public open source repository with a demonstration capability. We presented the work to Hackathon attendees (~50 people) and discussed the work with the specification’s author.

Here’s the specification for HTTP Transport Authentication [Internet Draft](https://www.ietf.org/archive/id/draft-schinazi-httpbis-transport-auth-05.html).  Here’s our  implementation [repository](https://github.com/guardianproject/HTTPTransportAuthentication).
