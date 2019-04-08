#Damani A.Philip
#Version 2.0

print ("Welcome to the Grade Calulator.\nIt is configured to calulate 4 grade averages.\n")
print ("Each assignment is out of fifty(50) points")

#Grade inputs

User_Grades = (float(input("Please input first grade:\n")),float(input("Please input second grade:\n")),float(input("Please input third grade:\n")),float(input("Please input fourth grade:\n")))

#Possible points per assignment. Set variable

Total_Possible = 50

"""Calculation"""

Calculation = ((sum(User_Grades))/(Total_Possible * len(User_Grades))) * 100

"""Output"""

print("Your overall percentage for all assignments is",Calculation,"percent.\n Thank you for using the Grade Calulator.") 
