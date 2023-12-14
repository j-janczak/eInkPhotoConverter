from config.config import PADDING_M
from utils.utils import shortenText
import customtkinter as ctk


class ProgressWindow(ctk.CTkToplevel):
    def __init__(
            self,
            master: any,
            text: str
    ) -> None:
        super().__init__(master)

        self.minsize(400, 0)
        self.transient(master)
        self.grab_set()
        self.overrideredirect(True)

        self.dialogFrame = ctk.CTkFrame(self)
        self.dialogFrame.pack(
            fill=ctk.BOTH,
            padx=PADDING_M,
            pady=PADDING_M
        )

        self.progressTextWidget = ctk.CTkLabel(self.dialogFrame)
        self.progressTextWidget.pack(
            pady=PADDING_M
        )

        self.progressBar = ctk.CTkProgressBar(self.dialogFrame)
        self.progressBar.set(0)
        self.progressBar.pack(
            fill=ctk.X,
            padx=PADDING_M,
            pady=[0, PADDING_M]
        )

        self.text = text

        self.update_idletasks()

        xPos = master.winfo_x() + (master.winfo_width() // 2) - (self.winfo_width() // 2)
        yPos = master.winfo_y() + (master.winfo_height() // 2) - \
            (self.winfo_height() // 2)
        self.geometry(f"+{xPos}+{yPos}")

    def progress(self, fileName: str, step: int, of: int) -> None:
        progressText = f"{self.text}: \"{shortenText(fileName, 15)}\" {step}/{of}"
        self.progressTextWidget.configure(text=progressText)
        self.progressBar.set(step/of)
