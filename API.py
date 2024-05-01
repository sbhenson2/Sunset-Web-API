import requests
# Latitude and longitude 
latitude = 37.7749
longitude = -122.4194

# Date for sunrise/sunset
date = "2024-05-02"

# API endpoint for sunrise/sunset
url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={date}"

# Send GET request to the API
response = requests.get(url)

# Extract sunrise and sunset times from the response
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Print the sunrise and sunset times
print("Sunrise:", sunrise)
print("Sunset:", sunset)