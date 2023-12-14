from .ImageSelectorFrameController import ImageSelectorFrameController
from view.galleryFrame.GalleryFrame import GalleryFrame
from config.config import PADDING_M, PADDING_S
from utils.GettextConfig import _
import customtkinter as ctk
from typing import List
from PIL import Image

class ImageSelectorFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

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

        self.controller = ImageSelectorFrameController(self)

    def getImagePaths(self) -> List:
        return self.galleryFrame.getImagePaths()
