import requests
import json


url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q": "Zaragoza,es",
               "lat": "0",
               "lon": "0",
               "callback": "test",
               "id": "2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
	"X-RapidAPI-Key": "1ca795b67amshfa6cf81e0962bf1p1e245ajsn33f3f8989a97"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(dict(response))

