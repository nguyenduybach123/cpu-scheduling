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

  return ganttGraph

@anvil.server.callable
def FCFSScheduling(processList):
  ganttGraph = []
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

  return ganttGraph
