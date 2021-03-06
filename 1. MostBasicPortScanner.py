#most basic port scanner. target specified in code

#!/usr/bin/python 			
#specifes path to python libraries that we will use

#imports library, allows us to perform the "connect" function on target ports which tells us if they are 'closed' or 'open' (connect or refuse)
import socket 		

#socket.socket defines socket, declares to variable
#socket.AF_INET stands for ipv4 addressing
#SOCK_STREAM means that we will use tcp packet for connection. Need 3-way tcp handshake
sock = socket.socket(socket.AF_INET, SOCK_STREAM)

host = "192.x.x.x.x"
port = x
#**specifies who and what is being scanned

def portscanner(port): 		
	if sock.connect_ex((host, port)) #if this connects to this host and this port, tell me whether it does or else it doesn't.
		print "Port %d is closed" % (port)
	else: 
		print "Port %d is open" % (port)

portscanner(port)

