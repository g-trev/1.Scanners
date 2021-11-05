#banner grabber for open ports. we can look up vulnerabilities with the information it provides

#!/usr/bin/python

import socket

def retBanner(ip, port):
		try:
			socket.setdefaulttimeout(2)
			s = socket.socket()
			s.connect((ip, port))
			banner = s.recv(1024) 	#once connected to target, we try to receive 1024 bytes or less and store in banner variable
			return banner
		
		except:
			return

		

def main():
	ip = input("[*] enter target IP: ")
	for port in range(1,1000):
		banner = retBanner(ip, port)
		if banner:
			print("[+] " + ip + "/" + str(port) + " : " + banner.strip('/n')
		
main()	

