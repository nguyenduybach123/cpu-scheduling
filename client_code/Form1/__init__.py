from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
from .SquareProcess import SquareProcess

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
      'at': int(self.txt_at.text),
      'bt': int(self.txt_bt.text),
      'prioty': int(self.txt_prioty.text)
    }]
    processListAdded = list(self.repeating_panel_process.items) + objProcess
    self.repeating_panel_process.items = processListAdded
    self.reset_txt_inser_process()

  def reset_txt_inser_process(self):
    self.txt_process.text = self.txt_at.text = self.txt_bt.text = self.txt_prioty.text = ""

  def button_solve_click(self, **event_args):
    processBackgrounds = {"A": "red", "B": "green", "C": "blue"}
    #processTimeLines = anvil.server.call('roundRobinScheduling', self.repeating_panel_process.items, 4)
    processTimeLines = anvil.server.call('SJFScheduling', self.repeating_panel_process.items)
    print(processTimeLines)
    self.drawProcessGanttCharts(processTimeLines, processBackgrounds)

  def drawProcessGanttCharts(self, processTimeLines, processBackgrounds):
    widthSquare = 40
    posX = 30
    posY = 0

    withTmp = 0
    for i in range(0,len(processTimeLines)):
      process = processTimeLines[i]
      timeEnd = process['time-end'] if i == len(processTimeLines) - 1 else ""
      withProcess = widthSquare + (int(process['time-end']) - int(process['time-start']))
      processSquare = SquareProcess(name_process = process['name'], time_start = process['time-start'], time_end = timeEnd, background_process = processBackgrounds[process['name']])
      self.xy_panel_process.add_component(processSquare, x=posX, y=posY, width=withProcess)
      posX = posX + withProcess 



      
    

