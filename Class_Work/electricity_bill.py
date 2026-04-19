#Qestion 3:  Calculate electricity bill based on units consumed.
#Input: Enter units
#Output: Total bill amount

#METHOD 1

units = int(input("Enter units consumed: "))
bill_amount = 0

if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = (100 * 5) + (units - 100) * 7
else:
    bill_amount = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total electricity bill is:", bill_amount)

#METHOD 2

# Using ternary operator (short logic)

# Program to check voting eligibility

# Taking input from user
age = int(input("Enter your age: "))

# Checking eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
     

#METHOD 3

# Using dictionary for slab rates

units = int(input("Enter units consumed: "))

rates = {100: 5, 200: 7, "above": 10}
bill = 0

if units <= 100:
    bill = units * rates[100]
elif units <= 200:
    bill = 100 * rates[100] + (units - 100) * rates[200]
else:
    bill = 100 * rates[100] + 100 * rates[200] + (units - 200) * rates["above"]

print("Total bill:", bill)


#METHOD 4

# Using while loop step calculation

units = int(input("Enter units: "))
bill = 0

i = 1
while i <= units:
    if i <= 100:
        bill += 5
    elif i <= 200:
        bill += 7
    else:
        bill += 10
    i += 1

print("Total bill:", bill)


#METHOD 5

# Using function

def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10

units = int(input("Enter units: "))
print("Total bill:", calculate_bill(units))


#METHOD 6

# Electricity bill + discount

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

# Discount condition
if bill > 1000:
    bill = bill * 0.9

print("Final bill:", bill)


#METHOD 7

units = int(input("Enter units: "))
rate = 6

bill = units * rate

print("Total bill:", bill)

if bill > 1000:
    print("High electricity usage")
