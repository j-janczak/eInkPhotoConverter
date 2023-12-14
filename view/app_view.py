from .outputPathSelector.OutputPathSelector import OutputPathSelector
from .imageSettingsFrame.ImageSettingsFrame import ImageSettingsFrame
from .imageSelectorFrame.ImageSelectorFrame import ImageSelectorFrame
from .progressWindow.ProgressWindow import ProgressWindow
from config.config import PADDING_S, PADDING_M
from utils.Converter import convertImages
import customtkinter as ctk
import threading

class AppView(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.minsize(640, 500)

        self.title("MVC Example")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.imageSelectorFrame = ImageSelectorFrame(self)
        self.imageSelectorFrame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_M, PADDING_S]
        )

        self.imageSettingsFrame = ImageSettingsFrame(self)
        self.imageSettingsFrame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_S, PADDING_M],
        )

        self.outputPathSelector = OutputPathSelector(
            self,
            convertCallback=self.convertImages
        )
        self.outputPathSelector.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_M, PADDING_S],
        )

        self.authorLabel = ctk.CTkLabel(self, text="by Jakub Janczak")
        self.authorLabel.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=[PADDING_S, PADDING_M],
            pady=[0, 0],
        )

    def convertImages(self) -> None:
        settings = self.imageSettingsFrame.getSettings()
        settings.outputPath = self.outputPathSelector.getOutputPath()
        imagePaths = self.imageSelectorFrame.getImagePaths()

        progressWindow = ProgressWindow(self, "Konwertowanie")

        thread = threading.Thread(
            target=convertImages,
            args=(
                imagePaths, 
                settings, 
                lambda name, step, of: self.after(
                    0, 
                    lambda: progressWindow.progress(
                        name, 
                        step, 
                        of
                    )
                ),
                lambda: progressWindow.destroy()
            )
        )
        thread.start()

    def on_resize(self, event):
        print(f"Okno zmieniło rozmiar: {event.width}x{event.height}")
