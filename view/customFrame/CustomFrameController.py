from utils.ConfigMapper import ConfigMapper
from customtkinter import CTkFrame

class CustomFrameController:
    def __init__(self, view: CTkFrame, configMapper: ConfigMapper) -> None:
        self.view = view
        self.configMapper = configMapper