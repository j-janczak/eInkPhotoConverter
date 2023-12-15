from utils.ConfigMapper import config, updateConfig
from tkinter import filedialog, StringVar
from .RightFrame import RightFrame
from typing import Callable


class RightFrameController():
    def __init__(
        self,
        view: RightFrame
    ) -> None:
        self.view = view
        self.imgOutputPathText = StringVar(
            value=config.outputPath)
        self.view.imgOutputPath.configure(textvariable=self.imgOutputPathText)
        self.view.imgActionBtn.configure(command=self.openDirSelDialog)

    def openDirSelDialog(self) -> None:
        selectedFolder = filedialog.askdirectory()
        if selectedFolder != "":
            updateConfig({
                "outputPath": selectedFolder
            })
            self.imgOutputPathText.set(selectedFolder)

    def setConvertCallback(self, callback: Callable[[], None] = None) -> None:
        self.view.imgConvertBtn.configure(command=callback)

    def getOutputPath(self) -> str:
        return self.imgOutputPathText.get()
