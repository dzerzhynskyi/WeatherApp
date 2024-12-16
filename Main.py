import customtkinter as ctk
from settings import *

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

#setting the IPA and getting the weather data
    def get_weather(latitude, longitude, units, period):
        full_url = f"{BASE_URL}&lat={latitude}&lon={longitude}&appid={API_KEY}&units={units}"
        print(full_url)


# weather for New York
get_weather(latitude=40.7128, longitude=74.0060, units="metric", period="today")

if __name__ == '__main__':
    # get location
    # does not work
    #with urllib.request.urlopen("https://ipapi.co/json/") as url:
        #data = json.loads(url.read().decode())

    App(app_width=500, app_height=350)
