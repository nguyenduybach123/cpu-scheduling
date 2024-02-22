from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def repeating_panel_process_show(self, **event_args):
    self.repeating_panel_process.items = [
      {'col_process':  'A', 'col_at': '6', 'col_bt': '6', 'col_prioty': '6'}
    ]
