import requests
import json

hakusana = input("Anna paikkakunta: ")

api = "f8571fccd625203d73e8144241d57ea3"

pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=5&appid={api}" 

try:

    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus = vastaus.json()
        print(vastaus)

    else:
        print("hakua ei voi suorittaa")

except requests.exceptions.RequestException as e:
    print("hakua ei voi suorittaa")
