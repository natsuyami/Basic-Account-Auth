import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors.emacs import EmacsBehavior

class registerAccount(StackLayout):
	pass

class registerLog(App):
	
	def build(self):
		return registerAccount()

register = registerLog()
register.run()

		