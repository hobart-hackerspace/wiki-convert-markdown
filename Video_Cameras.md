Some doco on our monitoring cameras (NVR, CCTV, video surveillance, ....)

- [Zoneminder](Zoneminder) was tried (fully FOSS), but is not well supported or up-to-date, so the experiment was discontinued.
- Now using [Agent-DVR](https://www.ispyconnect.com/):
	- It runs on the Docker server as a container
		- To start:
		
			``` bash
			ssh camera-user@hhs-docker-svr
			cd agent-dvr
			./run.sh
			docker ps
			```
		- To stop:
		
			``` bash
			docker stop AgentDVR
			docker rm AgentDVR
			```
		- The `run.sh` file:
		
			``` bash
			docker run -d --name=AgentDVR \
				-e PUID=1000 -e PGID=1000 \
				-e TZ=Australia/Hobart \
				-e AGENTDVR_WEBUI_PORT=8090 \
				-p 8090:8090 -p 3478:3478/udp -p 50000-50100:50000-50100/udp \
				-v /appdata/AgentDVR/config/:/AgentDVR/Media/XML/ \
				-v /appdata/AgentDVR/media/:/AgentDVR/Media/WebServerRoot/Media/ \
				-v /appdata/AgentDVR/commands:/AgentDVR/Commands/ \
				--restart unless-stopped \
				mekayelanik/ispyagentdvr:latest
			```
	

	- Configuration of Agent-DVR is done via its web interface. This ***must*** be opened in Chrome, at [http://wiki.local:8090/](http://wiki.local:8090/). 
	
		We're running without a paid licence, so it isn't remotely accessible. That happens via [`Home Assistant`](https://office.hobarthackerspace.org.au:8123/lovelace/container).

## Cameras
| Name | Address |Model | Location                           |
| :------: | :------: | :----------: | --------------------------------- |
| Container inner | | Axis 214 PTZ | Inside container NE corner |
| | | |


*More to come*  *BWM 2025-11-09*
