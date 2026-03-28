<<<<<<< HEAD
import os
import re

'''clear function'''
def clearTheConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

alert = "Python calculator - Rafał Michałuszek 2016\n"
programOn = 1

while programOn:
    clearTheConsole()
    print(alert)
    print('Type your mathematical operation:')

    operation = input()

    if operation is '':
        alert = "--Please do not write a text--"
        continue

    if re.search('[a-zA-Z]', operation):
        alert = "--Please do not write a text--"
        continue

    result = 0

    operation = 'result = '+operation
    exec(operation)

    operation = ''
    alert = "\n--The result is " + str(result) + "--"
=======
from math import *

while True:
  try:
    print(eval(input('Input a math problem: ')))

  except:
    print('Sorry?')
>>>>>>> f15c853 (first commit)
