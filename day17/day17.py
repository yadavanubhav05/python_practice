import os
# print(os.getcwd)

# files = os.listdir()
# print(files)

# if os.path.exists("sample.txt"):
#     print("File exists")
# else:    print("File does not exist")

# for file in os.listdir():
#     if file.endswith(".py"):
#         print(file)
count = 0
for file in os.listdir():
    count +=1
print(count)
