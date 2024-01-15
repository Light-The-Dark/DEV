import requests

parameters = {
    "lat": 31.837801,
    "lng": 35.240406,
    "tzid": "Israel",
    "formatted": 1,
}

sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunrise_sunset.raise_for_status()
sunrise_sunset = sunrise_sunset.json()


sunrise = sunrise_sunset["results"]["sunrise"]
sunset = sunrise_sunset["results"]["sunset"]
# print(sunrise)


sunrise = sunrise.split("T")
sunset = sunset.split("T")

print(sunrise)
print(sunset)