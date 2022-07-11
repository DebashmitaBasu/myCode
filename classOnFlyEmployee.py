#! python3
# -*- coding: utf-8 -*-
#title					:classOnFlyEmployee.py
#author					:Debashmita
#date of creation		:11/07/2022 14:37
#==============================================================================

class Employee():
    pass

employee = Employee()
employee.salary = 122000
employee.firstname = "alice"
employee.lastname = "wonderland"

print(employee.firstname + " " + employee.lastname + " " + str(employee.salary) + "$") # alice wonderland 122000$