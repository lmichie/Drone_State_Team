#!/usr/bin/env python3

import os

with open('flightlog.txt', 'r') as f:
	for line in f:
		line = line.strip()

