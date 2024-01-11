import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Getty_Images%2C_Eastcastle_Street%2C_London.JPG/1280px-Getty_Images%2C_Eastcastle_Street%2C_London.JPG"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2Q0NWZmZGU2MTc5NGUyNDpiYzk0NjMzNTE3NDhmYTYxYjQxODRhZmU4MDAxNjFhOA=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
