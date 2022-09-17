#from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder

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

class MyContent(MDBoxLayout):
    pass
class DisplayAllEmployee(Screen):
    pass
    '''
    def on_start(self):
        names= ["option 1", "option 2", "option 3"]
        
        for name in names:
            
            panel = MDExpansionPanel(title=name,icon="img/face.jpg",content= MyContent())
            
            self.manager.get_screen('displayallemployee').ids.panel_container.add_widget(panel)
            
     '''       
            
            
            
class AddEmployee(Screen):
    checks = []
    
    def checkbox_click(self, instance, value, topping):
        if value == True:
            AddEmployee.checks.append(topping)
            tops=''
            for x in AddEmployee.checks:
                tops=f'{tops}{x}'
             
            print(tops)
            #self.ids.output_label.text=f'You Selected: {tops} '
            
        else:
            AddEmployee.checks.remove(topping)
            tops=''
            for x in AddEmployee.checks:
                tops=f'{tops}{x}'
            print(tops)
            #self.ids.output_label.text=f'You Selected: {tops} '
    
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

#kv= Builder.load_file('design.kv')  
class Eapp(MDApp):

    #Window.size=(800, 500)
    #Window.clearcolor = "#ffffff"
    
    def build(self):
        kv= Builder.load_file('design.kv')  
        return kv
    
 


if __name__ == '__main__':
    Eapp().run()