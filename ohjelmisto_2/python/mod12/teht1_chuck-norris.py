import requests
import json

pyynto = "https://api.chucknorris.io/jokes/random" 

try:

    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus = vastaus.json()
        print(vastaus ["value"])

    else:
        print("hakua ei voi suorittaa")

except requests.exceptions.RequestException as e:
    print("hakua ei voi suorittaa")
