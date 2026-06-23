import pandas as pd

data = {
    "student_id" : [],
    "first_name" : [],
    "last_name" : [],
    "DateOfBirth" : [],
    "Gender" : [],
    "Email_address" : [],
    "Phone_number" : [],
    "Guardian_Name" : [],
    "Relationship" : [],
    "G_contact" : [],
    "G_email" : [],
    
}
try:
    df =  pd.read_excel("students.xlsx")
    data = df.to_dict(orient=list)
    
except:
    "jji"
cont = True

while(cont):
    student_id = input("Enter StudentID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    DateOfBirth = input("Enter Date of Birth: ")
    Gender = input("Enter Gender: ")
    Email_address = input("Enter Email Address: ")
    Phone_number = input("Enter Phone Number: ")
    Guardian_Name = input("Enter the Guardian name: ")
    Relationship =  input("Enter Relationship: ")
    G_contact =  input("Enter contact number: ")
    G_email =  input("Enter Guardian email: ")

    data["student_id"].append(student_id)
    data["first_name"].append(first_name)
    data["last_name"].append(last_name)
    data["DateOfBirth"].append(DateOfBirth)
    data["Gender"].append(Gender)
    data["Email_address"].append(Email_address)
    data["Phone_number"].append(Phone_number)
    data["Guardian_Name"].append(Guardian_Name)
    data["Relationship"].append(Relationship)
    data["G_contact"].append(G_contact)
    data["G_email"].append(G_email)

    is_cont =  input("Do you want enter more data(yes/no): ").lower()
    if is_cont ==  "no":
        cont = False

df = pd.DataFrame(data)

df.to_excel("students.xlsx",index=False)