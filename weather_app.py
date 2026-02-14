import requests
import json
city = input("Enter the name of the city : ")
url = f"http://api.weatherapi.com/v1/current.json?key=7f2ec82c25be4eb68c4164537250104&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
wind_speed = wdic["current"]["wind_kph"]
humidity = wdic["current"]["humidity"]
cloud = wdic["current"]["cloud"]
feels_like = wdic["current"]["feelslike_c"]
print(f"temperature -> {temp}\nwind speed -> {wind_speed}\nhumidity -> {humidity}\ncloud -> {cloud}\n feels like ->  {feels_like}")
