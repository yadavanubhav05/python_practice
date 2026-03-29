# import os
# for file in os.listdir():
#     print(file)

import os

def count_files():
    text_file = 0
    py_file = 0
    csv_file = 0
    json_file = 0

    for file in os.listdir():
        if file.endswith(".txt"):
            text_file += 1
        elif file.endswith(".py"):
            py_file += 1
        elif file.endswith(".csv"):
            csv_file += 1
        elif file.endswith(".json"):
            json_file += 1
    return text_file, py_file, csv_file, json_file

print(f"Text files: {text_file}")
print(f"Python files: {py_file}")
print(f"CSV files: {csv_file}")
print(f"JSON files: {json_file}")