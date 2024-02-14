
emno = int(input())
empname = input()
designation = input()
basic = int(input())
hra = int(input())
da = int(input())
ta = int(input())


netsalary = basic + da + ta + hra


if netsalary > 50000:
    tax = 0.05 * netsalary
elif netsalary > 35000:
    tax = 0.03 * netsalary
elif netsalary > 20000:
    tax = 0.01 * netsalary
else:
    tax = 0


print(f"Employee Number: {emno}")
print(f"Employee Name: {empname}")
print(f"Designation: {designation}")
print(f"Basic Salary: {basic}")
print(f"HRA: {hra}")
print(f"DA: {da}")
print(f"TA: {ta}")
print(f"Net Salary: {netsalary}")
print(f"Tax: {tax}")
