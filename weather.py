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

# Extracting necessary info
current_temperature = data['current']['temp_c']
humidity = data['current']['humidity']
description = data['current']['condition']['text']

# Displaying the data
print("Current weather:")
print("Current Temperature: " + str(current_temperature) + " Celsius")
print("Humidity: " + str(humidity) + "%")
print("Conditions: " + description)

