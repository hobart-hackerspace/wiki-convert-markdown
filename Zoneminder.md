# Zoneminder
From [Wikipedia](https://en.wikipedia.org/wiki/ZoneMinder):

> ZoneMinder is a free, open-source software application for monitoring via closed-circuit television - developed to run under Linux and FreeBSD and released under the terms of the GNU General Public License (GPL).
>
> Users control ZoneMinder via a web-based interface. The application can use standard cameras (via a capture card, USB, FireWire etc.) or IP-based camera devices.[3] The software allows three modes of operation:[4]
>
>  - monitoring (without recording)
>  - recording after detected movement
>  - permanent recording

# Our usage
Brian is trying Zoneminder (on Mark's suggestion) as a way of capturing and storing video from 
the Axis cameras that Trent provided. 
One camera in particular is being trialed - in the container to allow monitoring of the CNC machine.

When set up it will be interconnected to Home Assistant.

# Setup
The software is set up in a Docker container on the `hhs-docker-svr` machine.

Its web interface is accessible via port `7009` (one higher than the wiki). So: [http://192.168.2.2:7009](http://192.168.2.2:7009) Currently that's not set up in `nginx` with a doman name nor exposed outside the LAN.

The container uses [Zoneminder-base](https://github.com/zoneminder-containers/zoneminder-base) as its image souce.

## Server files and user
The user-id `camera-user` was created on the server and given the `sudo` and `docker` groups. Pasword is in the vault.

A directory `/home/camera-user/zoneminder/` was placed at the user's top level and is used as working directory for all files.

## Installation
The container was installed per [the instructions on Github](https://github.com/zoneminder-containers/zoneminder-base#how).
In particular:

- The files `.env` and `docker-compose.yml` were downloaded into the working directory.
- Minimal changes were made to the files:
	- One change to `.env`:
	```
	❯ diff env*
	5c5
	< TZ=America/Chicago
	---
	> TZ=Australia/Hobart
	>
	```
	- And one to `docker-compose.yml`:
	```
	❯ diff docker-compose*
	26c26
	<       - 80:80
	---
	>       - 7009:80
	>
	```
	- We have to adjust the port number because `wikmd` is already exposed at port `80` via `nginx`.
	


