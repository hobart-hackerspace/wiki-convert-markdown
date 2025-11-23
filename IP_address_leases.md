# Static IP address leases
## HHS devices

| Device             | Home Assistant ID | People responsible | IPv4 Address    | MAC address         | Purpose                                          | IPv6 Address (if stable) |
| ------------------ | ------------------ | ------------------ | :-------------: | :-------------------: | ------------------------------------------------ | :------------------------------------------: |
| Router             | | Leo & Brian        | 192.168.2.1   | `8c:30:66:a0:09:6c` | Gateway router & WiFi controller  |                                            |
| Docker server      | | Brian              | 192.168.2.2   | `00:23:24:f7:2f:ac` | Wiki; Secondary camera controller  | `2404:e80:1083:0:223:24ff:fef7:2fac` |
| NVR                | | Shane, Brian       | 192.168.2.6   | `c4:2f:90:95:30:17` | Primary camera controller & recorder  | `2404:e80:1083:0:c62f:90ff:fe95:3017` |
| Octoprint          | | Leo                | 192.168.2.7   | `e4:5f:01:31:56:c2` | Raspberry Pi running `Octoprint` for 3D printers | |
| Home Assistant     | | Brian              | 192.168.2.42  | `dc:a6:32:d6:20:f7` | Raspberry Pi running `hassos` | `2404:e80:1083:0:dd82:262a:5a48:9908` |
| ToiletCam          | | Shane, Brian       | 192.168.2.93  | `ec:71:db:88:f2:8a` | Camera mounted on old outside toilet |   |
| Radio-linux        | | Jason, Leo, DavidC  | 192.168.2.97  | `00:0a:f7:89:5c:90` | Linux machine on radio station bench | `2404:e80:1083:0:35ef:64b2:22af:404b` |
| Access-controller  | | Leo, Brian         | 192.168.2.125 | `b8:27:eb:c1:eb:e4` | Door system Pi Zero | `2404:e80:1083:0:fe64:4414:c7f:1fa5`   |
| Beambox            | | Tom                | 192.168.2.132 | `b8:27:eb:14:45:e5` | Laser Cutter |   |
| CNC PC             | | Mark               | 192.168.2.155 | `7c:f1:7e:ba:be:50` | Windows machine connected to CNC router |                                                                    |
| ContainerOutsideCam | | Brian              | 192.168.2.157 | `00:40:8c:c4:b7:55` | Camera mounted outside the container |                                                                    |
| 3D Printers        | | Leo                | 192.168.2.167 | `64:00:6a:4e:a0:7c` | Windows machine sitting between the 3D printers  |                                                                    |
| ContainerInsideCam     | | Shane, Brian       | 192.168.2.213 | `00:40:8c:ab:72:e5` | Camera (PTZ) mounted inside container |                                                                    |
| Rigol              | | Tom, Brian         | 192.168.2.239 | `00:19:af:7b:50:81` | The Rigol digital Oscilloscope  |                                                                    |
| back-light | | Committee | 192.168.2.165 | `bc:dd:c2:36:ac:83` | Outside light (Sonoff/Tasmota) |  |
| kitchen-light | | Committee | 192.168.2.207 | `f8:17:2d:80:17:50` | Kitchen light |  |
| Google-Home-Mini | | Committee | 192.168.2.244 | `38:8b:59:b3:2e:17` | Internal IP speaker |  |
|  |  |  | |  |  | |

## Members' devices

| Device           | Owner          | IP Address    | MAC address         | Purpose                         | IPv6 Address                          |
| ---------------- | -------------- | ------------- | ------------------- | ------------------------------- | ------------------------------------- |
| Brian-Backup-Pi4 | Brian Marriott | 192.168.2.100 | `dc:a6:32:73:eb:42` | Brian's off-site backup machine | `2404:e80:1083:0:975c:28d:2342:c0c6` (wired), |
|  |  |  | |  |  `2404:e80:1083:0:e86a:8725:c424:9e49` (wifi) |
|  |  |  | |  |  |


## Some not yet sorted out
These devices were reserved IP addresses on the old router but haven't properly set up yet on the Ubiquiti

| Hostname | IP address | MAC address | Purpose & responsible person |
| ---: | :---: | :---: | :--- 
| AP-BackRoom | 192.168.2.64 | `24:a4:3c:64:6f:c3` | WiFi access point
| AP-ServerRoom | 192.168.2.79 | `24:a4:3c:64:6f:d2` | WiFi access point
| Google-Home-Mini | 192.168.2.86 | `20:df:b9:d2:82:5a` | External IP speaker
| IPCam_07 | 192.168.2.113 | `04:e6:76:00:05:af` | Babakuarea Camera
| IPCam_08 | 192.168.2.116 | `04:e6:76:00:05:b2` | Bertrand Russell Room camera
| IPCam_09 | 192.168.2.120 | `04:e6:76:00:05:b6` | Margaret Hamilton Room camera
|  |  |  | |
