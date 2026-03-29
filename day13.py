# with open ("sample.txt", "r") as file:
#     content = file.read()
# print(content)

# with open ("sample.txt", "r") as file:
#     for line in file:
#         if line.startswith("ERROR") or line.startswith("error") or line.startswith("Error"):
#             print("Found an error line:", line.strip())

# with open ("output.txt", "w") as file:
#     file.write("hello from Python file handling")

count = 0
with open("sample.txt", "r") as file:
    for line in file:
        if line.startswith("ERROR") or line.startswith("error") or line.startswith("Error"):
            count += 1
print(f"Number of error lines in the file: ", count)


