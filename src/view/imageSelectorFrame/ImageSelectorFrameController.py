from ..galleryFrame.GalleryFrameController import GalleryFrameController
from .ImageSelectorFrame import ImageSelectorFrame
import tkinter.filedialog as filedialog
from utils.GettextConfig import _
from typing import List


class ImageSelectorFrameController():
    def __init__(
        self,
        view: ImageSelectorFrame
    ) -> None:
        self.view = view
        self.galleryFrameController = GalleryFrameController(
            self.view.galleryFrame)
        self.view.sel_imgs_btn.configure(command=self.openImgSelDialog)

    def openImgSelDialog(self) -> None:
        fileTypes = [(_("Image files"), "*.jpg *.jpeg *.png *.gif *.bmp")]
        imgPaths = filedialog.askopenfilenames(filetypes=fileTypes)
        self.galleryFrameController.loadThumbs(imgPaths)

    def getImagePaths(self) -> List[str]:
        return self.galleryFrameController.getImagePaths()
