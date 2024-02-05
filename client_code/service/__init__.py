from ._anvil_designer import serviceTemplate
from anvil import *
import anvil.server

class service(serviceTemplate):
    def __init__(self,user=None,**properties):
        self.init_components(**properties)
        self.user = user

 

   

  

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        query = self.text_box_1.text

        # Fetch user information from the "users" table
        user_info = app_tables.users.get(username=self.user['username'])

        if user_info is not None:
            # Update the "Services" table with the query and user information
            app_tables.sevices.add_row(
                username=user_info['username'],
                phone=user_info['phone'],
                Query=query
            )
            alert("Your query has been submitted, and our Technical Executive will get in touch with you")
        else:
            alert("User information not found.")

    def link_2_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("deposit",user=self.user)

    def link_3_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("transfer",user=self.user)

    def link_4_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("withdraw",user=self.user)

    def link_7_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("customer", user=self.user)

    def link_13_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("Home")

    def link_8_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("service",user=self.user)

   
