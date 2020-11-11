import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0cb598a6c3c3a8f09c1d6f99339201a6&units=metric&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
lon = json_data['coord']["lon"]
print("longitude:",lon)
lat= json_data['coord']["lat"]
print("longitude:",lat)
wea=  json_data['weather'][0]["main"]
print("mainly:",wea)
for k,v in json_data['main'].items():
    print(k,v)