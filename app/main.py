import os
import requests

API_KEY = os.environ.get("API_KEY")

BASE_URL = "http://api.weatherapi.com/v1"

def get_weather() -> None:
    if not API_KEY:
        print("API_KEY not found in environment variables.")
        return

    city_input = input("Enter city name or press Q to exit: ").strip()

    if city_input.lower() == "q":
        print("Exiting...")
    else:
        url = f"{BASE_URL}/current.json?key={API_KEY}&q={city_input}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        name = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]

        print(f"Weather in {name}, {country}: {temp_c}°C ({temp_f}°F)")

        get_weather()


if __name__ == "__main__":
    get_weather()
