import customtkinter as ctk
from .GalleryFrameController import GalleryFrameController

class GalleryFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = GalleryFrameController(self)