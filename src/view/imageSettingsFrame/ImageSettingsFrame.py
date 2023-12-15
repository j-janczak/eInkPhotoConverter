from view.customSegmentedButtons.CustomSegmentedButtons import CustomSegmentedButtons
from config.config import PADDING_XS, PADDING_S, PADDING_M
from model.ImageSettingsModel import Transform
from utils.ConfigMapper import config
from utils.GettextConfig import _
import customtkinter as ctk
from typing import Tuple
from PIL import Image


class ImageSettingsFrame(ctk.CTkFrame):
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

        imgDitherNone = ctk.CTkImage(
            Image.open("images/img_dither_none_white.png"))
        imgDitherFloydSteinberg = ctk.CTkImage(
            Image.open("images/img_dither_floyd_steinberg_white.png"))

        imgModeCrop = ctk.CTkImage(
            Image.open("images/img_mode_crop_white.png"))
        imgModeFit = ctk.CTkImage(
            Image.open("images/img_mode_fit_white.png"))
        imgModeStretch = ctk.CTkImage(
            Image.open("images/img_mode_stretch_white.png"))

        self.label1 = ctk.CTkLabel(self, text=_("Convert settings"))
        self.label1.pack(
            pady=[PADDING_S, PADDING_XS]
        )

        self.imgDitheringBtns = CustomSegmentedButtons(
            master=self,
            label=_("Dithering algorithm"),
            textValues=[_("None"), _("Floyd-Steinberg")],
            imgValues=[imgDitherNone, imgDitherFloydSteinberg],
            values=[Image.Dither.NONE, Image.Dither.FLOYDSTEINBERG],
            defaultValue=config.imageSettings.ditheringAlgorithm,
        )
        self.imgDitheringBtns.pack(
            side=ctk.LEFT,
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_XS, PADDING_M]
        )

        self.imgTransformBtns = CustomSegmentedButtons(
            master=self,
            label=_("Transform mode"),
            textValues=[_("Crop"), _("Fit"), _("Stretch")],
            imgValues=[imgModeCrop, imgModeFit, imgModeStretch],
            values=[Transform.CROP, Transform.FIT, Transform.STRETCH],
            defaultValue=config.imageSettings.transformMode,
        )
        self.imgTransformBtns.pack(
            side=ctk.RIGHT,
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_S, PADDING_M]
        )
