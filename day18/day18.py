import requests

url = "https://api.github.com"
try:
    response = requests.get(url)
# print(response.status_code)

# print("================================")
# print(response.text)

    data = response.json()
    print(data)
    print("================================")

    print(data["current_user_url"])

except:
    print("API request failed")