# module datetime

from datetime import datetime
# imports date time

n = datetime.now()
# stores current date and time in n

print(n)
#prints it

n = datetime.now().day
# stores current day in n

print(n)
#prints it

n = datetime.now().month
# stores current month in n

print(n)
#prints it

n = datetime.now().year
# stores current year in n

print(n)
#prints it

n = datetime.today()
# stores current local date and time in n

print(n)
#prints it

n = datetime.today().date()
# stores only current local date in n

print(n)
#prints it

m = '2024-10-13 13:44:40'
# string

n = datetime.strptime(m,'%Y-%m-%d %H:%M:%S')
# converts string into datetime object

print(n)
#prints it

m = datetime.now()
# gets current datetime object

n = m.strftime('%Y-%m-%d %H:%M:%S')
# converts or formats datetime object

print(n)
#prints it