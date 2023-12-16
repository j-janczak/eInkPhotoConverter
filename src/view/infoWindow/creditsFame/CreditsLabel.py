
from view.linkLabel.LinkLabel import LinkLabel
from config.config import PADDING_S
import customtkinter as ctk
from typing import Tuple


class CreditsLabel(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        libName: str = "",
        libUrl: str = "",
        libAuthor: str = "",
        libLicense: str = "",
        libLicenseUrl: str = "",
        **kwargs
    ) -> None:
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)

        LinkLabel(
            self,
            text=libName,
            url=libUrl
        ).grid(
            row=0,
            column=0,
            stick=ctk.W,
            padx=[PADDING_S, 0]
        )
        ctk.CTkLabel(
            self,
            text=f" {libAuthor}"
        ).grid(
            row=0,
            column=1,
            stick=ctk.E,
            padx=[0, PADDING_S]
        )
        LinkLabel(
            self,
            text=libLicense,
            url=libLicenseUrl
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            stick=ctk.W,
            padx=[PADDING_S, 0],
            pady=[0, PADDING_S]
        )