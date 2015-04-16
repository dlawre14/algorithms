class BinaryTree:
#Note: I'm choosing to define a binary tree as a set object
# Technically we could define the tree as a node with other nodes

  class Node:
    #Defines a node in our tree
    def __init__(self, data=None, parent=None):
      self._data = data
      self._parent = parent
      self._left = None
      self._right = None

    def getLeft(self): return self._left
    def getRight(self): return self._right
    def getParent(self): return self._parent

    def setLeft(self, c):
      self._left = c

    def setRight(self, c):
      self._right = c

  def __init__(self):
    self._root = None
    self._size = 0

  def getRoot(self): return self._root
  def getSize(self): return self._size

  def insert(self, value):
    if self._root is None:
      self._root = Node(value, None)
    else:
      pass #TODO

if __name__ == '__main__':
  t = BinaryTree()
