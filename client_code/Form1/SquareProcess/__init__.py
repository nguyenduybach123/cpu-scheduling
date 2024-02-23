from ._anvil_designer import SquareProcessTemplate
from anvil import *

class SquareProcess(SquareProcessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @property
  def name_process(self):
    return self.lbl_name.text
  
  @name_process.setter
  def name_process(self, value):
    self.lbl_name.text = value

  @property
  def time_start(self):
    return self.lbl_start.text
  
  @time_start.setter
  def time_start(self, value):
    self.lbl_start.text = value

  @property
  def time_end(self):
    return self.lbl_end.text
  
  @time_end.setter
  def time_end(self, value):
    self.lbl_end.text = value
  
  @property
  def background_process(self):
    return self.lbl_name.background

  @background_process.setter
  def background_process(self, value):
    self.lbl_name.background = value