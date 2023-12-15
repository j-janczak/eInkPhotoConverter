from customtkinter import CTkImage, CTkFrame, CTkLabel
from config.DimAndColors import IMG_THUMB_BG, PADDING_S
from dataclasses import dataclass


@dataclass
class PhotoModel:
    path: str
    name: str
    thumb: CTkImage

    def widget(self, master: any) -> CTkFrame:
        frame = CTkFrame(
            master,
            fg_color=IMG_THUMB_BG
        )
        CTkLabel(
            frame,
            image=self.thumb,
            text=self.name,
            compound='top'
        ).pack(
            padx=PADDING_S,
            pady=PADDING_S
        )
        return frame
