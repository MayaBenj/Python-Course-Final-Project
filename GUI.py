import os
from tkinter import *
from tkinter import ttk
from EmployeeReports import *
from EditingEmployee import *
from PIL import ImageTk, Image

List_Mend()
root = Tk()
root.title("Employee Management")

menu = Menu(root)
root.config(menu=menu)
root.geometry("500x300")
frame = Frame(root)
frame.grid()

def Clear_Window():
#Destroying all widgets in frame
    for widget in frame.winfo_children():
        widget.destroy()

def Open_Employees():
# Opens AllEmployees.txt in notepad
    try: os.startfile("AllEmployees.txt")
    except: print("Please enter at least one employee \n")
    
def Open_Attendance():
# Opens Attendance.txt in notepad
    try: os.startfile("Attendance.txt")
    except: print("Please mark at least one attendance \n")
    
def Add_Manual():
#Displaying add employee manually window
    Clear_Window()
    note = Label(frame, text = "Employee ID: ").grid(row=0,column=0,sticky="E")
    note2 = Label(frame, text="First Name: ").grid(row=1,column=0,sticky="E")
    note3 = Label(frame, text="Last Name: ").grid(row=2,column=0,sticky="E")
    note4 = Label(frame, text="Phone: ").grid(row=3,column=0,sticky="E")
    note5 = Label(frame, text="Age: ").grid(row=4,column=0,sticky="E")
    ent1 = Entry(frame)
    ent1.grid(row=0,column=1)
    ent2 = Entry(frame)
    ent2.grid(row=1,column=1)
    ent3 = Entry(frame)
    ent3.grid(row=2,column=1)
    ent4 = Entry(frame)
    ent4.grid(row=3,column=1)
    ent5 = Entry(frame)
    ent5.grid(row=4,column=1)
    b = Button(frame, text="Enter", command = lambda:Add_Employee(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get())).grid(row=5,column=1)

def Remove_Manual():
#Displaying remove employee manually window
    Clear_Window()
    note = Label(frame, text = "Employee ID: ").grid(row=0,column=0,sticky="E")
    ent1 = Entry(frame)
    ent1.grid(row=0,column=1)
    b = Button(frame, text="Enter", command = lambda:Remove_Employee(ent1.get())).grid(row=0,column=2)
    
def Add_File():
#Displaying add employee from file window
    Clear_Window()
    note = Label(frame, text = "Please enter a txt file. \nSeperate ID, name, phone and age by a space.\nHave every employee in a different line. \n(Example file: Employeestoadd.txt)", justify="left").grid(row=0, rowspan=4)
    ent1 = Entry(frame)
    ent1.grid(row=4,column=0,sticky="E")
    b = Button(frame, text="Enter", command = lambda: Add_Employee_File(ent1.get())).grid(row=4,column=1)


def Remove_File():
#Displaying remove employee from file window
    Clear_Window()
    note = Label(frame, text = "Please enter a txt file. \nPut each ID to remove in a different line.\n(Example file: Employeestoremove.txt)", justify="left").grid(row=0, rowspan=3)
    ent1 = Entry(frame)
    ent1.grid(row=3,column=0,sticky="E")
    b = Button(frame, text="Enter", command = lambda: Remove_Employee_File(ent1.get())).grid(row=3,column=1)

 
def Mark_Win():
#Displaying mark employee attendance window
    Clear_Window()
    note= Label(frame, text="Employee ID:").grid(sticky="E")
    ent1 = Entry(frame)
    ent1.grid(row=0,column=1)
    b = Button(frame, text="Enter", command = lambda: Mark_Attendance(ent1.get())).grid(row=1,column=1)

#Menu
SubMenu = Menu(menu)
SubMenuAdd = Menu(SubMenu)
SubMenuRemove = Menu(SubMenu)
menu.add_cascade(label="Edit", menu=SubMenu)

SubMenu.add_cascade(label="Add Employee",menu=SubMenuAdd)
SubMenuAdd.add_command(label="Manually", command=Add_Manual)
SubMenuAdd.add_command(label="From File", command=Add_File)

SubMenu.add_cascade(label="Remove Employee",menu=SubMenuRemove)
SubMenuRemove.add_command(label="Manually", command=Remove_Manual)
SubMenuRemove.add_command(label="From File", command=Remove_File)

FileMenu = Menu(menu)
menu.add_cascade(label="Actions", menu=FileMenu)
FileMenu.add_command(label="Mark Attendance", command=Mark_Win)

ReportsMenu = Menu(menu)
menu.add_cascade(label="Reports", menu=ReportsMenu)
ReportsMenu.add_command(label="Late Today", command=Late_Employee)
ReportsMenu.add_command(label="Late This Month", command=Month_Report)

DisplayManu = Menu(menu)
menu.add_cascade(label="Display", menu=DisplayManu)
DisplayManu.add_command(label="All Empolyees", command = Open_Employees)
DisplayManu.add_command(label="Attendance", command = Open_Attendance)

#Background image
img = ImageTk.PhotoImage(Image.open("Background.jpg"))
Label(frame, image=img).grid()

root.mainloop()
