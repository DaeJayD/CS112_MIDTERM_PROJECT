import time
import turtle
# Daily Calorie and Macronutrient Calculator for weight loss, maintain, and muscle gain

# Turtle function to print all the user input and results in turtle window for better visibility.


def draw_background(gender, age, weight_kg, height_cm, activity_level):
    screen = turtle.Screen()
    screen.title("Daily Calorie Calculator Results")
    screen.bgcolor("lightgray")

    turtle.penup()
    turtle.goto(-200, 160)
    turtle.pendown()
    turtle.color("black")
    turtle.write("User Information:", font=("Arial", 14, "bold"))
    turtle.penup()
    turtle.goto(-200, 130)
    turtle.pendown()
    turtle.write(f"Gender: {gender.capitalize()}", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.write(f"Age: {age} years", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 70)
    turtle.pendown()
    turtle.write(f"Weight: {weight_kg} kg", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 40)
    turtle.pendown()
    turtle.write(f"Height: {height_cm} cm", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, 10)
    turtle.pendown()
    turtle.write(f"Activity Level: {activity_level.capitalize()}", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -20)
    turtle.pendown()
    turtle.write("Your estimated daily calorie requirement is:", font=("Arial", 14, "bold"))
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.write(f"{round(daily_calories, 2)} calories", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -80)
    turtle.pendown()
    turtle.write("Macronutrient Distribution:", font=("Arial", 14, "bold"))
    turtle.penup()
    turtle.goto(-200, -110)
    turtle.pendown()
    turtle.write(f"Protein: {round(protein, 2)} grams", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -140)
    turtle.pendown()
    turtle.write(f"Fat: {round(fat, 2)} grams", font=("Arial", 14, "normal"))
    turtle.penup()
    turtle.goto(-200, -170)
    turtle.pendown()
    turtle.write(f"Carbohydrates: {round(carb, 2)} grams", font=("Arial", 14, "normal"))
    turtle.pendown()

    turtle.done()


def calculate_macros(daily_calories, goal):  # Calculates daily macronutrient needs based on the user input
    if goal.lower() == 'loss':
        protein_percentage = 0.30
        fat_percentage = 0.25
        carb_percentage = 0.45
    elif goal.lower() == 'maintain':
        protein_percentage = 0.25
        fat_percentage = 0.30
        carb_percentage = 0.45
    elif goal.lower() == 'gain':
        protein_percentage = 0.35
        fat_percentage = 0.25
        carb_percentage = 0.40
    else:
        raise ValueError("Invalid goal. Choose from: loss, maintain, gain.")

    protein_calories = daily_calories * protein_percentage
    fat_calories = daily_calories * fat_percentage
    carb_calories = daily_calories * carb_percentage

    protein_grams = protein_calories / 4  # 4 calories per gram of protein
    fat_grams = fat_calories / 9  # 9 calories per gram of fat
    carb_grams = carb_calories / 4  # 4 calories per gram of carbohydrate

    return protein_grams, fat_grams, carb_grams

# Calculate the daily caloric need based on the given user data


def calculate_daily_calories(age, gender, weight_kg, height_cm, activity_level, goal):
    # Constants for activity levels
    ACTIVITY_LEVELS = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "athletic": 1.9
    }
    if activity_level.lower() not in ACTIVITY_LEVELS:
        raise ValueError("Invalid activity level. Choose 1 out of the 4.")

    # Constants for gender
    GENDER_FACTORS = {
        "male": 5,
        "female": -161
    }

    # Calculate BMR (Basal Metabolic Rate)
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + GENDER_FACTORS[gender]

    # Adjust BMR based on activity level
    calorie_multiplier = ACTIVITY_LEVELS[activity_level]
    daily_calories = bmr * calorie_multiplier

    # Adjust calories based on goals
    if goal == 'lose':
        daily_calories -= 500  # Create a calorie deficit for weight loss
    elif goal == 'gain':
        daily_calories += 500  # Create a calorie surplus for weight gain

    return daily_calories


# Get user input
print("Welcome to the Daily Calorie and Macronutrient Calculator!")
time.sleep(0.8)
age = int(input("Enter your age: "))
time.sleep(0.3)
gender = input("Enter your gender (male/female): ").lower()
time.sleep(0.3)
weight_kg = float(input("Enter your weight in kilograms: "))
time.sleep(0.3)
height_cm = float(input("Enter your height in centimeters: "))
time.sleep(0.3)
activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/athletic): ")
time.sleep(0.3)
goal = input("Enter your goal (lose/maintain/gain): ").lower()
time.sleep(0.3)
print("")
print("Please wait for your results")
time.sleep(1.5)

# Print the user input
print("\nUser Information:")
time.sleep(0.2)
print("Gender:", gender.capitalize())
time.sleep(0.2)
print("Age:", age, "years")
time.sleep(0.2)
print("Weight:", weight_kg, "kg")
time.sleep(0.2)
print("Height:", height_cm, "cm")
time.sleep(0.2)
print("Activity Level:", activity_level.capitalize())
time.sleep(0.2)

# Calculate and display daily calorie requirements
daily_calories = calculate_daily_calories(age, gender, weight_kg, height_cm, activity_level, goal)
time.sleep(0.2)
print("\nYour estimated daily calorie requirement is:", round(daily_calories, 2), "calories.")
protein, fat, carb = calculate_macros(daily_calories, goal)
time.sleep(0.2)
print("\nMacronutrient Distribution:")
time.sleep(0.2)
print("Protein: {} grams".format(round(protein, 2)))
time.sleep(0.2)
print("Fat: {} grams".format(round(fat, 2)))
time.sleep(0.2)
print("Carbohydrates: {} grams".format(round(carb, 2)))

draw_background(gender, age, weight_kg, height_cm, activity_level)
