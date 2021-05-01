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
