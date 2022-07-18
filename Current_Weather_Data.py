import requests 
from myapi import user_api #here I have imported my api key from another files

location = input("Enter the city name: ").upper()

complete_api_link = "https://api.openweaxthermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link) 
api_data = api_link.json() 

print('Coordinates are', api_data['coord'])
temp_city  = ((api_data['main']['temp']))
weather_desc = api_data['weather'][0]['description']
humidity_mycity = api_data['main']['humidity']


print()
print('-------------------------')
print(f"Weather status for {location}")
print('-------------------------')
print(f"temperature is {int(temp_city) - 273.15 : .2f}°C ")
print(f"Weather description is {weather_desc}")
print(f"Humidity is {humidity_mycity} %" )