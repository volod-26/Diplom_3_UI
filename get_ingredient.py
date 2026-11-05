import requests

response = requests.get("https://qa-stellarburgers.education-services.ru/api/ingredients")
print(response.json()["data"][0]["_id"])