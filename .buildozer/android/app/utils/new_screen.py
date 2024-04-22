from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from utils.button import ReturnButton
from utils.module import CustomTextInput

from jnius import autoclass
import os
from os.path import join
import openpyxl as op

Environment = autoclass('android.os.Environment')
context = autoclass('org.kivy.android.PythonActivity').mActivity
files_dir = context.getFilesDir().getAbsolutePath()
file_path = os.path.join(files_dir, "password.xlsx")


class AddNewScreen(Screen):
    def __init__(self, **kwargs):
        super(AddNewScreen, self).__init__(**kwargs)
        self.name = "new"
        site_name_input, id_input, pw_input = self.load_screen()
        self.site_name_input = site_name_input
        self.id_input = id_input
        self.pw_input = pw_input

    def load_screen(self):

        wb = op.load_workbook(file_path)
        wb.active

        root = BoxLayout(orientation="vertical")
        self.add_widget(root)

        root.add_widget(Label(text="Input ID and password!"))

        site_name_layout = BoxLayout(size_hint=(1, 0.5))
        site_name_label = Label(text="SITE: ")
        site_name_layout.add_widget(site_name_label)
        site_name_input = CustomTextInput(
            multiline=False,
            hint_text="Input site name",
        )
        site_name_layout.add_widget(site_name_input)
        root.add_widget(site_name_layout)

        id_input_layout = BoxLayout(size_hint=(1, 0.5))
        id_label = Label(text="ID: ")
        id_input = CustomTextInput(
            multiline=False,
            hint_text="Input ID",
        )
        id_input_layout.add_widget(id_label)
        id_input_layout.add_widget(id_input)
        root.add_widget(id_input_layout)

        pw_input_layout = BoxLayout(size_hint=(1, 0.5))
        pw_label = Label(text="PW: ")
        pw_input = CustomTextInput(
            multiline=False,
            hint_text="Input password",
        )
        pw_input_layout.add_widget(pw_label)
        pw_input_layout.add_widget(pw_input)
        root.add_widget(pw_input_layout)

        from utils.button import SaveButton

        button_layout = BoxLayout(orientation="vertical", size_hint=(1, 1.5))
        button_layout.add_widget(SaveButton(text="Save"))
        button_layout.add_widget(ReturnButton(text="Cancel"))

        root.add_widget(button_layout)

        wb.save(file_path)

        return site_name_input, id_input, pw_input
