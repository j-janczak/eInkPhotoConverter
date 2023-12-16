from tkinter import PhotoImage
import customtkinter as ctk
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


def setIcon(window: ctk.CTk | ctk.CTkToplevel):  
    if sys.platform == 'darwin':
        window.iconbitmap(getPath("mac_icon.icns"))
    elif sys.platform == 'win32':
        window.iconbitmap(getPath("windows_icon.ico"))
    else:
        window.iconphoto(False, PhotoImage(file=getPath("linux_icon.png")))