Our internet connection is provided by Launtel. It is an FTTN service (100/20), about to be replaced by a fibre connection. Base service speed will be 100/20 but it will be upgradeable on a daily basis to much higher speeds as required.

The credentials to connect to the Launtel management page are in [the password vault](Password vault).

The internet IP address of the space is `144.48.164.114`. This is a static IP address so is unlikely to change unless we change our NBN RSP. 

There is also an IPv6 prefix: `2404:e80:fef::/48`. (IPv6 addresses are being allocated but no relevant ports are exposed yet.)

The firewall device is a [Ubiquiti Router & WiFi controller](WiFi7_upgrade). Connect to it from within the Space at [`192.168.2.1`](http://192.168.2.1). (Credentials in [the vault](Password vault).) Its managaement page is accessible from the WAN by logging into [Ubiquiti Unifi](https://unifi.ui.com/).

[Ubiquiti Router & WiFi controller](WiFi7_upgrade)

# Static IP assignments and exposed IP ports
Some of the devices in our LAN are given reserved IP addresses, rather than receiving a random address from the DHCP server. This is done for some to ensure a consistent IP address to allow NATing an external port to that device, so that it can provide member services (such as updating this wiki) or to allow maintenence or security services. For others it is a way of ensuring a consistent, specific address for device control or device-device interaction.

## [IP address reservations](IP_address_leases)

## [Externally exposed hosts](Exposed_ports)
