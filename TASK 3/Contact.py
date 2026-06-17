import os
import time

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

while True:
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
        add_contact(name, phone)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        name = input("Enter contact name to update: ")
        phone = input("Enter new phone number: ")
        update_contact(name, phone)

    elif choice == "4":
        name = input("Enter contact name to delete: ")
        delete_contact(name)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")

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
