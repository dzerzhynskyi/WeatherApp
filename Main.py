import customtkinter as ctk
from settings import *
import requests
import urllib.request
import json

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(ctk.CTk):
    def __init__(self, app_width=None, app_height=None):
        super().__init__()
        self.title("Weather App")

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
                print(index)
        if period == 'today':
            return current_data
        else:
            return forecast_data

# weather for New York
current_data = get_weather(latitude=40.7127281, longitude=-74.0060152, units="metric", period="today")
print(current_data)

if __name__ == '__main__':
    # get location
    # does not work
    # with urllib.request.urlopen("https://ipapi.co/json/") as url:
    # data = json.loads(url.read().decode())

    App(app_width=500, app_height=350)
