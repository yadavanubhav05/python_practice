error_count = 0 
info_count = 0

with open("sample.txt", "r") as file:
    for line in file:
        if line.startswith("ERROR") or line.startswith("error") or line.startswith("Error"):
            error_count += 1
        elif line.startswith("INFO") or line.startswith("info") or line.startswith("Info"):
            info_count += 1

print(f"Number of error lines: ", error_count)
print(f"Number of info lines: ", info_count)