
P = float(input("Enter principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter time in years: "))

CI_total = P * ((1+R /100) ** T)
CI = P * ((1+R /100) ** T) - P
SI = P * R * T / 100

print("The total amount is: ", CI_total)
print("Compound Interest is: ", CI)
print("Simple Interest is: ", SI)




