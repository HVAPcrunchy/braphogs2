# calculation.py
# Payroll calculation module - The Braphogs
# Written by ScorpSley
#
# This file figures out how much an employee gets paid.
# It uses the hours they worked and their pay rate.


OVERTIME_HOURS = 40        # after 40 hours in a week, it's overtime
OVERTIME_RATE = 1.5        # overtime pays 1.5 times the normal rate
MAX_HOURS = 168            # there are only 168 hours in a week

FEDERAL_TAX = 0.12         # 12% federal tax
SOCIAL_SECURITY = 0.062    # 6.2% social security
MEDICARE = 0.0145          # 1.45% medicare




def check_pay_rate(pay_rate):
    if type(pay_rate) != int and type(pay_rate) != float:
        raise ValueError("Pay rate must be a number")
    if pay_rate <= 0:
        raise ValueError("Pay rate must be more than 0")
    if pay_rate > 1000:
        raise ValueError("Pay rate is too high to be real")


def check_hours(hours):
    if type(hours) != int and type(hours) != float:
        raise ValueError("Hours must be a number")
    if hours < 0:
        raise ValueError("Hours cannot be negative")
    if hours > MAX_HOURS:
        raise ValueError("Hours cannot be more than 168 in a week")



def split_hours(total_hours):

    check_hours(total_hours)

    if total_hours > OVERTIME_HOURS:
        regular_hours = OVERTIME_HOURS
        overtime_hours = total_hours - OVERTIME_HOURS
    else:
        regular_hours = total_hours
        overtime_hours = 0

    return regular_hours, overtime_hours


def calculate_gross_pay(pay_rate, regular_hours, overtime_hours):
    # gross pay = pay before anything is taken out
    check_pay_rate(pay_rate)
    check_hours(regular_hours)
    check_hours(overtime_hours)

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * OVERTIME_RATE
    gross_pay = regular_pay + overtime_pay

    return round(regular_pay, 2), round(overtime_pay, 2), round(gross_pay, 2)


def calculate_deductions(gross_pay, extra_deductions=None):
    # deductions = money taken out of the paycheck
    # extra_deductions is a dictionary like {"health_insurance": 25}
    if gross_pay < 0:
        raise ValueError("Gross pay cannot be negative")

    federal = round(gross_pay * FEDERAL_TAX, 2)
    social = round(gross_pay * SOCIAL_SECURITY, 2)
    medicare = round(gross_pay * MEDICARE, 2)
    total = federal + social + medicare

    deductions = {
        "federal_tax": federal,
        "social_security": social,
        "medicare": medicare,
    }

    # add any extra deductions that belong to this employee
    if extra_deductions != None:
        for name in extra_deductions:
            amount = extra_deductions[name]
            if amount < 0:
                raise ValueError("Deductions cannot be negative")
            deductions[name] = round(amount, 2)
            total = total + amount

    deductions["total"] = round(total, 2)
    return deductions


def calculate_net_pay(gross_pay, total_deductions):
    # net pay = what the employee actually takes home
    if total_deductions > gross_pay:
        raise ValueError("Deductions cannot be more than gross pay")

    return round(gross_pay - total_deductions, 2)


#  putting it all together 

def calculate_pay(pay_rate, total_hours, extra_deductions=None):
    # does the whole calculation for one employee
    regular_hours, overtime_hours = split_hours(total_hours)
    regular_pay, overtime_pay, gross_pay = calculate_gross_pay(
        pay_rate, regular_hours, overtime_hours)
    deductions = calculate_deductions(gross_pay, extra_deductions)
    net_pay = calculate_net_pay(gross_pay, deductions["total"])

    # last check on our answer to make sure it makes sense
    if net_pay < 0 or net_pay > gross_pay:
        raise ValueError("Something went wrong with the net pay")

    result = {
        "pay_rate": pay_rate,
        "regular_hours": regular_hours,
        "overtime_hours": overtime_hours,
        "regular_pay": regular_pay,
        "overtime_pay": overtime_pay,
        "gross_pay": gross_pay,
        "deductions": deductions,
        "net_pay": net_pay,
    }
    return result


