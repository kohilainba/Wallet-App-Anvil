from ._anvil_designer import admin_add_userTemplate
from anvil import *
import anvil.users
import anvil.server
import re

class admin_add_user(admin_add_userTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args): 
    count=0
    if self.text_box_3.text != '':
      if self.text_box_3.text != self.text_box_7.text:
        self.label_17.text = "Passwords doesn't match"
        self.text_box_3.text =''
        self.text_box_3.focus()
        self.text_box_7.text =''
        self.text_box_7.focus()
      elif self.text_box_3.text == self.text_box_7.text:
        self.label_17.text = "Password matches"
        count=count+1
      converted_text = self.text_box_4.text 
      if self.is_pan_card_detail(converted_text):
        self.label_14.text ="Pan card is valid"
        count=count+1
      else:
        self.label_14.text ="Please check the entered pan card details"
        self.text_box_4.text=''
        self.text_box_4.focus()
        
      phone_number = self.text_box_6.text
  
      if self.validate_phone_number(phone_number):
        count=count+1
        self.label_15.text ="Phone number is correct"
      else:
        self.label_15.text ="Please check the entered phone number"
        self.text_box_6.text=''
        self.text_box_6.focus()
      aadharr= self.text_box_8.text
      if len(str(aadharr)) == 12:
        count=count+1
        self.label_16.text ="Aadhar detalis correct"
      else:
        self.label_16.text ="Please check the entered Aadhar details"
        self.text_box_8.text=''
        self.text_box_8.focus()
        
    if count==4:
      anvil.server.call(
        'add_info', 
        self.text_box_1.text, 
        self.text_box_2.text, 
        self.text_box_3.text,
        self.text_box_4.text,
        self.text_box_5.text,
        self.text_box_6.text,
        self.text_box_8.text
      )
      alert (self.text_box_2.text + ' added')
      open_form('LOGIN')

  def link_1_click(self, **event_args):
    open_form('Home')

  def text_box_4_change(self, **event_args):
    current_text = self.text_box_4.text
    converted_text = current_text.upper()
    self.text_box_4.text = converted_text
    
    
   
  def is_pan_card_detail(self, text):
        if (
            len(text) == 10 and
            text[:5].isalpha() and
            text[5:9].isdigit() and
            text[9].isalpha()
        ):
          return True
        else:
          return False

  def validate_button_click(self, **event_args):
    phone_number = self.text_box_6.text.strip()  # Remove leading/trailing whitespace
  
  

  def validate_phone_number(self, phone_number):
    pattern = r'^[6-9]\d{9}$'
    if re.match(pattern, str(phone_number)):
        return True  
    else:
        return False

  def link_8_click(self, **event_args):
   open_form('admin')

  def link_8_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin')

  def link_10_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.user_support')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def button_3_click(self, **event_args):
    open_form('admin.show_users')
