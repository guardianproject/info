---
id: 2820
title: 'ToFU/PoP in your Android App!  (a.k.a. extending Orlib to communicate over Tor)'
date: 2012-09-20T15:17:36-04:00
author: harlo
layout: post
guid: https://guardianproject.info/?p=2820
permalink: /2012/09/20/tofupop-in-your-android-app-a-k-a-extending-orlib-to-communicate-over-tor/
categories:
  - HowTo
  - Research
---
In doing my research for InformaCam, I learned a couple of neat tricks for getting an app to communicate over Tor. Here&#8217;s a how-to for app developers to use depending on your threat model, and how you have your web server set-up. Enjoy, and please post your comments/questions/suggestions below&#8230;

## Before we begin&#8230;

You&#8217;re going to need some basic stuff up-and-running for this to work. Before you get coding, make sure you have the following:

**Your Android device should have:**

  * Orbot downloaded and running
  * An encrypted data store to save keys, certificates, and addresses to, such as Guardian Project&#8217;s <a href="https://github.com/guardianproject/sqlcipher-android" target="_blank">SQLCipher</a> or <a href="https://github.com/guardianproject/IOCipher" target="_blank">IOCipher</a>. (SQLCipher is a database; if you want to have records for each hidden service such as &#8220;Onion Address,&#8221; &#8220;Certificate,&#8221; &#8220;Display Name,&#8221; etc. this is the model you can use. IOCipher is used like an encrypted java.io.File partition; you could easily store certificates in a java keystore with a .jks extension, and save a text file with a list of onion addresses. However you manage your backend is up to you.)

**Your server should have:**

  * A lightweight web server. According to the Tor documentation, smaller servers like LightTPD are preferred over Apache since there&#8217;s less of an opportunity to accidentally reveal your IP address in error logs or publicly-accessible config files.
  * Tor set up and running a hidden service
  * Your own self-signed SSL certificate for your server. (Directions can be found <a href="http://www.digicert.com/ssl-certificate-installation-lighttpd.htm" target="_blank">here</a>)
  * _For extra credit,_ you can set yourself up your own certificate authority. This can be used to sign client authentication keys (how you distribute them to users is also up to you) and directions to do this can be found <a href="http://it.toolbox.com/blogs/securitymonkey/howto-securing-a-website-with-client-ssl-certificates-11500" target="_blank">here</a>.

