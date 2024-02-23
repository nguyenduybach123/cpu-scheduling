from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def repeating_panel_process_show(self, **event_args):
    self.repeating_panel_process.items = []

  def drop_down_algorithm_show(self, **event_args):
    self.drop_down_algorithm.items = ["Round Robin", "FCFS", "SJC"]

  def drop_down_algorithm_change(self, **event_args):
    pass

  def button_add_process_click(self, **event_args):
    objProcess = [{
      'process': self.txt_process.text,
      'at': self.txt_at.text,
      'bt': self.txt_bt.text,
      'prioty': self.txt_prioty.text
    }]
    processListAdded = list(self.repeating_panel_process.items) + objProcess
    self.repeating_panel_process.items = processListAdded
    self.reset_txt_inser_process()

  def reset_txt_inser_process(self):
    self.txt_process.text = self.txt_at.text = self.txt_bt.text = self.txt_prioty.text = ""

  def button_solve_click(self, **event_args):
    processList = [
      {"name": "A", "time-start": 1, "time-end": 2},
      {"name": "B", "time-start": 1, "time-end": 2},
      {"name": "C", "time-start": 1, "time-end": 2},
      {"name": "D", "time-start": 1, "time-end": 2}
    ]
    for process in processList:
      print(process['name'])



