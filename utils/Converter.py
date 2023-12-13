from model.SettingsModel import SettingsModel, Orientation, Dithering, Transformation
from typing import List
from PIL import Image
import os.path
import sys

COLORS = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (0, 0, 255),
          (255, 0, 0), (255, 255, 0), (255, 128, 0)]
# Black, White, Green, Blue, Red, Yellow, Orange

TARGET_LONG_SIDE, TARGET_SHORT_SIDE = 800, 480
FILE_EXTENSION = "_eInk.bmp"


def convertImages(imagePaths: List[str], settings: SettingsModel) -> None:
    for imagePath in imagePaths:
        if not os.path.isfile(imagePath):
            print(f'Error: file {imagePath} does not exist')
            sys.exit(1)

        imageToConvert = Image.open(imagePath)

        orgWidth, orgHeight = imageToConvert.size
        targetWidth, tergetHeight = (TARGET_LONG_SIDE, TARGET_SHORT_SIDE) if orgWidth > orgHeight else (
            TARGET_SHORT_SIDE, TARGET_LONG_SIDE)

        if settings.transformation == Transformation.CROP:
            ratio = min(orgWidth / targetWidth, orgHeight / tergetHeight)
            newSize = (int(orgWidth / ratio), int(orgHeight / ratio))
            scalledImg = imageToConvert.resize(newSize, Image.ANTIALIAS)

            left = (scalledImg.width - targetWidth) / 2
            top = (scalledImg.height - tergetHeight) / 2
            right = (scalledImg.width + targetWidth) / 2
            bottom = (scalledImg.height + tergetHeight) / 2
            imgTransformed = scalledImg.crop((left, top, right, bottom))

        elif settings.transformation == Transformation.FIT:
            ratio = min(targetWidth / orgWidth, tergetHeight / orgHeight)
            newSize = (int(orgWidth * ratio), int(orgHeight * ratio))
            scalledImg = imageToConvert.resize(newSize, Image.ANTIALIAS)

            imgTransformed = Image.new(
                "RGB", (targetWidth, tergetHeight), "white")
            x = (targetWidth - newSize[0]) // 2
            y = (tergetHeight - newSize[1]) // 2
            imgTransformed.paste(scalledImg, (x, y))

        elif settings.transformation == Transformation.STRECH:
            imgTransformed = imageToConvert.resize(
                (targetWidth, tergetHeight), Image.ANTIALIAS)

        if imgTransformed.mode != "RGB":
            imgTransformed = imgTransformed.convert("RGB")

        palleteImg = Image.new("P", (1, 1))
        palleteImg.putpalette(
            [color for colorTuple in COLORS for color in colorTuple])

        convertedImage = imgTransformed.quantize(
            palette=palleteImg,
            dither=settings.dithering.toImageDither()
        )

        convertedImage.save(settings.outputPath + "/" +
                            os.path.splitext(os.path.basename(imagePath))[0] + FILE_EXTENSION)
