import math
k=1
while k==1:
    x=int(input("enter value"))
    y=int(input("enter value"))
    z=int(input("enter value"))
    a=4*x**4+3*y**3+9*z+6*math.pi
    print(a)
    print("Again(yes or no)")
    x=input()
    if(x=="yes"):
        k=1
    else:
        break
    
