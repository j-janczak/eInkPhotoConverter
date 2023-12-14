from dataclasses import dataclass


@dataclass
class ConvertErrorModel:
    file: str = ""
    reason: str = ""