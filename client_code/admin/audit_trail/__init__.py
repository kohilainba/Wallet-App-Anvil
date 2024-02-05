from ._anvil_designer import audit_trailTemplate
from anvil import *
import anvil.users
import anvil.server
from datetime import datetime

class audit_trail(audit_trailTemplate):
  def __init__(self, user=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user = user
    self.repeating_panel_1.items = app_tables.actions.search()


  def button_1_click(self, **event_args):
        entered_user = self.text_box_1.text
        filtered_actions = app_tables.actions.search(username=entered_user)
        self.repeating_panel_1.items = filtered_actions

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
    open_form('admin')


