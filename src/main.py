from view.mainView.MainView import MainView
from view.mainView.MainViewController import MainViewController
from utils.Utils import getPath
from tkinter import PhotoImage
import sys


def main() -> None:
    app = MainView()
    MainViewController(app)

    
    icon = PhotoImage(file=getPath("icon_mac.png")) if sys.platform == "darwin" else PhotoImage(file=getPath("icon.png"))
    app.wm_iconbitmap()
    app.iconphoto(False, icon)

    app.mainloop()


if __name__ == "__main__":
    main()
