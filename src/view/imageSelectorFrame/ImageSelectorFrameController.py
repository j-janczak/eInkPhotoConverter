import tkinter.filedialog as filedialog


class ImageSelectorFrameController():
    def __init__(self, view):
        self.view = view

        self.view.sel_imgs_btn.configure(command=self.openImgSelDialog)

    def openImgSelDialog(self):
        fileTypes = [("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        imgPaths = filedialog.askopenfilenames(filetypes=fileTypes)
        self.view.galleryFrame.controller.loadThumbs(imgPaths)
