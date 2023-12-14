from .OutputPathSelectorController import OutputPathSelectorController
from view.infoWindow.InfoWindow import InfoWindow
from config.config import PADDING_S, PADDING_M
import customtkinter as ctk
from typing import Callable
from PIL import Image


class OutputPathSelector(ctk.CTkFrame):
    def __init__(
            self, 
            master: any,
            convertCallback: Callable[[], None], 
            **kwargs) -> None:
        super().__init__(master, **kwargs)

        self.convertCallback = convertCallback

        img_save = ctk.CTkImage(light_image=Image.open("images/img_save_black.png"),
                                dark_image=Image.open("images/img_save_white.png"))
        
        img_start = ctk.CTkImage(light_image=Image.open("images/img_start_black.png"),
                                 dark_image=Image.open("images/img_start_white.png"))
        
        imgHelp = ctk.CTkImage(light_image=Image.open("images/img_help_black.png"),
                               dark_image=Image.open("images/img_help_white.png"))

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

        self.helpButton = ctk.CTkButton(
            self,
            text="Informacje",
            image=imgHelp,
            compound=ctk.RIGHT, command=lambda: InfoWindow()
        )
        self.helpButton.pack(
            fill=ctk.X,
            side=ctk.BOTTOM,
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M]
        )

        self.imgConvertBtn = ctk.CTkButton(
            self,
            text="Konwertuj!",
            image=img_start,
            compound=ctk.RIGHT,
            command=self.convertCallback
        )
        self.imgConvertBtn.pack(
            fill=ctk.X,
            side=ctk.BOTTOM,
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_S]
        )

        ctk.CTkFrame(self, height=2).pack(
            fill=ctk.X,
            side=ctk.BOTTOM,
            padx=PADDING_M,
            pady=[PADDING_S, 0]
        )

        self.controller.initController()

    def getOutputPath(self) -> str:
        return self.controller.imgOutputPathText.get()
