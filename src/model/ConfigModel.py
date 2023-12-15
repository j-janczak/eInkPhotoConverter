from .ImageSettingsModel import ImageSettingsModel
from pydantic import BaseModel
from enum import IntEnum


class Language(IntEnum):
    ENGLISH = 0
    POLSIH = 1

    def mapToName(self) -> str:
        return "en" if self.value == 0 else "pl"


class ConfigModel(BaseModel):
    imageSettings: ImageSettingsModel = ImageSettingsModel()
    outputPath: str = "",
    language: Language = Language.ENGLISH
