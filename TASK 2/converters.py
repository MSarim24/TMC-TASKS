def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def BMI(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


while True:
    print("\n=== Converter Menu ===")
    print("1. KM to Miles")
    print("2. Miles to KM")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. BMI Calculator")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")

    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")

    elif choice == "3":
        c = float(input("Enter temperature in °C: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

    elif choice == "4":
        f = float(input("Enter temperature in °F: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")

    elif choice == "5":
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        result = BMI(weight, height)

        print(f"Your BMI is {result:.2f}")

        if result < 18.5:
            print("Category: Underweight")
        elif result < 25:
            print("Category: Normal")
        elif result < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


