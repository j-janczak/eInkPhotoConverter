from .ImageSettingsModel import ImageSettingsModel
from pydantic import BaseModel


class ConfigModel(BaseModel):
    imageSettings: ImageSettingsModel = ImageSettingsModel()
    outputPath: str = ""
