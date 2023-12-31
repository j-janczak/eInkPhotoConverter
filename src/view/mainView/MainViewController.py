from ..imageSelectorFrame.ImageSelectorFrameController import ImageSelectorFrameController
from ..imageSettingsFrame.ImageSettingsFrameController import ImageSettingsFrameController
from ..rightFrame.RightFrameController import RightFrameController
from ..progressDialog.ProgressDialog import ProgressDialog
from model.ConvertErrorModel import ConvertErrorModel
from view.infoDialog.InfoDialog import InfoDialog
from utils.Converter import convertImages
from ..mainView.MainView import MainView
from utils.GettextConfig import _
from typing import List
import subprocess
import threading
import sys
import os


class MainViewController:
    def __init__(
            self,
            view: MainView
    ) -> None:
        self.view = view
        self.imageSelectorController = ImageSelectorFrameController(
            self.view.imageSelectorFrame)
        self.imageSettingsController = ImageSettingsFrameController(
            self.view.imageSettingsFrame)
        self.rightFrameController = RightFrameController(
            self.view.outputPathSelector)
        self.rightFrameController.setConvertCallback(self.convertImages)

    def convertImages(self) -> None:
        imageSettings = self.imageSettingsController.getSettings()
        outputPath = self.rightFrameController.getOutputPath()
        imagePaths = self.imageSelectorController.getImagePaths()

        if len(imagePaths) == 0:
            InfoDialog(
                window=self.view,
                text=_("No files selected")
            )
            return
        
        if not isinstance(outputPath, str) or not len(outputPath) > 0:
            InfoDialog(
                window=self.view,
                text=_("Save location not selected")
            )
            return

        self.progressDialog = ProgressDialog(
            window=self.view,
            text=_("Converting...")
        )

        thread = threading.Thread(
            target=convertImages,
            args=(
                imagePaths,
                imageSettings,
                outputPath,
                lambda name, step, of: self.view.after(
                    0,
                    lambda: self.progressDialog.progress(
                        name,
                        step,
                        of
                    )
                ),
                self.displayEndConvertDialog
            )
        )
        thread.start()

    def displayEndConvertDialog(self, errorFiles: List[ConvertErrorModel]) -> None:
        self.progressDialog.customDestroy()

        if len(errorFiles) == 0:
            text = _("Image conversion completed successfully!")
        else:
            text = _("There were errors converting some images")
            for error in errorFiles:
                text += f"\n\"{error.file}\" - {error.reason}"

        InfoDialog(
            window=self.view,
            text=text,
            action=(
                _("Open folder"),
                lambda: self.openFolder(self.rightFrameController.getOutputPath())
            )
        )

    def openFolder(self, path):
        if sys.platform == 'win32':
            os.startfile(path)
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])
