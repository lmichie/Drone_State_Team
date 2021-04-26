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

data2["Altitude"] = list_alt
new_structure["Flight Modes"] = data
new_structure["Parameters"] = data2
pprint.pprint(new_structure)
