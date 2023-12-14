from view.customSegmentedButtons.CustomSegmentedButtons import CustomSegmentedButtons
from model.SettingsModel import SettingsModel, Dithering, Transformation
from config.config import PADDING_XS, PADDING_S, PADDING_M
import customtkinter as ctk
from PIL import Image


class ImageSettingsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        img_dither_none = ctk.CTkImage(light_image=Image.open("images/img_dither_none_black.png"),
                                       dark_image=Image.open("images/img_dither_none_white.png"))
        img_dither_floyd_steinberg = ctk.CTkImage(light_image=Image.open("images/img_dither_floyd_steinberg_black.png"),
                                                  dark_image=Image.open("images/img_dither_floyd_steinberg_white.png"))

        img_mode_crop = ctk.CTkImage(light_image=Image.open("images/img_mode_crop_black.png"),
                                     dark_image=Image.open("images/img_mode_crop_white.png"))
        img_mode_scale = ctk.CTkImage(light_image=Image.open("images/img_mode_scale_black.png"),
                                      dark_image=Image.open("images/img_mode_scale_white.png"))

        self.label1 = ctk.CTkLabel(self, text="Ustawienia konwertowania")
        self.label1.pack(
            pady=[PADDING_S, PADDING_XS]
        )

        self.imgDitheringBtns = CustomSegmentedButtons(
            self,
            "Dithering",
            ["Brak", "Floyd-Steinberg"],
            [img_dither_none, img_dither_floyd_steinberg],
            [Dithering.NONE, Dithering.FLOYD_STEINBERG],
            1
        )
        self.imgDitheringBtns.pack(
            side=ctk.LEFT,
            padx=[PADDING_M, PADDING_S],
            pady=[PADDING_XS, PADDING_M]
        )

        self.imgTransformationBtns = CustomSegmentedButtons(
            self,
            "Tryb przekształcania",
            ["Przytnij", "Dopasuj", "Rozciągnij"],
            [img_mode_crop, img_mode_scale, img_mode_scale],
            [Transformation.CROP, Transformation.FIT, Transformation.STRECH]
        )
        self.imgTransformationBtns.pack(
            side=ctk.RIGHT,
            padx=[PADDING_S, PADDING_M],
            pady=[PADDING_S, PADDING_M]
        )

    def getSettings(self) -> SettingsModel:
        return SettingsModel(
            dithering=self.imgDitheringBtns.getValue(),
            transformation=self.imgTransformationBtns.getValue()
        )
