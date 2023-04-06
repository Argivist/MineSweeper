import urllib

import kivy
import MinesweeperP2 as mp2

kivy.require('2.0.0')  # replace with your current kivy version !
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


difficulty = ''


class HomePage(Screen):


    def start(self):
        print(self.diff)
        size=str(mp2.gameStart(self.diff)[0])
        print(size)






class GamePage(Screen):
    def __init__(self, **kwargs):
        self.ur=urllib.request.urlopen("https://i.imgur.com/1Z1Z1Z1.png").read()
    #def __init__(self,**kwargs):
      #  super(GamePage, self).__init__(**kwargs)
       # self.add_widget(Label(text='Hello World'))




class ScreenManagement(ScreenManager):
    pass


class SweeperApp(App):
    MineFieldSize = 0
    BombNum = 0
    mpe2 = mp2
    difficulty=""
    def build(self):
        return None




if __name__ == "__main__":
    SweeperApp().run()
