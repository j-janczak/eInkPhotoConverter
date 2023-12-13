from config.config import THUMB_MAX_WIDTH, THUMB_MAX_HEIGHT, THUMB_LABEL_MAX_LEN, PADDING_M
from model.PhotoModel import PhotoModel
import customtkinter as ctk
from typing import List
from PIL import Image
import os


class GalleryFrameController():
    def __init__(self, view) -> None:
        self.view = view
        self.view.bind("<Configure>", self.onFrameResize, add="+")
        self.colCount = 3
        self.images = []

    def displayThumbs(self, imgPaths) -> None:
        for path in imgPaths:
            alreadyExists = [img for img in self.images if img.path == path]
            if len(alreadyExists) > 0:
                continue

            self.images.append(
                PhotoModel(
                    path=path,
                    name=self.createTextLabel(os.path.basename(path)),
                    thumb=self.scaleImgWithAspectRatio(Image.open(path))
                )
            )
        self.refreshThumbs()

    def refreshThumbs(self) -> None:
        for widget in self.view.winfo_children():
            widget.destroy()

        row = 0
        col = 0
        for image in self.images:
            thumbWidget = image.widget(self.view)
            thumbWidget.grid(row=row, column=col,
                             padx=PADDING_M, pady=PADDING_M)

            col += 1
            if col >= self.colCount:
                row += 1
                col = 0

    def scaleImgWithAspectRatio(self, image: Image) -> ctk.CTkImage:
        widthRatio = (THUMB_MAX_WIDTH / float(image.size[0]))
        height = int((float(image.size[1]) * float(widthRatio)))
        width = THUMB_MAX_WIDTH

        if (height > THUMB_MAX_HEIGHT):
            heightRatio = (THUMB_MAX_HEIGHT / float(image.size[1]))
            width = int((float(image.size[0]) * float(heightRatio)))
            height = THUMB_MAX_HEIGHT

        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return ctk.CTkImage(resized_image, size=(width, height))

    def createTextLabel(self, text: str) -> str:
        if len(text) > THUMB_LABEL_MAX_LEN:
            return text[:THUMB_LABEL_MAX_LEN] + "..."
        else:
            return text

    def onFrameResize(self, size) -> None:
        allowedCollumns = (size.width + 20) // 150
        if (allowedCollumns != self.colCount):
            self.colCount = allowedCollumns
            self.refreshThumbs()

    def getImagePaths(self) -> List:
        return [image.path for image in self.images]
