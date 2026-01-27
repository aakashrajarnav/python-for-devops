import requests
import json

API_KEY = "4d9a1790febb4b8427554af263900aa7"

def fetch_weather_data(city):
    base_url = "https://api.weatherstack.com/current?"
    query = f"access_key={API_KEY}&query={city}/"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(base_url + query, headers=headers)
    return response

city = input("Enter the city name for weather information (e.g., London, New York): ")
response = fetch_weather_data(city)
print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print("Error: Failed to fetch data. Status code:", response.status_code)
    print("Response:", response.text)

query = input("Do you want to see any specific data like location or current weather data? (location/current): ")
def weather_data_choice():
    if query == "location":
        for key, value in response.json()["location"].items():
            print(f"{key}: {value}")
    elif query == "current":
        for key, value in response.json()["current"].items():
            print(f"{key}: {value}")
    else:
        print("Invalid choice. Please enter 'location' or 'current'.")

weather_data_choice()

with open("output.json", "w") as json_file:
    json.dump(response.json(), json_file, indent=4)
print("Weather data has been written to output.json")
    