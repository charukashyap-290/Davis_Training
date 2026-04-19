'''Question 13: Flatten Nested List
Problem Statement:
Flatten a nested list (1 level deep).
Input:
[[1, 2], [3, 4], [5]]
Output:
[1, 2, 3, 4, 5]'''


nested = [[1, 2], [3, 4], [5]]

flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)
