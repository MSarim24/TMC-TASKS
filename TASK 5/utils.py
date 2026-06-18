import time
import os

def FIZZBUZZ():
    for number in range(1,100):
        if number % 15 == 0:
            print("FIZZBUZZ")   
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")

def multiplication_table():
    for row in range(1, 11):
        for col in range(1, 11):
            print(f"{row * col:4}", end="")
        print()

def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
def number_guessing_game():
    import random
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

def word_count(string):
    word_count = {}
    for word in string.split():
        word = word.strip('.,!?";:()[]{}')
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    
    print("\nWord Count:")
    for word, count in word_count.items():  
        print(f"{word}: {count}")

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

def converter_menu():
    os.system('cls')
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


def loading():
    string1 = "|-----------------------------------------------------------------------------------------------------------|"
    string2 = ""
    string3 = "|-----------------------------------------------------------------------------------------------------------|"

    print(string1)
    print(string2)
    print(string3) 
    for i in range(107):
        string2 += "="
        print("\x1b[2A", end="")
        print(f"|{string2}{' ' * (107 - len(string2))}|")
        print("\x1b[1B", end="", flush=True)
        time.sleep(0.02)

    time.sleep(1)
    os.system('cls')

def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def update_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")
def contact_management():
    contacts = {}
    while True:
        
        os.system('cls')
        print("\n=== Contact Management ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number: ")
            update_contact(contacts, name, phone)

        elif choice == "4":
            name = input("Enter contact name to delete: ")
            delete_contact(contacts, name)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

        loading()


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. FizzBuzz")
        print("2. Multiplication Table")
        print("3. Simple Calculator")
        print("4. Number Guessing Game")
        print("5. Word Count")
        print("6. Converter")
        print("7. Contact Management")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            FIZZBUZZ()
        elif choice == "2":
            multiplication_table()
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")
            result = simple_calculator(num1, num2, operator)
            print(f"Result: {result}")
        elif choice == "4":
            number_guessing_game()
        elif choice == "5":
            string = input("Enter a string: ")
            word_count(string)
        elif choice == "6":
            converter_menu()
        elif choice == "7":
            contact_management()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

        loading()

main()