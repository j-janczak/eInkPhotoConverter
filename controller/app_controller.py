import tkinter.filedialog as filedialog
from config.config import THUMB_MAX_WIDTH, THUMB_MAX_HEIGHT, THUMB_LABEL_MAX_LEN
import customtkinter as ctk
from PIL import Image
import os


class AppController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # self.view.sel_imgs_btn.configure(command=self.openImgSelDialog)

    #     self.view.submit_button.configure(command=self.update_model)

    # def update_model(self):
    #     text = self.view.entry.get()
    #     self.model.set_text(text)
    #     self.update_view()

    # def update_view(self):
    #     self.view.result_label.configure(text=self.model.get_text())
