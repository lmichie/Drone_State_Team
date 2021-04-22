#!/usr/bin/env python3
import sys
import re
import os
import requests
import pprint

url = 'https://yld.me/raw/bUAw.txt'
data = {}

response = requests.get(url)
log = response.text
for line in log.split('}'):
	file_line = line[26:]
	if(file_line.startswith("PARM")):
		parm_name = (file_line.split(':')[2]).split(',')[0].lstrip()
		data[parm_name] = float(file_line.split(':')[3].lstrip())
pprint.pprint(data)
