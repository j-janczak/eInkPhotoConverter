from view.mainView.MainView import MainView
from view.mainView.MainViewController import MainViewController


def main() -> None:
    mainView = MainView()
    MainViewController(mainView)
    mainView.mainloop()


if __name__ == "__main__":
    main()
