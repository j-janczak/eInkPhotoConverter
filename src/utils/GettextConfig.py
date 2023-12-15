from utils.ConfigMapper import config
import gettext

gt = gettext.translation('messages', localedir='locale', languages=[config.language.mapToName()])
_ = gt.gettext
