
api_key = "14443324aad33aa75cab8c2ddbf51b88"
city = "Israel"
country = "Jerusalem"

api_request = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"


print(api_request)