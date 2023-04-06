import kivy

kivy.require('1.0.6')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name=ObjectProperty(None)
    lname=ObjectProperty(None)
    def btn(self):
        print("name",self.name.text)
        print("lname",self.lname.text)
        self.name.text=""
        self.lname.text=""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
