from customtkinter import CTkImage, CTkLabel
from PIL import Image

class PhotoModel:
    def __init__(
            self,
            path: str,
            name: str,
            image: Image,
            thumb: CTkImage,
            width: int = 130
            ) -> None:
        self.path = path
        self.name = name
        self.image = image
        self.thumb = thumb
        self.width = width

    def widget(self, master: any) -> CTkLabel:
        return CTkLabel(
            master,
            width=self.width,
            image=self.thumb, 
            text=self.name, 
            compound='top'
        )