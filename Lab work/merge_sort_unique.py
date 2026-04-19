'''Question 9: Merge and Sort Unique Elements
Problem Statement:
Merge two lists and return a sorted list of unique elements.
Input:
[3, 1, 2], [2, 4, 5]
Output:
[1, 2, 3, 4, 5]'''


list1 = [3, 1, 2]
list2 = [2, 4, 5]

merged = list1 + list2

unique = list(set(merged))
unique.sort()

print(unique)
