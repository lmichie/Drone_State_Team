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
		parm_name = (file_line.split(':')[2]).split(',')[0].lstrip()
		data[parm_name]["Value"] = float(file_line.split(':')[3].lstrip())
		data[parm_name]["Time"] = (file_line.split(':')[1]).split(',')[0].lstrip()
	
new_structure["PARM"] = data
pprint.pprint(new_structure)
