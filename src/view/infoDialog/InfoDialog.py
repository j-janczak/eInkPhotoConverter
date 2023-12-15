from view.customDialog.CustomDialog import CustomDialog
from config.config import PADDING_S, PADDING_M
from utils.GettextConfig import _
import customtkinter as ctk
from typing import Tuple


class InfoDialog(CustomDialog):
    def __init__(
            self,
            *args,
            fg_color: str | Tuple[str, str] | None = None,
            window: ctk.CTk,
            text: str,
            **kwargs,
    ) -> None:
        super().__init__(
            *args,
            fg_color=fg_color,
            window=window,
            **kwargs
        )
        self.title(_("Info"))

        ctk.CTkLabel(
            master=self,
            text=text
        ).pack(
            fill=ctk.X,
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_S]
        )

        ctk.CTkButton(
            master=self,
            text="OK",
            command=self.destroy
        ).pack(
            anchor="e",
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M]
        )
