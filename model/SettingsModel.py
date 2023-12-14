from dataclasses import dataclass
from enum import Enum
from PIL import Image


class Dithering(Enum):
    NONE = 1
    FLOYD_STEINBERG = 2

    def toImageDither(self) -> Image.Dither:
        return Image.Dither.NONE if self.value == 1 else Image.Dither.FLOYDSTEINBERG


class Transformation(Enum):
    CROP = 1
    FIT = 2
    STRECH = 3


@dataclass
class SettingsModel:
    dithering: Dithering
    transformation: Transformation
    outputPath: str = ""
