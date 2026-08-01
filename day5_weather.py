import requests
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.61&current_weather=true")
data = response.json()
temperature = data["current_weather"]["temperature"]
print(f"Сейчас в Москве {temperature}°C")