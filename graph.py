#############################################################
# CSE 20312 Preternship - Drone State Team
# File: graph.py
# Authors: Lindsey Michie, Weike Fang & Emie-Elvire Sabumukama
# 
# This file loads the new data structure created by parse.py
# and uses matplot to graph parameters.
##############################################################

import matplotlib.pyplot as plt
import parse


new_structure = parse.parse()

# x axis values and y axis values for Flight Mode
x = []
y = []
for i in range(1,7):
    x.append(float(new_structure["Flight Modes"][f"FLTMODE{i}"]["time"]))
    y.append(new_structure["Flight Modes"][f"FLTMODE{i}"]["value"])

# plotting the points 
# plt.plot(x, y, label = "Flight Mode")

# X and Y axis for Altitude
x_alt = new_structure["Parameters"]["altitude2"]["time"]
y_alt = new_structure["Parameters"]["altitude2"]["value"]

x_pres = new_structure["Parameters"]["pressure"]["value"]
y_pres = new_structure["Parameters"]["pressure"]["time"]

# plotting the altitude line
plt.plot(x_alt, y_alt, label = "Altitude")
plt.plot(x_pres, y_pres, label = "Pressure")

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('FlightMode')
  
# giving a title to my graph
plt.title('Graph ')

plt.legend()
  
# function to show the plot
plt.show()
