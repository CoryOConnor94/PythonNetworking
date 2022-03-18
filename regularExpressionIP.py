#!/usr/bin/env python3

"""Program imports re module and using regular expressions match IP address' from address.txt using the search function 

Usage example: 
Run the program on the command line
python3 regularExpressionIP

"""

import re
def main():
	#COMPILE REGULAR EXPRESSION PATTERN FOR IP ADDRESS' INTO REGULAR EXPRESSION OBJECT
	r1 = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	findIPs(r1)		#CALL FINDIPS FUNCTION AND PASS R1 OBJECT
	
def findIPs(r1):
	
	#OPEN FILE FOR READING
	with open("iplist.txt", "r") as f:
		listOfIPs = f.readlines()		#READ FILE INTO LIST OF SUBSTRINGS
		
		#LOOP THROUGH LIST LINE BY LINE
		for line in listOfIPs:
		
			#USE SEARCH MODULE TO SCAN FOR MATCH TO RE PATTERN AND RETURN MATCH OBJECT TO MATCHIP
			matchIP = r1.search(line)	
				
			print(matchIP.group())			#PRINT MATCH OBJECT AS STRING
			print(matchIP,'\n')			#PRINT MATCH OBJECT
		
main()
