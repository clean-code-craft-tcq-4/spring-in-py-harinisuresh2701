
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
