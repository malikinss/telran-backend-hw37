# Homework 37 – Weather API Integration

## Task Definition

The goal of Homework 37 is to implement a **weather information module** that retrieves current weather data for a given city using the **WeatherAPI**.

Specifically, the task requires:

1. Writing a module `tools.py` with a function `get_weather(city)` that returns a string containing:
    - City name
    - Temperature in Celsius
    - Condition (e.g., sunny, cloudy)
    - Humidity in percent
    - Wind speed in kph

2. Using the **WeatherAPI** (https://www.weatherapi.com/docs/) for real-time data.

3. Writing an **integration test** `weather_integration_test.py` that:
    - Calls `get_weather` for a valid city and verifies returned data.
    - Calls `get_weather` for an invalid/non-existent city and verifies that an error is raised.

---

## 📝 Description

This project implements a **Weather API client in Python** to fetch and display current weather conditions.

The key components:

- **`WeatherAPI` class** – wraps API calls and manages configuration.
- **`WeatherInfo` dataclass** – structured container for weather data.
- **Integration tests** – validate actual API calls for both valid and invalid cities.

Project structure:

```
./src/
 ├─ tools.py              # WeatherAPI wrapper and WeatherInfo dataclass
 ├─ main.py               # Example client or main usage
 └─ __init__.py           # Module exports

./tests/
 └─ test_weather_integration.py  # Integration tests for WeatherAPI
```

---

## 🎯 Purpose

The homework focuses on:

1. **API integration** – Interacting with an external HTTP API and handling responses.
2. **Error handling** – Gracefully catching failed requests, non-existent cities, and malformed responses.
3. **Data modeling** – Using Python dataclasses for clean, structured weather data.
4. **Testing practices** – Writing real integration tests to validate API behavior in real scenarios.

By combining a structured client class and integration tests, the project ensures **reliable, real-world API consumption**.

---

## 🔍 How It Works

1. **Initialization**
    - `WeatherAPI` reads API URL and API key from environment variables (`WEATHER_API_URL`, `WEATHER_API_KEY`).

2. **Fetching Weather**
    - `get_weather(city)` sends a GET request to WeatherAPI.
    - Receives JSON containing `location` and `current` weather data.
    - Converts JSON into a `WeatherInfo` object.

3. **Error Handling**
    - Raises `ValueError` if the city does not exist or API request fails.
    - Handles HTTP errors and missing environment variables.

4. **Integration Testing**
    - `TestWeatherIntegration` performs real API calls.
    - Confirms returned `WeatherInfo` fields are of correct type.
    - Validates error handling for non-existent cities.

---

## 📜 Output Example

### ✅ Valid city

```py
from src.tools import WeatherAPI

api = WeatherAPI()
info = api.get_weather("London")
print(info)
```

Output:

```
City: London
Temperature: 14.5 °C
Condition: Partly cloudy
Humidity: 78%
Wind speed: 12.3 kph
```

### ❌ Non-existent city

```py
info = api.get_weather("ThisCityDoesNotExist123456")
# → ValueError: City 'ThisCityDoesNotExist123456' not found.
```

---

## 📦 Usage

```py
from src.tools import WeatherAPI

api = WeatherAPI()
city_name = "New York"
weather_info = api.get_weather(city_name)
print(weather_info)
```

### Running Integration Tests

```bash
python -m unittest discover -s tests
```

Tests cover:

- Real API calls for existing cities.
- Handling of non-existent city queries.
- Validation of `WeatherInfo` object fields.

---

## ✅ Dependencies

- Python 3.10+
- `requests` library
- `python-dotenv` (for environment variable loading)

---

## 📊 Project Status

**Status:** ✅ Completed

- WeatherAPI integration implemented.
- Real-time data fetching works for valid cities.
- Robust error handling for invalid cities and network issues.
- Integration tests validate end-to-end API behavior.

---

## 📄 License

MIT License

---

## 🧮 Conclusion

This project demonstrates **real-world API integration** in Python with:

- Structured data modeling via `dataclass`,
- Clean separation between API logic and data representation,
- End-to-end integration testing for reliability.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
