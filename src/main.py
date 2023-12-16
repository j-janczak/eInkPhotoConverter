from view.mainView.MainView import MainView
from view.mainView.MainViewController import MainViewController
from utils.Utils import setIcon
import sys


def main() -> None:
    app = MainView()
    MainViewController(app)

    app.wm_iconbitmap()
    setIcon(app)

    app.mainloop()


if __name__ == "__main__":
    main()
