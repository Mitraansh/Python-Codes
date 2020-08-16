import datetime
print ("current date:" ,datetime.datetime.now().strftime("%d/%B/%y"))
x=int(datetime.date.today().strftime("%d"))

import calendar
y=int(calendar.monthrange(2019,x)[1])
z=y-x
print("No. of days left in current month:",end='')
print(z)

input()

