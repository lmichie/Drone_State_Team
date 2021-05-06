##### TASK = making a tkinter GUI which checks our data logs (dictionary/hash table) and draw a graph #####
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import parse
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

DATA = parse.parse()
def plot(var):  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),dpi = 100)
    # List of x's and y's
    x = []
    y = []
    for i in range(1,7):
        x.append(float(DATA["Flight Modes"][f"FLTMODE{i}"]["time"]))
        y.append(DATA["Flight Modes"][f"FLTMODE{i}"]["value"]) 
    x_var = DATA["Parameters"][var]["time"]
    y_var = DATA["Parameters"][var]["value"] 
    # adding the subplot
    plot1 = fig.add_subplot()  
    # plotting the graph
    plot1.plot(x, y,label = "Modes")
    plot1.plot(x_var, y_var, label = var)
    plot1.set(xlabel='Time', ylabel='Values', title='Graph')
    return fig

# Uppercase
path_drone = "drone.jpg"
alt = "Altitude.JPG"
volt = "Battery.JPG"
temperature = "Temperature.JPG"



# Make an tkinter window instance Tk()
window = Tk()

# Give a title to your tkinter window
window.title("Drone State")

# define the size of your tkinter window (mutable) "widthxheight"
window.geometry("500x500")

# define the minimum width and height of your window (width, height)
window.minsize(500,500)

# define the maximum width and height (width, height)
window.maxsize(1000,1000) 

def draw():
    var = var_entry.get()
    var_bg = var_entry2.get()
    check = 0
    for k,v in DATA["Parameters"].items():
        if k == var_bg and v:
            #messagebox.showinfo("It works!","Eligible parameter to draw")
            check = 1
            #window2 = Tk()
            window2 = Toplevel()
            window2.title("Visualization")
            window2.geometry('900x500')
            window2.minsize(500,500)
            window2.maxsize(1000,1000)
            L1 = Label(window2, text=f"Graph of {var} against {var_bg}", bg="black",fg='white', font=('Helvetica',10,'bold'),relief='sunken')
            L1.pack(fill=X)
            # Obtain Figure object from plot() function
            graph = plot(var_bg)
            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(graph,master = window2)  
            canvas.draw()
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()
            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas,window2)
            toolbar.update() 
            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()

            #image1 = Image.open(k+".JPG").resize((800,400), Image.ANTIALIAS)
            #img = ImageTk.PhotoImage(image1)
            #panel = Label(window2, image = img)
            #panel.pack(side = "bottom", fill="both",expand="yes")
            #window.destroy()
            window2.mainloop()
            break
    if not check:
        messagebox.showerror("Error",f"There is no variable {var_bg}")
    
# configure a color
window.config(bg='white')

# Adding a label to your window
# Features = background, foreground, borderwidth, relief, font(font, fontsize,..)
label1 = Label(window,text="Visualization of Flight Mode", bg="black", fg="white", 
                font=('Helvetica',20,'bold'),#width=500, height=500, 
                borderwidth=20,relief='sunken') #relief: proove,sunken,flat,raised,solid
# Features of pack() anchor=(ne,nw,se,sw,n,e,w,s), fill=(X,Y,BOTH)
# padx, pady ,ipadx, ipady - internal padding
label1.pack(fill=X)

var_label = Label(window,text="Variable: ")
var_label.pack(anchor='w')

# Adding an entry box to your window
var_entry = Entry(window)
var_entry.pack(anchor='w')

# Variable to be plotted against in the background
var_label2 = Label(window,text="Background Variable: ")
var_label2.pack(anchor='w')
var_entry2 = Entry(window)
var_entry2.pack(anchor='w')


# Adding a button to your tkinter window

Button1 = Button(window,text="Draw", command=draw)
Button1.pack()

image1 = Image.open(path_drone).resize((300,300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image1)
panel = Label(window, image = img)
panel.pack(side = "bottom", fill="both",expand="yes")

# Put it in a loop
window.mainloop()
