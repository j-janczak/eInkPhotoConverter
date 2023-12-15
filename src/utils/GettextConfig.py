from utils.ConfigMapper import config
from utils.Utils import getPath
import gettext

gt = gettext.translation('messages', localedir=getPath("", True), languages=[config.language.mapToName()])
_ = gt.gettext
