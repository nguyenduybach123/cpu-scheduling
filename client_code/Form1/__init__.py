from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import re
from .SquareProcess import SquareProcess

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.txt_quantum_time.visible = False
    self.plot_process.layout = {
      'title': 'Thời gian xử lý các tiến trình',
      'xaxis': {
        'title': 'thời gian chờ'
      },
      'yaxis': {
        'title': 'thời gian hoàn thành'
      }
    }

    

  
  
  def repeating_panel_process_show(self, **event_args):
    self.repeating_panel_process.items = []

  def drop_down_algorithm_show(self, **event_args):
    self.drop_down_algorithm.items = ["FCFS", "SJC", "Round Robin"]

  def drop_down_algorithm_change(self, **event_args):
    algorithmSelected = self.drop_down_algorithm.selected_value
    if(algorithmSelected == 'Round Robin'):
      self.txt_quantum_time.visible = True
    else:
      self.txt_quantum_time.visible = False

  def button_add_process_click(self, **event_args):
    if(self.isInputEmpty() == False):
      alert("Yêu cầu nhập đầy đủ thông tin tiến trình !!")
      return

    if(self.isInputNumberValue() == False):
      alert("Yêu cầu nhập số nguyên cho các giá trị tiến trình !!")
      return

    if(self.isColorValue(self.txt_color.text) == False):
      alert("Yêu cầu nhập mã màu hexa cho tiến trình !!")
      return
    
    objProcess = [{
      'index': len(self.repeating_panel_process.items),
      'process': self.txt_process.text,
      'at': int(self.txt_at.text),
      'bt': int(self.txt_bt.text),
      'color': self.txt_color.text
    }]
    processListAdded = list(self.repeating_panel_process.items) + objProcess
    self.repeating_panel_process.items = processListAdded
    self.reset_txt_insert_process()

  def reset_txt_insert_process(self):
    self.txt_process.text = self.txt_at.text = self.txt_bt.text = self.txt_color.text = ""

  def button_solve_click(self, **event_args):
    if(len(self.repeating_panel_process.items) == 0):
      alert("tiến trình không tồn tại !!!")
      return   
    self.xy_panel_process.clear()
    processBackgrounds = self.initDictColorFromProcessList(self.repeating_panel_process.items)

    algorithmSelected = self.drop_down_algorithm.selected_value
    if(algorithmSelected == 'Round Robin'):
      
      if(self.txt_quantum_time.text == "" or self.isNumberic(self.txt_quantum_time.text) == False):
        alert("Yêu cầu giá trị quantum cho giải thuật !!")
        return

      quantumTime = int(self.txt_quantum_time.text)
      if(quantumTime == 0):
        alert("Giá trị quantum phải khác 0 !!")
        return
      
      processTimeLines, processTimeList, timeAvg = anvil.server.call('roundRobinScheduling', self.repeating_panel_process.items, quantumTime)
    elif(algorithmSelected == 'FCFS'):
      processTimeLines, processTimeList, timeAvg = anvil.server.call('FCFSScheduling', self.repeating_panel_process.items)
    else:
      processTimeLines, processTimeList, timeAvg = anvil.server.call('SJFScheduling', self.repeating_panel_process.items)
    
    print(timeAvg)
    self.drawProcessGanttCharts(processTimeLines, processBackgrounds)
    self.label_wta.text = timeAvg['waiting-time-avg']
    self.label_taa.text = timeAvg['turnaround-time-avg']
    self.drawPlotProcess(processTimeList, processBackgrounds)
    self.plot_process.redraw()
  
  def initDictColorFromProcessList(self, processList):
    dictColor = {}
    for process in processList:
        name = process['process']
        color = process['color']
        dictColor[name] = color
    return dictColor
  
  def isInputNumberValue(self):
    if(self.isNumberic(self.txt_at.text) == False or self.isNumberic(self.txt_bt.text) == False):
      return False
    return True

  def isNumberic(self, input_string):
    pattern = r'^\d+$'
    if re.match(pattern, input_string):
        return True
    else:
        return False

  def isInputEmpty(self):
    if(self.txt_process.text == "" or self.txt_at.text == "" or self.txt_bt.text ==  "" or self.txt_color.text == ""):
      return False
    return True

  def isColorValue(self, color_string):
    hex_pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    if re.match(hex_pattern, color_string):
      return True
    return False
    
  def drawProcessGanttCharts(self, processTimeLines, processBackgrounds):
    widthSquare = 40
    posX = 30
    posY = 0

    withTmp = 0
    for i in range(0,len(processTimeLines)):
      process = processTimeLines[i]
      timeEnd = process['time-end'] if i == len(processTimeLines) - 1 else ""
      widthProcess = widthSquare + int(int(process['time-end']) - int(process['time-start']) * 1.3)
      processSquare = SquareProcess(name_process = process['name'], time_start = process['time-start'], time_end = timeEnd, background_process = processBackgrounds[process['name']])
      self.xy_panel_process.add_component(processSquare, x=posX, y=posY, width = widthProcess if widthProcess > 40 else widthSquare)
      posX = posX + widthProcess 

  def drawPlotProcess(self, processTimeList, processBackgrounds):
    self.plot_process.data = [
      go.Scatter(
        x = list([process['waiting-time'] for process in processTimeList]),
        y = list([process['turnaround-time'] for process in processTimeList]),
        name = list([process['name'] for process in processTimeList]),
        marker = dict(
          color= list(processBackgrounds.values()),
          size= 50,
          line = dict(
            width = 2
          )
        )
      )
    ]

      
    

