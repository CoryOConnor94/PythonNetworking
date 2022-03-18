"""Program imports pexpect and re modules and using pexpect functions to telnet to router and store ip route info in variable
Using re module to then search for a regular expression pattern

Usage: Run program from command line

Usage Example: python3 pexpectTelnet.py

"""
import pexpect
import re

def main():
	
	#COMPILE #COMPILE REGULAR EXPRESSION PATTERN FOR HOP VALUE INTO REGULAR EXPRESSION OBJECT
	r1 = re.compile(r'AS Hops \d')
	router = "route-views.routeviews.org"		#STORE ROUTER ADDRESS IN VARIABLE ROUTER
	hopValue = telnetToRouter(r1, router)		#CALL FUNCTION TO TELNET TO ROUTER, PASS RE PATTERN OBJECT AND ROUTER ADDRESS AND RETURN HOP VALUE
	displayHopValue(hopValue)		#CALL FUNCTION TO DISPLAY HOP VALUE AND PASS HOP VALUE TO FUNCTION
	
def telnetToRouter(r1, router):

	try:
		child = pexpect.spawn('telnet ' + router)	#CREATE CHILD PROCESS TO TELNET TO ROUTER
		child.expect('Username:')		#PASS PROMPT TO CHILD PROCESS
		child.sendline('rviews')		#SEND COMMAND TO CHILD PROCESS
		child.expect('route-views>')		
		child.sendline('show ip route 147.252.1.1')
		child.expect('route-views>')
		child.sendline('quit')
		bigString = (child.before.decode())		#STORE TEXT SET UP TO EXPECT CALL
		print(bigString)
		hopValue = r1.search(bigString)		#SEARCH BIGSTRING FOR RE PATTERN AND RETURN MATCH TO HOPVALUE
	
		return hopValue		#RETURN HOPVALUE TO MAIN
		
	
	except:
		print("Could not connect to router!")
	
def displayHopValue(hopValue):

	try:
		print(hopValue)		#PRINT HOP VALUE MATCH
		print(hopValue.group())	#PRINT HOPE VALUE AS STRING
		
		
	except:
		print("No match found")	#except block to catch type error if none type returned
	
main()

