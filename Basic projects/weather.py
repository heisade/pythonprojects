import requests

api_key = '6dccae404f96466c4fde6c0a23d0c32c'        # The API key
user_location = input("Enter Location: ")           # To get user location
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=imperial&APPID={api_key}")


if weather_data.json()['cod'] != 200:
    print("City not found, please try again")       # If location not found
else:
    weather = weather_data.json()['weather'][0]['main']     # To get the weather
    
    temp_in_fahrenheit = weather_data.json()['main']['temp']
    temp = round((5/9)*(temp_in_fahrenheit-32))             # To get the temperature and convert it from fahrenheit to celcius
    
    pressure = weather_data.json()['main']['pressure']      # To get the pressure

    wind_speed = weather_data.json()['wind']['speed']       # To get the wind speed

    humidity = weather_data.json()['main']['humidity']      # To get the humidity

    # Printing everything
    print(f"The weather is at {user_location} is: {weather}\n"
    f"The temperature at {user_location} is: {temp}° celcuis\n"
    f"The pressure is: {pressure}\n"
    f"The wind speed is {wind_speed}m/s\n"
    f"The humidity is {humidity}")