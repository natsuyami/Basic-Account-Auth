import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from pymongo import MongoClient
import os

class forgotPassAction(StackLayout):
	def forgotPass(self, username, password, conpass):
		client = MongoClient()
		db = client["remindersNote"]
		cursor = db.users.find({"username" : username}).count()
		if cursor > 0:
			if password == conpass:
				client = MongoClient()
				db = client["remindersNote"]
				db.users.update(
					{ "username" : username },
					{
						'$set': {"password" : password}
					}
				)
				popup = Popup(title='Message', content=Label(text="Password Updated"), size_hint=(None, None), size=(200, 80))
				popup.open()
			else:
				self.display.text = "Password Don't Match"
		else:
			self.display.text = "Username Dont Exist"

	def backHome(self):
		quit()

class forgotLog(App):

    def build(self):
        return forgotPassAction()

forgotlog = forgotLog()

forgotlog.run()