from tkinter import filedialog

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.select_img_orient(model.img_orient)
        self.view.select_img_mode(model.img_mode)

    def update_img_orient(self, orient):
        self.model.img_orient = orient

    def update_img_mode(self, mode):
        self.model.img_omode = mode

    def add_files(self):
        filepaths = filedialog.askopenfilenames()
        if filepaths:
            self.model.add_files(filepaths)
            self.update_view()

    def update_view(self):
        files = self.model.get_files()
        self.view.update_file_list(files)