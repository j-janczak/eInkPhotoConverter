from view.outputPathSelector.OutputPathSelector import OutputPathSelector
from view.imageSettingsFrame.ImageSettingsFrame import ImageSettingsFrame
from .imageSelectorFrame.ImageSelectorFrame import ImageSelectorFrame
from view.infoFrame.InfoFrame import InfoFrame
from config.config import PADDING_S, PADDING_M
from utils.Converter import convertImages
import customtkinter as ctk


class AppView(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        # self.bind("<Configure>", self.on_resize)
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

        self.outputPathSelector = OutputPathSelector(self)
        self.outputPathSelector.grid(
            row=1,
            column=0,
            rowspan=2,
            sticky="ew",
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_S, PADDING_M],
        )

        self.imageSettingsFrame = ImageSettingsFrame(
            self,
            convertImagesCallback=self.convertImages
        )
        self.imageSettingsFrame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_M, PADDING_S],
        )

        self.infoFrame = InfoFrame(self)
        self.infoFrame.grid(
            row=1,
            column=1,
            sticky="new",
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_S, 0],
        )

        self.authorLabel = ctk.CTkLabel(self, text="Made with love by Jojczak")
        self.authorLabel.grid(
            row=2,
            column=1,
            sticky="new",
            padx=[PADDING_S, PADDING_M],
            pady=[0, 0],
        )

    def convertImages(self) -> None:
        settings = self.imageSettingsFrame.getSettings()
        settings.outputPath = self.outputPathSelector.getOutputPath()
        convertImages(
            imagePaths=self.imageSelectorFrame.getImagePaths(),
            settings=settings
        )

    def on_resize(self, event):
        print(f"Okno zmieniło rozmiar: {event.width}x{event.height}")
