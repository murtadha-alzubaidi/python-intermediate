import requests
import json
url = "https://api.open-meteo.com/v1/forecast"
p={"latitude":36.19, "longitude":44.01,"current":"temperature_2m,wind_speed_10m"}
try:
    r=requests.get(url,params=p)
except requests.exceptions.ConnectionError:
    print("No internet connection")
    exit()
if r.status_code==200:
    data=r.json()
    temp=data["current"]["temperature_2m"]
    wind=data["current"]["wind_speed_10m"]
    print(f"Erbil: {temp} C, wind {wind} km/h")
    weather={"city":"Erbil","temp":temp ,"wind":wind}
    with open("weather.json","w")as f:
        json.dump(weather,f,indent=4)
else:
    print("Request failed:",r.status_code)