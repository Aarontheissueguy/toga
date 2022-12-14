from toga.colors import TRANSPARENT
from toga_cocoa.libs import NSTextField

from .base import SimpleProbe
from .properties import toga_color, toga_font


class LabelProbe(SimpleProbe):
    native_class = NSTextField

    @property
    def text(self):
        return self.native.stringValue

    @property
    def color(self):
        return toga_color(self.native.textColor)

    @property
    def font(self):
        return toga_font(self.native.font)

    @property
    def background_color(self):
        if self.native.drawsBackground:
            if self.native.backgroundColor:
                return toga_color(self.native.backgroundColor)
            else:
                return None
        else:
            return TRANSPARENT
