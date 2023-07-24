# Weather-Desktop-App

# Languages & Programs Used:
Python
Visual Studio Code

# Purpose:
The purpose of this project is to demonstrate skills in working with APIs, parsing JSON data, and using external libraries to display notifications on the desktop. The Weather Notifier allows users to stay informed about the current weather conditions in their chosen city.

# Key Features:
OpenWeatherMap API Integration: The application fetches weather data from the OpenWeatherMap API using the provided API key.

Temperature Conversion: The script converts temperature from Kelvin to Celsius and Fahrenheit for better readability.

Desktop Notifications: The script uses the win10toast library to display weather information as a desktop notification.

# Skills Gained: 
API Integration: The project demonstrates proficiency in working with APIs and handling JSON data.

Python Programming: The entire project is implemented in Python, showcasing strong programming skills.

Data Parsing: The script effectively parses the JSON response from the API to extract relevant weather information.

Third-Party Libraries: The usage of win10toast showcases the ability to utilize third-party libraries for desktop notifications.

# Usage:
Sign up for an API key from OpenWeatherMap and set API_KEY in the script.

Ensure you have Python and the required libraries installed.

Clone the repository and navigate to the directory containing the Python script.

Replace "YOUR API KEY" with your actual API key from OpenWeatherMap.

Set CITY to the desired city for which you want to receive weather updates.

Run the script using the command:
python weather_notifier.py
The script will continuously display weather notifications for the specified city with a one-second interval between updates.

# Note:
Please ensure that you have an active internet connection while running the script, as it fetches weather data from the OpenWeatherMap API in real-time.

Feel free to customize the application to meet your needs, such as adding more weather parameters or implementing error handling for potential network or API-related issues.

# Contributions
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to create a pull request or submit an issue on GitHub.

# License
This project is licensed under the MIT License.
