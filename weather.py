import requests
import json

# Enter your API key here
api_key = "f27bbe94a88d423fa13100714232903"

# Base URL for the API
base_url = "http://api.weatherapi.com/v1/forecast.json?"

# Enter the city name
city_name = input("Enter city name: ")

days = input("How many days of weather would you like? Range allowed is 1-10.")

# Complete URL for the API request
complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&days=" + days + "&aqi=no&alerts=no"

# Sending HTTP request
response = requests.get(complete_url)

# Parsing the response
data = response.json()

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Extracting necessary info
# temperature = data['main']['temp']
# humidity = data['main']['humidity']
# description = data['weather'][0]['description']

# Displaying the data
# print("Temperature : " +
#                     str(round(temperature - 273.15, 2)) + " Celsius")
# print("Humidity : " +
#                     str(humidity) + "%")
# print("Description : " +
#                     str(description))
