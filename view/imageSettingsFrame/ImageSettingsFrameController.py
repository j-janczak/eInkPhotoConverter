from view.customFrame.CustomFrameController import CustomFrameController
from model.ImageSettingsModel import Transformation
from utils.ConfigMapper import ConfigMapper
from customtkinter import CTkFrame
from PIL.Image import Dither


class ImageSettingsFrameController(CustomFrameController):
    def __init__(self, view: CTkFrame, configMapper: ConfigMapper) -> None:
        super().__init__(view, configMapper)

    def updateDitheringAlgorithm(self, value: Dither):
        self.configMapper.update({
            "imageSettings": self.configMapper.config.imageSettings.model_copy(
                update={"ditheringAlgorithm": value}
            )
        })

    def updateTransformationMode(self, value: Transformation):
        self.configMapper.update({
            "imageSettings": self.configMapper.config.imageSettings.model_copy(
                update={"transformationMode": value}
            )
        })
