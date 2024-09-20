# 17.  Weather Information Scraper   
#     *Description*: Scrape a weather website to fetch the current weather information for a specified city.  
#     *Skills*: Parsing structured data, handling user input.

import requests
from bs4 import BeautifulSoup

# Function to fetch and save HTML data from the URL to a file
def fetch_and_save_to_file(url, path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print("HTML content saved successfully.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except IOError as e:
        print(f"File operation failed: {e}")

# fetch_and_save_to_file("http://mfd.gov.np/weather/", 'Weather Information Scraper/weather.html')

# Function to extract weather data for a specific city
def extract_weather_for_city(city_name, html_content):
    # Parses the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Finds all weather-icon DIVs
    weather_icons = soup.find_all('div', class_='weather-icon')

    # Loop through each weather-icon div and check for the city name in the 'title' attribute
    for icon in weather_icons:
        title = icon.get('title', '').strip()

        # If the city name matches, extract weather details from 'data-pop' attribute
        if city_name.lower() in title.lower():
            weather_data_html = icon.get('data-pop', '')

            # Using BeautifulSoup again to parse the weather data
            weather_data_soup = BeautifulSoup(weather_data_html, 'html.parser')

            # Extract specific weather information
            weather_info = {}
            for dt, dd in zip(weather_data_soup.find_all('dt'), weather_data_soup.find_all('dd')):
                key = dt.text.strip()
                value = dd.text.strip()
                
                if key.startswith('Sunrise'):
                    weather_info['Sunrise'] = value
                elif key.startswith('Sunset'):
                    weather_info['Sunset'] = value
                elif key.startswith('Weather'):
                    weather_info['Weather'] = value
                elif key.startswith('Expected Temperature'):
                    weather_info['Expected Temperature'] = value
                elif key.startswith('Chances of Rain'):
                    weather_info['Chances of Rain'] = value

            return {
                'city': title,
                'weather_info': weather_info
            }

    return None

# Main program
if __name__ == "__main__":

    with open('Weather Information Scraper/weather.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    city_name = input("Enter the name of the city you want weather information for: ")

    # Extract weather data for the entered city
    weather_data = extract_weather_for_city(city_name, html_content)

    # Display the weather data if available
    if weather_data:
        print(f"Weather for {weather_data['city']}:")
        print("=" * 30)  
        for key, value in weather_data['weather_info'].items():
            print(f"{key:<25}: {value}")  
        print("=" * 30)  
    else:
        print(f"Weather data for {city_name} not found.")
