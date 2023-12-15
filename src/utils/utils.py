import sys
import os


def shortenText(text: str, length: int) -> str:
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text
    

def getPath(imgName: str, locale: bool = False):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, 'locale', imgName) if locale else os.path.join(base_path, 'images', imgName)


