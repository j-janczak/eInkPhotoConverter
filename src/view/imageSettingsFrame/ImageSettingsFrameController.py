from model.ImageSettingsModel import ImageSettingsModel
from utils.ConfigMapper import config, updateConfig
from .ImageSettingsFrame import ImageSettingsFrame
from model.ImageSettingsModel import Transform
from PIL.Image import Dither


class ImageSettingsFrameController():
    def __init__(
            self,
            view: ImageSettingsFrame
    ) -> None:
        self.view = view
        self.view.imgDitheringBtns.onClick = self.updateDitheringAlgorithm
        self.view.imgTransformBtns.onClick = self.updateTransformMode

    def updateDitheringAlgorithm(self, value: Dither) -> None:
        updateConfig({
            "imageSettings": config.imageSettings.model_copy(
                update={"ditheringAlgorithm": value}
            )
        })

    def updateTransformMode(self, value: Transform) -> None:
        updateConfig({
            "imageSettings": config.imageSettings.model_copy(
                update={"transformMode": value}
            )
        })

    def getSettings(self) -> ImageSettingsModel:
        return ImageSettingsModel(
            ditheringAlgorithm=self.view.imgDitheringBtns.getValue(),
            transformMode=self.view.imgTransformBtns.getValue()
        )
