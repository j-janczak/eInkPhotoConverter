from view.customDialog.CustomDialog import CustomDialog
from config.DimAndColors import PADDING_M
from utils.Utils import shortenText
from customtkinter import CTk
from _tkinter import TclError
import customtkinter as ctk
from typing import Tuple


class ProgressDialog(CustomDialog):
    def __init__(
            self,
            *args,
            fg_color: str | Tuple[str, str] | None = None,
            window: CTk,
            text: str,
            **kwargs
    ) -> None:
        super().__init__(
            *args,
            fg_color=fg_color,
            window=window,
            **kwargs
        )
        self.resizable(width=False, height=False)
        self.overrideredirect(True)

        self.dialogFrame = ctk.CTkFrame(self)
        self.dialogFrame.pack(
            fill=ctk.BOTH,
            padx=PADDING_M,
            pady=PADDING_M
        )

        self.progressTextWidget = ctk.CTkLabel(self.dialogFrame)
        self.progressTextWidget.pack(
            pady=PADDING_M
        )

        self.progressBar = ctk.CTkProgressBar(self.dialogFrame)
        self.progressBar.set(0)
        self.progressBar.pack(
            fill=ctk.X,
            padx=PADDING_M,
            pady=[0, PADDING_M]
        )

        self.text = text
        self.grabAndCenter()

    def progress(self, fileName: str, step: int, of: int) -> None:
        progressText = f"{self.text}: \"{shortenText(fileName, 15)}\" {step}/{of}"
        self.progressTextWidget.configure(text=progressText)
        self.progressBar.set(step/of)
        self.centerDialog()
