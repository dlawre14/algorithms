import unittest

class sortTester:

  def __init__(self):
    self._cases = [
      [1,3,6,2,6,2,5,3,2,1,6]
    ]

  #sortType should be a function
  def test(self, sortType):
      for case in self._cases:
        print (sortType(case))
