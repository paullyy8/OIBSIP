print("Welcome to FitCalc -- BMI Calculator")

weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

BMI = weight / (height * height)

print(f"Your BMI index is: {BMI}")
