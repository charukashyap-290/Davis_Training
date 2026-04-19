'''Question 6: Find Maximum and Minimum in Tuple
Problem Statement:
Find the maximum and minimum elements in a tuple without using built-in functions.
Input:
(5, 1, 8, 3)
Output:
Max = 8, Min = 1'''

t = (5, 1, 8, 3)

max_val = t[0]
min_val = t[0]

for item in t:
    if item > max_val:
        max_val = item
    if item < min_val:
        min_val = item

print("Max =", max_val)
print("Min =", min_val)
