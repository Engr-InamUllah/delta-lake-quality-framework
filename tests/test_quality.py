import unittest
from src.quality import completeness,uniqueness,quarantine
class QualityTest(unittest.TestCase):
 def test_rules(self):
  rows=[{"id":1,"name":"A"},{"id":1,"name":""}]
  self.assertFalse(completeness(rows,"name").passed);self.assertFalse(uniqueness(rows,"id").passed)
 def test_quarantine(self):self.assertEqual(len(quarantine([{"v":1},{"v":-1}],lambda r:r["v"]>=0)[1]),1)
if __name__=="__main__":unittest.main()