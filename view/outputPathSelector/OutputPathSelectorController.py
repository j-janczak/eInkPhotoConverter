from view.customFrame.CustomFrameController import CustomFrameController
from utils.ConfigMapper import ConfigMapper
from tkinter import filedialog, StringVar

class OutputPathSelectorController(CustomFrameController):
    def __init__(self, master: any, configMapper: ConfigMapper) -> None:
        super().__init__(master, configMapper)

        self.view = master
        self.imgOutputPathText = StringVar(value=configMapper.config.outputPath)

    def openDirSelDialog(self):
        selectedFolder = filedialog.askdirectory()
        if selectedFolder != "":
            self.configMapper.update({
                "outputPath": selectedFolder
            })
            self.imgOutputPathText.set(selectedFolder)
