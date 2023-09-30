from java import dynamic_proxy
from travertino.size import at_least

from android.view import View
from android.widget import Button as A_Button
from android.graphics.drawable import GradientDrawable  # Add this import
from android.content.res import ColorStateList  # Add this import

from .label import TextViewWidget

class TogaOnClickListener(dynamic_proxy(View.OnClickListener)):
    def __init__(self, button_impl):
        super().__init__()
        self.button_impl = button_impl

    def onClick(self, _view):
        self.button_impl.interface.on_press(None)

class Button(TextViewWidget):
    focusable = False

    def create(self):
        self.native = A_Button(self._native_activity)
        self.native.setOnClickListener(TogaOnClickListener(button_impl=self))
        self.cache_textview_defaults()

        # Set custom background drawable (rounded_button_background.xml)
        self.set_custom_background()

        # Set custom text color (replace with your custom color)
        self.set_custom_text_color()

    def set_custom_background(self):
        # Create a GradientDrawable with your custom background shape
        background = GradientDrawable()
        background.setColor(ColorStateList.valueOf(0xFF00FF00))  # Replace with your color
        background.setCornerRadius(20)  # Adjust the radius to match your rounded_button_background.xml

        # Set the background drawable to the button
        self.native.setBackground(background)

    def set_custom_text_color(self):
        # Set your custom text color (replace with your color)
        text_color = 0xFF0000FF  # Replace with your custom color in hexadecimal
        self.native.setTextColor(text_color)

    def get_text(self):
        return str(self.native.getText())

    def set_text(self, text):
        self.native.setText(text)

    def set_enabled(self, value):
        self.native.setEnabled(value)

    def rehint(self):
        self.native.measure(
            View.MeasureSpec.UNSPECIFIED,
            View.MeasureSpec.UNSPECIFIED,
        )
        self.interface.intrinsic.width = at_least(self.native.getMeasuredWidth())
        self.interface.intrinsic.height = self.native.getMeasuredHeight()
