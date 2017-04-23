import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.uix.behaviors.emacs import EmacsBehavior
from pymongo import MongoClient
import time
import sys

class registerAccount(StackLayout):
	
	def registerUser(self, pname, email, username, password, cpass):
		if pname and email and username and password and cpass:
			try:
				client = MongoClient()
				db = client['remindersNote']
				cursor = db.users.find({"username" : username}).count()
				if cursor <= 0:
					if password == cpass:
						popup = Popup(title='Message', content=Label(text="Account Created"), size_hint=(None, None), size=(200, 80))

						db.users.insert_one(
							{
								"username" : username,
								"password" : password,
								"personal_details": [
									{
										"fullname" : pname,
										"email" : email
									}
								],
								"date_registered": time.strftime("%d%m%Y")
							}
						)

						popup = Popup(title='Message', content=Label(text="Account Created"), size_hint=(None, None), size=(200, 80))
						popup.open()
						sys.exit()
					else:
						popup = Popup(title='Message', content=Label(text="Password Not Match"), size_hint=(None, None), size=(200, 80))
				else:
					popup = Popup(title='Message', content=Label(text="Username Already Exist!"), size_hint=(None, None), size=(200, 80))
				popup.open()
			except Exception:
				self.display.text = "Error Input"
		else:
			self.display.text = "Required Field"


class registerLog(App):
	
	def build(self):
		return registerAccount()

register = registerLog()
register.run()