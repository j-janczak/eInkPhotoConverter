from utils.ConfigMapper import updateConfig
from model.ConfigModel import Language
from .AppInfoFrame import AppInfoFrame


class AppInfoFrameController:
    def __init__(
            self,
            view: AppInfoFrame
    ) -> None:
        self.view = view
        self.view.languageButtons.onClick = self.updateLanguage

    def updateLanguage(self, language: Language) -> None:
        updateConfig({
            "language": language
        })
