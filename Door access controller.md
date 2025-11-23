## Functions
The door controller controls the lock on our back door, 
responding to the swipe card reader, the contacts within the lock unit and 
the big red *Alarm* button.

The controller reports door activity and swiped tags to its internal log file and to the central 
[(`Home Assistant`)](https://office.hobarthackerspace.org.au:8123/lovelace/default_view)
computer in the Space. In turn, it receives commands from Home Assistant and activity records to be logged.

It can operate independently of Home Assistant if that is not available, but some functions are then inoperative.

## Platform
The system runs on a 10+ year-old Raspberry Pi B+ and is written in Python. (Python 2, unfortunately.)

It uses:  

- A Raspberry Pi B+, with a high endrance microSD card
	- The Pi is currently running Raspbian 10 (Buster)
- A wired ethernet connection
- A custom locally-built level-changing hat
- Python 2.7.16 (one of the last Python2 versions to be supported.)
	- This could constrian upgrading of the Raspbian version -- no Python2 is available on Bookworm (12) or later)
- The `pigpio` software library 
	- `pigpio` provides a low-latency interface between the Python software and the Raspberry Pi GPIO ports.
	- The GPIO ports are used to:
		- sense the output of the RFID reader and the state of the door latch and *Alarm* button; and
		- control the locked/unlocked state of the door latch and turn on/off the beeper
	- `pigpio` is at version 1.35; the most recent is 1.78.
- MQTT is used to communicate with other systems. 
  MQTT allows for loosely-coupled systems that don't break if the link is inoperative.

### Power supply & Power failure actions
Power to the Rasperry Pi (5V DC) comes from a Power-over-Ethernet (PoE) adapter connected to the unit's network cable. The PoE power is sourced from the PoE switch in the network cabinet.

The RFID reader and door strike are powered by a second (12VDC) power supply. The door strike requires power to remain locked, so the door is unlocked whenever there is a power outage.

![The Raspberry Pi](attachments/Door_Controller_Pi_Box-czlm3ux4jimcnjy723wmh2sytyhd.jpg)

## [Remote access](/Access%20Controller%20Remote%20access)

(more to come ...)

## Management
- Add/Update/Remove users or RFID tags
- Logging
- Sync with TidyHQ

## Links to other systems
- MQTT
- Home Assistant

### Notifications
- Pushover
- Discord

## System maintenance
- Backups
	- Database
	- Logs
	- File system
	- System images
- Physical maintenance
	- Door strike
	- Raspberry Pi box
		- SD card removal & re-insertion