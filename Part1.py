# Calculate simple interest by gathering three things (principle, number of years, rate of interest).
# Get user input for p (p = principle).
# Get user input for n (n = number of years).
# Get user input for r (r = rate of interest).
# Convert user inputs p, n, r to int().Links to an external site.
# Calculate the simple interest of p, n, r (multiple p, n, r, and then divide by 100).
# Print out the simple interest value.

p = int(input("Enter principle: "))
n = int(input("Enter number of years: "))
r = int(input("Enter rate of interest: "))

simpleInterest = ((p * r * n) / 100)
print(simpleInterest)

