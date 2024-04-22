from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HelpScreen(Screen):
    def __init__(self, **kw):
        super(HelpScreen, self).__init__(**kw)
        self.name = "help"
        self.root = BoxLayout(orientation="vertical")
        self.add_widget(self.root)
        self.load_help_Screen()

    def load_help_Screen(self):
        head_layout = BoxLayout()
        head = Label(text="Help")
        head_layout.add_widget(head)

        main_adding_layout = BoxLayout(size_hint=(1, 1))
        main_adding = Label(
            text="[Adding]\nFirst, press the Add new + button.\nInput your informations and press the Save.\nIf you return to main screen,\na new button will be created.\n!!You can't save 'Blank'!!\n",
            size_hint=(1, 1),
        )
        main_adding_layout.add_widget(main_adding)

        main_watching_layout = BoxLayout(size_hint=(1, 1))
        main_watching = Label(
            text="[Watching]\nIf you wanna see your infos like ID and PW,\njust press the button added.\n",
            size_hint=(1, 1),
        )
        main_watching_layout.add_widget(main_watching)

        main_deleting_layout = BoxLayout(size_hint=(1, 1))
        main_deleting = Label(
            text="[Deleting]\nJust press Delete button at the info screen.\n!!CAUTION!!\nIf you delete your button(informations),\nit will be deleted permanently.\n",
            size_hint=(1, 1),
        )
        main_deleting_layout.add_widget(main_deleting)

        main_copying_layout = BoxLayout(size_hint=(1, 1))
        main_copying = Label(
            text="[Copying]\nThis app apply copying function.\nPress the copy button and paste to Login!\n",
            size_hint=(1, 1),
        )
        main_copying_layout.add_widget(main_copying)

        self.root.add_widget(head_layout)
        self.root.add_widget(main_adding_layout)
        self.root.add_widget(main_watching_layout)
        self.root.add_widget(main_deleting_layout)
        self.root.add_widget(main_copying_layout)

        from utils.button import ReturnButton

        button_layout = BoxLayout()
        button_layout.add_widget(ReturnButton(text="Return"))
        self.root.add_widget(button_layout)
