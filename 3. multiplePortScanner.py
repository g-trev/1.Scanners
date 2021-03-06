#this version can scan for multiple ports 

#!/usr/bin/python 			
#specifes path to python libraries that we will use

import socket 		
#imports library, allows us to perform the "connect" function on target ports which tells us if they are 'closed' or 'open' (connect or refuse)

from termcolor import colored
#allows us to color the font

sock = socket.socket(socket.AF_INET, SOCK_STREAM)
#socket.socket defines socket, declares to variable
#socket.AF_INET stands for ipv4 addressing
#SOCK_STREAM means that we will use tcp packet for connection. Need 3-way tcp handshake

socket.setdefaulttimeout(3)
#times out if longer than 3sec

host = input("[*] enter the host to scan: ")

def portscanner(port): 		#performs the function
	if sock.connect_ex((host, port)) #if this connects to this host and this port, tell me whether it does or else it doesn't.
		print(colored("[x] Port %d is closed" % (port), 'red'))
	else: 
		print(colored("[+]Port %d is open" % (port), 'green'))

for port in range(1,1000):
		portscanner(port)
		
	#specifies which ports to scan. goes from 1->1000
