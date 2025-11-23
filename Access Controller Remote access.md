## Manual Remote access
A new feature added to the access controller is the ability to remotely open the door via SSH.
Once you have gained access via SSH, you can enter the access controller directory with  
`cd HHSAccessControlV4`  
Then to open the door remotely you can type:  
`python manual_access.py open`  
Which will open the door.  

To later arm the alarm you can type:  
`python manual_access.py arm_alarm`  

## Remote access via Tailscale
Tailscale is a VPN software which you can access networks remotely with a simple user interface.
With Tailscale installed on your system you can connect to the access controller.
To access to the Tailscale you can find the link in the Bitwarden account under "Access Controller Tailscale"

## Remote access via Secure Shell (`ssh`)
The Pi has port `22` open for `ssh` access from within the LAN. 
This is NATed to Port `8386` for entry from the internet.

If you have access to a \*ix command line you can access it via:

``` bash
# Within the LAN at the Space
ssh -p 22 pi@access-controller.local
# or
# The wider internet
ssh -p 8386 pi@office.hobarthackerspace.org.au
```

As usual, the password is in the BitWarden vault.