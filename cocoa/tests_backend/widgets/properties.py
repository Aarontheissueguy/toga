from dataclasses import dataclass

from toga.colors import rgba
from toga.fonts import FANTASY, NORMAL, SYSTEM


def toga_color(color):
    if color:
        return rgba(
            color.redComponent * 255,
            color.greenComponent * 255,
            color.blueComponent * 255,
            color.alphaComponent,
        )
    else:
        return None


@dataclass
class Font:
    family: str
    size: int
    style: str = NORMAL
    variant: str = NORMAL
    weight: str = NORMAL


def toga_font(font):
    return Font(
        family={
            ".AppleSystemUIFont": SYSTEM,
            "Papyrus": FANTASY,
        }.get(str(font.familyName), str(font.familyName)),
        size=font.pointSize,
    )
