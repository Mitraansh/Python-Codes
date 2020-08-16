import math
k=1
while k==1:
    x=float(input("enter radius"))
    ans= math.pi*(x**2)
    print("Area of circle:",ans)
    print("Again(yes or no)")
    x=input()
    if(x=="yes"):
        k=1
    else:
        break
