import unittest
import statistics
import math

class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    assert math.isnan(computedStats["avg"])
    assert math.isnan(computedStats["max"])
    assert math.isnan(computedStats["min"])
  
  def test_raise_alerts_when_max_above_threshold(self):
    maxThreshold = 10.5
    array = [22.6, 12.5, 3.7]
    emailAlert, ledAlert = statistics.checkAndAlert(maxThreshold, array)
    for i in range(len(array)):
      if array[i] > maxThreshold:        
        self.assertTrue(emailAlert[i])
        self.assertTrue(ledAlert[i])
      else:
        self.assertFalse(emailAlert[i])
        self.assertFalse(ledAlert[i])
        
if __name__ == "__main__":
  unittest.main()
