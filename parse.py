#!/usr/bin/env python3
import sys
import re
import os
import requests
import pprint

url = 'https://yld.me/raw/bUAw.txt'
new_structure = {}
data = {}

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
	
new_structure["PARM"] = [data]
pprint.pprint(new_structure)
