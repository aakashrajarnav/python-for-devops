import requests
import json
import argparse

API_KEY = "4d9a1790febb4b8427554af263900aa7"

def fetch_weather_data(city):
    base_url = "https://api.weatherstack.com/current?"
    query = f"access_key={API_KEY}&query={city}/"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(base_url + query, headers=headers)
    return response

def weather_data_choice(response, data_type):
    if data_type == "location":
        for key, value in response.json()["location"].items():
            print(f"{key}: {value}")
    elif data_type == "current":
        for key, value in response.json()["current"].items():
            print(f"{key}: {value}")
    else:
        print("Invalid choice. Please enter 'location' or 'current'.")

def main():
    parser = argparse.ArgumentParser(description="Fetch weather data for a city")
    parser.add_argument("city", help="City name for weather information (e.g., London, New York)")
    parser.add_argument("-d", "--data", dest="data_type", default="current", 
                        choices=["location", "current"],
                        help="Specific data to display: 'location' or 'current' (default: current)")
    parser.add_argument("-o", "--output", dest="output_file", default="output.json",
                        help="Output file name to save the weather data (default: output.json)")
    
    args = parser.parse_args()
    
    response = fetch_weather_data(args.city)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        print("Response JSON:", response.json())
        weather_data_choice(response, args.data_type)
        
        with open(args.output_file, "w") as json_file:
            json.dump(response.json(), json_file, indent=4)
        print(f"Weather data has been written to {args.output_file}")
    else:
        print("Error: Failed to fetch data. Status code:", response.status_code)

if __name__ == "__main__":
    main()
    