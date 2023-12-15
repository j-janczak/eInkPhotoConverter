from view.galleryFrame.GalleryFrame import GalleryFrame
from config.config import PADDING_M, PADDING_S
from utils.GettextConfig import _
import customtkinter as ctk
from typing import Tuple
from PIL import Image

class ImageSelectorFrame(ctk.CTkFrame):
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
        **kwargs
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

        img_photo = ctk.CTkImage(Image.open("images/img_photo_white.png"))

        self.galleryFrame = GalleryFrame(
            self,
            label_text=_("Selected photos")
        )
        self.galleryFrame.pack(
            expand=True,
            fill=ctk.BOTH,
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_S]
        )

        self.sel_imgs_btn = ctk.CTkButton(
            self,
            text=_("Select photos"),
            image=img_photo,
            compound=ctk.RIGHT
        )
        self.sel_imgs_btn.pack(
            fill=ctk.X,
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M]
        )
