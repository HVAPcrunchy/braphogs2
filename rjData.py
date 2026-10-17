# Time Tracking Module
# Accepts reported hours from specific employees
# Validates that hours hopefully make sense
# Seperates normal hours from overtime hours
# Sends accurate time data to the database 
 

# This function gets the employee ID from the user

def get_employee_id():
    """Communicate with UI module: identify which employee is reporting."""
    while True:
        employee_ID = input("Please enter your employee ID: ").strip()
        if employee_ID:
            return employee_ID
        print("Employee ID cannot be empty. Try again.")



# This function asks the user for their hours worked
# It checks that the hours actually make sense

def get_hours_worked():
    """Accept reported hours and validate them (no improper hours)."""
    while True:
        try:
            hours_worked = float(input("Please enter total hours worked: "))
            if hours_worked < 0:
                print("Hours cannot be less than zero. Try again.")
            elif hours_worked > 168:  # More than a full week seems unrealistic
                print("Hours seem too high. Enter 168 or less.")
            else:
                break
        except ValueError:  # Prevents any letters being entered
            print("That's not a number. Try again.")
    return hours_worked



# This function seperates normal hours from overtime
# Anything over 40 hours in a week counts as overtime

def split_hours(hours_worked):
    """Separate normal hours from overtime (over 40 hours a week = overtime)."""
    # Caps normal hours at 40; if fewer than 40 were worked, keep the actual value
    normal_hours = min(hours_worked, 40)

    #Anything beyond 40 becomes overtime
    overtime_hours = max(hours_worked - 40, 0)

    # Return both values together as a pair
    return normal_hours, overtime_hours



def save_to_database(employee_ID, normal_hours, overtime_hours):
    """Hand accurate time tracking info to the database."""

 # Placeholder for database
    print("Saving to database...")

 # Hopefully readable summary line
    print("Employee ID: " + employee_ID + " Normal: " + str(normal_hours) + " hours, Overtime: " + str(overtime_hours) + " hours")



employee_ID = get_employee_id()
hours_worked = get_hours_worked()
normal_hours, overtime_hours = split_hours(hours_worked)
save_to_database(employee_ID, normal_hours, overtime_hours)
