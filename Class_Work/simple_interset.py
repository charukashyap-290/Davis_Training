def calculate(p,r,t):
    return((p*r*t)/100)
principal = float(input("Enter principal(in rs):"))
rate = float(input("Enter rate of interest(in %):"))
time = int(input("Enter time (in year):"))
print("Simple interest: Rs", calculate (principal,rate,time))
