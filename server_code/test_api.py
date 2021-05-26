# test code for the API

import requests

BASE_ADR = "http://127.0.0.1:5000/"

res = requests.get(BASE_ADR)
print("GET responce :",res.json())

res = requests.post(BASE_ADR)
print("POST responce :",res.json())
