# Basics
## Server

[[info]] Server setup

- We're using the previous "hhs-security" machine that sits in the "server" rack. (A small Lenovo desktop box.)
- The OS was re-installed, using Ubuntu version 24.04 LTS on a clean file system.
	- some apps were installed at OS load time but later removed. These were installed as "snap" installations by the OS installer. Doco on `docker` installation strongly recommends against installing with snap, so it, `mosquitto` and `microk8s` were removed. 
	- Problems had been encountered with docker across some reboots. This cleanup seems to have resolved that.
- Base machine has hostname `hhs-docker-svr` and responds as `hhs-docker-svr.lan`
- Initially, just one user was set up: `hhs-admin`, with [password in our vault](Password vault). (To start with, it is the usual "spacehackers@#".)
- SSH service was enabled to provide admin access. Authorized_keys can be added as required for convenience.
- Installed `avahi-daemon` and `avahi-utils` with `apt`. 
	This enables an internal HHS network address of `hhs-docker-svr.local`, and sets us up to do a fiddle to allow addressing as `wiki.local`. See [URL Adjustments](#URL_Adjustments) below.

## Docker software

[[info]] Base Docker

- Installed `docker` and `portainer`. 
- Docker is installed with `apt`, after adding the relevant `apt` config stuff:
```
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor \
		-o /usr/share/keyrings/docker-archive-keyring.gpg
	echo "deb [arch=$(dpkg --print-architecture) \
		signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
		$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt update
	sudo apt-get install docker-ce docker-ce-cli containerd.io
	sudo systemctl status docker
	sudo docker run hello-world
```
- Noting that the last bits ("run hello-world" & "status docker") are checks that it worked ok

- Then we installed `portainer`:
```
	sudo docker volume create portainer_data
	sudo docker volume inspect portainer_data  # ( a check step )
	sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always \
		-v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data \
		portainer/portainer-ce:latest
	sudo docker ps # should show it running
```
- Connecting to `https://hhs-docker-svr.local:9443` with a browser should show the portainer web GUI
	- On first connection from a given browser, the browser may warn about insecure connections - this is because the certificate is locally-generated. Over-ride the warning.
	- On first connection after (re)installation, Portainer will ask for an admin user to be created and a password supplied. The password to use is in the [vault](Password vault). (While testing it's simply: "spacehackers@#").

- Add the linux user to the `docker` group to avoid the need for `sudo` all the time:
```
	sudo usermod -aG docker hhs-admin
```

- Then we need a user-id on the docker server as owner of the wiki. This is to avoid permissions issues and to make it easy to work at the filesystem level for backup etc:
	- User is "wiki-user"; password in [the vault](Password vault).
```
	sudo adduser wiki-user
	# and add it to the "sudo" group
	sudo usermod -aG sudo wiki-user
	sudo usermod -aG docker wiki-user
```

- Now we're set up to install our wiki. 
	- (In fact, this took a few trials. If you're interested, you can follow [the history here](Wiki%20software%20trial%20installations) ).

## The working wiki installation
- [See here for details of our working wiki...](The Wikmd server)

<a id="URL_Adjustments"></a>

## URL Adjustments

[[info]] Simpler URLs

The above is sufficient to get us up and running, but for convenience sake some networking "adjustments" have been made to provide for simpler URLs.

The basic networking setup gives us page URLs of the form `http://hhs-docker-host:7008/` which is not very memorable. A couple of additions give us much easier-to-remember addresses:

1. An `mDNS` alias to allow a hostname of the form `wiki.local`
1. A reverse proxy to pass requests on port 80 to whichever actual port the wiki uses, so our address ia simply `http://wiki.local/`

### mDNS alias
We're already running `mDNS`, so it's a simple enhancement to call `avahi-publish-address` to provide an alternate address. The command `avahi-publish-address` has to be running for the address to be active, so we run it as a service. `avahi-publish` was installed as part of `avahi-utils`. The guide for doing this came from a ['Painfully Obvious' post](https://andrewdupont.net/2022/01/27/using-mdns-aliases-within-your-home-network/).

The service file is `/etc/systemd/system/wiki-mdns-cname.service`. Its contents are:

~~~ ini
[Unit]
Description=Avahi/mDNS CNAME publisher
After=network.target avahi-daemon.service
PartOf=avahi-daemon.service

[Service]
User=wiki-user
Group=wiki-user
Type=simple
WorkingDirectory=/tmp/
ExecStart=/usr/bin/avahi-publish-address  -R wiki.local 192.168.2.2
Restart=no
PrivateTmp=true
PrivateDevices=true

[Install]
WantedBy=multi-user.target
~~~


The service is activated by the commands:

~~~ bash
sudo systemctl enable wiki-mdns-cname
sudo systemctl start wiki-mdns-cname.service && sudo journalctl -u wiki-mdns-cname -f
~~~

### Reverse proxy
`Nginx` is used to provide a reverse proxy service. A longer-term aspiration is to use it to provide authenticated access from ourside our local network.

`Nginx` was installed with: `sudo apt install nginx` 
and an appropriate config file created in `/etc/nginx/sites-available/wiki.conf`, containing:

~~~ nginx
server {
  listen 80;      # for IPv4
  listen [::]:80; # for IPv6

  server_name wiki.local wiki.hobarthackerspace.org.au;
  access_log /var/log/nginx/wiki.log;

  location / {
	proxy_pass http://hhs-docker-svr.local:7008;

	proxy_set_header Host            $host;
	proxy_set_header X-Real-IP       $remote_addr;
	proxy_set_header X-Forwarded-For $remote_addr;
	proxy_http_version 1.1;

	proxy_set_header Upgrade $http_upgrade;
	proxy_set_header Connection "upgrade";
	proxy_cache_bypass 1;
	proxy_no_cache 1;

	port_in_redirect on;
  }
}
~~~

The config file was linked from the `sites-available` directory and `nginx` restarted:

~~~ bash
cd ../sites-enabled
sudo ln -s ../sites-available/wiki.conf .
sudo systemctl restart nginx && sudo journalctl -u nginx -f
~~~