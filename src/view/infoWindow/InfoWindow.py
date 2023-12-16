from view.customDialog.CustomDialog import CustomDialog
from .appInfoFrame.AppInfoFrame import AppInfoFrame
from .appInfoFrame.AppInfoFrameController import AppInfoFrameController
from .manualFrame.ManualFrame import ManualFrame
from .creditsFame.CreditsFrame import CreditsFrame
from config.config import PADDING_S, PADDING_M
from utils.GettextConfig import _
import customtkinter as ctk
from typing import Tuple


class InfoWindow(CustomDialog):
    def __init__(
        self,
        *args,
        fg_color: str | Tuple[str, str] | None = None,
        window: ctk.CTk,
        **kwargs
    ) -> None:
        super().__init__(
            *args,
            fg_color=fg_color,
            window=window,
            **kwargs
        )
        self.title(_("About"))
        self.resizable(width=False, height=False)

        appInfoFrame = AppInfoFrame(self)
        appInfoFrame.pack(
            fill=ctk.Y,
            side=ctk.LEFT,
            padx=[PADDING_M, PADDING_S],
            pady=PADDING_M
        )
        AppInfoFrameController(appInfoFrame)

        ManualFrame(self).pack(
            fill=ctk.BOTH,
            side=ctk.LEFT,
            padx=[PADDING_S, PADDING_S],
            pady=PADDING_M
        )

        CreditsFrame(self).pack(
            fill=ctk.BOTH,
            side=ctk.LEFT,
            padx=[PADDING_S, PADDING_M],
            pady=PADDING_M
        )

        self.grabAndCenter()
