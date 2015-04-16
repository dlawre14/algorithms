class QuickSort:

  def __init__(self):
    pass

  def sort(self, container):
    #Note: this is inplace and so does not 'return' a container
    self._sort(container, 0, len(container)-1)
    return container

  def _sort(self, container, low, high):
    if (high > low):
      p = self._partition(container, low, high)
      self._sort(container, low, p-1)
      self._sort(container, p+1, high)

  def _partition(self, container, low, high):
    p = container[low]
    i = low
    j = high+1
    while i < j:
      i+=1
      while i < high and container[i] < p:
        i+=1

      j-=1
      while j > low and container[j] > p:
        j-=1
      if (i < j):
        temp = container[i]
        container[i] = container[j]
        container[j] = temp

    if j == low:
      return j

    temp = container[low]
    container[low] = container[j]
    container[j] = temp

    return j
