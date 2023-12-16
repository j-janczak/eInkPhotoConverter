from config.DimAndColors import PADDING_XS, PADDING_S, PADDING_M
from utils.GettextConfig import _
import tkinter.font as tkFont
import customtkinter as ctk
from typing import Tuple


class ManualFrame(ctk.CTkFrame):
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

        ctk.CTkLabel(
            self,
            text=_("The \"eInk Photo Converter\" program converts photos into 24-bit BMP files with a resolution of 800x480, utilizing a 7-color palette. Photos in this format are suitable for display on the PhotoPainter device from WaveShare."),
            wraplength=400,
            justify="left"
        ).pack(
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_XS]
        )

        ditherSettingsLabel = ctk.CTkLabel(
            self,
            text=_("Dithering algorithm settings:"),
            justify="left"
        )
        ditherSettingsLabel.pack(
            anchor="w",
            padx=PADDING_M,
            pady=[PADDING_S, 0]
        )
        currentFont = tkFont.Font(font=ditherSettingsLabel.cget("font"))
        newFont = (currentFont.actual("family"), currentFont.actual("size"), "bold")
        ditherSettingsLabel.configure(font=newFont)

        ctk.CTkLabel(
            self,
            text=_("None - does not apply a dithering algorithm; for each pixel of the image, the most fitting color from the seven-color palette is chosen."),
            wraplength=400,
            justify="left"
        ).pack(
            anchor="w",
            padx=PADDING_M,
            pady=[0, PADDING_XS]
        )

        ctk.CTkLabel(
            self,
            text=_("Floyd-Steinberg - Simulate greater color depth with a limited palette. It distributes the quantization error of a pixel to its neighboring pixels, allowing for smoother color transitions. (Recommend)"),
            wraplength=400,
            justify="left"
        ).pack(
            anchor="w",
            padx=PADDING_M,
            pady=[PADDING_XS, PADDING_XS]
        )

        transformSettingsLabel = ctk.CTkLabel(
            self,
            text=_("Transform mode settings:"),
            justify="left"
        )
        transformSettingsLabel.pack(
            anchor="w",
            padx=PADDING_M,
            pady=[PADDING_S, 0]
        )
        currentFont = tkFont.Font(font=transformSettingsLabel.cget("font"))
        newFont = (currentFont.actual("family"), currentFont.actual("size"), "bold")
        transformSettingsLabel.configure(font=newFont)

        ctk.CTkLabel(
            self,
            text=_("Crop - If the image has different proportions than the target size, it is cropped to fill the entire available space. This may result in trimmed edges."),
            wraplength=400,
            justify="left"
        ).pack(
            anchor="w",
            padx=PADDING_M,
            pady=[0, PADDING_XS]
        )

        ctk.CTkLabel(
            self,
            text=_("Fit - If the image has different proportions than the target size, it is scaled down while maintaining its aspect ratio to fit within the specified dimensions. If the proportions differ from the target dimensions, empty spaces are filled with a white background."),
            wraplength=400,
            justify="left"
        ).pack(
            anchor="w",
            padx=PADDING_M,
            pady=[PADDING_XS, PADDING_XS]
        )

        ctk.CTkLabel(
            self,
            text=_("Stretch - If the image has different proportions than the target size, it is stretched to fill the entire available space. This results in distortion of the image."),
            wraplength=400,
            justify="left"
        ).pack(
            anchor="w",
            padx=PADDING_M,
            pady=[PADDING_XS, PADDING_M]
        )