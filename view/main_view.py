import tkinter as tk
from tkinter import ttk
from config.config import PADDING_S, PADDING_M
from tkinter import filedialog
import view.widgets as widgets

class MainView:
    def __init__(self, root):
        self.root = root
        self.initialize_ui()
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def initialize_ui(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        #self.root.grid_columnconfigure(1, weight=1, pad=PADDING_M)

        self.img_opt_right_frame = tk.Frame(self.root)
        self.img_opt_right_frame.grid(row=0, column=1, sticky="n")

        self.img_opt_btns_frame = tk.Frame(self.img_opt_right_frame)
        self.img_opt_btns_frame.grid(row=1, column=0, sticky="ew", padx=(PADDING_S, PADDING_M), pady=(PADDING_S, PADDING_M))
        self.img_opt_btns_frame.grid_columnconfigure(0, weight=1)
        self.img_opt_btns_frame.grid_columnconfigure(1, weight=1)

        widgets.add_select_files_widgets(self)
        widgets.add_select_destination_folder_widget(self)
        widgets.add_img_mode_btns(self)
        widgets.add_img_orient_btns(self)
        widgets.add_img_dither_btns(self)

    def on_add_files(self):
        if self.controller:
            self.controller.add_files()

    def update_file_list(self, file_list):
        for file in file_list:
            self.file_tree.insert('', tk.END, values=(file))

    def select_img_orient(self, orient):
        if self.controller:
            self.controller.update_img_orient(orient)

        if orient == 0:
            self.img_orient_horiz_btn.config(relief="sunken")
            self.img_orient_vert_btn.config(relief="raised")
        elif orient == 1:
            self.img_orient_vert_btn.config(relief="sunken")
            self.img_orient_horiz_btn.config(relief="raised")

    def select_img_mode(self, mode):
        if self.controller:
            self.controller.update_img_mode(mode)

        if mode == 0:
            self.img_mode_scl_btn.config(relief="sunken")
            self.img_mode_cut_btn.config(relief="raised")
        elif mode == 1:
            self.img_mode_cut_btn.config(relief="sunken")
            self.img_mode_scl_btn.config(relief="raised")

    def select_img_dither(self, dither):
        if dither == 0:
            self.img_dither_none_btn.config(relief="sunken")
            self.img_dither_fs_btn.config(relief="raised")
        elif dither == 1:
            self.img_dither_fs_btn.config(relief="sunken")
            self.img_dither_none_btn.config(relief="raised")

    def select_destination_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.destination_folder.set(folder_selected)