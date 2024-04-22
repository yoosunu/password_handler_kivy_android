from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.bind(text=self.on_text_changed)

    def on_text_changed(self, instance, value):
        self.text = self.text.strip()
