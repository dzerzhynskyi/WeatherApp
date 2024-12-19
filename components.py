import customtkinter as ctk

class SimplePanel(ctk.CTkFrame):
    def __init__(self, parent, weather, col, row, color, animation=None):
        super().__init__(master=parent, fg_color=color['main'], corner_radius=0)
        self.grid(column=col, row=row, sticky='nsew')

        # Layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='a')

        # Widgets
        temp_frame = ctk.CTkFrame(self, fg_color='transparent')
        ctk.CTkLabel(temp_frame, text=f"{weather['temp']}\N{DEGREE SIGN}",
                     font=ctk.CTkFont(family='Calibri', size=50), text_color=color['text']).pack()
        ctk.CTkLabel(temp_frame, text=f"feels like: {weather['feels_like']}\N{DEGREE SIGN}",
                     font=ctk.CTkFont(family='Calibri', size=16), text_color=color['text']).pack()
        temp_frame.grid(row=0, column=0)


