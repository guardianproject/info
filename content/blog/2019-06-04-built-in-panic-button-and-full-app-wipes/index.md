---
title: 'PanicKit 1.0: built-in panic button and full app wipes'
author: Hans-Christoph Steiner
categories:
  - Development
  - News
tags:
  - Android
  - calyxos
  - fdroid
  - panic
  - panic button
  - panicbutton
  - panickit
  - prototype
  - replicant
  - ripple
  - security
---

Panic Kit is 1.0!  After over three years of use, it is time to call
this stable and ready for widespread use.

{{< gallery >}}

## Built-in panic button

This round of work includes a new prototype for embedding PanicKit
directly into Android.  Android 9.0 Pie introduced a new "lockdown"
mode which follows some of the patterns laid out by PanicKit.  There
is an _Enter lockdown_ button available on the power button menu, so
it is rapidly available.  This is a great panic trigger button, so we
made a prototype of a System Settings app that lets users connect the
full flexibility of PanicKit responses to this _Enter lockdown_
button.  The functionality that Google links to this new button is
extremely limited, it seems to be a [one time restriction on how you
login](https://www.androidpolice.com/2018/03/08/android-p-feature-spotlight-new-lockdown-option-power-menu-turns-off-fingerprint-unlocking-something-called-extended-access/).
The PanicKit responses are in addition to what Google
included. CalyxOS is
[working](https://gitlab.com/calyxos/calyxos/issues/72) to integrate
this, look for test releases soon!


## Full wipes of selected apps

[F-Droid v1.7-alpha1](https://f-droid.org) has alpha support for
uninstalling and wiping all data from selected apps in response to a
panic trigger, including Ripple and F-Droid.  So the whole panic setup
could be wiped as part of the response.  It is essential to have a
complete, tested backup before trying this new feature, since it will
delete all of the data for each app that is uninstalled.

This requires [F-Droid Privileged
Extension](https://f-droid.org/packages/org.fdroid.fdroid.privileged.ota)
be installed on the device, in order to uninstall apps without a
prompt for each app.  Android ROMs like CalyxOS, CopperheadOS,
Fairphone Open, Replicant, and Lineage-for-microG all include F-Droid
Privileged Extension.


## Ripple is polished up

Ripple also received some modernization and polish.  Google has
reinstated the Ripple app in Google Play, so it is again widely
available.  Ripple was of course available the whole time via F-Droid.
Google suspended Ripple without explanation, then a long while later
reinstated it without explanation.

This work was made possible in part from donations from Handshake Foundation.
