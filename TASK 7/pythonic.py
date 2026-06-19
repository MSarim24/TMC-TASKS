numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]
print(squares)

square_dict = {num: num ** 2 for num in numbers}
print(square_dict)

nums = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = {num for num in nums}
print(unique_numbers)

generator = (num ** 2 for num in range(5))

for value in generator:
    print(value, end=" ")

print()

square = lambda x: x ** 2
print(square(6))

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

names = ["Muhammad", "Ali", "Sara", "Ayesha"]

sorted_names = sorted(names, key=len)
print(sorted_names)

for index, name in enumerate(names):
    print(index, name)

ages = [20, 22, 19, 25]

for name, age in zip(names, ages):
    print(f"{name} -> {age}")


class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")


while True:
    try:
        age = int(input("Enter your age: "))
        validate_age(age)

    except ValueError:
        print("Please enter a valid integer.")

    except InvalidAgeError as error:
        print(error)

    else:
        print(f"Valid age entered: {age}")
        break

    finally:
        print("Validation attempt completed.\n")