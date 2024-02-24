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
  waitingTimeList = []
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
      waitingTimeList.append({'name': processReady['name'], 'waiting-time': timeLine - processList[processReady['index']['bt']]})
  return ganttGraph, waitingTimeList

@anvil.server.callable
def FCFSScheduling(processList):
  ganttGraph = []
  waiting_time = [0]
  waitingTimeList = []
  processListSortedByAT = sorted(processList, key=lambda item: item['at'])
  timeLine = 0
  processQueue = queue.Queue()
  for process in processListSortedByAT:
    processQueue.put(process)

  i = 1
  while(processQueue.empty() == False):
    processReady = processQueue.get()
    ganttGraph.append({'name': processReady['process'], 'time-start': str(timeLine), 'time-end': str(timeLine + processReady['bt'])})
    waiting_time_value = waiting_time[i-1] + processReady['bt'] - processReady['at']
    if waiting_time_value < 0:
          waiting_time_value = 0
    waiting_time.append(waiting_time_value)
    waitingTimeList.append({'name': processReady['name'], 'waiting-time': waiting_time_value})
    i += 1
    timeLine = timeLine + processReady['bt']
  return ganttGraph, waitingTimeList
0
@anvil.server.callable
def SJFScheduling(processList):
  ganttGraph = []
  waiting_time = [0]
  waitingTimeList = []
  timeLine = 0
  processListSortedByAT = sorted(processList, key=lambda item: item['bt'])
  processQueue = queue.Queue()
  for process in processListSortedByAT:
    processQueue.put(process)

  i = 1
  while(processQueue.empty() == False):
    processReady = processQueue.get()
    ganttGraph.append({'name': processReady['process'], 'time-start': str(timeLine), 'time-end': str(timeLine + processReady['bt'])})
    waiting_time_value = waiting_time[i-1] + processReady['bt'] - processReady['at']
    if waiting_time_value < 0:
          waiting_time_value = 0
    waiting_time.append(waiting_time_value)
    waitingTimeList.append({'name': processReady['name'], 'waiting-time': waiting_time_value})
    i += 1
    timeLine = timeLine + processReady['bt']
  return ganttGraph, waitingTimeList

