import requests
import json
import argparse

def fetch_weather_forecast(latitude, longitude):
    base_url = 'https://api.weather.gov'
    endpoint = f'/points/{latitude},{longitude}'

    url = base_url + endpoint

    try:
        response = requests.get(url)
        if response.status_code == 200:
            response2 = requests.get(response.json()['properties']['forecast'])
            data = response2.json()
            forecast = data['properties']['periods']
            try:
                with open('forecast.json', 'w') as f:
                    json.dump(response2.json(), f, indent=4)
                print(f"JSON data saved to {'forecast.json'}")
            except IOError as e:
                print(f"Error saving JSON data: {e}")
            return forecast
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(help="Enter a latitude value", dest="latitude", type=float)
    parser.add_argument(help="Enter a longitude", dest="longitude", type=float)
    # Fetch the weather forecast
    cliarg = parser.parse_args()
    periods = fetch_weather_forecast(cliarg.latitude, cliarg.longitude)
    
    for period in periods:
        print(f"Period: {period['name']}")
        print(f"Start Time: {period['startTime']}")
        print(f"End Time: {period['endTime']}")
        print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
        print(f"Probability of Precipitation: {period['probabilityOfPrecipitation']['value']}%")
        print(f"Wind Speed: {period['windSpeed']}")
        print(f"Wind Direction: {period['windDirection']}")
        print(f"Short Forecast: {period['shortForecast']}")
        print(f"Detailed Forecast: {period['detailedForecast']}")
        print("---------------------\n")

if __name__ == "__main__":
    main()

