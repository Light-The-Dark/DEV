import requests

with open(r"Udemy\Day 35 weather app API\api_key.txt", "r") as file:
    api_key = str(file.readlines()[0])

city = "Israel"
country = "Jerusalem"

# API request with print to make sure it's correct format
api_request = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
print(api_request)

# Print out the response as txt
req = requests.get(api_request)
print(req.text)


