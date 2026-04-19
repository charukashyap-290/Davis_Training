'''Question 14: Symmetric Difference of Sets
Problem Statement:
Find elements that are in either of the sets but not in both.
Input:
Set1 = {1, 2, 3}, Set2 = {3, 4, 5}
Output:
{1, 2, 4, 5}'''


set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 ^ set2

print(result)
