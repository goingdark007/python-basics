weight = float(input("Enter your weight in kg:  "))
height = float(input("Enter your height in m: "))
bmi = weight / (height**2)

if bmi < 18.5:
  print(f"Your BMI is {bmi:.2f}, you are underweight.")
  
elif bmi >= 18.5 and bmi < 25:
  print(f"Your BMI is {bmi:.2f}, you have a normal weight.")

elif bmi >= 25 and bmi < 30:
  print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")

else:
  print(f"Your BMI is {bmi:.2f}, you are obese.")