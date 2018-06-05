import os
import string
from EmployeeClass import *
from EmployeeReports import *


def Add_Employee_Manually():
# This function allows to add an employee to file&list
# handeling input interaction in python
    while True:
        try:
            employee_id = int(input("Enter Employee ID to add: "))
            break
        except ValueError:
            print("Please enter a number")
    while True:
        namef = input("Enter Employee's first name: ")
        if not namef.isalpha():
            print("Your name must consist of letters only")
        else:
            break
    while True:
        namel = input("Enter Employee's last name: ")
        if not namel.isalpha():
            print("Your name must consist of letters only")
        else:
            break
    while True:
        phone = input("Enter Employee's phone: ")
        if phone.isdigit() and (len(phone)==10 or len(phone)==9):
            break
        else:
            print ("Please enter 9 or 10 digits only")
    while True:
        try:
            age = int(input("Enter Employee's age: "))
            if 0<age<121:
                break
            else:
                print("Please enter an age between 1 to 120")
        except ValueError:
            print("Please enter a number")
    if not Is_Employee_Listed(employee_id):
        Employee(employee_id,namef,namel,str(phone),age)
        print("Employee added.")
    else: print("Employee already in the system")

def Add_Employee_File(FileName):
# This function allows adding employee/s from file.
# Prints error if there's a problem with opening the file.
    try:
        f = open(FileName,"r")
        for line in f:
            words = line.split()
            Add_Employee(words[0],words[1],words[2],words[3],words[4])
        f.close()
        print("Employee/s added.")
    except Exception as e: print(e)


def Add_Employee(employee_id,namef,namel,phone,age):
# Function checks input, if vaild adds to file&list
    while True:
        if not employee_id.isdigit():
            print("Invalid ID for employee {}".format(int(employee_id)))
            break
        if Is_Employee_Listed(employee_id):
            print("Employee ID {} already in the system".format(int(employee_id)))
            break
        if not namef.isalpha():
            print("Invalid first name for employee {}".format(employee_id))
            break
        if not namel.isalpha():
            print("Invalid last name for employee {}".format(employee_id))
            break
        if not phone.isdigit() or not (len(phone)==10 or len(phone)==9):
            print("Invalid phone for employee {}".format(employee_id))
            break
        if not age.isdigit() or not 0<int(age)<121:
            print("Invalid age for employee {}".format(employee_id))
            break
        if not Is_Employee_Listed(int(employee_id)):
            Employee(int(employee_id),namef,namel,str(phone),int(age))
            break 
        break
    
def Remove_Employee_File(FileName):
# This function allows removing employee/s from file.
# Prints error if there's a problem with opening the file. 
    try:
        f = open(FileName,"r")
        for line in f:
            Remove_Employee(line)
        f.close()
        print("Employee/s removed.")
    except Exception as e: print(e)

    
def Remove_Employee_Input():
# Function allows to remove an employee from file&list
# handeling input interaction in python
    while True:
        try:
            employee_id = int(input("Enter Employee ID to remove: "))
            break
        except ValueError:
            print("Please enter a number")
    Remove_Employee(employee_id)

def Remove_Employee(Employee_ID):
# Function checks input (number and if listed), if vaild removes from file&list
    if Is_Number(Employee_ID):
        if Is_Employee_Listed(Employee_ID):
            for Employee in Employees_List:
                if int(Employee_ID) == Employee[0]:
                    Employees_List.remove(Employee)
                    Remove_from_File(int(Employee_ID))
        else: print("Employee ID not in list of employees")

def List_Mend():
# This function refreshes the Employees_List and Attendance_List
# to be updated with the AllEmployees and Attendance file in case
# the program previously ran.
    CurrentDir = os.getcwd()
    FilePathEmployees=os.path.join(CurrentDir,"AllEmployees.txt")
    FilePathAttendance=os.path.join(CurrentDir,"Attendance.txt")    
    if (os.path.isfile(FilePathEmployees)):  #If file exists
      f = open("AllEmployees.txt","r")
      for line in f:
        words = line.split()
        Employees_List.append((int(words[0][1:-1]),words[1][1:-2],words[2][1:-2],str(words[3][1:-2]),int(words[4][0:-1])))
    if (os.path.isfile(FilePathAttendance)): #If file exists
      f = open("Attendance.txt","r")
      for line in f:
        words = line.split()
        Attendance_List.append((words[0],words[1],words[2]))
        





            
