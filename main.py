#The main driver for everything, maintained for python 3

from classes.bubbleSort import BubbleSort

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
  selection = input()
  os.system('cls')

  test = sortTester()
  if selection == '1':
    sorter = BubbleSort()

  test.test(sorter.sort)
