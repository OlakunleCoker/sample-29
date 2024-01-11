import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://upload.wikimedia.org/wikipedia/commons/2/23/Old_photo_of_a_busy_street_in_Tehran.jpg"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2Q0NWZmZGU2MTc5NGUyNDpiYzk0NjMzNTE3NDhmYTYxYjQxODRhZmU4MDAxNjFhOA=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
