from pydantic import BaseModel
from PIL.Image import Dither
from enum import IntEnum

class Transformation(IntEnum):
    CROP = 1
    FIT = 2
    STRECH = 3


class ImageSettingsModel(BaseModel):
    ditheringAlgorithm: Dither = Dither.FLOYDSTEINBERG
    transformationMode: Transformation = Transformation.CROP