from customtkinter import CTkToplevel, CTk
from _tkinter import TclError
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
        
        self.window = window
        self.minsize(400, 0)
        self.transient(self.window)

        self.update_idletasks()
        self.grab_set()
        self.centerDialog()

    def centerDialog(self) -> None:
        xPos = self.window.winfo_x() + (self.window.winfo_width() // 2) - \
            (self.winfo_width() // 2)
        yPos = self.window.winfo_y() + (self.window.winfo_height() // 2) - \
            (self.winfo_height() // 2)
        self.geometry(f"+{xPos}+{yPos}")

    def customDestroy(self):
        self.after_idle(
            self.destroy
        )
