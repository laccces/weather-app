import requests
import json

# Enter your API key here
api_key = "f27bbe94a88d423fa13100714232903"

# Base URL for the API
base_url = "http://api.weatherapi.com/v1/forecast.json?"

# Enter the city name
location = input("Enter city name or post code: ")

# Complete URL for the API request
complete_url = base_url + "key=" + api_key + "&q=" + location + "&days=4" + "&aqi=no&alerts=no"

# Sending HTTP request
response = requests.get(complete_url)

# Parsing the response
data = response.json()

# Extracting necessary info
current_temperature = data['current']['temp_c']
humidity = data['current']['humidity']
description = data['current']['condition']['text']
day_one_temp = data['forecast']['forecastday'][1]['day']['avgtemp_c']
day_one_humidity = data['forecast']['forecastday'][1]['day']['avghumidity']
day_one_conditions = data['forecast']['forecastday'][1]['day']['condition']['text']
day_two_temp = data['forecast']['forecastday'][2]['day']['avgtemp_c']
day_two_humidity = data['forecast']['forecastday'][2]['day']['avghumidity']
day_two_conditions = data['forecast']['forecastday'][2]['day']['condition']['text']
day_three_temp = data['forecast']['forecastday'][3]['day']['avgtemp_c']
day_three_humidity = data['forecast']['forecastday'][3]['day']['avghumidity']
day_three_conditions = data['forecast']['forecastday'][3]['day']['condition']['text']

# Displaying the data
print("Current weather:")
print("Current Temperature: " + str(current_temperature) + " Celsius")
print("Humidity: " + str(humidity) + "%")
print("Conditions: " + description)

# tomorrow
print("Weather tomorrow:")
print("Average Temperature: " + str(day_one_temp) + " Celsius")
print("Average Humidity: " + str(day_one_humidity) + "%")
print("Conditions: " + day_one_conditions)

# day 2
print("Day 2 weather:")
print("Average Temperature: " + str(day_two_temp) + " Celsius")
print("Average Humidity: " + str(day_two_humidity) + "%")
print("Conditions: " + day_two_conditions)

# day 3
print("Day 3 weather:")
print("Average Temperature: " + str(day_three_temp) + " Celsius")
print("Average Humidity: " + str(day_three_humidity) + "%")
print("Conditions: " + day_three_conditions)