def right_triangle(lines):
    for i in range(lines):
        for j in range(i+1):
            print("*",end="")
        print()

def left_triangle(lines):
    for i in range(lines):
        for j in range(lines-(i+1)):
            print(" ", end="")

        for k in range(i+1):
            print("*",end="")
        print()

def inverted_right_triangle(lines):
    for i in range(lines):
        for j in range(lines - (i)):
            print("*",end="")
        print()

def inverted_left_triangle(lines):
    for i in range(lines):
        for k in range(i):
            print(" ",end="")
        for j in range(lines - (i)):
            print("*",end="")
        print()

def pyramid(lines):
    for i in range(lines):
        for j in range(lines-(i+1)):
            print(" ",end="")

        if i == 0:
            print("*",end="")
        else:
            for k in range(i*2+1):
                print("*",end="")
            
        print()


lines = int(input("Enter the number of lines for the patterns: "))
print("\nRight Triangle:")
right_triangle(lines)
print("\nLeft Triangle:")
left_triangle(lines)
print("\nInverted Right Triangle:")
inverted_right_triangle(lines)
print("\nInverted Left Triangle:")
inverted_left_triangle(lines)
print("\nPyramid:")
pyramid(lines)


def find_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


n = int(input("Enter a number to find all prime numbers up to it: "))
prime_numbers = find_prime_numbers(n)
print(f"Prime numbers up to {n}: {prime_numbers}")
