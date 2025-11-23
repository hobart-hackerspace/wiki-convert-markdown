# Background
Quite some years ago we set up WiFi in the Hackerspace using two Ubiquiti Unifi access points. These were 2.4GHz only and were placed in the Tesla and Shannon rooms. They are now both slow and limited in features.

We purchased in May of this year a new Ubiquiti U7 (WiFi 7-capable) access point as part of an upgrade for the WiFi, with the intention of getting a second as soon as they came into stock. Leo set it up with the aid of a second device, a free-standing Controller that was surplus from Shane.

Since then the NBN connection has been upgraded, giving us access to both much higher up/download speeds and also to IPv6 addressing. The existing border router was at its limits with the speed and incapable of supporting IPv6. So, after consultation with Shane, we have purchased a Ubiquiti UX7 combined controller/router/WiFi7 access point.

# UX7 installation
The router and wifi aspects are listed separately below.

Our intention in setting it up has been to minimise the disruption to existing services and connections. Any future alterations to take advantage of the extra capabilities can be done in a staged manner.

## Router

- Before shutting down the old iiNet router, its screens listing static IP allocations and NATed ports were screencapped for historic documentation. These images are [linked here for the record](https://hobarthackerspace.sharepoint.com/:f:/s/Committee/ErThmBa3igFJnEpFVwAiV2IBXRpNJzWGirmj7rxSqaQlwA?e=EX2DHf).
- The UX7 includes a controller so the old free-standing controller was renamed `HackerspaceOld` so that we could give the `"Hackerspace"` name to the new one.
- The new router was set up with its uplink connected to the NBN connection box and its downlink connected to the 24-port Juniper switch. It is pyhsically sited on top of the Juniper box stack so that it isn't shielded by a metal cabinet.
- It was set up with this basic configuration:
	- Base IP address 192.168.2.1
	- WAN IP 144.48.164.114 (Link named `Launtel`)
	- DHCP IP address range 192.168.2.6 - 192.168.2.254
- A second IP subnet was set up by default (192.168.3.1/25)
	- this was left active but not in use.
	- It would be sensible to use it in conjunction with the 2.4GHz-only `hackerspace-iot` secondary wifi.
- Wherever possible, settings were left at default or set to "automatic"

### Static IP allocation
- The DHCP static leases that were on the iiNet router were replicated to the extent possible.
	- It wasn't obvious how to create static leases for devices that aren't active onthe network, so only those devices visible were given static leases.
	- We need to review the ones that didn't get set up to decide if they remain necessary

### Port forwarding
- Port forwarding was set up for most of the ports that had been configured on the iiNet router.
- Two that were no  longer in use were not set up:
	- A second`ssh` port to the docker server hosting the wiki and other stuff
	- An allocated port to an instance of `zoneminder` that Brian was trying for the camera in the container

## WiFi
The UX7 serves as both a WiFi access point and a controller for other access points. Both modes are in use.

### WiFi 7

- Both the UX7 access point and the U7 AP that we purchased earlier both support WiFi 7 (802.11be). This offers multi-gigabit throughput utilising RF in the 2.4, 5 and 6GHz bands. 
- These newer devices also support the WPA3 security features that were unavailable on the older APs. 
- Both APs have been set up to utilise any of the WiFi 7 features supported by connecting devices, but not to enforce their use that so that older devices can also connect. 
- Despite that flexibility, some of the more primitive IoT devices won't connect to WiFi 7 APs. It's become standard practice to provide a separate 2.4GHz-only SSID to obviate this and that's recommended by Ubiquiti. See [[#IoT Wifi]] below.

### Access point locations

- The UX7 is a desktop device and will sit in the Tesla room, in the networking cabinet. We can't, however, put it in a metal rack because of the shielding effects.
- The U7 is a wall/ceiling mount and will replace the earlier access point mounted on the wall in the large room (Claude Shannon/Ada Lovelace) as that is the space that often houses the most people.
	- That hasn't been tested yet, as that device needs a more powerful PoE injector than the earlier ones. Leo has obtained one and will install it this week.
- One of the older APs is destined for the container. This will ensure stable WiFi to the computers in there even when the door is closed.
- The other AP is up for suggestions. Any ideas?

### IoT Wifi

- Ubiquiti recommends having a 2.4GHz-only WiFi for IoT devices. This is confirmed by the observation that some of out IoT devices didn't connect until the old 2.4GHz access points were got working.
- So a second SSID –`hackerspace-iot` – was set up. This is 2.4GHz-only, with none of the later wifi capabilities enabled, so that the more basic devices don't get confused.
- We still have to migrate our IoT devices (things like the kitchen and outside lights and the Google Home audio devices that talk when we come in) to the new SSID. At the moment they are connecting via the old APs.

# Unresolved previous static IP leases

- Hackerprint - 192.168.2.20 - no device. 
	- Was this an old allocation no longer in use?
- Missing devices
	- Not visible on LANScan or Ubiquiti
		- Printercam - was 192.168.2.45
		- back-light - was 2.122
		- kitchen-light - was 2.196

# Static IP address leases and LAN ports opened

- [Addresses](IP_address_leases)
- [Port forwarding](Exposed_ports)

