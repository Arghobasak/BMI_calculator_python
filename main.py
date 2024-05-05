# For loop and if, else statements using

print("Male and Female BMI calculator !!")
age = int(input("\n\nEnter your age: "))
height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

BMI = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
BMI1 = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

print("\nYour BMI is (Male): " + str(BMI)+ " calory")
print("Your BMI is (Female): "+ str(BMI1)+ " calory")

workout = input("\nDo you work out(y/n)?: ")
for _ in workout: 
  if workout == "y": 
    print("Your corect BMI is: "+str(BMI * 1.2)+ " calory")
  elif workout == "y": 
    print("Your corect BMI is: "+str(BMI1 * 1.2)+ " calory")
  else: 
    print("Okay")
    break

lightwork = input("Do you light work out and weekly 2-3 days playing (y/n)?: ")
for _ in lightwork: 
  if lightwork == "y": 
    print("Your corect BMI is: "+str(BMI * 1.375)+ " calory")
  elif lightwork == "y": 
    print("Your corect BMI is: "+str(BMI1 * 1.375)+ " calory")
  else: 
    print("Okay")
    break

workout2 = input("Do you work out and weekly 2-3 very playing (y/n)?: ")
for _ in workout2:
  if workout2 == "y": 
    print("Your corect BMI is: "+str(BMI * 1.55)+ " calory")
  elif workout2 == "y": 
    print("Your corect BMI is: "+str(BMI1 * 1.55)+ " calory")
  else: 
    print("Okay")
    break

workout3 = input("Do you work out and weekly everyday very playing (y/n)?: ")
for _ in workout3: 
  if workout3 == "y": 
    print("Your corect BMI is: "+str(BMI * 1.725)+ " calory")
  elif workout3 == "y": 
    print("Your corect BMI is: "+str(BMI1 * 1.725)+ " calory")
  else: 
    print("Okay")
    break

hardwork = input("Do you hardworkout and very runing, playing (y/n)?: ")
for _ in hardwork: 
  if hardwork == "y": 
    print("Your corect BMI is: "+str(BMI * 1.9)+ " calory")
  elif hardwork == "y": 
    print("Your corect BMI is: "+str(BMI1 * 1.9)+ " calory")
  else: 
    print("Okay")
    break
print("\nThank you for using my BMI calculator !!")