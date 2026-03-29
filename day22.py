import os

def count_files(extension):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
    return count

print(f"Text files: {count_files('.txt')}")
print(f"Python files: {count_files('.py')}")
print(f"CSV files: {count_files('.csv')}")
print(f"JSON files: {count_files('.json')}")