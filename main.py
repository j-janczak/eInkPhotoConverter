from view.main_view import MainView
from model.data_model import DataModel
from controller.main_controller import MainController
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    model = DataModel()
    view = MainView(root)
    controller = MainController(model, view)
    view.set_controller(controller)
    root.mainloop()