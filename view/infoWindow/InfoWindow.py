from typing import Optional, Tuple, Union
import customtkinter as ctk


class InfoWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Informacje")
        self.geometry("300x200")
        self.after(100, self.lift)
