# IP Commands listener

This listener will wait to receive Twilio's "IP Commands" as UDP Datagrams and then do something.

This is a barebones script to demonstrate the underlying functionality and security, such as PSK, has not been implemented.


## Usage
This script runs in the foreground and displays messages inline
```bash
python ipcommands.py
```

Once running, send an IP Command to the device using Twilio's Super SIM with a curl:

```curl
curl -X POST -u $ACCOUNT_SID:$API_KEY https://supersim.twilio.com/v1/IpCommands \
-d "Sim=HSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
-d "Payload=ssh" \
-d "PayloadType=text" \
-d "DevicePort=14550"
```


Currently, the script can receive and parse two commands:

`shutdown` - This will send `sudo shutdown -h now` to a raspberry pi host to turn it off.

`ssh` - This simply prints a message to the console. This is where you might kick off an SSH Tunnel to a cloud service.


## Variables in code
### IP address
```python
localIP = get_ip_address('wwan0')
```
On line 17, we get the IP address of the `wwan0` interface. If you are using a usb-based modem, this may need to be changed to `usb0` or something else. If you would rather use a known IP address of the interface, comment this line out and insert an IP instead, eg:
```python
#localIP = get_ip_address('wwan0')
localIP = x.x.x.x
```
### Port
```python
localPort = 14550
```
Feel free to change this port as necessary, but update your curl to reflect it if so.
