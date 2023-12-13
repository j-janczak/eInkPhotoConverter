from tkinter import filedialog, StringVar


class OutputPathSelectorController:
    def __init__(self, master: any) -> None:
        self.view = master
        self.imgOutputPathText = StringVar()

    def initController(self):
        self.view.imgActionBtn.configure(command=self.openDirSelDialog)

    def openDirSelDialog(self):
        folder_selected = filedialog.askdirectory()
        self.imgOutputPathText.set(folder_selected)
