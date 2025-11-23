# Software
- The software we're using is Wikimd. 
	- [Github repo](https://github.com/Linbreux/wikmd)
	- [More details](#wiki-software-details)
- We run it in a `docker` container.
	- [Details of the docker container are below](#active-docker-configuration)

# Running the wiki
The wiki is set up as a docker container that starts automatically on system boot and restarts on failure, so nothing is normally required just to get it to run. Just go to [http://wiki.local](http://wiki.local) from within our local network. 

The detailed configuration of the docker instance is given below under [Docker configuration](#Docker_configuration)

# Administering the wiki
This is done by logging into the wiki server (`hhs-docker-svr.local`). The wiki runs as the user `wiki-user`, so you need to log in as that user (the password is in [the vault](Password vault)):

~~~ bash
ssh wiki-user@hhs-docker-svr.local
# then, when logged in:
cd ~/wikmd
docker ps
docker image inspect linbreux/wikmd
...
~~~

Access it from within our LAN at `http://wiki.local` or, if for some reason `nginx` or `mDNS` are not working, `http://hhs-docker-svr:7008`

# Managing the wiki files
- The wiki pages are all Markdown files, with `.md` extensions.
	- Image files can be uploaded for embedding in  pages (or simply linking to)
	- As yet we can't upload PDF files.
- The files reside in the directory `~/wikmd/wiki/` and its subdirectories.
- Contents can be created and/or updated through the web interface.
- Files can also be manipulated with any text editor on another machine and copied to/from the above directory with `scp`, for example:

~~~ bash
scp xxx.md wiki-user@hhs-docker-svr.local:~/wikmd/wiki/
# or
scp wiki-user@hhs-docker-svr.local:~/wikmd/wiki/xxx.md .
# note the "." at the end of the line above
~~~

- Note that `wikmd` keeps a history of changes using `git`. The `git` repository is in the `~/wikmd/wiki/` directory. History can be found (and, if necessary, adjusted) using `git`:

~~~ bash
cd ~/wikmd/wiki/
git status
git log
#etc
~~~

- The usual git commands can be used to revert, checkpoint, create branches, etc

# Backup
The wikmd files are being backed up to Brian's local Ubuntu server (`bwm-backup-laptop.local`). The following bash command runs on that server under brian's user-id, using `cron`. It is currently run twice a day (~11:00am and ~11:00pm).

~~~ bash
rsync -az -e 'ssh -p 22'  wiki-user@hhs-docker-svr.local:~/wikmd/ /mnt/zfs-2/hhs-wiki-backup
~~~

(The `-e 'ssh -p 22'` bit ensures that the link between the wikmd machine and the backup machine is on the normal `ssh` port. The backup machine defaults to a different port in order to be accessible from outside the building.

The `rsync`ed files are then pulled off-site daily to a server at Brian's house in Franklin.


# Wiki software details

- The software we're using is Wikimd. 
	- [Github repo](https://github.com/Linbreux/wikmd)
	- [Doco and installation instructions](https://linbreux.github.io/wikmd/)
- This is available as a python install (via `pip` or `git`) or as a `docker` container. We're running the `docker` container.
	- [Details of the docker container are below](#active-docker-configuration)
	- [We went through a few different approaches to before settling on the Docker container.](Wiki software trial installations)

See [The Docker Server running our Wiki](The Docker Server running our Wiki) for server setup details.

# The Docker container
A couple of explanations:

- The TCP port `7008` was chosen for the service (7008 is the New Town postcode).
- The user and group ID numbers of `1002` are that given by the system when the user and its group were created.
	- If you're working on a new/replacement installation, you can verify the user & group IDs with:
	- `grep wiki-user /etc/passwd`

## Active Docker configuration

- After some experimentation, the following has been found to work (and is saved as `~/wikmd/start_wiki.sh` for the `wiki-user` userID):

~~~ bash
#!/usr/bin/bash
docker run -d \
  --name wikmd \
  -e TZ=Australia/Hobart \
  -e PUID=1002 \
  -e PGID=1002 \
  -e HOMEPAGE=Hackerspace\ Wiki.md \
  -e HOMEPAGE_TITLE="Hackerspace Wiki" \
  -p 7008:5000 \
  -e WIKMD_LOGGING=1 \
  -e WIKMD_LOGGING_FILE=/logdir/wikmd_log.log \
  -e PROTECT_EDIT_BY_PASSWORD=1 \
  -e PASSWORD_IN_SHA_256=4a7535584332981f8a0d95e5b997c358096c699da2b533df16e9d3fd1a339438 \
  -v /home/wiki-user/wikmd/wiki/:/wiki \
  -v /home/wiki-user/wikmd/:/logdir \
  --restart unless-stopped \
  -u 1002:1002 \
  linbreux/wikmd:latest
sleep 3 # give time to get going or crash
docker ps # just to check
~~~

- The SHA256 hash above is for the password "spacehackers@#"
