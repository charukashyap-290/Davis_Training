"""Question 3: Remove Common Elements from Two Lists
Problem Statement:
Remove elements from the first list that are present in the second list.
Input:
List1 = [1, 2, 3, 4], List2 = [3, 4, 5]
Output:
[1, 2]"""

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

result = []

for item in list1:
    if item not in list2:
        result.append(item)

print(result)
