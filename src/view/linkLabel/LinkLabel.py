from typing import Tuple
import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
import webbrowser


class LinkLabel(ctk.CTkLabel):
    def __init__(
            self,
            master: any,
            width: int = 0,
            height: int = 0,
            corner_radius: int | None = None,
            bg_color: str | Tuple[str, str] = "transparent",
            fg_color: str | Tuple[str, str] | None = None,
            text_color: str = "#1F51FF",
            text_color_disabled: str | Tuple[str, str] | None = None,
            text: str = "CTkLabel",
            font: tuple | CTkFont | None = None,
            image: CTkImage | None = None,
            compound: str = "center",
            anchor: str = "center",
            cursor="hand2",
            url: str = "",
            wraplength: int = 0, **kwargs
    ) -> None:
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            bg_color,
            fg_color,
            text_color,
            text_color_disabled,
            text,
            font,
            image,
            compound,
            anchor,
            wraplength,
            cursor=cursor,
            **kwargs
        )
        self.bind("<Button-1>", lambda e: webbrowser.open_new(url))
