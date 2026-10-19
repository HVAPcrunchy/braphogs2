#nicoleData stores pay and employee data for use with other methods.  Saves final results to a text file. made by Nicole Metzler
import array as arr
import rjData
import sleyData
import math
import json
employee_Name_list = ["John Cena", "Jeremy Erikson", "Amy Johnson", "Robert Jordan", "Zintia Mendoza", "Miguel Diaz", "Ibrahim alAhksa", "Erika Walschlag", "Donald Drumpf", "Alice Jacobs"]
employee_Id_list =["0001","0002","0003","0004","0005","0006","0007","0008","0009","0010"]
employee_Dependents=[0,0,0,0,0,0,0,0,0,0]
employee_Pay_rate= arr.array("d",[15, 20, 15, 15, 25, 30, 15, 15, 15, 15])
employee_total_Hours=arr.array("d",[0,0,0,0,0,0,0,0,0,0,0])
employee_total_Overtime=arr.array("d",[0,0,0,0,0,0,0,0,0,0])
employee_Pay_pretaxapp= arr.array("d",[0,0,0,0,0,0,0,0,0,0])
employee_Pay_posttaxapp=arr.array("d",[0,0,0,0,0,0,0,0,0,0])
employee_Index_Number=math.nan


#gets name and ID and confirms they match together
def employeeAuth():
  tempName=getEmployeeName()
  tempID=get_employee_Id()
  if check_List_Name(tempName)==check_List_Id(tempID):
    employee_Index_Number=tempName
    return employee_Index_Number
  print("The employee name and ID combination did not match the database")

#checks if the name entered is in the list
def check_List_Name(name):
  if name in employee_Name_list
    position=employee_Name_list.index(name)
    return position
  print("Name not found in employee database ")
#checks if the id entered is in the list
def check_List_Id(id):
  if id in employee_Id_list
    position=employee_Name_list.index(id)
    return position
  print("ID not found in database")
#modifies hours list to have appropriate employee hours
def add_Employee_Hours():
  temp_Hours=get_hours_Worked()
  tempNormalHours, tempOvertimeHours=split_hours(temp_Hours)
  employee_total_Hours.insert(employee_Index_Number,temp_Hours)
  employee_total_Overtime.insert(employee_Index_Number, tempOvertimeHours)
#adds employee pay to both pretax and post tax lists
def add_Employee_Pay():
  pretaxTotalTemp,postTaxTotalTemp= calculate_final_pay(employee_Pay_rate[Employee_Index_Number],employee_total_Hours[Employee_Index_Number])
  employee_Pay_pretaxapp.insert(employee_Index_Number, pretaxTotalTemp)
  employee_Pay_posttaxapp.insert(employee_Index_Number, postTaxTotalTemp)
#inserts employee dependents
def add_Employee_Dependents():
  dependentsTemp=get_Employee_Dependents()
  employee_Dependents.insert(employee_Index_Number,dependentsTemp)
#reinitilializes employee index number in case another account will be accessed
def reInitialize():
  employee_Index_Number=math.nan
#saves updated tables and data to a json file
def saveTo():
  jsonPayRate=employee_Pay_rate.tolist()
  jsonTotalHours=employee_total_Hours.tolist()
  jsonTotalOvertime=employee_total_Overtime.tolist()
  jsonPreTax=employee_Pay_pretaxapp.tolist()
  jsonPostTax=employee_Pay_posttaxapp.tolist()
  master_list = [employee_Name_list, employee_Id_list, employee_Dependents, jsonPayRate, jsonTotalHours, jsonTotalOVertime, jsonPreTax, jsonPostTax]
  with open("data.json", "w") as json_fileProject:
    json.dump(master_list, json_fileProject, indent=4)
  
  
  
  


  
  
  
  



    
    
  
 
  
  





