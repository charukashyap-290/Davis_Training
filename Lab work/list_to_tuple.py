'''Question 5: Convert List to Tuple and Remove Duplicates
Problem Statement:
Convert a list into a tuple after removing duplicate elements.
Input:
[1, 2, 2, 3, 4, 4]
Output:
(1, 2, 3, 4)'''

lst = [1, 2, 2, 3, 4, 4]

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

result = tuple(unique)

print(result)
