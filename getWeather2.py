APPID = 'b4d8a377bb56fd78e3ff290fa06f0a87'
import json, requests, sys

if len(sys.argv) < 2:
    print("To use: getWeather2.py cityName, 2letterCountryCode")
    sys.exit()

location = ' '.join(sys.argv[1:])
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' %(location, APPID)
response = requests.get(url)
response.raise_for_status()
print(response.text)
