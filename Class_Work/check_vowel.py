# Open file in read mode
file = open("firstfile.txt", "r")

data = file.read()

count = 0
vowels = "aeiouAEIOU"

for ch in data:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

file.close()
