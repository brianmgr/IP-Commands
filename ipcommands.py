import socket
import fcntl
import struct
from time import sleep
from subprocess import call

# Get the IP address associated with 'wwan0' for QMI
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15]))[20:24])

# Alter this to use the ifconfig entry as necessary, eg: usb0
localIP = get_ip_address('wwan0')

# Port to listen on
localPort = 14550
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening on wwan0 at " + str(localIP))

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)

    # Print every message that comes in
    print(clientMsg)
    print(clientIP)

    if message == "shutdown":
        # Shut down the pi if "shutdown" received
        print("Shutting down...")
        call("sudo shutdown -h now", shell=True)
    elif message == "ssh":
        # Example of SSH, doesn't work for real
        print("Starting SSH Tunnel...")
        sleep(1)
        print("...no SSH code found.")
        # SSH Code goes here
