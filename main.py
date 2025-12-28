import requests

API_KEY = "" # TU wklej API KEY


def check_coordinates(city, API_KEY):
  response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
  lat = response.json()[0]['lat']
  lon = response.json()[0]['lon']
  country = response.json()[0]['country']
  return lat, lon, city, country

def get_weather_info(lat,lon, API_KEY):
  response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
  response_json = response.json()
  weather = response_json['weather'][0]['description']
  temperature = response_json['main']['temp']
  temperature = temperature - 273.15
  pressure = response_json['main']['pressure']
  humidity = response_json['main']['humidity']
  return weather, temperature, pressure, humidity

def get_country_full_name(country_code):
  url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
  response = requests.get(url)
  country_name = response.json()[0]['name']['common']
  return country_name


def get_currency_code(country_code):
  url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
  response = requests.get(url)
  currency_code = list(response.json()[0]['currencies'].keys())[0]
  return currency_code


def get_currency_ratio(ori_curr,dest_curr):
  if ori_curr != "PLN":
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{ori_curr.lower()}/"
    response = requests.get(url)
    ori_ratio = response.json()['rates'][0]['mid']
  else:
    ori_ratio = 1

  if dest_curr != "PLN":
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{dest_curr.lower()}/"
    response = requests.get(url)
    dest_ratio = response.json()['rates'][0]['mid']
  else: 
    dest_ratio = 1
  ratio = float(ori_ratio)/float(dest_ratio)
  return ratio

def print_weather_info(place):
  lat, lon, _ = check_coordinates(place, API_KEY)
  weather, temperature, pressure, humidity = get_weather_info(lat, lon, API_KEY)
  print(f"Pogosa dla miasta {place}: {weather}")
  print(f"Temperatura: {temperature - 273.15} st. Celsjusza")
  print(f"Cisnienie: {pressure} hPa")
  print(f"Wilgotnosc: {humidity} %")
# Petla while ktora jest true
# 1. Podaj/zmien miejsce startowe
# 2. Podaj/zmien miejsce docelowe
# 3. Sprawdz lokalizacje miejsca startowego
# 4. Sprawdz lokalizacje miejsca docelowego
# 5. Sprawdz pogode miejsca startowego
# 6. Sprawdz pogode miejsca docelowego
# 7. Dowiedz sie wiecej o walucie
# 8. Koniec

origin_place = None
destination_place = None
while True:
  print('''
      Jaka akcje chcesz wykonac?
        1. Podaj/zmien miejsce startowe
        2. Podaj/zmien miejsce docelowe
        3. Sprawdz lokalizacje miejsca startowego
        4. Sprawdz lokalizacje miejsca docelowego
        5. Sprawdz pogode miejsca startowego
        6. Sprawdz pogode miejsca docelowego
        7. Dowiedz sie wiecej o walucie
        8. Koniec
''')
  choosen_option = int(input())
  if choosen_option == 1:
    orgin_place = input("Podaj miasto startowe: ")
  elif choosen_option == 2:
    destination_place = input("Podaj miasto docelowe: ")
  elif choosen_option == 3:
    if origin_place is not None:
      lat, lon, country = check_coordinates(origin_place, API_KEY)
      country_name = get_country_full_name(country)
      print(f"Miasto: {origin_place} lezy w kraju: {country_name}\n Dlugosc geograficzna: {lon}, szerokosc geograficzna: {lat}")
    else:
      print("Najpierw musisz podac miasto startowe")
  elif choosen_option == 4:
    if destination_place is not None:
      lat, lon, country = check_coordinates(destination_place, API_KEY)
      country_name = get_country_full_name(country)
      print(f"Miasto: {destination_place} lezy w kraju: {country_name}\n Dlugosc geograficzna: {lon}, szerokosc geograficzna: {lat}")
    else:
      print("Najpierw musisz podac miasto docelowe")
  elif choosen_option == 5:
    if origin_place is not None:
      print_weather_info(origin_place)
    else:
      print("Najpierw musisz podac miasto startowe")
  elif choosen_option == 6:
    if destination_place is not None:
      print_weather_info(destination_place)
    else:
      print("Najpierw musisz podac miasto docelowe")
  elif choosen_option == 7:
    if origin_place is not None:
      if destination_place is not None:
        # 1. Pobierz koordynaty dla obu lokalizacji
        # 2. Sprawdz za pomoca get_currency_code dla obu krajow jaka jest waluta
        # 3. Wyswietl ratio
        pass
      else:
        print("Najpierw musisz podac miasto docelowe")
    else:
      print("Najpierw musisz podac miasto startowe")
  elif choosen_option == 8:
    quit()
  else:
    print("Podano bledna opcje")
    print("Nacisnij enter aby kontynoowac....")
    input()

# print("Witaj, jestem Travelinator, twoj intelignetny asystent podrózy")
# origin_city = input("Podaj nazwe miasta z którego podrózujesz: ")
# destination_city = input("Podaj nazwe miasta do ktorego podrozujesz: ")

# origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)
# destination_lat, destination_lon, destination_city, destination_country = check_coordinates(destination_city, API_KEY)
# weather, temperature, pressure, humidity = get_weather_info(destination_lat, destination_lon, API_KEY)
# origin_country_full_name = get_country_full_name(origin_country)
# destination_country_full_name = get_country_full_name(destination_country)
# ori_curr = get_currency_code(origin_country)
# dest_curr = get_currency_code(destination_country)
# ratio = get_currency_ratio(ori_curr, dest_curr)

# print(f"Miasto z którego podróżujesz: {origin_city}")
# print(f"Lezy w kraju: {origin_country_full_name}")
# print(f"Obowiazujaca waluta to: {ori_curr}")
# print(f"Miasto do którego podróżujesz: {destination_city}")
# print(f"Lezy w kraju: {destination_country_full_name}")
# print(f"Obowiazujaca waluta to: {dest_curr}")
# print(f"Sredni kurs {ori_curr} na {dest_curr} to {ratio}")
# print(f"Jego wspolrzednie geograficzne to:\n{destination_lat} szerokosci geograficznej\n{destination_lon} dlugosci geograficznej")
# print(f"Pogoda: {weather}")
# print(f"Temperatura: {temperature} st. Celcjusza")
# print(f"Wilgotnosc: {humidity}%")
# print(f"Ciśnienie atmosferyczne: {pressure}hPa")


# GET - Pobiera dane z api
# POST - Tworzy nowe dane w api
# PUT (PATCH) - Aktualizuje dane
# DELETE - usuwa dane 
# Kody odpowiedzi z serwera
# 2xx - OK, wszystko dobrze  200 - success 201 - created - zasob zostal utworzony
# 3xx - przekierowania 301 - zasob zostal przeniesiony pod inny URL
# 4xx - (Client Error) - kody bledów po stronie klienta np zle zadanie lub brak uprawnien
# 400 - Bad Request - zadnie jest niepoprawne
# 401 - Unauthorized - brak autoryzacji - wymagane uwierzytelenienie
# 404 - Not Found - Serwer nie moze znalezc zasoby (np. niewlasciwy url)
# 5xx -Błedy serwera (server Error)
# 500 - Internal Server Error = Blad na serwerze
# 501 - Not Implemented - serwer nie obsluguje zadanej metody
# 503 - serwer tymczasowo niedostepny 