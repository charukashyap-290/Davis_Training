'''Question 11: Remove Empty Sets from List
Problem Statement:
Remove all empty sets from a list of sets.
Input:
[{1, 2}, set(), {3, 4}, set()]
Output:
[{1, 2}, {3, 4}]'''

lst = [{1, 2}, set(), {3, 4}, set()]

result = []

for item in lst:
    if item:
        result.append(item)

print(result)
