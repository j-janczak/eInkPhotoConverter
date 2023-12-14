from .GalleryFrameController import GalleryFrameController
from model.PhotoModel import PhotoModel
from config.config import THUMB_WIDTH, IMG_THUMB_BG, IMG_THUMB_HOVER_BG
import customtkinter as ctk
from tkinter import Event
from typing import List


class GalleryFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = GalleryFrameController(self)
        self.bind("<Configure>", self.onFrameResize, add="+")
        self.colCount = 0

    def refreshThumbs(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()

        row = 0
        col = 0
        for index, image in enumerate(self.controller.images):
            thumbWidget = image.widget(self)

            for child in thumbWidget.winfo_children():
                if isinstance(child, ctk.CTkLabel):
                    child.bind("<Enter>", lambda _, widget=thumbWidget: self.onFrameHover(widget))
                    child.bind("<Leave>", lambda _, widget=thumbWidget: self.onFrameLeave(widget))
                    child.bind("<Button-3>", lambda _, index=index: self.controller.removeImage(index))
                    child.configure(width=THUMB_WIDTH)

            thumbWidget.grid(
                sticky="nsew",
                row=row,
                column=col
            )
            col += 1
            if col >= self.colCount:
                row += 1
                col = 0

    def onFrameHover(self, widget: ctk.CTkFrame) -> None:
        widget.configure(fg_color=IMG_THUMB_HOVER_BG)

    def onFrameLeave(self, widget: ctk.CTkFrame) -> None:
        widget.configure(fg_color=IMG_THUMB_BG)

    def onFrameResize(self, size) -> None:
        allowedCollumns = size.width // (THUMB_WIDTH + 10)
        if (allowedCollumns != self.colCount):
            self.colCount = allowedCollumns
            self.refreshThumbs()

    def getImagePaths(self) -> List:
        return self.controller.getImagePaths()
