from ._anvil_designer import SquareProcessTemplate
from anvil import *

class SquareProcess(SquareProcessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
