name = input("Enter the name of an employee: ")
company = input("Enter the institute: ")
funcAmount = int(input("Enter the functionary amount: "))
monthlyPayment = float(input("Enter the month payment average: "))

print(name + " work at the company " + company)
print("The", company, "has:", funcAmount, "employees ")
print("The monthly payment average is: " + str(monthlyPayment))

print(" ")
print("======Check the data type below=======")
print(" ")

print("The data type of the variable [name] is: ", type(name))
print("The data type of the variable [company] is: ",  type(company))
print("The data type of the variable [funcAmount] is: ",  type(funcAmount))
print("The data type of the variable [monthlyPayment] is: ",  type(monthlyPayment))