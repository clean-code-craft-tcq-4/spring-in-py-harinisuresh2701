
def calculateStats(numbers):
  if len(numbers)>0:
    maximum = max(numbers)
    minimum = min(numbers)
    total = sum(numbers)
    average = total/len(numbers)
    x = {"avg":average,"min":minimum,"max":maximum}
  else:
    y = float("NaN")
    x = {"avg":y,"min":y,"max":y} 
  return x

def checkAndAlert(maxThreshold, number):
  emailAlert = []
  ledAlert = []
  for i in number:
    if i > maxThreshold:
      emailAlert.append(True)
      ledAlert.append(True)
    else:
      emailAlert.append(False)
      ledAlert.append(False)
  return emailAlert , ledAlert
