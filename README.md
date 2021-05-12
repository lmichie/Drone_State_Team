# Drone State Team Preternship
Software Engineers:
|Name|Email|
|----|-----|
|Weike Fang|wfang@nd.edu|
|Lindsey Michie|lmichie@nd.edu|
|Emie-Elvire Sabumukama|esabumuk@nd.edu|




The objective of the Drone State Project is to build a [Python GUI](https://realpython.com/python-gui-tkinter/) to display drone state data produced over the course of a drone flight. This data is initially accumulated in [data log files](https://yld.me/raw/bH38.csv) have as different [parameters](https://ardupilot.org/copter/docs/parameters.html) organized in flat lists. Parsing these parameters, organizing them into a dictionary, and visualizing them with Python GUI would facilitate the interpretation of the data produced over a drone flight, the comparison of different parameters data, and the searchability of the parameter data for future research. 

## Code

The implementation of this project is organized into two main python codes: `parse.py` and `visual.py`.

`parse.py` contains the function to parse a url to a new organized dictionary (`parsed_data.txt` *contains an example of the new data structure the code produces*) for select parameters (altitude, current, pressure, altitude from the gps, and flight modes). **Note:** `parse` is only compatible with the sample data logs we were provided at the beginning of our project. 

`visual.py` creates a tkinter python GUI window that draws graphs based on the parsed data. First, it imports needed libraries for the python GUI and the parse library that links the parsed data to the `visual.py` code. Then, two functions define the plotting specifications and a main function opens the windows and sets the plotting specifications.

*example output*
![*example output*](https://lh3.googleusercontent.com/3uyATFz48eITWMIYa43MaiLjFNmSqv970jdYvtbx97xkgs49rdijOd88njFcBnuaRBkgVAHvyEDfkLReFmeels2xndO0AWjzYnZcmX1_G27p3e29BdbVO-HU9YYDZEHwHsdQQjKN)

## Usage
 
When the window opens, the user can input a variable and a background variable. As the code is currently written, the variable is "Flight Modes" which is plotted in parallel  with a chosen background variable (both plotted against time). The background variable can be chosen from the different parsed parameters such as current, pressure, etc.

## Installation
	
To replicate our project follow the following commands on your terminal:

```Bash
wget -O setup.sh https://raw.githubusercontent.com/lmichie/Drone_State_Team/main/drone_state_team/setup.sh?token=AQUX25TVDOQNHDMNE5TEIETAUG5DU
chmod a+rx setup.sh
./setup.sh 
```

## Requirements

Graphic application (such as XMing on Windows)

Python Environment

Required Python Packages:
- tkinter
- matplotlib
- PIL (Python Imaging Library)
- sys
- os
- request

## Sample Run

*On Ubuntu*

Steps:
1. Open XMing or other graphic applications in the background.
2. Set DISPLAY environment variables temporarily (export DISPLAY=localhost:0.0) or permanently
3. Run python code visual.py, in which parse module is used to extract key data
4. Enter the main variable (Flight Modes) and a background variable (pressure, current, etc.)

[![ubuntu1.jpg](https://i.postimg.cc/90ZcJwzH/ubuntu1.jpg)](https://postimg.cc/5Q9ct0ws)

*On VSCode*

Once all the packages are downloaded, the visualization can run using the terminal.
