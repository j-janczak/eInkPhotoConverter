from config.DimAndColors import PADDING_S
from .CreditsLabel import CreditsLabel
from utils.GettextConfig import _
import tkinter.font as tkFont
import customtkinter as ctk
from typing import Tuple


class CreditsFrame(ctk.CTkFrame):
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
        **kwargs
    ):
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

        creditsLabel = ctk.CTkLabel(
            self,
            text=_("Credits"),
            height=0
        )
        creditsLabel.pack(
            anchor="nw",
            padx=PADDING_S,
            pady=[PADDING_S, 0]
        )
        currentFont = tkFont.Font(font=creditsLabel.cget("font"))
        newFont = (currentFont.actual("family"), 20, "bold")
        creditsLabel.configure(font=newFont)

        CreditsLabel(
            self,
            libName="Python",
            libUrl="https://www.python.org/",
            libAuthor="Python Software Foundation",
            libLicense="Python License",
            libLicenseUrl="https://docs.python.org/3/license.html"
        ).pack(
            fill=ctk.X,
            pady=[PADDING_S, 0],
            padx=[PADDING_S]
        )

        CreditsLabel(
            self,
            libName="Tkinter",
            libUrl="https://tcl.tk/",
            libAuthor="Steen Lumholt and\nGuido van Rossum",
            libLicense="Python License",
            libLicenseUrl="https://github.com/python/cpython?tab=License-1-ov-file#readme"
        ).pack(
            fill=ctk.X,
            pady=[PADDING_S, 0],
            padx=[PADDING_S]
        )

        CreditsLabel(
            self,
            libName="CustomTkinter",
            libUrl="https://github.com/TomSchimansky/CustomTkinter",
            libAuthor="Tom Schimansky",
            libLicense="MIT license",
            libLicenseUrl="https://github.com/TomSchimansky/CustomTkinter?tab=MIT-1-ov-file#readme"
        ).pack(
            fill=ctk.X,
            pady=[PADDING_S, 0],
            padx=[PADDING_S]
        )

        CreditsLabel(
            self,
            libName="Packaging",
            libUrl="https://github.com/pypa/packaging",
            libAuthor="Donald Stufft",
            libLicense="Apache Software License",
            libLicenseUrl="https://github.com/pypa/packaging/blob/main/LICENSE.APACHE"
        ).pack(
            fill=ctk.X,
            pady=[PADDING_S, 0],
            padx=[PADDING_S]
        )

        CreditsLabel(
            self,
            libName="Pillow",
            libUrl="https://github.com/python-pillow/Pillow",
            libAuthor="Jeffrey A. Clark",
            libLicense="HPND License",
            libLicenseUrl="https://github.com/python-pillow/Pillow?tab=License-1-ov-file#readme"
        ).pack(
            fill=ctk.X,
            pady=[PADDING_S, 0],
            padx=[PADDING_S]
        )

        CreditsLabel(
            self,
            libName="Pydantic",
            libUrl="https://github.com/pydantic/pydantic",
            libAuthor="Samuel Colvin",
            libLicense="MIT License",
            libLicenseUrl="https://github.com/pydantic/pydantic?tab=MIT-1-ov-file#readme"
        ).pack(
            fill=ctk.X,
            pady=[PADDING_S, 0],
            padx=[PADDING_S]
        )
