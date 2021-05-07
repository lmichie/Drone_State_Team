#############################################################
# CSE 20312 Preternship - Drone State Team
# File: parse.py
# Authors: Lindsey Michie, Weike Fang & Emie-Elvire Sabumukama
# 
# This file contains the method to parse the raw flight log
# data and to store/organize it into a new data structure.
##############################################################

#!/usr/bin/env python3
import sys
import os
import requests
import pprint

url = 'https://yld.me/raw/bH38.csv'
new_structure = {}
mode = {}
parms = {}
list_alt = []
list_time = []
list_volt=[]
list_curr_time=[]
list_press=[]
list_baro_time=[]
list_gps_alt=[]
list_gps_time=[]

# Convert time from microsec to second
# since the system starts
def time_convert(time_us):
	return (time_us / 1000000)

def parse():
	#Read in data from flight log
	response = requests.get(url)
	log = response.text
	for line in log.split('}'):
		file_line = line[25:]
		if file_line.startswith("PARM"):
			#Get Parm data
			temp_data = {}
			parm_name = (file_line.split(':')[2]).split(',')[0].lstrip()
			if parm_name.startswith("FLT"):
				#Get flight mode & time vlaues
				temp_data["value"] = float(file_line.split(':')[3].lstrip())
				temp_data["time"] = time_convert(float((file_line.split(':')[1]).split(',')[0].lstrip()))
				mode[parm_name] = temp_data
		if file_line.startswith("CMD"):
			list_alt.append(float(file_line.split(':')[11].lstrip()))
			# Add a list of time corresponding to the altitude value
			str = [letter for letter in file_line.split(':')[1] if letter.isnumeric()]
			str1 = ''.join(str)
			list_time.append(time_convert(float(str1)))

		if file_line.startswith("CURR"):
			#get volt values		
			list_volt.append(float(file_line.split(':')[2].split(',')[0].lstrip()))
			#get time values
			list_curr_time.append(time_convert(float(file_line.split(':')[1].split(',')[0].lstrip())))

		if file_line.startswith("BARO"):
			#get pressure
			list_press.append(float(file_line.split(':')[3].split(',')[0].lstrip()))
			#get time values
			list_baro_time.append(time_convert(float(file_line.split(':')[1].split(',')[0].lstrip())))
		
		if file_line.startswith("GPS"):
			#get altitude
			list_gps_alt.append(float(file_line.split(':')[9].split(',')[0].lstrip()))
			#get time values
			list_gps_time.append(time_convert(float(file_line.split(':')[1].split(',')[0].lstrip())))

		
	parms["altitude1"] = {
		"value":list_alt,
		"time":list_time,
	}
	parms["current"]={
		"value":list_volt,
		"time": list_curr_time
	}
	parms["pressure"]={
		"value":list_press,
		"time":list_baro_time
	}
	parms["altitude2"]={
		"value":list_gps_alt,
		"time":list_gps_time
	}
	new_structure["Flight Modes"] = mode
	new_structure["Parameters"] = parms
	return new_structure

if __name__ == '__main__':
	new_structure = parse()
	pprint.pprint(new_structure)
