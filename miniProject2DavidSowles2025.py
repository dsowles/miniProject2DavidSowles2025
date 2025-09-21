
import numpy as np
import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import faker

myFaker = faker.Faker()

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

  persons = {
    'Name' : ['Bob', 'Bill', 'Joe'],
    'Age' : [55, 43, 22],
    'Eye Color' : ['Blue', 'Brown', 'Hazel']
  }
  #frame1 = pd.DataFrame(persons)

  data = generatePersonDataSet(100)
  #print(data)
  frame1 = pd.DataFrame(data)
  print(frame1)

# Function for generating a set of personal data for a number of individuals.
# The param n defines the number of individuals to put in the set.
# The set of data is returned as a Python dict object.
def generatePersonDataSet(n = None) :
  if (n == None or (type(n) != int) or n < 1) :
    print(f'[ERROR]: bad param, n = {n}')
  
  else :
    personData = { 'Name': [],
                  'Sex': [],
                  'Age': [],
                  'Height (in)': [],
                  'Bodyweight (lb)': [],
                  'Eye Color': [],
                  'Hair Color': [],
                  'Income ($)': [],
                  'Savings ($)': []
                  }
    
    for _ in range(n) :
      person = generatePersonData()

      if person == None:
        print(f'[ERROR]: bad return, person = {person}')
      else :
        personData['Name'].append(person['Name'])
        personData['Sex'].append(person['Sex'])
        personData['Age'].append(person["Age"])
        personData['Height (in)'].append(person['Height (in)'])
        personData['Bodyweight (lb)'].append(person['Bodyweight (lb)'])
        personData['Eye Color'].append(person['Eye Color'])
        personData['Hair Color'].append(person['Hair Color'])
        personData['Income ($)'].append(person['Income ($)'])
        personData['Savings ($)'].append(person['Savings ($)'])

    return personData

# Function for generating random personal data for one person.
def generatePersonData() :
  person = {}

  # Determine sex first.
  person['Sex'] = random.choice(('F', 'M'))

  # Use sex to determine name.
  if person['Sex'] == 'F' :
    person['Name'] = myFaker.name_female()
    person['Bodyweight (lb)'] = random.randint(85, 200)
    person['Height (in)'] = random.randint(50, 74)
  else :
    person['Name'] = myFaker.name_male()
    person['Bodyweight (lb)'] = random.randint(115, 220)
    person['Height (in)'] = random.randint(58, 81)

  person['Age'] = random.randint(15,89)
  person['Eye Color'] = random.choice(('Blue', 'Brown', 'Green', 'Hazel', 'Gray', 'Amber'))
  person['Hair Color'] = random.choice(('Black', 'Brown', 'Dark Brown', 'Light Brown', 'Blonde', 'Red'))
  person['Income ($)'] = random.randint(14_500,350_000)
  person['Savings ($)'] = random.randint(50, 120_000)
  

  return person





main()