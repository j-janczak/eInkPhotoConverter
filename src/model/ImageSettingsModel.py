from pydantic import BaseModel
from PIL.Image import Dither
from enum import IntEnum


class Transform(IntEnum):
    CROP = 1
    FIT = 2
    STRETCH = 3


class ImageSettingsModel(BaseModel):
    ditheringAlgorithm: Dither = Dither.FLOYDSTEINBERG
    transformMode: Transform = Transform.CROP
