"""
principle = p
num of years = n
interest rate = r
simple intrest rate = sir
"""

p = int(input("Please enter princliple: "))
n = int(input("Please enter number of years: "))
r = float(input("Please enter interest rate: "))

sir = (p*n*r)/100

print("Simple intrest rate: " + str(sir))