# Input salary
salary = float(input("Enter your salary: "))

# Calculate tax rate
if salary < 30000:
    tax_rate = 0.05
elif salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

# Calculate tax
tax = salary * tax_rate

# Output result
print("Salary:", salary)
print("Tax Rate:", tax_rate * 100, "%")
print("Tax Amount:", tax)
