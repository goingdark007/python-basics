from datetime import datetime

d1 = int(input("Enter date of birth: "))
m1 = int(input("Enter month of birth: "))
y1 = int(input("Enter year of birth: "))

d2 = datetime.now().day
m2 = datetime.now().month
y2 = datetime.now().year

r3 = y2 - y1 
r2 = m2 - m1 
r1 = d2 - d1 

if r2<0:
    r3 = r3 - 1
    r2 = r2 + 12


if r1<0:
    r2 = r2 - 1 
    r1 = r1 + 31
    

print(f'year {r3} month {r2} day {r1}')