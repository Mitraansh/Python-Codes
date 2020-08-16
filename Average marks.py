k=1
while k==1:
    a=int(input("Enter marks in first subject"))
    b=int(input("Enter marks in first subject"))
    c=int(input("Enter marks in first subject"))
    d=int(input("Enter marks in first subject"))
    e=int(input("Enter marks in first subject"))
    avg=(a+b+c+d+e)/5
    print("Average marks:",avg)
    print("Again(yes or no)")
    x=input()
    if(x=="yes"):
        k=1
    else:
        break
    
