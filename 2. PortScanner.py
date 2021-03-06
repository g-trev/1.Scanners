#basic port scanner. this version promts user for specific IP and port to scan

#!/usr/bin/python 			
#specifes path to python libraries that we will use

import socket 		
#imports library, allows us to perform the "connect" function on target ports which tells us if they are 'closed' or 'open' (connect or refuse)

sock = socket.socket(socket.AF_INET, SOCK_STREAM)
#socket.socket defines socket, declares to variable
#socket.AF_INET stands for ipv4 addressing
#SOCK_STREAM means that we will use tcp packet for connection. Need 3-way tcp handshake

socket.setdefaulttimeout(3)
#times out if longer than 3sec

host = raw_input("[*] enter the host to scan: ")
port = int(raw_input("[*] enter the port to scan: "))
#raw_input prompts user who to scan

def portscanner(port): 		#performs the function
	if sock.connect_ex((host, port)) #if this connects to this host and this port, tell me whether it does or else it doesn't.
		print "Port %d is closed" % (port)
	else: 
		print "Port %d is open" % (port)

portscanner(port)

