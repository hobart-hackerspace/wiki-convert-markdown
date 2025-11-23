The Hackerspace has a number of internet domain names for different purposes.
We also have domain name records that are used as part of managiing these domains.
Most domains are registered and their records hosted and managed by [VentraIP](https://vip.ventraip.com.au/dashboard). 

One domain (`hobarthackerspace.onmicrosoft.com`) is separately managed, as part of our free NFP Microsoft365 subscription.

Relevant access credentials are in [the password vault](Password vault).

## The domain names 
### Base level names
- [`hobarthackerspace.org.au`](https://hobarthackerspace.org.au)
	- This is used for:
		- our website
		- our email addresses
		- and as a base address for more specific subdomains.
	- The website is hosted as a [**`pages.github.com`**](https://pages.github.com) service, so the **A** and **AAAA** records are set per [their specs for hosting web sites](https://docs.github.com/en/pages):
		- **A** (IPv4) records are set directing to:
			- `185.199.108.153`
			- `185.199.109.153`
			- `185.199.110.153`
			- `185.199.111.153`
		- **AAAA** (IPv6) records are set directing to:
			- `2606:50c0:8000::153`
			- `2606:50c0:8001::153`
			- `2606:50c0:8002::153`
			- `2606:50c0:8003::153`
		- These work in conjunction with a **CNAME** record for
			[`www.hobarthackerspace.org.au`](https://www.hobarthackerspace.org.au). 
			See below and [the pages.github.com specs](https://docs.github.com/en/pages).
	- There is also an **MX** record to identify where to send incoming email to addresses like 
		`joe.bloggs@hobarthackerspace.org.au`.
		- Incoming mail is handled as part of our free Microsoft365 subscription, 
			so it's set to priority `0` and redirects to
			`hobarthackerspace-org-au.mail.protection.outlook.com`
- `hobarthackerspace.com`
- `hobarthackerspace.org`
	- These are both secondary names, registered to prevent domain name poaching by others. 
		There are no current DNS records for them.
	- Both are registered with [VentraIP](https://vip.ventraip.com.au/dashboard)

### Subdomains used for other web-based access 
These all use **A** records  

- [`office.hobarthackerspace.org.au`](https://office.hobarthackerspace.org.au:8123/)
	- This gives access to our Home Assistant instance
		- An **A** record points to `100.67.51.201`,
			the current IP address for our NBN connection.
- [`wiki.hobarthackerspace.org.au`](http://wiki.hobarthackerspace.org.au:7008)
	- This gives access to this wiki from outside the space
		- An **A** record points to `100.67.51.201`,
			the current IP address for our NBN connection.
- [`cnc.hobarthackerspace.org.au`](https://cnc.hobarthackerspace.org.au)
	- This is a Shane special page hosting CNC documentation
		- An **A** record points to `103.13.100.230`,
			the IP address for Shane's NISS server.


### "Subdomains" registered to support specific services 
These are not actual reachable subdomains, rather they are DNS records that use the subdomain format to be reachable and authenticated.
Typically these are created on request for or on the recommendation of the provider of an external service.

- **CNAME** keys direct automated enquiries in relation to specific services to the actual source of that service, 
- **TXT** records hold cryptgraphic keys whose specific content demonstrates that we are owners of the domain.
- a few **SRV** records point to specific external service providers.

| Type | "Subdomain" | Required by | Contents | Params | Purpose
| :--- | ---: | :---: | :--- | :---: | :--- 
| CNAME | `autodiscover`  | MS Outlook app | `autodiscover.outlook.com` |  | Automatic configuration of MS Outlook 
| CNAME | `enterpriseenrollment` | Microsoft365 | `enterpriseenrollment.manage.microsoft.com` |  | Microsoft365 configuration stuff 
| CNAME | `enterpriseregistration` | Microsoft365 | `enterpriseregistration.windows.net` |  |  ditto
| CNAME | `k2._domainkey` | Mailchimp | `dkim2.mcsv.net` |  |  Used by Mailchimp to increase reliability of
| CNAME | `k3._domainkey` | Mailchimp | `dkim3.mcsv.net` |  |  delivery of emails sent from `hobarthackerspace.org.au` addresses
| CNAME | `mail` | Microsoft365  | `portal.microsoftonline.com` |  |  Yet more Microsoft365 configuratiion stuff
| CNAME | `msoid`  | Microsoft365 | `clientconfig.microsoftonline-p.net` |  |  ditto
| CNAME | `selector1._domainkey` | Microsoft365  | `selector1-hobarthackerspace-org-au._domainkey.hobarthackerspace.onmicrosoft.com` |  |  Microsoft365 email deliverability support
| CNAME | `selector2._domainkey` | Microsoft365  | `selector2-hobarthackerspace-org-au._domainkey.hobarthackerspace.onmicrosoft.com` |  |  ditto
| CNAME | `www` | Github Pages  | `hobarthackerspace.github.io` | TTL = 3600 |  Used by pages.github.com to redirect web pages
| TXT | `[no subdomain]` | All email agents | `"v=spf1 +a +mx +a:hosting.niss.net.au include:spf.protection.outlook.com include:mailgun.org -all"` |  |  Our SPF record. Lists the servers authorized to send emails from our domain
| TXT | `_dmarc` | All email servers | `"v=DMARC1; p=none"` |  |  Our (very open) DMARC policy. Tells other email servers how to handle mail might be spoofed. This is per Mailchimp specs.
| TXT | `mailo._domainkey` |  | `k=rsa; p=[redacted]` |  |  
| SRV | `_sipfederationtls._tcp` | Microsoft Teams | `10 25 5061 sipfed.online.lync.com` |  |  Used by Microsoft Teams as part of our Microsoft365 subscription

The text values of keys marked `[redacted]` above are held in our password vault
