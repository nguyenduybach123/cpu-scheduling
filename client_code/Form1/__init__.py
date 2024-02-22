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
      {'col_process':  '', 'col_at': '', 'col_bt': '', 'col_prioty': ''}
    ]

  def plot_process_show(self, **event_args):
    self.plot_1.data = [
    go.Scatter(
      x = [1, 2, 3],
      y = [3, 1, 6],
      marker = dict(
        color= 'rgb(16, 32, 77)'
      )
    ),
    go.Bar(
      x = [1, 2, 3],
      y = [3, 1, 6],
      name = 'Bar Chart Example'
    )
  ]
