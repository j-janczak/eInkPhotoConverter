from .GalleryFrameController import GalleryFrameController
import customtkinter as ctk
from typing import List
from PIL import Image


class GalleryFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = GalleryFrameController(self)

    def getImagePaths(self) -> List:
        return self.controller.getImagePaths()
