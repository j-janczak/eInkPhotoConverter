from ..outputPathSelector.OutputPathSelector import OutputPathSelector
from ..imageSettingsFrame.ImageSettingsFrame import ImageSettingsFrame
from ..imageSelectorFrame.ImageSelectorFrame import ImageSelectorFrame
from config.config import PADDING_S, PADDING_M
from utils.ConfigMapper import ConfigMapper
from utils.GettextConfig import _
import customtkinter as ctk


class MainView(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.configMapper = ConfigMapper()

        self.minsize(840, 500)

        self.title(_("eInk Images Converter by Jakub Janczak"))
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

        self.imageSettingsFrame = ImageSettingsFrame(
            self, configMapper=self.configMapper)
        self.imageSettingsFrame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_S, PADDING_M],
        )

        self.outputPathSelector = OutputPathSelector(
            self,
            configMapper=self.configMapper
        )
        self.outputPathSelector.grid(
            row=0,
            column=1,
            rowspan=2,
            sticky="nsew",
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_M, PADDING_M],
        )
