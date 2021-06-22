# test code for the API

import requests

ADDDATA_TODB_ADR = "http://127.0.0.1:5000/addData"
GET_ANALYTICS_ADR = "http://127.0.0.1:5000/view/All-database"

#res = requests.get(GET_ANALYTICS_ADR)
#print("GET responce :",res.json())
data = {"time":"1:43:23 PM", 
		"date":"02/06/2021",
		"temp":99}

for i in range(10):
	res = requests.post(ADDDATA_TODB_ADR, json=data)

data = {"time":"2:43:23 PM", 
		"date":"03/06/2021",
		"temp":45}

for i in range(10):
	res = requests.post(ADDDATA_TODB_ADR, json=data)

data = {"time":"3:43:23 PM",
		"date":"04/06/2021",
		"temp":34.93}

for i in range(10):
	res = requests.post(ADDDATA_TODB_ADR, json=data)
print("POST responce :",res.json())
