#Damani A.Philip


#Version 1.0


"""Introduction"""
Name = str(input("Hello,please enter name:"))
print ("Hello %s, this program is designed to provide you with information about your B.M.I.\n" % (Name))

Age = int(input("This application is configured to work for persons over the age of 20. Please enter your age:"))

if Age < 20:
    print ("Your age does not meet the requirements for this application.\n")
    exit()
else:
    print ("This application is right for you!! Please follow the next instruction.\n")
    

"""Actual Program"""

BMI = float(input("Please enter your Body Mass Index value:"))

if BMI < 18.5:
    print("Unfortunately you are considered underweight, please seek medical attention from a licensed professional.\n")
elif 18.5 <= BMI <= 24.9:
    print("Your current B.M.I is considered correct for your current age.\n")
elif 25 <= BMI <= 29.9:
    print("You are currently considered as overweight, please seek medical attention immediately and find out about ways you can cchange your diet.\n")
elif BMI > 30:
    print("You are currently considered as obese, and at this status, medical attention is highly suggested. Please watch your diet and consume less processed foods.\n")

print("Thank you for using my B.M.I informational tool, remember your health is your wealth.")
