from ..outputPathSelector.OutputPathSelector import OutputPathSelector
from ..imageSettingsFrame.ImageSettingsFrame import ImageSettingsFrame
from ..imageSelectorFrame.ImageSelectorFrame import ImageSelectorFrame
from config.config import PADDING_S, PADDING_M
from utils.GettextConfig import _
import customtkinter as ctk
from typing import Tuple


class MainView(ctk.CTk):
    def __init__(
            self,
            fg_color: str | Tuple[str, str] | None = None,
            **kwargs
    ) -> None:
        super().__init__(
            fg_color,
            **kwargs
        )

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

        self.imageSettingsFrame = ImageSettingsFrame(self)
        self.imageSettingsFrame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_S, PADDING_M],
        )

        self.outputPathSelector = OutputPathSelector(self)
        self.outputPathSelector.grid(
            row=0,
            column=1,
            rowspan=2,
            sticky="nsew",
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_M, PADDING_M],
        )
