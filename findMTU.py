#!/usr/bin/env python3
"""Reads inputted interface name from command line, using pexpect module to automate ifconfig command, parse for MTU of interface

Usage: 
chmod +x findMTU.py to make executable
Usage Example: ./findMTU.py lo
 
"""

import sys
import pexpect

def main(argv):

	"""find MTU value of interface"""
	
	if len(argv) !=2:
		print("USAGE: ./lab3ex4.py <iface name>")
		
	else:
		#intName = argv[1]
		interfaceData = findIntData(argv[1])
		findMTU(interfaceData)
		
		
def findIntData(intName):

	""" Atomates ifconfig command and stores resulting bytes in variable to return to main """
	
	ifconfigData = pexpect.spawn("ifconfig -s " + intName)
	result = ifconfigData.expect([pexpect.EOF, pexpect.TIMEOUT])
	outp = ifconfigData.before
	
	return outp
		
def findMTU(interfaceData):

	""" Decodes interface data from bytes to string, stores in List, splits list to 2 and converts to dictionary and displays MTU value """
	
	bigList = interfaceData.decode().split()
	keysList = bigList[:len(bigList)//2]
	valueList = bigList[len(bigList)//2:]
	myDict = dict(zip(keysList, valueList))
	print (myDict['Iface'], 'has ', myDict['MTU'], 'bytes')


if __name__ == "__main__":

	main(sys.argv)
