# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# age = input("Enter your age: ")

# try:
#     age = int(age)
#     print(f"You entered: {age}")
# except ValueError:
#     print("Please enter numbers only :)")

values = [10, 60, 30, 80, 45, "abc"]
for value in values:
    try:
        num = int(value)
        print(f"Value '{value}' is a number: {num}")
    except ValueError:
        print(f"Value '{value}' is not a number, skipping")