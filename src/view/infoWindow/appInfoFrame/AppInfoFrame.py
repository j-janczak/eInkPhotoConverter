from config.config import PADDING_XS, PADDING_S, PADDING_M
from ...customSegmentedButtons.CustomSegmentedButtons import CustomSegmentedButtons
from model.ConfigModel import Language
from utils.ConfigMapper import config
from utils.GettextConfig import _
from utils.Utils import getPath
import tkinter.font as tkFont
import customtkinter as ctk
from typing import Tuple
from PIL import Image
import webbrowser

GITHUB_URL = "https://github.com/TheFlashes/eInkPhotoConverter"


class AppInfoFrame(ctk.CTkFrame):
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

        imgLangEng = ctk.CTkImage(
            Image.open(getPath("img_lang_eng.png")))
        imgLangPl = ctk.CTkImage(
            Image.open(getPath("img_lang_pl.png")))

        appNameLabel = ctk.CTkLabel(
            self,
            text=_("eInk Photo Converter")
        )
        appNameLabel.pack(
            anchor="nw",
            padx=PADDING_M,
            pady=[PADDING_XS, 0]
        )
        currentFont = tkFont.Font(font=appNameLabel.cget("font"))
        newFont = (currentFont.actual("family"), 20, "bold")
        appNameLabel.configure(font=newFont)

        ctk.CTkLabel(
            self,
            text=_("By Jakub Janczak")
        ).pack(
            anchor="nw",
            padx=PADDING_M
        )

        self.languageButtons = CustomSegmentedButtons(
            self,
            label=_("\nApp language\n(Requires app restart)\n"),
            textValues=["", ""],
            imgValues=[imgLangEng, imgLangPl],
            values=[Language.ENGLISH, Language.POLSIH],
            defaultValue=config.language,
            btnWidth=91
        )
        self.languageButtons.pack(
            side=ctk.BOTTOM,
            anchor="s",
            pady=[PADDING_S, PADDING_M]
        )

        ctk.CTkLabel(
            self,
            text=_("v 1.0")
        ).pack(
            side=ctk.BOTTOM,
            anchor="sw",
            padx=PADDING_M,
        )

        githubLink = ctk.CTkLabel(
            self,
            text=_("GitHub"),
            text_color="#1F51FF",
            cursor="hand2"
        )
        githubLink.pack(
            side=ctk.BOTTOM,
            anchor="sw",
            padx=PADDING_M
        )
        githubLink.bind("<Button-1>", lambda e: webbrowser.open_new(GITHUB_URL))
