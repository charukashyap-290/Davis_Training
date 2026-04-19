#Question 2: Check whether a person is eligible to vote.
#Input: Enter age
#Output: Eligible / Not Eligible
#Answer:-
# Program to check voting eligibility

# Taking input from user
# Using ternary operator (short logic)

age = int(input("Enter your age: "))

result = "Eligible to vote" if age >= 18 else "Not eligible to vote"

print(result)


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

 # Using function + boolean return

def is_eligible(age):
    return age >= 18

age = int(input("Enter your age: "))

if is_eligible(age):
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#METHOD 4

# Using try-except

try:
    age = int(input("Enter age: "))
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
except:
    print("Invalid input")


#METHOD 5

# Direct boolean output

age = int(input("Enter age: "))

print("Eligible" if age >= 18 else "Not Eligible")
     

#METHOD 6

n = int(input("Enter number of persons: "))

for i in range(n):
    age = int(input("Enter age: "))
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")


#METHOD 7

# Count eligible voters

n = int(input("Enter number of people: "))

eligible_count = 0

for _ in range(n):
    age = int(input("Enter age: "))
    if age >= 18:
        eligible_count += 1

print("Total eligible voters:", eligible_count)


#METHOD 8

while True:
    age = int(input("Enter age: "))

    if age < 0:
        print("Invalid age")
    else:
        break

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
    
