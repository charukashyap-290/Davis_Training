'''Question 1: Find Duplicate Elements in a List Problem Statement: Write a program to find all duplicate elements in a given list. 
Input: [1, 2, 3, 2, 4, 5, 1] 
Output: [1, 2]'''

# Find duplicate elements in a list

my_list = [1, 2, 3, 2, 4, 5, 1]

duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate elements:", duplicates)
