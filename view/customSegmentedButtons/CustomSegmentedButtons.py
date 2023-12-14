from config.config import PADDING_S, PADDING_XS, PRESSED_BTN_COLOR, SELECTED_BTN_COLOR
from utils.ConfigMapper import ConfigMapper
from view.customFrame.CustomFrame import CustomFrame
from typing import List, Tuple, Callable
import customtkinter as ctk


class CustomSegmentedButtons(CustomFrame):
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
        label: str = "",
        textValues: List[str] = [],
        imgValues: List[ctk.CTkImage] = [],
        values: List[any] = [],
        defaultValue: any = None,
        onClick: Callable[[any], None] = None,
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

        self.values = values
        self.selectedItem = self.values.index(defaultValue)
        self.onClick = onClick

        self.widgetLabel = ctk.CTkLabel(self, text=label)
        self.widgetLabel.pack()

        self.btnsArray = []

        for btnId in range(len(textValues)):
            btn = ctk.CTkButton(self, text=textValues[btnId], image=imgValues[btnId], compound="top",
                                width=100, fg_color=PRESSED_BTN_COLOR, command=lambda btnId=btnId: self.btnClick(btnId))

            padx = [PADDING_S if btnId == 0 else PADDING_XS,
                    PADDING_S if btnId == len(textValues)-1 else PADDING_XS]

            btn.pack(
                side=ctk.LEFT,
                padx=padx,
                pady=[0, PADDING_S],
                expand=True
            )
            self.btnsArray.append(btn)

        self.btnsArray[self.selectedItem].configure(
            fg_color=SELECTED_BTN_COLOR)

    def btnClick(self, btnId: int) -> None:
        self.resetBtns()
        self.btnsArray[btnId].configure(fg_color=SELECTED_BTN_COLOR)
        self.selectedItem = btnId
        self.onClick(self.getValue())

    def resetBtns(self) -> None:
        for btn in self.btnsArray:
            btn.configure(fg_color=PRESSED_BTN_COLOR)

    def getValue(self) -> any:
        return self.values[self.selectedItem]
