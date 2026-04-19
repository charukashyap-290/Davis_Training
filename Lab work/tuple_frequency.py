
'''Question 4: Tuple Element Frequency
Problem Statement:
Count the frequency of each element in a tuple.
Input:
(1, 2, 2, 3, 1, 4)
Output:
{1: 2, 2: 2, 3: 1, 4: 1}'''

t = (1, 2, 2, 3, 1, 4)

freq = {}

for item in t:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)
