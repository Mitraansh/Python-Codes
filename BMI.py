k=1
while k==1:
    weight=float(input("enter weight in kg"))
    height=float(input("enter height in meters"))
    BMI=weight/(height**2)
    print("BMI : ",BMI)
    print("continue(yes or no)")
    x=input()
    if(x=="yes"):
        k=1
    else:
        break


