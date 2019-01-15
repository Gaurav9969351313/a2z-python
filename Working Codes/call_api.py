import requests
import json

# GET
url = "http://localhost:5000/Authenticate"
querystring = {"UserName":"Admin","Password":"Admin"}
response = requests.request("GET", url, params=querystring)
print(response.text)

# POST
data = {"username":   "Admin",
    "password": "A"}
r = requests.post("http://localhost:5000/login", json=data)
print(r.json())