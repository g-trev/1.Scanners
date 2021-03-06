#advanced port scanner. help options, ports, uses threading library to scan faster

#!/usr/bin/python 			
#specifes path to python libraries that we will use

from socket import * 		#imports everything from socket
import optparse 			#specifies help options if prompted
from threading import *

def main():
		parser = optparse.OptionParser("Useage of program: " + "-H <target host> -p <target port>")
		parser.add_option("-H", dest ="targetHost", type"String", help="specifiy target host")
		parser.add_option("-p", dest ="targetPort", type"String", help="specifiy target ports seperated by comma")
		(options, args) = parsec.parse_args()
		tgtHost = options.tgtHost
		tgtPorts = string(options. tgtPorts).split(',')
		if tgtHost == None) | (tgtPorts[0] == None):
			print(parser.usage)
			exit(0)
		portScan(tgtHost, tgtPorts)
if __name__ == "__main__":		
main()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except: 
		print("can't resolve host %s" %tgtHost)
	try:
		tgtName = gethostbyaddr(tgtIP)	
		print("[+] scan results for: " + tgtName[0])
	except: 
		print("[+] scan results for: " + tgtIP)
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
			t = Thread(target = connScan, args = (tgtHost, int(tgtPorts)))
			t.start()
			
def connScan(tgtHost, tgtPorts):
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((tgtHost, tgtPorts))
			print(colored("[+d] %d/tcp OPEN" % tgtPorts"), "green"))
		except:
			print(colored("[x] %d/tcp CLOSED" % tgtPorts"), red))
		finally:
			socket.closed()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		