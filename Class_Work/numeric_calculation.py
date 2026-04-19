# functions

def calculatesum(x, y):
    return x + y

def calculatedifference(x, y):
    return x - y

def calculateproduct(x, y):
    return x * y

def dividenumber(x, y):
    if y == 0:
        return "Division by zero not allowed"
    return x / y

def calculatemodule(x, y):
    return x % y
m = 10
n = 20

print("Sum is:", calculatesum(m, n))
print("Difference is:", calculatedifference(m, n))
print("Product is:", calculateproduct(m, n))
print("Division is:", dividenumber(m, n))
print("Modulus is:", calculatemodule(m, n))
