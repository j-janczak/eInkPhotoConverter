import customtkinter as ctk
from config.config import BTN_IMG_SIZE, PADDING_M, PADDING_S, PADDING_XS, PRESSED_BTN_COLOR, SELECTED_BTN_COLOR
from typing import List


class CustomSegmentedButtons(ctk.CTkFrame):
    def __init__(
            self,
            root: any,
            label: str,
            textValues: List[str],
            imgValues: List[ctk.CTkImage],
            values: List[any]
    ) -> None:
        super().__init__(root)

        self.values = values
        self.selectedItem = 0

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

        self.btnsArray[0].configure(fg_color=SELECTED_BTN_COLOR)

    def btnClick(self, btnId: int) -> None:
        self.resetBtns()
        self.btnsArray[btnId].configure(fg_color=SELECTED_BTN_COLOR)
        self.selectedItem = btnId

    def resetBtns(self) -> None:
        for btn in self.btnsArray:
            btn.configure(fg_color=PRESSED_BTN_COLOR)

    def getValue(self) -> any:
        return self.values[self.selectedItem]
