import os


Employees_List = []

class Employee:
   def __init__(self, employee_id, namef, namel, phone, age):
        self.employee_id = employee_id
        self.namef = namef
        self.namel = namel
        self.phone = phone
        self.age = age
        Employees_List.append((employee_id, namef, namel, phone, age))
        Add_to_File(employee_id, namef, namel, phone, age)
        
def Add_to_File(employee_id, namef, namel, phone, age):
#Writes employee information to AllEmployees file
    File = open("AllEmployees.txt",'a')
    employee = (employee_id, namef, namel, phone, age)
    File.write("{} \n".format(employee))
    File.close()

def Remove_from_File(employee_id):
#Rewrites employees information to AllEmployees file without subject to remove
    File = open("AllEmployees.txt",'w')
    for employee in Employees_List:
        File.write("{} \n".format(employee))
    File.close()
    
def Attendance_File(Employee_ID,date,time):
#Writes attendance information to Attendance file
    File = open("Attendance.txt",'a')
    File.write("{} {} {} \n".format(Employee_ID,date,time))
    File.close()





 
