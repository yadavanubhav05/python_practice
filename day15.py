# with open ("users.csv", "r") as file:
#     for line in file:
#         print(line.strip())

# with open("users.csv", "r") as file:
#     next(file)  # Skip the header line
#     for line in file:
#         parts = line.strip().split(",")
#         if int(parts[2]) > 5:
#             print(parts[0], parts[1])

count = 0
with open("users.csv", "r") as file:
    next(file)  # Skip the header line
    for line in file:
        count += 1
print("Total users:", count)