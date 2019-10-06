# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        
        #make every row a dictionary
        new_employee_dict = dict(row)
            
        new_employee_dict['email'] = f"{row['first_name']}_{row['last_name']}@fakemail.com"
        
        new_employee_data.append(new_employee_dict)
    
# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w", newline = '') as csvfile:
    fieldnames = ["first_name", "last_name", "ssn", "email"]
    
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
   
    for x in new_employee_data:
       
        writer.writerow(x)
    
    # Hint: You can use csv.DictWriter