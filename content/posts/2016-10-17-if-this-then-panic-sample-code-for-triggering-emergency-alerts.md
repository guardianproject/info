---
id: 13423
title: '&#8220;If This, Then Panic!&#8221; Sample Code for Triggering Emergency Alerts'
date: 2016-10-17T09:55:22-04:00
author: n8fr8
layout: post
guid: https://guardianproject.info/?p=13423
permalink: /2016/10/17/if-this-then-panic-sample-code-for-triggering-emergency-alerts/
publish_post_category:
  - "5"
publish_to_discourse:
  - "1"
discourse_post_id:
  - "456"
discourse_permalink:
  - https://talk.developersquare.net/t/if-this-then-panic-sample-code-for-triggering-emergency-alerts/330
discourse_comments_count:
  - "3"
discourse_comments_raw:
  - '{"id":330,"posts_count":4,"filtered_posts_count":4,"posts":[],"participants":[{"id":213,"username":"mu22le","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/mu22le/{size}/235_1.png"},{"id":19,"username":"gpadmin","avatar_template":"https://avatars.discourse.org/v2/letter/g/d07c76/{size}.png"},{"id":9,"username":"n8fr8","avatar_template":"https://discourse-cdn-sjc2.com/standard16/user_avatar/talk.developersquare.net/n8fr8/{size}/19_1.png"}]}'
discourse_last_sync:
  - "1553085413"
wpdc_sync_post_comments:
  - "0"
image: http://guardianproject.info/wp-content/uploads/2016/10/9c96b071463f74e8567536dde06b1591.jpg
categories:
  - Development
  - HowTo
tags:
  - panic button
  - panickit
