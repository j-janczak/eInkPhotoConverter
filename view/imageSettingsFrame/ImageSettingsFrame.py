from view.customSegmentedButtons.CustomSegmentedButtons import CustomSegmentedButtons
from config.config import PADDING_XS, PADDING_S, PADDING_M
import customtkinter as ctk
from PIL import Image

class ImageSettingsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        img_orient_horiz = ctk.CTkImage(light_image=Image.open("images/img_orient_horiz_black.png"),
                                        dark_image=Image.open("images/img_orient_horiz_white.png"))
        img_orient_vert = ctk.CTkImage(light_image=Image.open("images/img_orient_vert_black.png"),
                                        dark_image=Image.open("images/img_orient_vert_white.png"))
        
        img_dither_none = ctk.CTkImage(light_image=Image.open("images/img_dither_none_black.png"),
                                       dark_image=Image.open("images/img_dither_none_white.png"))
        img_dither_floyd_steinberg= ctk.CTkImage(light_image=Image.open("images/img_dither_floyd_steinberg_black.png"),
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

        self.img_orient_mode = CustomSegmentedButtons(
            self, 
            "Orientacja",
            ["Poziomo", "Pionowo"],
            [img_orient_horiz, img_orient_vert]
        )
        self.img_orient_mode.pack(padx=PADDING_M, pady=[PADDING_XS, PADDING_S])

        self.imgDitheringBtns = CustomSegmentedButtons(
            self, 
            "Dithering",
            ["Brak", "Floyd-Steinberg"],
            [img_dither_none, img_dither_floyd_steinberg]
        )
        self.imgDitheringBtns.pack(padx=PADDING_M, pady=PADDING_S)

        self.imgModeBtns = CustomSegmentedButtons(
            self, 
            "Tryb przekształcania",
            ["Przycinanie", "Skalowanie"],
            [img_mode_crop, img_mode_scale]
        )
        self.imgModeBtns.pack(padx=PADDING_M, pady=[PADDING_S, PADDING_S])

        self.imgConvertBtn = ctk.CTkButton(self, text="Konwertuj!", image=img_start, compound=ctk.RIGHT)
        self.imgConvertBtn.pack(
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M]
        )

