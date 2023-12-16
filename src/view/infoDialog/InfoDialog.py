from view.customDialog.CustomDialog import CustomDialog
from config.DimAndColors import PADDING_S, PADDING_M
from utils.GettextConfig import _
from typing import Callable
import customtkinter as ctk
from typing import Tuple


class InfoDialog(CustomDialog):
    def __init__(
            self,
            *args,
            fg_color: str | Tuple[str, str] | None = None,
            window: ctk.CTk,
            text: str,
            action: Tuple[str, Callable[[], None]] = None,
            **kwargs,
    ) -> None:
        super().__init__(
            *args,
            fg_color=fg_color,
            window=window,
            **kwargs
        )
        self.title(_("Info"))
        self.resizable(width=False, height=False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            master=self,
            text=text
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            stick="nsew",
            padx=PADDING_M,
            pady=[PADDING_M, PADDING_S]
        )

        ctk.CTkButton(
            master=self,
            text="OK",
            command=self.destroy
        ).grid(
            row=1,
            column=1,
            stick="se",
            padx=PADDING_M,
            pady=[PADDING_S, PADDING_M]
        )

        if action:
            ctk.CTkButton(
                master=self,
                text=action[0],
                command=lambda: self.executeCommand(action[1])
            ).grid(
                row=1,
                column=0,
                padx=PADDING_M,
                pady=[PADDING_S, PADDING_M]
            )
        
        self.grabAndCenter()

    def executeCommand(self, command: Callable):
        command()
        self.customDestroy()
