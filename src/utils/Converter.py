from model.ImageSettingsModel import ImageSettingsModel, Transform
from model.ConvertErrorModel import ConvertErrorModel
from typing import List, Callable
from utils.GettextConfig import _
from PIL import Image
import os.path

COLORS = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (0, 0, 255),
          (255, 0, 0), (255, 255, 0), (255, 128, 0)]
# Black, White, Green, Blue, Red, Yellow, Orange

TARGET_LONG_SIDE, TARGET_SHORT_SIDE = 800, 480
FILE_EXTENSION = "_eInk.bmp"


def convertImages(
    imagePaths: List[str],
    imageSettings: ImageSettingsModel,
    outputPath: str,
    progressCallback: Callable[[str, int, int], None],
    endCallback: Callable[[List[ConvertErrorModel]], None]
) -> None:
    filesCount = len(imagePaths)
    filesProgress = 0
    errorFiles: List[ConvertErrorModel] = []
    for imagePath in imagePaths:
        filesProgress += 1
        fileName = os.path.splitext(os.path.basename(imagePath))[0]

        progressCallback(fileName, filesProgress, filesCount)

        if not os.path.isfile(imagePath):
            errorFiles.append(ConvertErrorModel(
                file=fileName,
                reason=_("Unable to open")
            ))
            continue

        imageToConvert = Image.open(imagePath)

        orgWidth, orgHeight = imageToConvert.size
        targetWidth, tergetHeight = (TARGET_LONG_SIDE, TARGET_SHORT_SIDE) if orgWidth > orgHeight else (
            TARGET_SHORT_SIDE, TARGET_LONG_SIDE)

        if imageSettings.transformMode == Transform.CROP:
            ratio = min(orgWidth / targetWidth, orgHeight / tergetHeight)
            newSize = (int(orgWidth / ratio), int(orgHeight / ratio))
            scalledImg = imageToConvert.resize(newSize, Image.LANCZOS)

            left = (scalledImg.width - targetWidth) / 2
            top = (scalledImg.height - tergetHeight) / 2
            right = (scalledImg.width + targetWidth) / 2
            bottom = (scalledImg.height + tergetHeight) / 2
            imgTransformed = scalledImg.crop((left, top, right, bottom))

        elif imageSettings.transformMode == Transform.FIT:
            ratio = min(targetWidth / orgWidth, tergetHeight / orgHeight)
            newSize = (int(orgWidth * ratio), int(orgHeight * ratio))
            scalledImg = imageToConvert.resize(newSize, Image.LANCZOS)

            imgTransformed = Image.new(
                "RGB", (targetWidth, tergetHeight), "white")
            x = (targetWidth - newSize[0]) // 2
            y = (tergetHeight - newSize[1]) // 2
            imgTransformed.paste(scalledImg, (x, y))

        elif imageSettings.transformMode == Transform.STRETCH:
            imgTransformed = imageToConvert.resize(
                (targetWidth, tergetHeight), Image.LANCZOS)

        if imgTransformed.mode != "RGB":
            imgTransformed = imgTransformed.convert("RGB")

        colorsPallete = tuple(
            color for colorTuple in COLORS for color in colorTuple) + (0, 0, 0) * 249

        palleteImg = Image.new("P", (1, 1))
        palleteImg.putpalette(colorsPallete)

        convertedImage = imgTransformed.quantize(
            palette=palleteImg,
            dither=imageSettings.ditheringAlgorithm
        ).convert('RGB')

        try:
            convertedImage.save(outputPath + "/" + fileName + FILE_EXTENSION)
        except:
            errorFiles.append(ConvertErrorModel(
                file=fileName,
                reason=_("Unable to save")
            ))
    endCallback(errorFiles)
