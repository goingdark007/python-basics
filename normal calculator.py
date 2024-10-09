a = input("What arithmetic operation would you like to perform? :")
b = float(input("Enter the first number:"))
c = float(input("Enter the first number:"))
if a == "+" :
  print(b + c)
elif a == "-" :
  print(b - c)
elif a == "*" :
  print(b * c)
elif a == "/" :
  print(b / c)
else :
  print("Invalid input")