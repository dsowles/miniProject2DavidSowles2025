
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import faker

# Check to see if packages are all loaded
'''
print(f'Is matplotlib.pyplot loaded?: {plt}')
print(f'Is pandas loaded? {pd}')
print(f'Is numpy loaded?: {np}')
print(f'Is faker loaded?: {faker}')
print(f'Is OS module loaded?: {os}')
'''

def main():
  print("Hello World!")

  myFaker = faker.Faker()

  persons = {
    'Name' : ['Bob', 'Bill', 'Joe'],
    'Age' : [55, 43, 22],
    'Eye Color' : ['Blue', 'Brown', 'Hazel']
  }

  frame1 = pd.DataFrame(persons)

  print(frame1)
  
  frame1.plot(kind='scatter', x='Name', y='Age')
  plt.show()



main()