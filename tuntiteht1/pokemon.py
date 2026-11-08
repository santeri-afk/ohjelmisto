import requests
import json

hakusana = input("Anna hakusana: ")


pyynto = f"https://pokeapi.co/api/v2/pokemon/{hakusana}" 

try:

    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus = vastaus.json()
        print(vastaus["types"][0]["type"]["name"])

    else:
        print("hakua ei voi suorittaa")

except requests.exceptions.RequestException as e:
    print("hakua ei voi suorittaa")
