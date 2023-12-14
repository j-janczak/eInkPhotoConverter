import gettext

gt = gettext.translation('messages', localedir='locale', languages=['pl'])
print("test")
_ = gt.gettext