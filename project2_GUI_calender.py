# Import Required Libraries
from tkinter import *
from tkcalendar import Calendar

# Create Tkinter window
root = Tk()

#Create Title name
root.title("Calendar")

#configure the Background colour 
root.configure(background="white")

# Set the geometry of tkinter window
root.geometry("350x450")


# Add Calendar widget
cal = Calendar(root, selectmode='day',date_pattern='dd-mm-yyyy')
cal.pack(padx = 60 ,pady = 60)

#Function works when click on select button
def getting_date():
	date.config(background="light blue", text = "Selected Date is: " + cal.get_date())

# Add Button
Button(root, text = "Select the Date and Click to get Date",
	command = getting_date).pack(padx = 20 ,pady = 20)

#Add Label for Showing Date
date = Label(root, text = "")
date.pack(padx = 20 , pady = 20)


# Execute Tkinter
root.mainloop()









