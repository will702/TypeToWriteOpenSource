from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from PIL import Image
import string
import random

def randoming_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(random.randint(3, 5)))

    return result_str
#...


username_input = """
MDTextField:
    hint_text: "Enter Text"
    helper_text: "Try Again if unrecognized"
    helper_text_mode: "on_focus"
    icon_right: "android"
    multiline:True
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'top': 1}
    size_hint_x:None
    width:500
"""
import requests
import json

class DemoApp(MDApp):

    def build(self):
        self.title = "TypeToWrite"
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.04},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)

        return screen

    def show_data(self,obj):
        if self.username.text != "":
            user_error = "Text already executed" +"\nFinished already."
        else:
            user_error = "Enter what u wanna write"
        self.dialog = MDDialog(title='writing check',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        sambungkan = requests.get('https://salism3.pythonanywhere.com/nulis?text='+self.username.text)
        isi = randoming_string()
        for i in json.loads(sambungkan.content)['images']:

            gambar = requests.get(i)
            open(f'{isi}.png','wb').write(gambar.content)
            print('selesai')
            break





        self.dialog.open()
        img = Image.open(f'{isi}.png')
        img.show()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog


DemoApp().run()