from ..galleryFrame.GalleryFrameController import GalleryFrameController
from .ImageSelectorFrame import ImageSelectorFrame
from ..infoDialog.InfoDialog import InfoDialog
import tkinter.filedialog as filedialog
from ...utils.GettextConfig import _
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
        imgPaths: List[str] = filedialog.askopenfilenames(filetypes=fileTypes)

        if len(imgPaths) > 100:
            InfoDialog(
                window=self.view.winfo_toplevel(),
                text=_("You can select a maximum of 100 files")
            )
            return
        elif len(imgPaths) > 0:
            self.galleryFrameController.loadThumbs(imgPaths)

    def getImagePaths(self) -> List[str]:
        return self.galleryFrameController.getImagePaths()
