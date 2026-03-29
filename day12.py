numbers = [1,2,3,4,5,6,7,8,9,10]
squares = [] #empty list to store squares

# for n in numbers:
#     squares.append(n**2)
#     # print(n)
# print(f"Squares of numbers from 1 to 5: ", squares)

# even_numbers = []
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
# print(f"Even numbers from 1 to 10: ", even_numbers)

nums_grtr_than_5 = []
for n in numbers:
    if n > 5:
        nums_grtr_than_5.append(n)
print(f"Numbers greater than 5: ", nums_grtr_than_5)     