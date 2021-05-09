# Drone State Team Preternship
Software Engineers:
|Name|Email|
|----|-----|
|Weike Fang|wfang@nd.edu|
|Lindsey Michie|lmichie@nd.edu|
|Emie-Elvire Sabumukama|esabumuk@nd.edu|


[Data File](https://yld.me/raw/bH38.csv)

The objective of the Drone State Project is to build a Python GUI to display drone state data produced over the course of a drone flight. This data is initially accumulated in data log files have as different parameters organized in flat lists. Parsing these parameters, organizing them into a dictionary, and visualizing them with Python GUI would facilitate the interpretation of the data produced over a drone flight, the comparison of different parameters data, and the searchability of the parameter data for future research. 

The implementation of this project is organized into two main codes: parse.py and visual.py.

Parse.py parses a url to a data log file for select parameters (altitude, current, pressure, altitude from the gps, and flight modes).

Visual.py creates a tkinter python GUI window that draws graphs based on the parsed data. First, it imports needed libraries for the python GUI and the parse library that links the parsed data to the visual.py code. Then, two functions define the plotting specifications and a main function opens the window and its specifications and calls the two functions. 
