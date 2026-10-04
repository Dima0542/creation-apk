__version__ = "1.0"

from kivy.app import App
from kivy.uix.button import Button


class VexApp(App):
    def build(self):
        return Button(
            text="VEX IS ALIVE",
            font_size=32
        )


VexApp().run()