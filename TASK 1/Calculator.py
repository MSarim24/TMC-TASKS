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
    
string = input("Enter the first number, operator, and second number (e.g., 5 + 3): ")
num1, operator, num2 = string.split()
num1 = float(num1)
num2 = float(num2)
result = simple_calculator(num1, num2, operator)
print("Result:", result)   
