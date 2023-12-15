import gettext

gt = gettext.translation('messages', localedir='locale', languages=['pl'])
_ = gt.gettext
