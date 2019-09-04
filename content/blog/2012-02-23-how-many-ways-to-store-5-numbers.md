---
id: 1562
title: How many ways to store 5 numbers?
date: 2012-02-23T12:29:49-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=1562
permalink: /2012/02/23/how-many-ways-to-store-5-numbers/
categories:
  - Development
tags:
  - dsa
  - encryption
  - keys
  - otr
  - psst
---
At the core of all software that aims to be secure, private and anonymous is encryption, or as I think of it, amazing math tricks with really large numbers. These really large numbers can serve as a token of identity or the key to information locked away behind the encryption math. There are a number of different encryption methods commonly used based on different mathematical ideas, but they all rely on people managing sets of really large numbers, usually known as keys.

[<img src="https://farm4.staticflickr.com/3589/3378152784_2be2969ae6.jpg" alt="Skeleton Keys IMG_0774" width="500" height="333" />](http://www.flickr.com/photos/stevendepolo/3378152784/ "Skeleton Keys IMG_0774 by stevendepolo, on Flickr")

It turns out that managing these sets of really large numbers can be tricky to do well, so there are all manner of key management apps and approaches. On top of that, there seems to be decades of people wanting to make their own formats for these sets of really large numbers. So if you want to work directly with the keys themselves, you not only have to sort out the difference between the kinds of numbers used in DSA, RSA, Elliptical Curve, etc., but you will also have to figure out which of the many many formats those numbers are stored in. There are base64 formats, hex formats, standardized binary formats with names like PKCS#8/DER and X.509, old formats like S-Expressions (sexp) as well as non-standard formats like keyczar’s JSON format that uses web-safe base64. Then, there are different ways of reading and writing those different formats into a file.

We started out working on the particular problem of translating the 5 numbers (x, y, p, q, g) used in DSA keys. DSA keys are used for OTR encryption, and we want to make it possible to translate the DSA key information stored by one OTR messaging app into the format used by others. Here are three examples of storing DSA keys:

_(In general, its a very bad idea to post private keys anywhere at all public. These three are private keys that have been generated for test purposes)_

libotr private key from Pidgin (sexp with hex numbers):

> (account  
> (name “&#x67;p&#x74;&#x65;s&#x74;@j&#x61;bb&#x65;r.&#x6f;rg/”)  
> (protocol prpl-jabber)  
> (private-key  
> (dsa  
> (p  
> #00CD96479A2F404FB600F9C85EE3DCD69FDF93F217AEE54A1286069983BA7731D0C73C7CB3B8CFA482A0AF6FF906E470EB4EF7F4D201D087AEDBF0086710F3039CBF42358C1BFA7D86A36332E21D32BE31538571CBC8D4F281DDD1076BA2B29B549ED29B3C19C341AEF83C80157E87FF2930B5E15C84A09AFCE28A06E06A62BCEF#)  
> (q #00D5B4647E688974D1B6B199E1A59AB2F985DBCE01#)  
> (g  
> #0093E333135FCBCE68FC6E410B304482F2F95D82BF53534C3636EADB0C22241CF35BD294B096070DC08138EFE73B03C88FD444595974E9455274F695147AF9D46B85286B4CFEF3D00BCA1D3BEB8C7EFFBA08132E1A1E4D9F115B863C52C72971F4695758354FC3BE3C4A45AF6A47747B59733905C33EE86ED68D9D90494877AE33#)  
> (y  
> #362C06B9CDD67FC4E7A7A62289D6C1E8BA061A024946A5ACC1A7DC70F6B03D99A1D3B3215D20BC4F8458EEC3F31E1391E9B519FDCDCC3CF0FBA38F8A7213551B32D59DE655F506633FB6B0EA94C4174D227DB614EF6723AB057B40CF36E2A414D0A8DCF223EE7EDD851793C4DC92282C79503030045D49A0ABCC3C6CC4080909#)  
> (x #24FE542B1C7DC8337F6F8030C7D639B7BF091B40#)  
> )  
> )

otr4j private key from Gibberbot (PKCS#8 DER with ASCII armor, escaped for Java Properties):

> &#x67;p&#x74;es&#x74;@&#x6a;ab&#x62;e&#x72;.o&#x72;g&#x2e;&#x70;r&#x69;va&#x74;e&#x4b;ey=MIIBSgIBADCCASsGByqGSM44BAEwggEeAoGBAMtPbcgvf2CAHN4djUb+gCPw/e8Xpeyc9GknS9zs\nJjSCg9vgiKBVlQBceiKAkK8SVVEaA671SS0XO575OK/sAc4j0n2t9QJP1wyGCOhV79WbwhPPEVhs\ncpAHakr9IAW6WdSnwhL/seZLYRKiVGpxXJffwN+sYjH00PulKNxmz2+DAhUAxh9yFSC1uuGk6IR0\ntnVAfsPUt7cCgYBGfHU40n0HgKIkVe3XtX0G3CbiGbR++qaEjNqnfWynggqeeVkYliLaDlVrR4B0\nnLrHZLEcUMO38YKmrwug02acp9P65IcjZ2yaioPBSmV7R6pMGOdJFR3V7Pd5R2+NcUdJd2xSffLf\nrChM82SKqa7b3DOPHkSoIdp/vJiRgikZrwQWAhRE5snYBaoR84hWVdxlumAYkBRUEA\=\=

private key from keyczar (JSON with websafe base64):

> {  
> “publicKey”: {  
> “q”: “AJJfsQZrhUV8p6TmpPqa084JwX9j”,  
> “p”: “AIAAAAAAAAXxHhQxJRZ-PPj2BDrHHLV8c8pX6nyOLAW3Bc7CX\_SfBiGH2VyImoz6JlAOZi6x\_XspxdUvpTjV7J9uO9hwnF31m3SQjdkZW2DQDb5OS1rW\_4MGrTJCktKtlZz7f8\_5AoO8yHSY2XWNDqrpBEiNvaTX1ttQ59nREiR1”,  
> “y”: “AGlQuRpbat4drE\_fcdSZrEVfS6Fme3tNfUoJVRec1pUhoSo9PBHKFx3lbBmI8Vnub8vuY1nM2yTadOZ8H4-TYxB5JNMVTK7vLNdVcWvUUF9zRZCwps1bl0\_Al29X0I1iQYJN6Klxi\_QbKaSf5PhfXLVom9bJYp7\_TwZCouaab296”,  
> “g”: “AES5hk-DKXP\_\_t6yDsXIdykf7lhSKHqQCW5H2V5dMg8JkoFBSP7mIvaCHT4IxoxdM2AIpWgcoi5XSrd\_hD2sjNa1JHTb9BUh31dHJLym6rTsV12ClN6f78Cjt0oKFIRI\\_\_yWn9KM-vLEsjpd10VHlPfbEgKYePCnXFt7Y78G0wGr”,  
> “size”: 1024  
> },  
> “x”: “AGLJry5Q0CZo9cH6XRYd2ZZZppwg”,  
> “size”: 1024,  
> }

There are many instant messaging (IM) apps that provide solid support for the OTR chat encryption protocol. Many people use the same IM account across multiple computers and programs, but this generally causes lots of headaches when using OTR. One technique for eliminating these headaches is to use the same private OTR key across all programs and computers, but since each program has a different file format, this is hard to setup. In order to address this issue, we first mapped out the key and file formats for a number of the most widely used OTR programs (Pidgin, Adium, Gibberbot, Jitsi, irssi). As part of the [OTRFileConverter project](https://github.com/guardianproject/otrfileconverter), we have written parsers for these file formats, and are close to being able to convert between all of them. These parsers not only convert the private keys for each account, but also the known public keys of remote accounts as well as their verified status. In this process, we discovered a fundamental incompatibility in the otr4j library used in Gibberbot, Jitsi, beem-otr, and other software. Fortunately, it should be possible to fix the otr4j library itself and all the software based on it should have the issue transparently fixed by including the updated otr4j.

Coming soon, OTRFileConverter will be able to sync all of your key information between Pidgin and Gibberbot, so that means private keys, other people’s public keys, and whether those keys have been manually verified, or verified via the Socialist Millionaire’s Protocol (SMP).

Track our progress at: <https://github.com/guardianproject/otrfileconverter>