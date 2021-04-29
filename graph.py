import matplotlib.pyplot as plt

new_structure = {
    "Flight Modes":{
                    'FLTMODE1': {'time': '144362902', 'value': 2.0},
                  'FLTMODE2': {'time': '144362921', 'value': 5.0},
                  'FLTMODE3': {'time': '144362939', 'value': 3.0},
                  'FLTMODE4': {'time': '144362958', 'value': 6.0},
                  'FLTMODE5': {'time': '144362977', 'value': 6.0},
                  'FLTMODE6': {'time': '144362996', 'value': 6.0},
                  },
    "Parameters":{
        'Altitude': {'time': [144625462.0, 144625483.0,144656671.0,144656691.0,144656738.0,144656759.0,144656781.0,144656802.0,144656823.0,144656844.0,144657046.0,144657067.0,144657088.0,144657109.0],
                             'value': [217.33999633789062,10.0,12.0,12.0,20.0,14.0,12.0,17.0,17.0,20.0,20.0,20.0,12.0,0.0],
                    },
    }
}

# x axis values and y axis values for Flight Mode
x = []
y = []
for i in range(1,7):
    x.append(float(new_structure["Flight Modes"][f"FLTMODE{i}"]["time"]))
    y.append(new_structure["Flight Modes"][f"FLTMODE{i}"]["value"])

# plotting the points 
plt.plot(x, y, label = "Flight Mode")

# X and Y axis for Altitude
x_alt = new_structure["Parameters"]["Altitude"]["time"][1:-1]
y_alt = new_structure["Parameters"]["Altitude"]["value"][1:-1]

# plotting the altitude line
plt.plot(x_alt, y_alt, label = "Altitude")

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('FlightMode')
  
# giving a title to my graph
plt.title('Graph ')

plt.legend()
  
# function to show the plot
plt.show()
