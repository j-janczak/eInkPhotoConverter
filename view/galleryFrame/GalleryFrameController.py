from config.config import THUMB_MAX_WIDTH, THUMB_MAX_HEIGHT, THUMB_LABEL_MAX_LEN, PADDING_M
from view.progressDialog.ProgressDialog import ProgressDialog
from model.PhotoModel import PhotoModel
from utils.utils import shortenText
from typing import List, Callable
import customtkinter as ctk
from PIL import Image
import threading
import os


class GalleryFrameController():
    def __init__(self, view) -> None:
        self.view = view
        self.images: List[PhotoModel] = []

    def loadThumbs(self, imgPaths: List[str]) -> None:
        progressDialog = ProgressDialog(
            window=self.view.winfo_toplevel(),
            text="Tworzenie miniatur"
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
                lambda: progressDialog.destroy()
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

            self.images.append(
                PhotoModel(
                    path=path,
                    name=shortenText(os.path.basename(
                        path), THUMB_LABEL_MAX_LEN),
                    thumb=self.scaleImgWithAspectRatio(Image.open(path))
                )
            )
        endCallback()
        self.view.refreshThumbs()

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
        self.view.refreshThumbs()

    def getImagePaths(self) -> List[str]:
        return [image.path for image in self.images]
