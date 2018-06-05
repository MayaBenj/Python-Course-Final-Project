"""

This is a demonstration of all the functions.

"""

from EditingEmployee import *
from EmployeeReports import *
from  EmployeeClass import *

"""Adding employees from file Employeestoadd.txt """
Add_Employee_File("Employeestoadd.txt")

print("Employee list after adding from file: \n")
print(Employees_List)

"""Removing employees from file Employeestoremove.txt """
Remove_Employee_File("Employeestoremove.txt")

print("Employee list after removing from file: \n")
print(Employees_List)


"""Removing and adding employees manually """
Add_Employee_Manually()
Remove_Employee_Input()

print("Employee list after adding and removing manually: \n")
print(Employees_List)

"""Marking attendance for report """
Mark_Attendance_Input()

"""Printing late today and active monthly reports"""
Late_Employee()
Month_Report()


