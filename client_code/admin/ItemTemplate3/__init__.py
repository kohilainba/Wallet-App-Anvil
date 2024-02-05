from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.users
import anvil.server


class ItemTemplate3(ItemTemplate3Template):
    def __init__(self, **properties):
        self.init_components(**properties)
       
       
    def button_1_click(self, **event_args):
        # Access the data for the selected user
        selected_user = self.item  # Assuming you have set the 'item' property of the repeating panel to the user row
        
        # Open the admin_view form and pass the user details
        open_form('admin.admin_view', user_data=selected_user)

    

  
      
       

   

   

  



    
    
