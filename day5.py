#Creating a dictionary

person = {
    "name": "Anubhav",
    "age": 30,
    "city": "GGN"
}

# print(f"Name of person is : ", person["name"])
# print(person["age"])

# person["age"] = 35

# print(f"Updated age of person is : ", person["age"])

# for key in person:
#     print(f"{key} : {person[key]}")

marks = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

count = 0
for values in marks.values():
    if values > 80:
        count += 1
print(f"Number of subjects with marks greater than 80: ", count)