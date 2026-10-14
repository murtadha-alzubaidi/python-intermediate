import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 33.31, "longitude": 44.36, "current": "temperature_2m"}

response= requests.get(url,params=params)
if response.status_code==200:
    data= response.json()
    temp=data["current"]["temperature_2m"]
    print(f"Baghdad now:{temp} C")
else:
    print(f"Request failed: {response.status_code}")