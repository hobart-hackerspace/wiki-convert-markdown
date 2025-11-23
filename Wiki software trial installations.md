# Wiki software
- The software we're using is Wikimd. 
	- [Github repo](https://github.com/Linbreux/wikmd)
	- [Doco and installation instructions](https://linbreux.github.io/wikmd/)
- This is available as a python install (via `pip` or `git`) or as a docker container. 

# A dedicated user-id for the wiki
A username and home directory were set up to manage the wiki and house its files. The user was added to both the sudo and docker groups. The password was added to [our password vault](Password vault).

~~~ bash
# (logged in as hhs-admin)
sudo adduser wiki-user
sudo usermod -aG sudo docker wiki-user
~~~

# Docker first attempt
The first trial was a docker container.

- Log in to the server `ssh wiki-user@hhs-docker-svr.local`.
	- User is "wiki-user"; password in [the vault](Password vault).

- Make a storage space for it:
```
	docker volume create wiki_data
	docker volume inspect wiki_data  # ( a check step )
	sudo chown wiki-user /var/lib/docker/volumes/wiki_data \
		/var/lib/docker/volumes/wiki_data/_data
```

- For some reason the directory `/var/lib/docker` was not readble, preventing non-root access to anything below it. There seemed no reason for this as some of its sub-directories are world-readable, so this was adjusted.
```
	sudo chmod +x /var/lib/docker
	# this allowed:
	touch /var/lib/docker/volumes/wiki_data/_data/test
	rm /var/lib/docker/volumes/wiki_data/_data/test
```

- Ran a trial installation direct from the repository, [per the instructions](https://linbreux.github.io/wikmd/installation/docker.html), to avoid any issues:
```
	docker pull linbreux/wikmd
```
- With config as per the installation instructions with minimal changes:
```
sudo docker run -d \
  --name wikmd \
  -e TZ=Australia/Hobart \
  -e PUID=1002 \
  -e PGID=1002 \
  -e WIKMD_LOGGING=1 `#optional` \
  -p 7008:7008 \
  -v wiki_data:/wiki \
  --restart unless-stopped \
  linbreux/wikmd:latest
```

- **Which didn't work:-(**
- The docker installation failed initialisation:

```
ERROR in git_manager: New local repo initialization failed >>> Cmd('git') failed due to: exit code(128)
  cmdline: git checkout -b main
  stderr: 'fatal: detected dubious ownership in repository at "/wiki"
To add an exception for this directory, call:

git config --global --add safe.directory /wiki'
```

- In theory, it should be possible to get access to a shell in the working directory within the container while it is running, with: `docker exec -it wikmd /bin/bash`.
	But when that was tried, the response was:
```
OCI runtime exec failed: exec failed: unable to start container process: exec: "/bin/bash": stat /bin/bash: no such file or directory: unknown
```

- At this point, in order to expidite getting *something* going, the docker experiment was abandonned in favour of something else. All the docker stuff was removed so we can get a clean start again later.

# Wiki setup via *pip*
This was installed without docker, directly as the "wiki-user" user, within a virtual environment in which the app is installed with `pip`.

Setup process:
```
mkdir wikmd-pip
cd wikmd-pip
virtualenv venv
source venv/bin/activate
pip install wikmd
# (many lines of installation report)
wikmd # starts the app in this directory (note no config variables have been applied)
# then we can open a web page (which will be on the default port 5000)
```

- Which almost worked:-/

- One more "adjustment" was necessary -- the updating of `pandoc-xnos` to allow for later `pandoc` versions:
```
python -m pip install --force-reinstall git+https://github.com/tomduck/pandoc-xnos@284474574f51888be75603e7d1df667a0890504d#egg=pandoc-xnos
```

- **Which worked:-)**

- At this point, existing content in the trial installation on Brian's Mac was been copied over (using `scp`).

## Running the pip-based wiki
Log in as `wiki-user`:

~~~ bash
ssh wiki-user@hhs-docker-svr.local
# then, when logged in:
cd wikmd-pip
source venv/bin/activate
wikmd
~~~

Access it at `http://hhs-docker-svr:5000`

## Managing the pip-wiki files
- The wiki pages are all Markdown files, with `.md` extensions.
- Files reside in the directory `~/wikmd-pip/wiki/`
- Contents can be created and/or updated through the web interface
- Files can also be manipulated with any text editor on another machine and copied to/from the above directory with `scp`:

~~~ bash
scp xxx.md wiki-user@hhs-docker-svr.local:~/wikmd/wiki/
# or
scp wiki-user@hhs-docker-svr.local:~/wikmd/wiki/xxx.md .
# note the "." at the end of the line above
~~~

# Docker second attempt

The above is all very well and comforting, but it requires the wiki-owning user to be logged in from a terminal somewhere. There *are* instructions for transitioning to a service, but it was decided to try again using Docker, as this is the preferred long-term approach (to provide better management of the server resource).

The first docker attempt used docker-managed storage, created & managed using `docker volume`. While this is a great approach when using multiple containers and/or docker clusters, we don't need that for our simple use case and local user storage on the host is more directly accessible for backups, management etc. So we create a local directory and configure docker to use it.

A couple of explanations:

- The TCP port `7008` was chosen for the service (7008 is the New Town postcode).
- The user and group ID numbers of `1002` are that given by the system when the user and its group were created.

## Active Docker configuration

See: [the page on the working system](The Wikmd server) for details.
