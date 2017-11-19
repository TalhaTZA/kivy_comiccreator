from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty ,ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class StatusBar(ButtonBehavior,BoxLayout):
    counter=NumericProperty(0)
    previous_counter=0

    def on_counter(self,instance,value):
        if value==0:
            self.msg_text.text= "Drawing Space Cleraed"
        
        elif value-1 == self.__class__.previous_counter:
            self.msg_text.text = "Widget Added"

        elif value+1 == StatusBar.previous_counter:
            self.msg_text.text = "Widget Removed"

        self.__class__.previous_counter=value
    
    def on_release(self):
        the_content=Label(text='OPEN SOURCE KIVY PROJECT \n COMIC CREATOR')
        the_content.color=(1,0,0,1)

        popup=Popup(title='Pop Up',content=the_content,size_hint=(None,None),size=(350,150))
        popup.open()