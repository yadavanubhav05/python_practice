student = {
"name": "Rakesh",
"age": 30,
"course": "Python"
}

# print(student["name"])
# print(student.get("age"))

# student["age"] = 36
# student["name"] = "Naresh"
# print(student["name"])
# print(student["age"])

for key, value in student.items():
    print(f"{key}: {value}")