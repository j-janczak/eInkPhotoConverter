from config.DimAndColors import IMG_THUMB_BG, IMG_THUMB_HOVER_BG
from customtkinter.windows.widgets.font import CTkFont
from typing import Tuple, Literal, Tuple
import customtkinter as ctk


class GalleryFrame(ctk.CTkScrollableFrame):
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
        scrollbar_fg_color: str | Tuple[str, str] | None = None,
        scrollbar_button_color: str | Tuple[str, str] | None = None,
        scrollbar_button_hover_color: str | Tuple[str, str] | None = None,
        label_fg_color: str | Tuple[str, str] | None = None,
        label_text_color: str | Tuple[str, str] | None = None,
        label_text: str = "", label_font: tuple | CTkFont | None = None,
        label_anchor: str = "center",
        orientation: Literal['vertical', 'horizontal'] = "vertical"
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
            scrollbar_fg_color,
            scrollbar_button_color,
            scrollbar_button_hover_color,
            label_fg_color,
            label_text_color,
            label_text,
            label_font,
            label_anchor,
            orientation
        )

    def onFrameHover(self, widget: ctk.CTkFrame) -> None:
        widget.configure(fg_color=IMG_THUMB_HOVER_BG)

    def onFrameLeave(self, widget: ctk.CTkFrame) -> None:
        widget.configure(fg_color=IMG_THUMB_BG)
