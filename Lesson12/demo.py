def get_weight_and_height():
    while True:
        try:
            weight = float(input("Enter your weight: "))
            height = float(input("Enter your height: "))

            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            return weight, height
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter positive numbers.")

def convert_units(weight, height):
    unit_choice = input("Do you want to use (1) Metric (kg/m) or (2) Imperial (lbs/ft)? Enter 1 or 2: ")

    if unit_choice == "1":
        return weight, height
    elif unit_choice == "2":
        weight = weight * 0.453592  # lbs to kg
        height = height * 0.3048  # ft to meters
        return weight, height
    else:
        print("Invalid choice. Defaulting to Metric (kg/m).")
        return weight, height

def calculate_bmi(weight, height, is_child=False):
    if is_child:
        # Adjustment for children - you can use a different calculation for children if needed
        # We will assume a similar formula but with different thresholds for underweight, etc.
        bmi = weight / (height ** 2)
        return bmi
    else:
        bmi = weight / (height ** 2)
        return bmi

def categorize_bmi(bmi, is_child=False):
    if is_child:
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18.5:
            return "Normal weight"
        else:
            return "Obese"
    else:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

def display_result(bmi, category):
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

def bmi_app():
    print("Welcome to the BMI Calculator!")

    # Ask if it's an adult or child
    is_child_input = input("Are you calculating for an adult or a child? (Enter 'adult' or 'child'): ").strip().lower()
    is_child = is_child_input == "child"

    # Get weight and height
    weight, height = get_weight_and_height()

    # Convert units if necessary
    weight, height = convert_units(weight, height)

    # Calculate BMI
    bmi = calculate_bmi(weight, height, is_child)

    # Categorize BMI
    category = categorize_bmi(bmi, is_child)

    # Display result
    display_result(bmi, category)

# Run the app
bmi_app()
