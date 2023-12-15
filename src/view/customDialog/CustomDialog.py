from customtkinter import CTkToplevel, CTk
from utils.Utils import getPath
from tkinter import PhotoImage
from typing import Tuple


class CustomDialog(CTkToplevel):
    def __init__(
        self,
        *args,
        fg_color: str | Tuple[str, str] | None = None,
        window: CTk,
        **kwargs
    ) -> None:
        super().__init__(
            *args,
            fg_color=fg_color,
            **kwargs
        )
        self.active = False
        self.bind("<Visibility>", self.onVisibilityChange)
        
        self.window = window
        self.minsize(400, 0)
        self.transient(self.window)

    def centerDialog(self) -> None:
        xPos = self.window.winfo_x() + (self.window.winfo_width() // 2) - \
            (self.winfo_width() // 2)
        yPos = self.window.winfo_y() + (self.window.winfo_height() // 2) - \
            (self.winfo_height() // 2)
        self.geometry(f"+{xPos}+{yPos}")

    def customDestroy(self):
        self.grab_release()
        self.after_idle(
            self.destroy
        )

    def grabAndCenter(self) -> None:
        if (not self.active):
            self.wait_visibility()
        self.centerDialog()
        self.grab_set()
        icon = PhotoImage(file=getPath("icon.png"))
        self.wm_iconbitmap()
        self.after(300, lambda:self.iconphoto(False, icon))

    def onVisibilityChange(self, e):
        self.active = True