---
Earlier this year, we announced the [PanicKit Library for Android](https://guardianproject.info/2016/01/12/panickit-making-your-whole-phone-respond-to-a-panic-button/) and [Ripple](https://dev.guardianproject.info/news/257), our basic app for alerts any compatible app that you are in an emergency situation. Rather than build a solitary, enclosed &#8220;panic button&#8221; app that only can provide a specific set of functionality, we decided, as we often do, to build a framework, and encourage others to participate. Since then, we&#8217;ve had [over 10 different apps implement PanicKit r](https://dev.guardianproject.info/projects/panic/news)esponder functionality, including Signal, OpenKeyChain, Umbrella app, StoryMaker and Zom.

It is great to have so many apps implement helpful features for users to react during an emergency situation. This might include sending an emergency message, putting sensitive data behind a password, hiding the app icon, or even wiping data. All of this can be triggered by a simple tap and swipe on the Ripple&#8217;s app user interface.

However, we would like to promote PanicKit trigger functionality that goes beyond something a user has to actively do, or at least obviously do. In many emergency scenarios, the user might be unable to actively trigger a panic, because they are unconscious, detained or have had their device taken away. In some cases, the activation may need to be subtle, such typing an incorrect phone number. In others, rapidly pressing a button or shaking the phone, may be safer and easier than unlocking your device and using an app.

<img class="alignnone size-thumbnail" src="https://media.giphy.com/media/K673Q5D4KGWAg/giphy.gif" alt="" width="738" height="415" /> 

_a truly panic-inducing situation_

PanicKit works by connecting trigger apps with receiver apps. Triggers are what create the alert that there is an emergency or panic situation. Responders receive the alert, and take an appropriate, user configured or default action.

The new [PanicKitSamples project](https://github.com/n8fr8/PanicKitSamples) demonstrates new possible triggers that could be implemented in an app like Ripple, or any app that wishes to do so. In the [&#8220;info.guardianproject.fakepanicbutton.triggers&#8221;](https://github.com/n8fr8/PanicKitSamples/tree/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers) package, you will find the following classes:

[BaseTrigger](https://github.com/n8fr8/PanicKitSamples/blob/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers/BaseTrigger.java#L40): a base class that handles launching of the &#8220;panic intent&#8221; from a set of stored preferences to trigger the responders

<pre>public static void launchPanicIntent (Context context)
{
    final SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context.getApplicationContext());

    String email = prefs.getString("email",null);
    String phone = prefs.getString("phone",null);
    String subject = prefs.getString("subject","panic message");
    String message = prefs.getString("message","i triggered a panic!");

    launchIntent(context, email, phone, subject, message);
}

public static void launchIntent (Context context, String emailAddress, String phoneNumber, String subject, String message)
{
    final PackageManager pm = context.getPackageManager();
    final Set&lt;String&gt; receiverPackageNames = PanicTrigger.getResponderActivities(context);

    Intent intent = new Intent(Panic.ACTION_TRIGGER);</pre>

&nbsp;

[GeoTrigger](https://github.com/n8fr8/PanicKitSamples/blob/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers/GeoTrigger.java): Using the awesome &#8220;LOST&#8221; open-source geofencing library, this trigger sends a panic if the device moves outside of a pre-defined area (in this sample, it is Times Square NYC)

<pre>private void setupGeoFence ()
{

    //setup geofence for Times Square area
    String requestId = "geof1-timesSquare";
    double latitude = 40.758896;
    double longitude = -73.985130;
    float radius = 0.0001f;

    Geofence geofence = new Geofence.Builder()
            .setRequestId(requestId)
            .setCircularRegion(latitude, longitude, radius)
            .setExpirationDuration(Geofence.NEVER_EXPIRE)
            .build();

    GeofencingRequest request = new GeofencingRequest.Builder()
            .addGeofence(geofence)
            .build();</pre>

&nbsp;

[MediaButtonTrigger](https://github.com/n8fr8/PanicKitSamples/blob/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers/MediaButtonTrigger.java): This trigger will notice multiple rapid pushes of a headset mic button or a bluetooth mic call button, and send a trigger.

<pre>public class MediaButtonTrigger extends BaseTrigger {

    private static int mTriggerCount = 0;
    private final static int TRIGGER_THRESHOLD = 3;

    private static long mLastTriggerTime = -1;

    public MediaButtonTrigger(Activity context)
    {
        super (context);
    }

    @Override
    public void activateTrigger() {

        //if a headset button or a bluetooth "call" button is pressed, trigger this

        IntentFilter filter = new IntentFilter(Intent.ACTION_MEDIA_BUTTON);
        MediaButtonIntentReceiver r = new MediaButtonIntentReceiver();
        getContext().registerReceiver(r, filter);


    }

    public class MediaButtonIntentReceiver extends BroadcastReceiver {

        public MediaButtonIntentReceiver() {
            super();
        }

        @Override
        public void onReceive(Context context, Intent intent) {

            KeyEvent event = (KeyEvent)intent.getParcelableExtra(Intent.EXTRA_KEY_EVENT);
            if (event == null) {
                return;
            }

            int action = event.getAction();
            if (action == KeyEvent.ACTION_DOWN) {

                //check for 3 rapidly pressed key events

                long triggerTime = new Date().getTime();

                //if the trigger is the first one, or happened with a second of the last one, then count it
                if (mLastTriggerTime == -1 || ((triggerTime - mLastTriggerTime)&lt;1000))
                    mTriggerCount++;

                mLastTriggerTime = triggerTime;

                if (mTriggerCount &gt; TRIGGER_THRESHOLD) {
                    launchPanicIntent(context);
                    mTriggerCount = 0;
                }


            }
            abortBroadcast();
        }
    }
}</pre>

[PhoneNumberTrigger](https://github.com/n8fr8/PanicKitSamples/blob/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers/PhoneNumberTrigger.java) (OutgoingCallReceiver): This trigger monitors phone calls, looking for a pre-defined fake &#8220;panic number&#8221;.

<pre>public class OutgoingCallReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {

        String phoneNumber = intent.getStringExtra(Intent.EXTRA_PHONE_NUMBER);

        if (phoneNumber != null
                && phoneNumber.equals(PhoneNumberTrigger.PHONE_NUMBER_TRIGGER)) {
            PhoneNumberTrigger.launchPanicIntent(context);
        }

    }
}</pre>

[SuperShakeTrigger](https://github.com/n8fr8/PanicKitSamples/blob/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers/SuperShakeTrigger.java): This trigger looks for the phone being rapidly shaken. It could be expanded to wait for a series of shakes within a certain time window to avoid false positives.

<pre>//setup shake detection using ShakeDetector library
SensorManager sensorManager = (SensorManager) getContext().getSystemService(Context.SENSOR_SERVICE);

ShakeDetector sd = new ShakeDetector(new ShakeDetector.Listener()
{
    public void hearShake() {

        //you shook me!
        launchPanicIntent(getContext());

    }
});

sd.start(sensorManager);</pre>

[WifiTrigger](https://github.com/n8fr8/PanicKitSamples/blob/master/app/src/main/java/info/guardianproject/fakepanicbutton/triggers/WifiTrigger.java): This triggers waits for the user to connect to a specific wifi network (in this sample &#8220;Starbucks&#8221;). It could also be set to trigger if the devices leaves the wifi network.

<pre>NetworkInfo netInfo = intent.getParcelableExtra (WifiManager.EXTRA_NETWORK_INFO);
if (ConnectivityManager.TYPE_WIFI == netInfo.getType ()
        && netInfo.isConnected()) {

    WifiManager wifiManager = (WifiManager) context.getSystemService(Context.WIFI_SERVICE);
    WifiInfo info = wifiManager.getConnectionInfo();
    String ssid = info.getSSID();

    //Check if I am connected to the "trigger" SSID, and if so send an alert!

    if (!TextUtils.isEmpty(ssid)
        && ssid.equals(WIFI_SSID_TRIGGER))
    {
        launchPanicIntent(getContext());
    }
}</pre>

&nbsp;

All of these samples are configured to work with the FakePanicButton sample app, which allows you to choose a contact to alert, and set a panic message. That said, these are meant to point in a direction of functionality, and have not been fully debugged or tested on all devices and OS versions.

If you have more ideas on other panic triggers that could be implemented, please share them here. We are also happy to take pull requests or fixes to our sample project, in order to improve on the ideas we have. Finally, we will announce more Panic responder and trigger apps, as they are available in the coming months. We looking forward to the continued growth of our PanicKit ecosystem, though of course, we hope even more for a world where there are less reasons to panic.

## 

&nbsp;