# Project 1
# Version 0.0.1
# CLIENT SOFTWARE (Software distributed to all users)
# IM Software - Socketing
import socket

# Create socket that supports IPv4, TCP Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print "Socket created."
# Requests for IP of host (DNS)
dns = "localhost"
host = socket.gethostbyname(dns)
port = 25565


print "IP Address of " + dns + " is " + host
        
# Connect to server
s.connect((host,port))

print "Socket connected to " + dns + " on IP " + host

# Assign message to be sent to server to a variable
message = raw_input("Message to be sent to server: ")

#Send the actual message to server
s.sendall(message)
print "Message sent successfully"
