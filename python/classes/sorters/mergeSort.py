class MergeSort:

  def __init__(self):
    pass

  def sort(self, container):
    if len(container) <= 1:
      return container

    midp = len(container)//2
    left = container[0:midp]
    right = container[midp::]

    self.sort(left)
    self.sort(right)

    li, ri = 0, 0
    for i in range(len(container)):
      lv = left[li] if li < len(left) else None
      rv = right[ri] if ri < len(right) else None

      if (lv and rv and lv < rv) or rv is None:
        container[i] = lv
        li += 1
      elif (lv and rv and lv >= rv) or lv is None:
        container[i] = rv
        ri += 1
      else:
        pass

    return container
