p = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate in % (r): "))
n = int(input("Enter the number of years (n): "))
a=p*(1+r/100)**n
print(f"Total Amount after {n} years (A): {a}")
