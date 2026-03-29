# def add(a,b):
#     """Returns the sum of a and b."""
#     return a + b

# print("Inputs both numbers:")
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# result = add(a, b)
# print(f"The sum of {a} and {b} is {result}")

# def is_even(num):
#     """Returns True if num is even, False otherwise."""
#     return num % 2 == 0

# number = int(input("Enter a number: "))
# print(is_even(number))


def count_above_50(marks):
    """Returns the count of marks above 50."""
    count = 0
    for mark in marks:
        if mark > 50:
            count += 1
    return count

marks = {
    "Math": 85,
    "Science": 78,
    "English": 45,
    "History": 92,
    "Geography": 55
}

print(f"Number of subjects with marks above 60 is : ", count_above_50(marks.values()))