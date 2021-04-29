#!/usr/bin/env python3
import sys
import re
import os
import requests
import pprint

url = 'https://yld.me/raw/bUAw.txt'
new_structure = {}
data = {}
data2 = {}
list_alt = []
list_time = []
list_volt=[]
list_curr_time=[]
list_press=[]
list_baro_time=[]
list_gps_alt=[]
list_gps_time=[]

response = requests.get(url)
log = response.text
for line in log.split('}'):
	file_line = line[26:]
	if(file_line.startswith("PARM")):
		temp_data = {}
		parm_name = (file_line.split(':')[2]).split(',')[0].lstrip()
		if(parm_name.startswith("FLT")):
			temp_data["value"] = float(file_line.split(':')[3].lstrip())
			temp_data["time"] = (file_line.split(':')[1]).split(',')[0].lstrip()
			data[parm_name] = temp_data
	if(file_line.startswith("CMD")):
		list_alt.append(float(file_line.split(':')[11].lstrip()))
		# Add a list of time corresponding to the altitude value
		str = [letter for letter in file_line.split(':')[1] if letter.isnumeric()]
		str1 = ''.join(str)
		list_time.append(float(str1))

	if(file_line.startswith("CURR")):
		#get volt values		
		list_volt.append(float(file_line.split(':')[2].split(',')[0].lstrip()))
		#get time values
		list_curr_time.append(file_line.split(':')[1].split(',')[0].lstrip())

	if(file_line.startswith("BARO")):
		#get pressure
		list_press.append(float(file_line.split(':')[3].split(',')[0].lstrip()))
		#get time values
		list_baro_time.append(file_line.split(':')[1].split(',')[0].lstrip())
	
	if(file_line.startswith("GPS")):
		#get altitude
		list_gps_alt.append(float(file_line.split(':')[9].split(',')[0].lstrip()))
		#get time values
		list_gps_time.append(file_line.split(':')[1].split(',')[0].lstrip())

	
data2["Altitude"] = {
	"value":list_alt,
	"time":list_time,
}
data2["Current"]={
	"volt":list_volt,
	"time": list_curr_time
}
data2["Pressure"]={
	"pressure":list_press,
	"time":list_baro_time
}
data2["GPS"]={
	"altitude":list_gps_alt,
	"time":list_gps_time
}
new_structure["Flight Modes"] = data
new_structure["Parameters"] = data2
pprint.pprint(new_structure)
