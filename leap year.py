a = int(input("Enter the number :"))
if (a%400==0):
  print("The year is leap year")
elif (a%100!=0and a%4==0):
  print("The number is leap year")
else:
  print("The number is not leap year")