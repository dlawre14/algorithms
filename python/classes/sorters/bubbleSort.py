class BubbleSort:

  def __init__(self):
    pass

  def sort(self, container):
    if len(container) <= 1:
      return container

    swapped = True
    while swapped:
      swapped = False
      for i in range(1, len(container)):
        if container[i-1] > container[i]:
          temp = container[i]
          container[i] = container[i-1]
          container[i-1] = temp
          swapped = True
    return container
