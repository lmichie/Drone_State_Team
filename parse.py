#!/usr/bin/env python3
import sys
import re
import os
import requests

url = 'https://yld.me/raw/bUAw.txt'
data = {}

response = requests.get(url)
print(response.text)
