basic = float(input("Enter your basic salary: "))
dearness_allowance = basic * 32/100
house_rent = basic * 15/100
city_compensatory_allowance = 584

net_salary = basic + dearness_allowance + house_rent + city_compensatory_allowance
print("basic salary is: ", basic)
print("dearness allowance is: ", dearness_allowance)
print("house rent  is: ", house_rent)
print("city compensatory allowance is: ", city_compensatory_allowance)
print("net salary is",net_salary)