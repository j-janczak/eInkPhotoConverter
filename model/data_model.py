class DataModel:
    def __init__(self):
        self.files = []
        self.img_mode = 0
        self.img_orient = 0

    def add_files(self, filepaths):
        self.files.extend(filepaths)

    def get_files(self):
        return self.files