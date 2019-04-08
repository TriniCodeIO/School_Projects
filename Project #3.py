#Damani A.Philip


#Version 1.0

print ("Welcome to the Grade Calulator.\nIt is configured to calulate 4 grade averages.\n")
print ("Each assignment is out of fifty(50) point")

#Grade inputs

User_Grade1 = float(input("Please input first grade:\n"))
User_Grade2 = float(input("Please input second grade:\n"))
User_Grade3 = float(input("Please input third grade:\n"))
User_Grade4 = float(input("Please input fourth grade:\n"))

#Possible points per assignment. Set variable

Total_Possible = 50

"""Calculation"""

Calculation = ((User_Grade1 + User_Grade2 + User_Grade3 + User_Grade4)/(Total_Possible * 4)) * 100

"""Output"""

print("Your overall percentage for all assignments is",Calculation,"percent.\n Thank you for using the Grade Calulator.") 
