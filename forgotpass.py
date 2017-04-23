import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from pymongo import MongoClient
import os

class forgotPassAction(StackLayout):
	pass

class forgotLog(App):

    def build(self):
        return forgotPassAction()

forgotlog = forgotLog()

forgotlog.run()