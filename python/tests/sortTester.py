import unittest

class sortTester:

  def __init__(self):
    self._cases = [
      [],
      [1],
      [1,1],
      [2,1],
      [2,1,2],
      [3,3,2],
      [1,2,3,4],
      [2,4,1,3],
      [7,-3,4,-2,-3],
      ['cat','dog','ape','fish']
    ]

    self._answers = [
      [],
      [1],
      [1,1],
      [1,2],
      [1,2,2],
      [2,3,3],
      [1,2,3,4],
      [1,2,3,4],
      [-3,-3,-2,4,7],
      ['ape', 'cat', 'dog', 'fish']
    ]

  #sortType should be a function
  def test(self, sortType):
      for i in range(len(self._cases)):
        out = sortType(self._cases[i])
        try:
          assert(out == self._answers[i])
        except:
          print ('Sorting case: ' + str(self._cases[i]) + ' failed.')
          print ('Output: ' + str(out))
          print ('Expected output: ' + str(self._answers[i]))
