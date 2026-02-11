# ./src/tools.py

import os
import requests
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class WeatherInfo:
    """
    Container for weather data of a city.
    """
    city: str
    temperature: float
    condition: str
    humidity: int
    wind_kph: float

    def __str__(self) -> str:
        return (
            f"City: {self.city}\n"
            f"Temperature: {self.temperature} °C\n"
            f"Condition: {self.condition}\n"
            f"Humidity: {self.humidity}%\n"
            f"Wind speed: {self.wind_kph} kph"
        )


class WeatherAPI:
    """
    Simple wrapper for accessing weather information via WeatherAPI.
    """

    def __init__(
        self,
        url_env: str = "WEATHER_API_URL",
        key_env: str = "WEATHER_API_KEY"
    ) -> None:
        """
        Initialize API wrapper using environment variables.

        Args:
            url_env: Environment variable name for API base URL.
            key_env: Environment variable name for API key.
        """
        self.api_url = os.getenv(url_env)
        self.api_key = os.getenv(key_env)

        if not self.api_url or not self.api_key:
            raise RuntimeError(
                "Weather API environment variables are not set."
            )

    def get_weather(self, city: str) -> WeatherInfo:
        """
        Get current weather for a city.

        Args:
            city: City name to query.

        Returns:
            WeatherInfo object containing current weather data.

        Raises:
            ValueError: If city is not found or API request fails.
        """
        params = {
            "key": self.api_key,
            "q": city,
            "aqi": "no"
        }

        try:
            response = requests.get(self.api_url, params)  # type: ignore
            response.raise_for_status()
            data = response.json()

            if "error" in data:
                raise ValueError(f"City '{city}' not found.")

            location = data["location"]["name"]
            current = data["current"]

            return WeatherInfo(
                city=location,
                temperature=current["temp_c"],
                condition=current["condition"]["text"],
                humidity=current["humidity"],
                wind_kph=current["wind_kph"],
            )

        except requests.RequestException as e:
            raise ValueError(f"Failed to get weather for '{city}': {e}")
