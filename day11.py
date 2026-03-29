# text = "    hello"
# print(text.strip())

# print(text.upper())
# print(text.lower())

# line = "INFO server started at 10:00"
# parts = line.split(",")
# print(parts)

# words = ["devOps", "is", "fun", "I", "love", "it"]
# result = " ".join(words)
# print(result)

# log = "ERROR: Failed to connect to database"
# if log.startswith("ERROR") or log.startswith("error") or log.startswith("Error"):
#     print("Error detected in application")

logs = ["INFO Start", "ERROR Disk", "WARN Memory", "ERROR Network"]
for log in logs:
    if log.startswith("ERROR") or log.startswith("error") or log.startswith("Error"):
        print(f"Error detected: {log}")