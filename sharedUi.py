#shared UI that brings all our stuff together and acts as the main
#considering that this is meant to be a secure payroll app, the user arrays are premade. Running this program does not allow you to create new users, it only allows them to log in and update their payroll.
#the correct user names and correct user ID's must be entered together, but they may be entered in any order desired.  If a user does not enter payroll, their information defaults to 0 as well.

import nicoleData

count=0
end='y'
while end=='y' or count<=9:
    nicoleData.employeeAuth()
    nicoleData.add_Employee_Hours()
    nicoleData.add_Employee_Pay()
    nicoleData.add_Employee_Dependents()
    nicoleData.print_Employee_Data()
    nicoleData.reInitialize()
    count+=1
    end=input("would you like to enter another employee? (y/n) ").strip().lower()
    if end!='y':
        break
    

nicoleData.saveTo()





