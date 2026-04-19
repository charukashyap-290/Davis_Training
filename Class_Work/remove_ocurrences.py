# Step 1: Take a list of 15 numbers from user
numbers = []
print("Enter 15 numbers:")
for i in range(15):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 2: Ask user for the number to search
target = int(input("Enter the number to search: "))

# Step 3: Check if number exists
if target in numbers:
    first_index = numbers.index(target)

    # Step 4: Keep first occurrence, remove others
    result = []
    count = 0

    for num in numbers:
        if num == target:
            count += 1
            if count == 1:
                result.append(num)  # keep first occurrence
            # skip other occurrences
        else:
            result.append(num)

    print("Updated list:", result)
else:
    print("Number not found in the list.")
