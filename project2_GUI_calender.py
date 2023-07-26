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
root.geometry("400x500")

# Add Calendar widget
cal = Calendar(root, selectmode='day',date_pattern='dd-mm-yyyy')
cal.pack(pady = 60)

#Function works when click on select button
def gt_date():
	date.config(background="light blue", text = "Selected Date is: " + cal.get_date())

# Add Button
Button(root, text = "Select the Date and Click to get Date",
	command = gt_date).pack(pady = 20)

#Add Label for Showing Date
date = Label(root, text = "")
date.pack(pady = 20)


# Execute Tkinter
root.mainloop()









