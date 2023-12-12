from model.app_model import AppModel
from view.app_view import AppView
from controller.app_controller import AppController

def main():
    model = AppModel()
    view = AppView()
    controller = AppController(view, model)
    view.mainloop()

if __name__ == "__main__":
    main()