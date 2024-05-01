import requests
# Latitude and longitude 
latitude = 35.31371
longitude = -83.17653

# Date for sunrise/sunset
date = "2024-05-01"

# API endpoint for sunrise/sunset
url = f"https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2024-05-01&tzid=%20America/New_York"
# Send GET request to the API
response = requests.get(url)

# Extract sunrise and sunset times from the response
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Print the sunrise and sunset times
print("Sunrise:", sunrise)
print("Sunset:", sunset)
