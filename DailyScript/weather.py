import json
import os

LAST_WEATHER_FILE = 'last_weather.json'

# Simulated weather data for some cities
SIMULATED_WEATHER_DATA = {
    'New York': {'temp': 25, 'description': 'Sunny', 'humidity': 50, 'wind_speed': 5},
    'London': {'temp': 15, 'description': 'Cloudy', 'humidity': 60, 'wind_speed': 7},
    'Tokyo': {'temp': 30, 'description': 'Clear', 'humidity': 40, 'wind_speed': 3},
    'Paris': {'temp': 20, 'description': 'Rainy', 'humidity': 70, 'wind_speed': 6},
    'Mumbai': {'temp': 32, 'description': 'Hot', 'humidity': 80, 'wind_speed': 10},
}

# Function to get weather data for a city
def get_weather_data(city):
    return SIMULATED_WEATHER_DATA.get(city, None)

# Function to display weather data
def display_weather(weather_data, units='metric'):
    if not weather_data:
        print("No weather data to display.")
        return
    
    description = weather_data['description']
    temperature = weather_data['temp']
    humidity = weather_data['humidity']
    wind_speed = weather_data['wind_speed']
    unit_symbol = '°C' if units == 'metric' else '°F'

    print(f"\nWeather:")
    print(f"Description: {description}")
    print(f"Temperature: {temperature} {unit_symbol}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("")

# Function to save last queried weather data
def save_last_weather(city, weather_data):
    data = {'city': city, 'weather_data': weather_data}
    with open(LAST_WEATHER_FILE, 'w') as file:
        json.dump(data, file)

# Function to load last queried weather data
def load_last_weather():
    if os.path.exists(LAST_WEATHER_FILE):
        with open(LAST_WEATHER_FILE, 'r') as file:
            return json.load(file)
    return None

# Function to convert temperature units
def convert_temperature(temp, to_unit):
    if to_unit == 'metric':
        return (temp - 32) * 5.0/9.0  # Fahrenheit to Celsius
    return (temp * 9.0/5.0) + 32  # Celsius to Fahrenheit

# Main function to run the weather app
def main():
    last_weather = load_last_weather()
    current_units = 'metric'

    while True:
        print("\nMenu:")
        print("1. Get weather for a city")
        print("2. View last queried weather")
        print("3. Convert temperature units")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            city = input("Enter city name: ")
            weather_data = get_weather_data(city)
            if weather_data:
                display_weather(weather_data, current_units)
                save_last_weather(city, weather_data)
                last_weather = {'city': city, 'weather_data': weather_data}
            else:
                print("Weather data not available for the specified city.")
        elif choice == '2':
            if last_weather:
                city = last_weather['city']
                weather_data = last_weather['weather_data']
                display_weather(weather_data, current_units)
            else:
                print("No last queried weather data available.")
        elif choice == '3':
            if last_weather:
                weather_data = last_weather['weather_data']
                current_temp = weather_data['temp']
                if current_units == 'metric':
                    new_temp = convert_temperature(current_temp, 'imperial')
                    current_units = 'imperial'
                    weather_data['temp'] = new_temp
                else:
                    new_temp = convert_temperature(current_temp, 'metric')
                    current_units = 'metric'
                    weather_data['temp'] = new_temp
                display_weather(weather_data, current_units)
                save_last_weather(last_weather['city'], weather_data)
            else:
                print("No last queried weather data available to convert.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
