#! /usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100
print("Basic Fuzzing - send A until we cause a crash.")
port = input("Input port number")
address = input("Input IP address")
command = input("Input Command we are fuzzing")
while True:
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((address, port))
        print("Sending buffer of size: %s" % str(len(buffer)))
        s.send((command + " /.:/" + buffer))
        sleep(1)
        buffer = buffer + "A" * 100
    except:
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
