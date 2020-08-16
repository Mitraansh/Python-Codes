import calendar
j=0
a=int(input("enter year"))
x=int(input("enter month"))
z=int(input("enter day"))
q=int(calendar.monthrange(a,x)[1])
while x>=1 :
    y=int(calendar.monthrange(a,x)[1])
    j+=y
    x=x-1
l=q-z
m=j-l
print("Day of the year:",m)


