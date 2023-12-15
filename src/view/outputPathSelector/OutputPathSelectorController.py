from utils.ConfigMapper import config, updateConfig
from .OutputPathSelector import OutputPathSelector
from tkinter import filedialog, StringVar
from typing import Callable


class OutputPathSelectorController():
    def __init__(
        self,
        view: OutputPathSelector
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
