from view.infoWindow.InfoWindow import InfoWindow
from config.config import PADDING_S, PADDING_M
from typing import Callable, Tuple
from utils.GettextConfig import _
import customtkinter as ctk
from PIL import Image


class OutputPathSelector(ctk.CTkFrame):
    def __init__(
            self,
            master: any,
            width: int = 200,
            height: int = 200,
            corner_radius: int | str | None = None,
            border_width: int | str | None = None,
            bg_color: str | Tuple[str, str] = "transparent",
            fg_color: str | Tuple[str, str] | None = None,
            border_color: str | Tuple[str, str] | None = None,
            background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
            overwrite_preferred_drawing_method: str | None = None,
            **kwargs,
        ) -> None:
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )

        img_save = ctk.CTkImage(Image.open("images/img_save_white.png"))
        
        img_start = ctk.CTkImage(Image.open("images/img_start_white.png"))
        
        imgHelp = ctk.CTkImage(Image.open("images/img_help_white.png"))

        self.imgOutputPath = ctk.CTkEntry(
            self,
            placeholder_text=_("Location of photos"),
        )
        self.imgOutputPath.pack(
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_S],
            fill=ctk.X
        )

        self.imgActionBtn = ctk.CTkButton(
            self,
            text=_("Select a save location"),
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
            text=_("Help"),
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
            text=_("Convert!"),
            image=img_start,
            compound=ctk.RIGHT,
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
    
    def setConvertCallback(self, callback: Callable[[], None] = None) -> None:
        self.imgConvertBtn.configure(command=callback)
