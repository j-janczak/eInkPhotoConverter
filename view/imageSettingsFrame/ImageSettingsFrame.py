from view.customSegmentedButtons.CustomSegmentedButtons import CustomSegmentedButtons
from model.ImageSettingsModel import ImageSettingsModel, Transformation
from .ImageSettingsFrameController import ImageSettingsFrameController
from config.config import PADDING_XS, PADDING_S, PADDING_M
from view.customFrame.CustomFrame import CustomFrame
from utils.ConfigMapper import ConfigMapper
import customtkinter as ctk
from typing import Tuple
from PIL import Image


class ImageSettingsFrame(CustomFrame):
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
        configMapper: ConfigMapper = ...,
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
            configMapper,
            **kwargs
        )
        self.controller=ImageSettingsFrameController(self, configMapper)

        img_dither_none = ctk.CTkImage(Image.open("images/img_dither_none_white.png"))
        img_dither_floyd_steinberg = ctk.CTkImage(Image.open("images/img_dither_floyd_steinberg_white.png"))

        img_mode_crop = ctk.CTkImage(Image.open("images/img_mode_crop_white.png"))
        img_mode_scale = ctk.CTkImage(Image.open("images/img_mode_scale_white.png"))

        self.label1 = ctk.CTkLabel(self, text="Ustawienia konwertowania")
        self.label1.pack(
            pady=[PADDING_S, PADDING_XS]
        )

        self.imgDitheringBtns = CustomSegmentedButtons(
            master=self,
            label="Dithering",
            textValues=["Brak", "Floyd-Steinberg"],
            imgValues=[img_dither_none, img_dither_floyd_steinberg],
            values=[Image.Dither.NONE, Image.Dither.FLOYDSTEINBERG],
            defaultValue=configMapper.config.imageSettings.ditheringAlgorithm,
            onClick=self.controller.updateDitheringAlgorithm
        )
        self.imgDitheringBtns.pack(
            side=ctk.LEFT,
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_XS, PADDING_M]
        )

        self.imgTransformationBtns = CustomSegmentedButtons(
            master=self,
            label="Tryb przekształcania",
            textValues=["Przytnij", "Dopasuj", "Rozciągnij"],
            imgValues=[img_mode_crop, img_mode_scale, img_mode_scale],
            values=[Transformation.CROP,
                    Transformation.FIT, Transformation.STRECH],
            defaultValue=configMapper.config.imageSettings.transformationMode,
            onClick=self.controller.updateTransformationMode
        )
        self.imgTransformationBtns.pack(
            side=ctk.RIGHT,
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_S, PADDING_M]
        )

    def getSettings(self) -> ImageSettingsModel:
        return ImageSettingsModel(
            ditheringAlgorithm=self.imgDitheringBtns.getValue(),
            transformationMode=self.imgTransformationBtns.getValue()
        )
