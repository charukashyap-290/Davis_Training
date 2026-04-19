#Question 2: List Rotation
#Problem Statement:
#Rotate a list to the right by k positions.
#Input:
#List = [10, 20, 30, 40, 50], k = 2
#Output:
#[40, 50, 10, 20, 30]

# Rotate a list to the right by k positions

my_list = [10, 20, 30, 40, 50]
k = 2

# Handle cases where k > length of list
k = k % len(my_list)

# Rotation logic
rotated_list = my_list[-k:] + my_list[:-k]

print("Rotated List:", rotated_list)
