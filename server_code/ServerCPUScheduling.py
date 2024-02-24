import anvil.server
import queue
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:


@anvil.server.callable
def roundRobinScheduling(processList, quantumTime):
  ganttGraph = []
  processTimeList = []
  processListSortedByAT = sorted(processList, key=lambda item: item['at'])
  timeLine = 0
  processQueue = queue.Queue()
  for process in processListSortedByAT:
    processQueue.put(process)

  while(processQueue.empty() == False):
    processReady = processQueue.get()
    
    if(processReady['bt'] > quantumTime):
      processReady['bt'] = processReady['bt'] - quantumTime
      ganttGraph.append({'name': processReady['process'], 'time-start': str(timeLine), 'time-end': str(timeLine + quantumTime)})
      timeLine = timeLine + quantumTime
      processQueue.put(processReady)
      
    else:
      ganttGraph.append({'name': processReady['process'], 'time-start': str(timeLine), 'time-end': str(timeLine + processReady['bt'])})
      timeLine = timeLine + processReady['bt']
      processTimeList.append({'name': processReady['name'], 'turnaround-time': timeLine, 'waiting-time': timeLine - processList[processReady['index']['bt']]})
  
  timeAvg = {
    'waiting-time-avg': avgList([processTime['waiting-time'] for processTime in processTimeList]),
    'turnaround-time-avg': avgList([processTime['turnaround-time'] for processTime in processTimeList])
  }
  
  return ganttGraph, processTimeList, timeAvg

@anvil.server.callable
def FCFSScheduling(processList):
  ganttGraph = []
  turnaround_time = [0]
  processTimeList = []
  processListSortedByAT = sorted(processList, key=lambda item: item['at'])
  timeLine = 0
  processQueue = queue.Queue()
  for process in processListSortedByAT:
    processQueue.put(process)

  i = 1
  while(processQueue.empty() == False):
    processReady = processQueue.get()
    ganttGraph.append({'name': processReady['process'], 'time-start': str(timeLine), 'time-end': str(timeLine + processReady['bt'])})
    turnaround_time_value = turnaround_time[i-1] + processReady['bt'] - processReady['at']
    if turnaround_time_value < 0:
          turnaround_time_value = 0
    turnaround_time.append(turnaround_time_value)
    processTimeList.append({'name': processReady['name'], 'turnaround-time': turnaround_time_value, 'waiting-time': timeLine})
    i += 1
    timeLine = timeLine + processReady['bt']
  
  timeAvg = {
    'waiting-time-avg': avgList([processTime['waiting-time'] for processTime in processTimeList]),
    'turnaround-time-avg': avgList([processTime['turnaround-time'] for processTime in processTimeList])
  }
  
  return ganttGraph, processTimeList, timeAvg


@anvil.server.callable
def SJFScheduling(processList):
  ganttGraph = []
  turnaround_time = [0]
  processTimeList = []
  timeLine = 0
  processListSortedByAT = sorted(processList, key=lambda item: item['bt'])
  processQueue = queue.Queue()
  for process in processListSortedByAT:
    processQueue.put(process)

  i = 1
  while(processQueue.empty() == False):
    processReady = processQueue.get()
    ganttGraph.append({'name': processReady['process'], 'time-start': str(timeLine), 'time-end': str(timeLine + processReady['bt'])})
    turnaround_time_value = turnaround_time[i-1] + processReady['bt'] - processReady['at']
    if turnaround_time_value < 0:
          turnaround_time_value = 0
    turnaround_time.append(turnaround_time_value)
    processTimeList.append({'name': processReady['process'], 'turnaround-time':turnaround_time_value, 'waiting-time': timeLine })
    i += 1
    timeLine = timeLine + processReady['bt']

  timeAvg = {
    'waiting-time-avg': avgList([processTime['waiting-time'] for processTime in processTimeList]),
    'turnaround-time-avg': avgList([processTime['turnaround-time'] for processTime in processTimeList])
  }
  
  return ganttGraph, processTimeList, timeAvg

def avgList(lst):
  return sum(lst) / len(lst)
