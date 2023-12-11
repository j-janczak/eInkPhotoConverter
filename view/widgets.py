import tkinter as tk
from tkinter import ttk
from config.config import PADDING_S, PADDING_M

def add_select_files_widgets(self):
    self.select_files_frame = tk.Frame(self.root, bg="lightblue")
    self.select_files_frame.grid(row=0, column=0, sticky="nsew")
    self.select_files_frame.grid_rowconfigure(0, weight=1)
    self.select_files_frame.grid_columnconfigure(0, weight=1)

    self.file_tree = ttk.Treeview(self.select_files_frame, columns=('files', 'delete'), show='headings')
    self.file_tree.heading('files', text='Pliki')
    self.file_tree.heading('delete', text='Usuń')
    self.file_tree.grid(row=0, column=0, sticky="nsew", padx=(PADDING_M, PADDING_S), pady=(PADDING_M, PADDING_S))

    self.add_files_button = tk.Button(self.select_files_frame, text="Dodaj pliki", command=self.on_add_files)
    self.add_files_button.grid(row=1, column=0, sticky="ew", padx=(PADDING_M, PADDING_S), pady=(PADDING_S, PADDING_M))

def add_select_destination_folder_widget(self):
    self.folder_frame = tk.Frame(self.img_opt_right_frame)
    self.folder_frame.grid(row=0, column=0, sticky="ew", padx=(PADDING_S, PADDING_M), pady=(PADDING_M, PADDING_S))
    self.folder_frame.grid_columnconfigure(0, weight=1)

    self.destination_folder = tk.StringVar(value="Wybierz folder docelowy")
    self.destination_label = tk.Label(self.folder_frame, textvariable=self.destination_folder)
    self.destination_label.grid(row=0, column=0)

    self.select_folder_button = tk.Button(self.folder_frame, text="Wybierz folder docelowy", command=self.select_destination_folder)
    self.select_folder_button.grid(row=1, column=0, sticky="ew")

def add_img_orient_btns(self):
    self.img_orient_horiz_btn = tk.Button(self.img_opt_btns_frame, text="Horizontal", command=lambda: self.select_img_orient(0))
    self.img_orient_horiz_btn.grid(row=0, column=0, sticky="we", padx=(0, PADDING_S))

    self.img_orient_vert_btn = tk.Button(self.img_opt_btns_frame, text="Vertical", command=lambda: self.select_img_orient(1))
    self.img_orient_vert_btn.grid(row=0, column=1, sticky="we", padx=(PADDING_S, 0))

def add_img_mode_btns(self):
    self.img_mode_scl_btn = tk.Button(self.img_opt_btns_frame, text="Scale", command=lambda: self.select_img_mode(0))
    self.img_mode_scl_btn.grid(row=1, column=0, sticky="we", padx=(0, PADDING_S))

    self.img_mode_cut_btn = tk.Button(self.img_opt_btns_frame, text="Cut", command=lambda: self.select_img_mode(1))
    self.img_mode_cut_btn.grid(row=1, column=1, sticky="we", padx=(PADDING_S, 0))

def add_img_dither_btns(self):
    self.img_dither_none_btn = tk.Button(self.img_opt_btns_frame, text="NONE", command=lambda: self.select_img_dither(0))
    self.img_dither_none_btn.grid(row=2, column=0, sticky="we", padx=(0, PADDING_S))

    self.img_dither_fs_btn = tk.Button(self.img_opt_btns_frame, text="FLOYDSTEINBERG", command=lambda: self.select_img_dither(1))
    self.img_dither_fs_btn.grid(row=2, column=1, sticky="we", padx=(PADDING_S, 0))