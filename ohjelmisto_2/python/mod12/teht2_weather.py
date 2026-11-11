import requests
import json

#hakusana = input("Anna paikkakunta: ")
hakusana = "Helsinki"

pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=5&appid={"f8571fccd625203d73e8144241d57ea3"}" 

try:

    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        vastaus = vastaus.json()
        print(vastaus)
        lat = (vastaus[0]["lat"])
        lon = (vastaus[0]["lon"])
        #käytin open weather omaa paramtetria nimeltä units=metric mikä antaa lämpötilan suoraan celsiuksena
        pyynto2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={"f8571fccd625203d73e8144241d57ea3"}"
        try:

            vastaus2 = requests.get(pyynto2)
            if vastaus2.status_code==200:
                vastaus2 = vastaus2.json()
                print(vastaus2)
                print(f"Antamisessasi paikkakunassa lämpötila on {vastaus2["main"]["temp"]} C°")

                
            else:
                print("hakua ei voi suorittaa")

        except requests.exceptions.RequestException as e:
            print("hakua ei voi suorittaa")

    else:
        print("hakua ei voi suorittaa")

except requests.exceptions.RequestException as e:
    print("hakua ei voi suorittaa")
