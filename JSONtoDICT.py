"""Program imports json module to read data from json file to dictionary using load function.
Then change primary IP address in dictionary and write to new json file using dump function.
Usage: Run from command line from directory containing JSON file to read in
"""
import json
def main():

	myDict = filetoDict()		#CALL FUNCTION TO READ DATA FROM JSON FILE TO DICTIONARY AND RETURN DICTIONARY
	newDict = changeIp(myDict)	#CALL FUNCTION TO CHANGE IP ADDRESS, PASS DICTIONARY TO AND EDITED DICTIONARY IS RETURNED
	writetoFile(newDict)		#CALL FUNCTION TO WRITE DICTIONARY TO NEW JSON FILE, PASS EDITED DICTIONARY TO BE WRITTEN
	
def filetoDict():

	with open("ciscodata.json","r") as f:
		myDict = json.load(f)		#LOAD FUNCTION READS IN JSON FILE AND DATA IS STORED IN DICTIONARY
	print(myDict)	
		
	return myDict
	
def changeIp(myDict):

	#ACCESS PRIMARY IP ADDRESS IN DICTIONARY AND ASSIGN NEW VALUE 
	myDict['Cisco-IOS-XE-native:GigabitEthernet']["ip"]["address"]["primary"]["address"] = "10.0.0.10"
	
	
	return myDict
	
def writetoFile(newDict):

	with open("ciscodata2.json", "w") as f:
		json.dump(newDict, f, indent=4)		#DUMP FUNCTION WRITES DATA TO JSON FILE FROM DICTIONARY AND DATA IS INDENTED
		
main()
