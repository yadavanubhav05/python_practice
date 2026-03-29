try:
    x = int(input("Enter a number: "))
    print(10/x)
except ValueError:
    print("Invalid input, please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")