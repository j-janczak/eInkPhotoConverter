from config.DimAndColors import THUMB_MAX_WIDTH, THUMB_MAX_HEIGHT, THUMB_LABEL_MAX_LEN, THUMB_WIDTH
from view.progressDialog.ProgressDialog import ProgressDialog
from model.PhotoModel import PhotoModel
from .GalleryFrame import GalleryFrame
from utils.Utils import shortenText
from utils.GettextConfig import _
from typing import List, Callable
import customtkinter as ctk
from PIL import Image
import threading
import os


class GalleryFrameController():
    def __init__(self, view: GalleryFrame) -> None:
        self.view = view
        self.colCount = 0
        self.images: List[PhotoModel] = []
        self.view.bind("<Configure>", self.onFrameResize, add="+")

    def loadThumbs(self, imgPaths: List[str]) -> None:
        progressDialog = ProgressDialog(
            window=self.view.winfo_toplevel(),
            text=_("Creating thumbnails...")
        )

        thread = threading.Thread(
            target=self.loadThumbsThread,
            args=(
                imgPaths,
                lambda name, step, of: self.view.after(
                    0,
                    lambda: progressDialog.progress(
                        name,
                        step,
                        of
                    )
                ),
                lambda: progressDialog.customDestroy()
            )
        )
        thread.start()

    def loadThumbsThread(
        self,
        imgPaths: List[str],
        progressCallback: Callable[[str, int, int], None],
        endCallback: Callable[[], None]
    ) -> None:
        filesCount = len(imgPaths)
        filesProgress = 0
        for path in imgPaths:
            fileName = os.path.splitext(os.path.basename(path))[0]
            filesProgress += 1
            progressCallback(fileName, filesProgress, filesCount)

            alreadyExists = [img for img in self.images if img.path == path]
            if len(alreadyExists) > 0:
                continue

            try:
                image = Image.open(path)
            except FileNotFoundError:
                continue

            self.images.append(
                PhotoModel(
                    path=path,
                    name=shortenText(os.path.basename(
                        path), THUMB_LABEL_MAX_LEN),
                    thumb=self.scaleImgWithAspectRatio(image)
                )
            )
        endCallback()
        self.refreshThumbs()

    def refreshThumbs(self) -> None:
        for widget in self.view.winfo_children():
            widget.destroy()

        row = 0
        col = 0
        for index, image in enumerate(self.images):
            thumbWidget = image.widget(self.view)

            for child in thumbWidget.winfo_children():
                if isinstance(child, ctk.CTkLabel):
                    child.bind("<Enter>", lambda _,
                               widget=thumbWidget: self.view.onFrameHover(widget))
                    child.bind("<Leave>", lambda _,
                               widget=thumbWidget: self.view.onFrameLeave(widget))
                    child.bind("<Button-2>", lambda _,
                               index=index: self.removeImage(index))
                    child.bind("<Button-3>", lambda _,
                               index=index: self.removeImage(index))
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

    def scaleImgWithAspectRatio(self, image: Image) -> ctk.CTkImage:
        widthRatio = (THUMB_MAX_WIDTH / float(image.size[0]))
        height = int((float(image.size[1]) * float(widthRatio)))
        width = THUMB_MAX_WIDTH

        if (height > THUMB_MAX_HEIGHT):
            heightRatio = (THUMB_MAX_HEIGHT / float(image.size[1]))
            width = int((float(image.size[0]) * float(heightRatio)))
            height = THUMB_MAX_HEIGHT

        resized_image = image.resize((width, height), Image.LANCZOS)
        return ctk.CTkImage(resized_image, size=(width, height))

    def removeImage(self, index: int) -> None:
        del self.images[index]
        self.refreshThumbs()

    def onFrameResize(self, size) -> None:
        allowedCollumns = size.width // (THUMB_WIDTH + 10)
        if (allowedCollumns != self.colCount):
            self.colCount = allowedCollumns
            self.refreshThumbs()

    def getImagePaths(self) -> List[str]:
        return [image.path for image in self.images]
