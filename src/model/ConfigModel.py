from .ImageSettingsModel import ImageSettingsModel
from pydantic import BaseModel
from enum import IntEnum
import os


class Language(IntEnum):
    ENGLISH = 0
    POLSIH = 1

    def mapToName(self) -> str:
        return "en" if self.value == 0 else "pl"


class ConfigModel(BaseModel):
    imageSettings: ImageSettingsModel = ImageSettingsModel()
    outputPath: str = os.getcwd()
    language: Language = Language.ENGLISH
