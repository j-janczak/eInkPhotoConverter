from dataclasses import dataclass
from enum import Enum
from PIL import Image


class Orientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


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
    orientation: Orientation
    dithering: Dithering
    transformation: Transformation
    outputPath: str = ""
