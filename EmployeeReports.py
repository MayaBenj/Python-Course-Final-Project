import os
from time import strftime
import string
import re
from EmployeeClass import *

Attendance_List = []
Active_Month = []


def Is_Employee_Listed(Employee_ID):
# Returns True if employee is in Employees_List, otherwise returns False
   for Employee in Employees_List:
      if int(Employee_ID) == Employee[0]:
         return True
   return False

def Is_Number(arg):
# Checks if string received is a number
    try:
        int(arg)
        return True
    except ValueError:
        print("Employee ID not a number")
        return False

def Mark_Attendance_Input():
#Reciving ID from user untill an integer
   while True:
        try:
            Employee_ID = int(input("Enter Employee ID to mark attendance: "))
            break
        except ValueError:
            print("Please enter a number")
   Mark_Attendance(Employee_ID)


def Mark_Attendance(Employee_ID):
# If ID is in Employees_List, adds attendance (current time) to  Attendance_List
   if Is_Number(Employee_ID):
      if Is_Employee_Listed(Employee_ID):
         date = strftime("%x")
         time = strftime("%X")
         Attendance_List.append((Employee_ID,date,time))
         Attendance_File(int(Employee_ID),date,time)
         print("Attendance marked for employee {}".format(int(Employee_ID)))
      else: print("Employee ID not in list of empolyees")

def Month_Report():
# Prints all employees whose attendance was marked at least once in current month
   Current_Month = (strftime("%m"))
   for tuple in Attendance_List:
      Month =re.search(r'\d+', tuple[1]).group()
      if (Month == Current_Month and not int(tuple[0]) in Active_Month):
         Active_Month.append(int(tuple[0]))
   print("The active employees this month:")
   for p in Active_Month: print (p)

def Late_Employee(Time_Limit =  "09:30:00", Date = strftime("%x")):
# Prints all employees who arrived after Time_Limit on Date.
   print("Employees who were late on {} : ".format(Date))
   for tuple in Attendance_List:
      if Date == tuple[1] and tuple[2]>Time_Limit :
         print(int(tuple[0]))

