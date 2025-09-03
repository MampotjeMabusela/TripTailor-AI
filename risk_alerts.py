import requests

def get_weather_alerts(location):
    url = f"https://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q={location}"
    response = requests.get(url).json()
    return response["forecast"]["forecastday"][0]["day"]["condition"]["text"]

def get_geopolitical_alerts(location):
    # Simulated API call
    alerts = {
        "Paris": "No current geopolitical risks",
        "Tel Aviv": "Travel advisory due to regional tensions"
    }
    return alerts.get(location, "No data available")

# Example
print(get_weather_alerts("Paris"))
print(get_geopolitical_alerts("Paris"))
