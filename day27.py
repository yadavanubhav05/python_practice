# try:
#     x = int(abc)
# except NameError:
#     print("Not a number")

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Cannot divide by zero")

# print(divide(10, 0))

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Both arguments must be numbers")
print(safe_divide(10, 0))
print(safe_divide(10, "a"))