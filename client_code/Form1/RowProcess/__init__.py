from ._anvil_designer import RowProcessTemplate
from anvil import *

class RowProcess(RowProcessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_delete_click(self, **event_args):
    self.remove_from_parent()
    
