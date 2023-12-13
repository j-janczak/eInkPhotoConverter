from .OutputPathSelectorController import OutputPathSelectorController
from config.config import PADDING_S, PADDING_M
import customtkinter as ctk
from PIL import Image


class OutputPathSelector(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        img_save = ctk.CTkImage(light_image=Image.open("images/img_save_black.png"),
                                dark_image=Image.open("images/img_save_white.png"))

        self.controller = OutputPathSelectorController(self)

        self.imgOutputPath = ctk.CTkEntry(
            self,
            placeholder_text="Lokalizacja zdjęć wynikowych",
            textvariable=self.controller.imgOutputPathText
        )
        self.imgOutputPath.pack(
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_S],
            fill=ctk.X
        )

        self.imgActionBtn = ctk.CTkButton(
            self,
            text="Wybierz lokalizację zapisu",
            image=img_save,
            compound=ctk.RIGHT
        )
        self.imgActionBtn.pack(
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M],
            fill=ctk.X
        )

        self.controller.initController()

    def getOutputPath(self) -> str:
        return self.controller.imgOutputPathText.get()
