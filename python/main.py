#The main driver for everything, maintained for python 3

from classes.sorters.bubbleSort import BubbleSort
from classes.sorters.mergeSort import MergeSort
from classes.sorters.quickSort import QuickSort

from tests.sortTester import sortTester

#Generic Imports
import cs1graphics as cs1
import os

print ('Please select a subset of algorithms:')
print ('1. Sorting Algorithms')
selection = input()
os.system('cls')

if selection == '1':
  print ('Select sort algorithm:')
  print ('1. Bubble sort')
  print ('2. Merge sort')
  print ('3. Quick sort')
  selection = input()
  os.system('cls')

  test = sortTester()
  if selection == '1':
    sorter = BubbleSort()
  elif selection == '2':
    sorter = MergeSort()
  elif selection == '3':
    sorter = QuickSort()

  test.test(sorter.sort)
