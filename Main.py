import customtkinter as ctk
from settings import *
import requests
import urllib.request
import json
from main_widgets import *
from components import *

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(ctk.CTk):
    def __init__(self, app_width=None, app_height=None, current_data=None, forecast_data=None, city=None, country=None):
        super().__init__()
        self.title("Weather App")
        self.color = WEATHER_DATA[current_data['weather']]
        self.current_data = current_data
        self.forecast_data = forecast_data
        self.location = {'city': city, 'country': country}
        self.widget = SmallWidget(self, self.current_data, self.location, self.color)

        # Setting the app to open in the middle of the screen
        top = int(self.winfo_screenwidth() / 2 - app_width / 2)
        left = int(self.winfo_screenheight() / 2 - app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{top}+{left}")
        self.minsize(app_width, app_height)
        self.maxsize(app_width, app_height)
        ctk.set_appearance_mode("light")

        # The main loop
        self.mainloop()


if __name__ == '__main__':
    # setting the IPA and getting the weather data
    def get_weather(latitude, longitude, units, period):
        full_url = f"{BASE_URL}&lat={latitude}&lon={longitude}&appid={API_KEY}&units={units}"
        response = requests.get(full_url)

        current_data = {}
        forecast_data = {}

        if response.status_code == 200:
            data = response.json()
            for key, value in data.items():
                if key == "list":
                    for index, data_entry in enumerate(value):
                        if index == 0:
                            current_data['temp'] = int(round(data_entry['main']['temp'], 0))
                            current_data['feels_like'] = int(round(data_entry['main']['feels_like'], 0))
                            current_data['weather'] = data_entry['weather'][0]['main']
                            today = data_entry['dt_txt'].split(' ')[0]
                        else:
                            if data_entry['dt_txt'].split(' ')[0] != today:
                                start_index = index + 4  # setting up the time 12 am
                                break
            for index in range(start_index, len(data['list']), 8):
                forecast_entry = data['list'][index]
                date = forecast_entry['dt_txt'].split(' ')[0]
                forecast_data[date] = {
                    'temp': int(round(forecast_entry['main']['temp'], 0)),
                    'feels_like':int(round(forecast_entry['main']['feels_like'], 0)),
                    'weather': forecast_entry['weather'][0]['main']
                }
        if period == 'today':
            return current_data
        else:
            return forecast_data


if __name__ == '__main__':
    # get location
    # does not work
    # with urllib.request.urlopen("https://ipapi.co/json/") as url:
    # data = json.loads(url.read().decode())
    # weather for New York
    current_data = get_weather(latitude=40.7127281, longitude=-74.0060152, units="metric", period="today")
    forecast_data = get_weather(latitude=40.7127281, longitude=-74.0060152, units="metric", period="forecast")
    App(app_width=300, app_height=250, current_data=current_data, forecast_data=forecast_data, city='city', country='country')