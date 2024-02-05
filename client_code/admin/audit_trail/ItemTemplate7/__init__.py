from ._anvil_designer import ItemTemplate7Template
from anvil import *
import anvil.server
import anvil.users

class ItemTemplate7(ItemTemplate7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    
