from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.metrics import dp

import gtts
from playsound import playsound

class MyBox(BoxLayout):
    text = StringProperty()
    filetitle = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.l1 = Label(text="My TTS App", font_size=30, size_hint_y=0.50)

        self.box = BoxLayout(orientation = "horizontal")
        self.l2 = Label(text="Title of File", size_hint_y=0.25)
        self.t2 = TextInput(text="", size_hint_y=0.25)
        self.box.add_widget(self.l2)
        self.box.add_widget(self.t2)

        self.t1 = TextInput(text="")
        self.b1 = Button(text="Convert", on_press=self.callback, size_hint_y=0.25)
        self.add_widget(self.l1)
        self.add_widget(self.box)
        self.add_widget(self.t1)
        self.add_widget(self.b1)

    def callback(self, instance):
        self.text = self.t1.text
        self.filetitle = self.t2.text
        return self.converter()

    def converter(self):
        tts = gtts.gTTS(self.text)
        tts.save(f'{self.filetitle}.mp3')
        #playsound("myfile.mp3")

class MyTTSApp(App):
    def build(self):
        bx = MyBox()

        return bx


if __name__ == "__main__":
    MyTTSApp().run()




