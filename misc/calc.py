print("Enter the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the number corresponding to the operation: ")

# validate operation first
if operation not in ['1', '2', '3', '4']:
    print("Selected operation is not allowed")
else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        print(f"The sum is {num1 + num2}")
    elif operation == '2':
        print(f"The difference is {num1 - num2}")
    elif operation == '3':
        print(f"The product is {num1 * num2}")
    elif operation == '4':
        if num2 != 0:
            print(f"The quotient is {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
