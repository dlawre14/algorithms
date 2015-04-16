class Queue:
  #Note: this queue is list based

  def __init__(self):
    self._content = []

  def push(self, value):
    self._content.append(value)

  def pop(self):
    if (self.isEmpty()):
      raise Exception('Can not pop an empty queue')

    return self._content.pop(0)

  def getSize(self):
    return len(self._content)

  def isEmpty(self):
    return self.getSize() == 0

if __name__ == '__main__':

  q = Queue()
  q.push(1)
  q.push(3)
  q.push(4)
  print (q.getSize())
  print (q.isEmpty())
  print (q.pop())
  print (q.pop())
  print (q.pop())
