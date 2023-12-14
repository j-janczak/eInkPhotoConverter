from ..progressDialog.ProgressDialog import ProgressDialog
from model.ConvertErrorModel import ConvertErrorModel
from view.infoDialog.InfoDialog import InfoDialog
from utils.Converter import convertImages
from ..mainView.MainView import MainView
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
                text="Nie wybrano plików"
            )
            return

        progressDialog = ProgressDialog(
            window=self.view,
            text="Konwertowanie"
        )

        thread = threading.Thread(
            target=convertImages,
            args=(
                imagePaths,
                imageSettings,
                outputPath,
                lambda name, step, of: self.view.after(
                    0,
                    lambda: progressDialog.progress(
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
        if len(errorFiles) == 0:
            text = "Konwersja obrazów zakończona pomyślnie"
        else:
            text = "Wystąpiły błędy przy niektórych obrazach"
            for error in errorFiles:
                text += f"\n\"{error.file}\" - {error.reason}"

        InfoDialog(
            window=self.view,
            text=text
        )