## Ok, let&#8217;s get coding!

  1. **Use case: I don&#8217;t actually need Tor support, but I do want to add my custom SSL certificate to the app&#8217;s trust chain.**</p> 
    What you need to do this is to create a custom Trust Manager, and use it when you instantiate your SSL connection. 
    
    In this example, the trust manager loads (or creates, if it&#8217;s the first time use) your encrypted keystore. When your app makes a request to your web server, the Trust Manager will first check to see if the host name is in your &#8220;white list&#8221; (either in your SQLite database or in the encrypted flat file you created.) If that checks out, the Trust Manager will add the X509 certificate to your encrypted keystore (if it doesn&#8217;t exist there already.) I&#8217;ve omitted the part of the code where you load up your keystore, and where you save any changes to it; you can do that on your own, depending on how you have it set up.
    
    The following code I cribbed heavily from <a href="https://github.com/ge0rg/MemorizingTrustManager" target="_blank">ge0rg&#8217;s memorizing trust manager</a>. Please have a look at that, too, and thank the guy for his great work!
    
    <pre style="font-size:0.8em;">public class MyTrustManager implements X509TrustManager {
	private KeyStore keyStore;
	private X509TrustManager defaultTrustManager;
	private X509TrustManager appTrustManager;
		
	byte[] keyStored = null;
	String pwd;
	
	public MyTrustManager() {
		loadKeyStore();
		
		defaultTrustManager = getTrustManager(false);
		appTrustManager = getTrustManager(true);
	}
	
	private X509TrustManager getTrustManager(boolean withKeystore) {
		try {
			TrustManagerFactory tmf = TrustManagerFactory.getInstance("X509");
			if(withKeystore)
				tmf.init(keyStore);
			else
				tmf.init((KeyStore) null);
			for(TrustManager t : tmf.getTrustManagers())
				if(t instanceof X509TrustManager)
					return (X509TrustManager) t;
		} catch (KeyStoreException e) {
			Log.e(LOG, "key store exception: " + e.toString());
		} catch (NoSuchAlgorithmException e) {
			Log.e(LOG, "no such algo exception: " + e.toString());
		}
		return null;
	}
	
	private void loadKeyStore() {
		//TODO: this is where you load up your keystore and store the bytes into the keyStored field if neccessary.
		try {
			keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
		} catch(KeyStoreException e) {
			Log.e(LOG, "key store exception: " + e.toString());
		}
		
		try {
			keyStore.load(null, null);
			if(keyStored != null)
				keyStore.load(new ByteArrayInputStream(keyStored), pwd.toCharArray());
			
			
		} catch(CertificateException e) {
			Log.e(LOG, "certificate exception: " + e.toString());
		} catch (NoSuchAlgorithmException e) {
			Log.e(LOG, "no such algo exception: " + e.toString());
		} catch (IOException e) {
			Log.e(LOG, "IOException: " + e.toString());
		}
	}
	
	private void storeCertificate(X509Certificate[] chain) {
		try {
			for(X509Certificate cert : chain) {
				keyStore.setCertificateEntry(cert.getSubjectDN().toString(), cert);
			}
		} catch(KeyStoreException e) {
			Log.e(LOG, "keystore exception: " + e.toString());
		}
		
		appTrustManager = getTrustManager(true);
		try {
			ByteArrayOutputStream baos = new ByteArrayOutputStream();
			keyStore.store(baos, pwd.toCharArray());
			updateKeyStore(baos.toByteArray());
			Log.d(LOG, "new key encountered!  length: " + baos.size());
		} catch(KeyStoreException e) {
			Log.e(LOG, "keystore exception: " + e.toString());	
		} catch (NoSuchAlgorithmException e) {
			Log.e(LOG, "no such algo exception: " + e.toString());
		} catch (IOException e) {
			Log.e(LOG, "IOException: " + e.toString());
		} catch (CertificateException e) {
			Log.e(LOG, "Certificate Exception: " + e.toString());
		}
	}
	
	private void updateKeyStore(byte[] newKey) {
		// TODO: this is where YOU update your own keystore if you need to (ie, if it's in an SQLite database)
	}
	
	private boolean isCertKnown(X509Certificate cert) {
		try {
			return keyStore.getCertificateAlias(cert) != null;
		} catch(KeyStoreException e) {
			return false;
		}
	}
	
	private boolean isExpiredException(Throwable e) {
		do {
			if(e instanceof CertificateExpiredException)
				return true;
			e = e.getCause();
		} while(e != null);
		return false;
	}
	
	private void checkCertificateTrusted(X509Certificate[] chain, String authType, boolean isServer) throws CertificateException {
		try {
			if(isServer)
				appTrustManager.checkServerTrusted(chain, authType);
			else
				appTrustManager.checkClientTrusted(chain, authType);
		} catch(CertificateException e) {
			if(isExpiredException(e))
				return;
			if(isCertKnown(chain[0]))
				return;
			
			try {
				if(isServer)
					defaultTrustManager.checkServerTrusted(chain, authType);
				else
					defaultTrustManager.checkClientTrusted(chain, authType);
			} catch(CertificateException ce) {
				storeCertificate(chain);
			}
		}
	}

	@Override
	public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
		checkCertificateTrusted(chain, authType, false);
	}

	@Override
	public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
		checkCertificateTrusted(chain, authType, true);
	}

	@Override
	public X509Certificate[] getAcceptedIssuers() {
		return defaultTrustManager.getAcceptedIssuers();
	}
	
}
</pre>
    
    Next, you want to initiate an Https request to use this custom Trust Manager. As most of you Android programmers know, you have to do any network stuff on another, non-UI thread. I like to use Future/Callables because it returns the contents of the web site you access into a variable that I can parse. Here&#8217;s how you do that for a standard POST request:
    
    <pre style="font-size:0.8em;">public static String executeHttpsPost(final String host, final Map&lt;String, Object> postData, final String contentType) {
		ExecutorService ex = Executors.newFixedThreadPool(100);
		Future&lt;String> future = ex.submit(new Callable&lt;String>() {
			String result = "FAIL";
			String HYPHENS = "--";
			STRING LINE_END = "\r\n";
			String BOUNDARY = "***7hisIsMyBoUND4rY***";
			String hostname;
			
			URL url;
			HttpsURLConnection connection;
			HostnameVerifier hnv;
			DataOutputStream dos;
			SSLContext ssl;
			
			MyTrustManager itm;
			
			private void buildQuery() {
				Iterator&lt;Entry&lt;String, Object&gt;&gt; it = postData.entrySet().iterator();
				
				connection.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + BOUNDARY);
				StringBuffer sb = new StringBuffer();
				try {
					dos = new DataOutputStream(connection.getOutputStream());
					sb = new StringBuffer();
					while(it.hasNext()) {
						sb = new StringBuffer();
						Entry&lt;String, Object&gt; e = it.next();
						
						sb.append(HYPHENS + BOUNDARY + LINE_END);
						
						sb.append("Content-Disposition: form-data; name=\"" + e.getKey() + "\"" + LINE_END);
						sb.append("Content-Type: " + contentType + "; charset=UTF-8" + LINE_END );
						sb.append("Cache-Control: no-cache" + LINE_END + LINE_END);
						sb.append(String.valueOf(e.getValue()) + LINE_END);
						dos.writeBytes(sb.toString());
					}
					
					dos.writeBytes(HYPHENS + BOUNDARY + HYPHENS + LINE_END);
					
					dos.flush();
					dos.close();
					
				} catch (IOException e) {
					Log.e(LOG, e.toString());
					e.printStackTrace();
				}
			}
			
			@Override
			public String call() throws Exception {
				hostname = host.split("/")[0];
				url = new URL("https://" + host);
								
				hnv = new HostnameVerifier() {
					@Override
					public boolean verify(String hn, SSLSession session) {
						if(hn.equals(hostname))
							return true;
						else
							return false;
					}
				};
				
				itm = new MyTrustManager();
								
				ssl = SSLContext.getInstance("TLS");
				ssl.init(null, new TrustManager[] {itm}, new SecureRandom());
				
				HttpsURLConnection.setDefaultSSLSocketFactory(ssl.getSocketFactory());
				HttpsURLConnection.setDefaultHostnameVerifier(hnv);
				
				connection = (HttpsURLConnection) url.openConnection();
				
				connection.setRequestMethod("POST");
				connection.setRequestProperty("Connection", "Keep-Alive");
				connection.setUseCaches(false);
				connection.setDoInput(true);
				connection.setDoOutput(true);
				
				buildQuery();
				
				try {
					InputStream is = connection.getInputStream();
					BufferedReader br = new BufferedReader(new InputStreamReader(is));
					String line;
					StringBuffer sb = new StringBuffer();
					while((line = br.readLine()) != null)
						sb.append(line);
					br.close();
					connection.disconnect();
					result = sb.toString();
				} catch(NullPointerException e) {
					Log.e(LOG, e.toString());
					e.printStackTrace();
				}
				return result;
			}
			
		});
		
		try {
			return future.get();
		} catch (InterruptedException e) {
			Log.e(LOG, e.toString());
			e.printStackTrace();
			return null;
		} catch (ExecutionException e) {
			Log.e(LOG, e.toString());
			e.printStackTrace();
			return null;
		}
	}
