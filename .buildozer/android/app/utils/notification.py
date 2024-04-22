from kivy.uix.label import Label
from kivy.clock import Clock


class CopyNotification(Label):
    def __init__(self, popup, text, **kwargs):
        super(CopyNotification, self).__init__(**kwargs)
        self.text = text
        self.popup = popup

        Clock.schedule_once(self.dismiss, 1)

    def dismiss(self, dt):
        self.popup.dismiss()


class ValidateNotification(Label):
    def __init__(self, popup, text, **kwargs):
        super(ValidateNotification, self).__init__(**kwargs)
        self.text = text
        self.popup = popup


class BracketNotification(Label):
    def __init__(self, popup, text, **kwargs):
        super(BracketNotification, self).__init__(**kwargs)
        self.text = text
        self.popup = popup
