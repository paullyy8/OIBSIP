print("Welcome to FitCalc -- BMI Calculator")

#Prompt for user to fetch the weight and height 
weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

#formula to calculate the BMI
BMI = weight / (height * height)

#making the BMI as round figure
BMI_rounded = round(BMI, 2)

# Classify the BMI
if BMI < 18.5:
    classification = "underweight"
elif 18.5 <= BMI < 24.9:
    classification = "normal weight"
elif 25 <= BMI < 29.9:
    classification = "overweight"
else:
    classification = "obese"

#print the user's BMI and the calssification
print(f"Your BMI index is: {BMI_rounded}")
print(f"You are classified as: {classification}")
