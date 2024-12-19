from customtkinter import CTkFrame
from components import *


class SmallWidget(ctk.CTkFrame):
    def __init__(self, parent, current_data, location, color):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        # Layout
        self.rowconfigure(0, weight=6, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')

        # Widgets
        SimplePanel(self, current_data, 0, 0, color)




