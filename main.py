from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
"""
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

"""

class Welcome(Screen):
    pass
class Login(Screen ):
    pass
    """
    def press(self):
        email= self.email.text
        password= self.password.text
        self.email.text= ""
        self.password.text=""

    """
class Menu(Screen):
    pass

class AddEmployee(Screen):
    pass
    
    """
    fname= ObjectProperty(none) 
    lname= ObjectProperty(none) 
    mail= ObjectProperty(none) 
    gender= ObjectProperty(none) 
    
    def press(self):
        fname: self.fname.text
        lname: self.lname.text
        mail: self.mail.text
        
        print({fname, lname, mail})
        
     """

class WindowManager(ScreenManager):
    pass

kv= Builder.load_file('design.kv')  
class Eapp(App):
    #Window.size=(800, 500)
    Window.clearcolor = "#ffffff"
    def build(self):
        return kv
    


if __name__ == '__main__':
    Eapp().run()