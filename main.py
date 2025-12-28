import requests
from pprint import pprint

API_KEY = ""  # TU wklej api key


def check_coordinates(city, API_KEY):
  response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
  lat = response.json()[0]['lat']
  lon = response.json()[0]['lon']
  city = response.json()[0]['name']
  country = response.json()[0]['country']
  return lat, lon, city, country

print("Witaj, jestem Travelinator, twoj intelignetny asystent podrózy")
origin_city = input("Podaj nazwe miasta z którego podrózujesz: ")
destination_city = input("Podaj nazwe miasta do ktorego podrozujesz: ")

origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)
destination_lat, destination_lon, destination_city, destination_country = check_coordinates(destination_city, API_KEY)




def get_weather_info(lat,lon, API_KEY):
  response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
  response_json = response.json()
  weather = response_json['weather'][0]['description']
  temperature = response_json['main']['temp']
  pressure = response_json['main']['pressure']
  humidity = response_json['main']['humidity']
  return weather, temperature, pressure, humidity


weather, temperature, pressure, humidity = get_weather_info(destination_lat, destination_lon, API_KEY)

print(f"Miasto z którego podróżujesz: {origin_city}")
print(f"Miasto do którego podróżujesz: {destination_city}")
print(f"Jego wspolrzednie geograficzne to:\n{destination_lat} szerokosci geograficznej\n{destination_lon} dlugosci geograficznej")
print(f"Pogoda: {weather}")
print(f"Temperatura: {temperature} st. Celcjusza")
print(f"Wilgotnosc: {humidity}%")
print(f"Ciśnienie atmosferyczne: {pressure}hPa")