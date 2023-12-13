from view.customSegmentedButtons.CustomSegmentedButtons import CustomSegmentedButtons
from model.SettingsModel import SettingsModel, Orientation, Dithering, Transformation
from config.config import PADDING_XS, PADDING_S, PADDING_M
import customtkinter as ctk
from PIL import Image


class ImageSettingsFrame(ctk.CTkFrame):
    def __init__(self, master, convertImagesCallback, **kwargs):
        super().__init__(master, **kwargs)

        self.convertImagesCallback = convertImagesCallback

        img_orient_horiz = ctk.CTkImage(light_image=Image.open("images/img_orient_horiz_black.png"),
                                        dark_image=Image.open("images/img_orient_horiz_white.png"))
        img_orient_vert = ctk.CTkImage(light_image=Image.open("images/img_orient_vert_black.png"),
                                       dark_image=Image.open("images/img_orient_vert_white.png"))

        img_dither_none = ctk.CTkImage(light_image=Image.open("images/img_dither_none_black.png"),
                                       dark_image=Image.open("images/img_dither_none_white.png"))
        img_dither_floyd_steinberg = ctk.CTkImage(light_image=Image.open("images/img_dither_floyd_steinberg_black.png"),
                                                  dark_image=Image.open("images/img_dither_floyd_steinberg_white.png"))

        img_mode_crop = ctk.CTkImage(light_image=Image.open("images/img_mode_crop_black.png"),
                                     dark_image=Image.open("images/img_mode_crop_white.png"))
        img_mode_scale = ctk.CTkImage(light_image=Image.open("images/img_mode_scale_black.png"),
                                      dark_image=Image.open("images/img_mode_scale_white.png"))

        img_start = ctk.CTkImage(light_image=Image.open("images/img_start_black.png"),
                                 dark_image=Image.open("images/img_start_white.png"))

        self.label1 = ctk.CTkLabel(self, text="Ustawienia konwertowania")
        self.label1.pack(
            pady=[PADDING_S, PADDING_XS]
        )

        self.imgOrientBtns = CustomSegmentedButtons(
            self,
            "Orientacja",
            ["Poziomo", "Pionowo"],
            [img_orient_horiz, img_orient_vert],
            [Orientation.HORIZONTAL, Orientation.VERTICAL]
        )
        self.imgOrientBtns.pack(
            padx=PADDING_M,
            pady=[PADDING_XS, PADDING_S]
        )

        self.imgDitheringBtns = CustomSegmentedButtons(
            self,
            "Dithering",
            ["Brak", "Floyd-Steinberg"],
            [img_dither_none, img_dither_floyd_steinberg],
            [Dithering.NONE, Dithering.FLOYD_STEINBERG]
        )
        self.imgDitheringBtns.pack(
            padx=PADDING_M,
            pady=PADDING_S
        )

        self.imgTransformationBtns = CustomSegmentedButtons(
            self,
            "Tryb przekształcania",
            ["Przytnij", "Dopasuj", "Rozciągnij"],
            [img_mode_crop, img_mode_scale, img_mode_scale],
            [Transformation.CROP, Transformation.FIT, Transformation.STRECH]
        )
        self.imgTransformationBtns.pack(
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_S]
        )

        self.imgConvertBtn = ctk.CTkButton(
            self,
            text="Konwertuj!",
            image=img_start,
            compound=ctk.RIGHT,
            command=self.convertImagesCallback
        )
        self.imgConvertBtn.pack(
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M]
        )

    def getSettings(self) -> SettingsModel:
        return SettingsModel(
            orientation=self.imgOrientBtns.getValue(),
            dithering=self.imgDitheringBtns.getValue(),
            transformation=self.imgTransformationBtns.getValue()
        )
