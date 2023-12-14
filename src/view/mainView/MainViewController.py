from ..progressDialog.ProgressDialog import ProgressDialog
from model.ConvertErrorModel import ConvertErrorModel
from view.infoDialog.InfoDialog import InfoDialog
from utils.Converter import convertImages
from ..mainView.MainView import MainView
from utils.GettextConfig import _
from typing import List
import threading


class MainViewController:
    def __init__(
            self,
            view: MainView
    ) -> None:
        self.view = view
        self.view.outputPathSelector.setConvertCallback(self.convertImages)

    def convertImages(self) -> None:
        imageSettings = self.view.imageSettingsFrame.getSettings()
        outputPath = self.view.outputPathSelector.getOutputPath()
        imagePaths = self.view.imageSelectorFrame.getImagePaths()

        if len(imagePaths) == 0:
            InfoDialog(
                window=self.view,
                text=_("No files selected")
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

    def displayEndConvertDialog(self, errorFiles: List[ConvertErrorModel]):
        self.progressDialog.destroy()
        
        if len(errorFiles) == 0:
            text = _("Image conversion completed successfully!")
        else:
            text = _("There were errors converting some images")
            for error in errorFiles:
                text += f"\n\"{error.file}\" - {error.reason}"

        InfoDialog(
            window=self.view,
            text=text
        )
