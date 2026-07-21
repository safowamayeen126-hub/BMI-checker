# Project: BMI Checker
# Name: Safowa Mayeen(captain),Araf(member),Sourjo(member),Kabbo(member)

print("      WELCOME TO BMI CHECKER      ")

while True:
    print("\n Enter Your Information")
    print("-" *27)

    # Weight Input Validation
    while True:
        weight = float(input(" Enter your weight (kg): "))
        if weight > 0:
            break
        print("Weight must be greater than 0!")

    # Height Input Validation
    while True:
        height_cm = float(input(" Enter your height (cm): "))
        if height_cm > 0:
            break
        print("Height must be greater than 0!")

    # Convert cm to meter
    height = height_cm / 100

    # BMI Calculation
    bmi = weight / (height ** 2)

    print("Your BMI is:", bmi)


    # BMI Category
    if bmi < 18.5:
        print(" Category: Underweight")
        print("-" * 10)
    
        print(" Advice: Eat nutritious foods and consult a doctor if needed.")
        print("-" * 8)
    elif bmi < 25:
        print(" Category: Normal Weight")
        print("-" * 10)
        print(" Advice: Great! Maintain your healthy lifestyle.")
        print("-" * 8)
    elif bmi < 30:
        print(" Category: Overweight")
        print("-" * 10)
        print(" Advice: Exercise regularly and reduce junk food.")
        print("-" * 8)
    else:
        print(" Category: Obese")
        print("-" * 10)
        print(" Advice: Consult a doctor and start a healthy diet plan.")
        print("-" * 8)
    
    break

print("\n Thank you for using BMI Checker!")
print(" Stay Healthy & Have a Nice Day!")
