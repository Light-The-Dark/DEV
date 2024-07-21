import requests

with open(r"Udemy\Day 35 weather app API\api_key.txt", "r") as file:
    api_key = str(file.readlines()[0])

city = "Israel"
country = "Jerusalem"
url = "https://api.openweathermap.org/data/2.5/forecast"


params = {
    "lat": 31.768318,
    "lon": 35.213711,
    "appid": api_key
}

# API request with print to make sure it's correct format
# api_request = f"{url}q={city},{country}&appid={api_key}"
# print(api_request)

# Print out the response as txt
req = requests.get(url=url, params=params)
print(req.json())


