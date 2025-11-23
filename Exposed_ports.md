# Externally exposed hosts

| Hostname            | IP address    | MAC address       | LAN port | WAN port | Purpose & responsible person                       |
| ------------------- | ------------- | ----------------- | -------- | -------- | -------------------------------------------------- |
| hhs-docker-svr      | 92.168.2.2    | 00:23:24:f7:2f:ac | 80       | 7008     | Wiki - Brian Marriott                              |
| hhs-docker-svr      | 92.168.2.2    | 00:23:24:f7:2f:ac | 22       | 8382     | Wiki SSH access - (works only from within LAN???)  |
| NVR-443             | 192.168.2.6   | c4:2f:90:95:30:17 | 443      | 8384     | Security cameras - Shane, Brian, ...               |
| NVR-8000            | 192.168.2.6   | c4:2f:90:95:30:17 | 8000     | 8385     | Security cameras - Shane, Brian, ...               |
| homeassistant       | 192.168.2.42  | dc:a6:32:d6:20:f7 | 8123     | 8123     | Home Assistant (Security) - Leo, Brian, ...        |
| homeassistant       | 192.168.2.42  | dc:a6:32:d6:20:f7 | 80       | 80       | LetsEncrypt certificate renewal) - Leo, Brian, ... |
| brian-backup-laptop | 192.168.2.100 | 00:08:ca:86:fd:88 | 3316     | 3316     | Laptop used by BrianM for external backup          |
| access-controller   | 192.168.2.125 | b8:27:eb:c1:eb:e4 | 22       | 8386     | Raspberry Pi Door controller - Leo, Brian          |

