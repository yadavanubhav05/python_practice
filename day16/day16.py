# import json
# with open ("day16/user.json", "r") as file:
#     data = json.load(file)
#     print(data)

# import json

# new_user = {
#     "name": "Rahul",
#     "role": "DevOps",
#     "experience": 5
# }

# with open("day16/output.json", "w") as file:
#     json.dump(new_user, file)

import json
with open ("day16/user.json", "r") as file:
    data = json.load(file)
    if data ["experience"] > 5:
        print(data["role"])