from view.infoWindow.InfoWindow import InfoWindow
from config.config import PADDING_M, PADDING_S
import customtkinter as ctk
from PIL import Image
import webbrowser


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        imgHelp = ctk.CTkImage(light_image=Image.open("images/img_help_black.png"),
                               dark_image=Image.open("images/img_help_white.png"))

        self.helpButton = ctk.CTkButton(
            self, text="Informacje", image=imgHelp, compound=ctk.RIGHT, command=lambda: InfoWindow())
        self.helpButton.pack(
            fill=ctk.X,
            padx=PADDING_M,
            pady=PADDING_M
        )

    #     self.authorLabel = ctk.CTkLabel(self, text="Made with love by Jojczak ❤️")
    #     self.authorLabel.pack(
    #         anchor="nw",
    #         padx=PADDING_M,
    #     )

    #     self.githubLink = ctk.CTkLabel(self, text="Github ⇗", text_color="#1E90FF", cursor="hand2")
    #     self.githubLink.bind("<Button-1>", lambda e: self.openGithub())
    #     self.githubLink.pack(
    #         anchor="nw",
    #         padx=PADDING_M,
    #     )

    # def openGithub(self):
    #     webbrowser.open("https://www.google.pl/maps/")
