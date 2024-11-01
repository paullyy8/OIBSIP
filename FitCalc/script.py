print("\n")
print("Welcome to FitCalc -- Your Personal BMI Calculator!")

# Prompt for user to fetch the weight and height with a friendly tone
print("\n")
weight = float(input("🌟 Enter your weight in kilograms (kg): "))
height = float(input("📏 Now, please enter your height in centimeters (cm): "))

# Formula to calculate the BMI
BMI = weight / (height / 100) ** 2

# Making the BMI a round figure
BMI_rounded = round(BMI, 2)

# Classify the BMI
if BMI < 18.5:
    classification = "underweight 😕"
elif 18.5 <= BMI < 24.9:
    classification = "healthy 😊"
elif 25 <= BMI < 29.9:
    classification = "overweight 😟"
else:
    classification = "obese"

# Print the user's BMI and the classification in a more engaging way
print("\n" + "-" * 70)
print(f"\n🎉 Your BMI index is: {BMI_rounded}")
print(f"🏷️ Based on your input, you are classified as: {classification}")
print("-" * 70)
print("\n")