(This is a work in progress. Brian is using it initially to capture notes -- it will get filled out over time.)

# HTTPS address
[office.hobarthackerspace.org.au:8123](https://office.hobarthackerspace.org.au:8123/)

We use a Let's Encrypt SSL certificate. [See below.](#letsencrypt)

# Video cameras
## Hikvision NVR
Most of the cameras are (currently ) connected to a Hikvision NVR. IP address is [192.168.2.6](http://192.168.2.6). The password is in [the password vault](Password vault).

Home Assistant doesn't seem to have a plugin; the recommendation is to use [iVMS-4200](https://www.hikvision.com/au-en/support/download/software/ivms4200-series/) instead. This works well, even on a Mac with the ARM processor:-) From outside, configure it to use IP address office.hobarthackerspace.org.au and port 8385.

## Container inner camera
This is an Axis 214 PTZ. It's connected to the ethernet in the container. Video is captured using `xxx` software, which is running in a contaner on the `docker host` machine.

# Automatic Alarm Setting -- AutoAlarm
The "Alarm panel" system is set to enable the alarm after a period of no movement detected in the Space.
Currently that periold is two hours.
Timing is done by monitoring the PIRs within the building:

- Back corridor
- Kitchen
- Ada Lovelace room
- Tesla room
- Margaret Hamilton room
- Bertrand Russell room

If none of them is activated for the defined period, the alarm panel plug-in is told to arm the building.
This is preceeded by a five-minute "pre-warning" period of progressively more frequent warning beeps and chatter from the alarm system.

When the alarm is set, an MQTT message is posted (to `security/alarm/message`) to report this. The door Raspberry Pi logs it and passes it on to the relevant message systems. 

## Configuration of the AutoAlarm
This is done with a Home Assistant helper ([`Movement sensed timer`](https://office.hobarthackerspace.org.au:8123/logbook?entity_id=timer.movement_sensed_timer)) and two Home Assistant automations ([`Movement timer: set`](https://office.hobarthackerspace.org.au:8123/logbook?entity_id=automation.set_movement_timer) and [`Movement timer: timeout`](https://office.hobarthackerspace.org.au:8123/logbook?entity_id=automation.no_movement_timeout)). 
A second Home Assistant helper ([`Alarm pre-warning`](https://office.hobarthackerspace.org.au:8123/logbook?entity_id=input_boolean.alarm_pre_warning)) is set when the "pre-warning" period starts. This is reset whenever movemnet is sensed, to short-circuit the setting of the alarm.

- To alter the timeout duration, change the value that `Movement sensed timer` is set to in `Movement timer: set`.
- To prevent the AutoAlarm from operating for some reason (eg sleepover), simply turn off the "switch" that enables the `Movement timer: timeout` automation. Don't forget to re-enable it!
- If the warnings start to happen, the system should reset whenever movement is sensde by the above set of movement detectors.

<a name="letsencrypt"></a>

# Let's Encrypt SSL certificate
We have the `Let's Encrypt` add-on installed to update the certificate. It requires port 80 to be open on a machine in this domain (it doesn't matter which). If the certificate doesn't get updated for whatever reason, we can be locked out of the web GUI.

The backdoor way to fix this is to `ssh` into the box (as `root`: `ssh root@192.168.2.42`) and run:
``` bash
ha addons start core_letsencrypt # update the certificates
reboot # certs don't get used until reboot
```
	