</pre>

  2. **Use case: I have a web server set up with a hidden service running. How can my app access the web site?**</p> 
    Simple! Just make some minor modifications to your SSLContext by adding a proxy! Take the executeHttpsPost method above, and add the following _after_ the line &#8220;HttpsURLConnection.setDefaultHostnameVerifier(hnv);&#8221;
    
    <pre style="font-size:0.8em;">Proxy proxy = new Proxy(Proxy.Type.HTTP, new InetSocketAddress("localhost", 8118));
</pre>
    
    Then, change your declaration of connection to:
    
    <pre style="font-size:0.8em;">connection = (HttpsURLConnection) url.openConnection(proxy);
</pre>
    
    So, as long as your device is also running Orbot (Tor) you can do the same POST over Tor! </li> 
    
      * **Use case: I have a web server that requires client authentification. How can I add a client certificate to the SSL context?**</p> 
        To do this, you&#8217;re going to need to add a KeyManager to your SSLContext. As I stated before, getting your client auth key to your app users is up to you (bluetooth, NFC, sneakernet???) but once it&#8217;s in there, and visible to your app, install it by adding your own custom KeyManager. In my testing, I added this method below to the MyTrustManager class, simply because it already had access to my encrypted keystore. But you can ostensibly place this anywhere:
        
        <pre style="font-size:0.8em;">public X509KeyManager[] getKeyManagers(byte[] kBytes, String clientCertificatePassword, String keystorePassword) {
	KeyManagerFactory kmf = null;
	KeyManager[] km = null;
	X509KeyManager[] xkm = null;

	try {
		kmf = KeyManagerFactory.getInstance("X509");
			
		KeyStore xks = KeyStore.getInstance("PKCS12");
			
		ByteArrayInputStream bais = new ByteArrayInputStream(kBytes);
		xks.load(bais, keystorePassword.toCharArray());
				
		kmf.init(xks, clientCertificatePassword.toCharArray());
		km = kmf.getKeyManagers();
		xkm = new X509KeyManager[km.length];
				
		for(int x=0;x&gt;km.length;x++) {
			X509KeyManager k = (X509KeyManager) km[x];
			xkm[x] = k;
		}

	} catch (NoSuchAlgorithmException e) {
		Log.e(LOG, e.toString());
		e.printStackTrace();
	} catch (UnrecoverableKeyException e) {
		Log.e(LOG, e.toString());
		e.printStackTrace();
	} catch (KeyStoreException e) {
		Log.e(LOG, e.toString());
		e.printStackTrace();
	} catch (IOException e) {
		Log.e(LOG, e.toString());
		e.printStackTrace();
	} catch (CertificateException e) {
		Log.e(LOG, e.toString());
		e.printStackTrace();
	}
	return xkm;
}
</pre>
        
        Finally, when you instantiate your SSLContext for your POST request, include the returned value of the getKeyManager method as the KeyManager parameter. So, replace this line:
        
        <pre style="font-size:0.8em;">ssl.init(null, new TrustManager[] {itm}, new SecureRandom());
</pre>
        
        with this:
        
        <pre style="font-size:0.8em;">X509KeyManager[] x509KeyManager = getKeyManager(kBytes, clientCertificatePassword, keystorePassword);
ssl.init(x509KeyManager, new TrustManager[] {itm}, new SecureRandom());
</pre></ol> 
    
    That&#8217;s it! Good luck hacking, hackers&#8230;