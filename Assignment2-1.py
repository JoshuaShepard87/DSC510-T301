# Joshua Burden
# DSC510-T301 Introduction to Programming (2225-1)
# Michael Eller
# Bellevue University
# 03/27/2022

# Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Refer to the submission instructions for an example of a header.
# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# Include appropriate comments throughout the program.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.








user = input('what is your name?')
print(f'Welcome, {user}!')
company = input('Where you work?')
feet_of_cable = int(input('How much feet do you need of that cable, yo?'))
maff = float(0.87)
total_temp = feet_of_cable * maff
cost = '${:,.2f}'.format(total_temp)
print(f'Well... {user}, that works at {company}, you wanted {feet_of_cable} feet of cable which costs {cost}... good job or something. ')
print(f'good bye {user}')

        
    
def calculate_pay(hourly_pay_rate, work_hours, 
                  overtime_pay_rate, overtime_work_hours, 
                  is_eligible_overtime_rate):
  total_pay = 0
  totay_pay = hourly_pay_rate * work_hours
  if is_eligible_overtime_rate:
    total_pay = total_pay + overtime_pay_rate * overtime_work_hours
  else:
    total_pay = total_pay + hourly_pay_rate * overtime_work_hours
  return total_pay