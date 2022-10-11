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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.toast import toast
import pandas as pd

"""
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

"""
# class to call the popup function
class Popup(Widget):
	def btn(self):
		popFun()

# class to build GUI for a popup window
class P(FloatLayout):
	pass

# function that displays the content
def popFun():
	show = P()
	window = Popup(title = "popup", content = show,
				size_hint = (None, None), size = (300, 300))
	window.open()
class Welcome(Screen):
    pass
class Login(Screen ):
	def validate(self):
		# validating if the email already exists
		if self.email.text not in users['Email'].unique():
			popFun()
		else:
			# switching the current screen to display validation result
			self.manager.current = 'menu'

			# reset TextInput widget
			self.email.text = ""
			self.password.text = ""
class CreateAnAccount(Screen):
	def createbtn(self):
        
		# creating a DataFrame of the info
		user = pd.DataFrame([[self.fullname.text, self.email.text, self.password.text]],
							columns = ['Name', 'Email', 'Password'])
		if self.email.text != "" and self.password.text !="":
			if self.email.text not in users['Email'].unique():
                
				# if email does not exist already then append to the csv file
				# change current screen to log in the user now
				user.to_csv('login.csv', mode = 'a', header = False, index = False)
				self.manager.current = 'menu'
				self.fullname.text = ""
				self.email.text = ""
				self.password.text = ""
                
		else:
			# if values are empty or invalid show pop up
			popFun() 
            

class Menu(Screen):
    pass

class MyContent(MDBoxLayout):
    pass
class DisplayAllEmployee(Screen):
    pass
    """
    def on_start(self):
        empdatas= pd.read_csv('empdata.csv', sep=',')
        
        for empdata in empdatas:
            
            panel = MDExpansionPanel(title=name,content= Employeedetails())
            
            self.manager.get_screen('displayallemployee').ids.container.add_widget(panel)
            
    """      
  
class UpdateEmployee(Screen):
    pass
    """
    gender = " "
    designation = " "
    def gender(self, instance, value, topping):
        if value == True:
            AddEmployee.gender= topping
            #self.ids.output_label.text=f'You Selected: {tops} '
            
        else:
            AddEmployee.gender= "Gender"
           
            #self.ids.output_label.text=f'You Selected: {tops} '
    def designation(self, instance, value, topping):
        if value == True:
            AddEmployee.designation= topping
            #self.ids.output_label.text=f'You Selected: {tops} '
            
        else:
            AddEmployee.gender= "Manager"
           
            #self.ids.output_label.text=f'You Selected: {tops} '
    

    fname= ObjectProperty(none) 
    lname= ObjectProperty(none) 
    mail= ObjectProperty(none) 
    gender= ObjectProperty(none) 
    
    def press(self):
        fname: self.fname.text
        lname: self.lname.text
        mail: self.mail.text
        address : self.mail.address
        
        print({fname, lname, mail})
        
        # creating a DataFrame of the info
		empdata = pd.DataFrame([[fname, lname, mail, address, gender, designation]],
							columns = ['First Name', 'Last Name 'Email', 'Address','Gender', 'Designation'])
        empdata.to_csv('empdata.csv', mode = 'a', header = False, index = False)       
        self.manager.current = 'menu'   
        
     """


          
class EmployeeDetails(Screen):
       
    empdatas= pd.read_csv('empdata.csv', sep=',')   
    print("Emp Details", empdatas['First Name'][0], empdatas['Last Name'][0], empdatas['Email'][0] )
            
class AddEmployee(Screen):
    gender = " "
    designation = " "
    def gender(self, instance, value, topping):
        if value == True:
            AddEmployee.gender= topping
            #self.ids.output_label.text=f'You Selected: {tops} '
            
        else:
            AddEmployee.gender= "Male" #default
           
            #self.ids.output_label.text=f'You Selected: {tops} '
    def designation(self, instance, value, topping):
        if value == True:
            AddEmployee.designation= topping
            #self.ids.output_label.text=f'You Selected: {tops} '
            
        else:
            AddEmployee.designation= "Manager"
           
            #self.ids.output_label.text=f'You Selected: {tops} '

    #fname= ObjectProperty(none) 
    #lname= ObjectProperty(none) 
    #mail= ObjectProperty(none) 
    #gender= ObjectProperty(none) 
    

    def press(self):
        fname= self.fname.text
        lname= self.lname.text
        mail= self.mail.text
        address = self.address.text
        
        print({fname, lname, mail, address, AddEmployee.gender, AddEmployee.designation})
        
        # creating a DataFrame of the info
		#empdata = pd.DataFrame([[fname, lname, mail, address, AddEmployee.gender, "Admin"]],
                         #columns = ['First Name', 'Last Name', 'Email', 'Address','Gender', 'Designation'])
        
       # empdata.to_csv('empdata.csv', mode = 'a', header = False, index = False)       
        self.manager.current = 'menu'   
        
        


class WindowManager(ScreenManager):
    pass

users=pd.read_csv('login.csv',sep=',')
empdatas= pd.read_csv('empdata.csv', sep=',')
print('users: ',users)
#print("Employee:", empdatas)
#kv= Builder.load_file('design.kv')  
class Eapp(MDApp):

    #Window.size=(800, 500)
    #Window.clearcolor = "#ffffff"

    def build(self):
        kv= Builder.load_file('design.kv')  
        return kv
    
 


if __name__ == '__main__':
    Eapp().run()