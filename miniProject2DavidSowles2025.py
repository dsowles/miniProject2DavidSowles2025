
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
  print("*****************")
  print("* Pandas Charts *")
  print("*****************\n")

  menu()



# App's main selection menu.
def menu() :
  print("[0]: Insurance Cost Charts\n"
        "[1]: Personal Info Charts\n"
        "[Q]: Quit App")

  n = input("->")
  
  # Using basic recursion loop for menu functionality,
  # don't ask too many chart function calls!!!!!
  match n:
    case '0':
      print("\n")
      insuranceCostCharts()
      menu()
      
    case '1':
      personalCharts()
      print("\n")
      menu()
      
    case 'q' | 'Q':
      print("END.")

    case _:
      print("Bad input.\n")
      menu()

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
    person['Bodyweight (lb)'] = random.choice([80,90,100,110,120,130,140,150,160,170,180,190,200]) #random.randint(85, 200)
    person['Height (in)'] = random.choice([50,55,60,65,70,75]) #random.randint(50, 74)
  else :
    person['Name'] = myFaker.name_male()
    person['Bodyweight (lb)'] = random.choice([110,120,130,140,150,160,170,180,190,200,200]) #random.randint(115, 220)
    person['Height (in)'] = random.choice([50,55,60,65,70,75,80,85,90]) #random.randint(58, 81)

  person['Age'] = random.choice([15,17,20,23,24,25,26,27,28,29,30,33,35,37, 43, 50, 55, 62, 67, 71, 83, 88]) #random.randint(15,89)
  person['Eye Color'] = random.choice(('Blue', 'Brown', 'Green', 'Hazel', 'Gray', 'Amber'))
  person['Hair Color'] = random.choice(('Black', 'Brown', 'Dark Brown', 'Light Brown', 'Blonde', 'Red'))
  person['Income ($)'] = random.choice([14_500, 14_900, 25_000, 30_000, 35_000, 37_000, 40_000, 45_000, 150_000, 155_000, 175_000, 250_000, 350_000]) #random.randint(14_500,350_000)
  person['Savings ($)'] = random.choice([50, 150, 1250, 3500, 5500, 12500, 25_000, 123_000]) #random.randint(50, 120_000)
  

  return person

# Example function using the above two functions for constructing
# A few charts for a set of personal data.
def personalCharts() :
  data = generatePersonDataSet(300)
  frame = pd.DataFrame(data)

  # Show what the basic plot would look like.
  frame.plot()
  plt.show()
  # Show what using basic subplots would look like.
  frame.plot(subplots=True)
  plt.show()

  # Show something more elaborate
  fig, axes = plt.subplots(nrows = 2, ncols= 2)
  frame.plot(subplots=True, ax=axes[0,0], kind='scatter', x='Age', y='Income ($)')
  frame.plot(subplots=True, ax=axes[0,1], kind='scatter', x='Age', y='Savings ($)')

  eyeColors = frame[['Eye Color']].value_counts().plot(subplots=True, ax=axes[1,0], kind='bar')
  hairColors = frame[['Hair Color']].value_counts().plot(subplots=True, ax=axes[1,1], kind='box')
  plt.show()

  young = frame.loc[frame['Age'] < 30, ['Age', 'Sex', 'Bodyweight (lb)', 'Eye Color']]
  # Show basic chart for subset.
  young.plot()
  plt.show()

  fig, axes = plt.subplots(nrows=1,ncols=2)
  young.plot(subplots=True, ax=axes[0], kind="scatter", x = "Age", y = "Bodyweight (lb)")
  young[['Eye Color']].value_counts().plot(subplots=True, ax=axes[1], kind='bar')

  plt.show()

def insuranceCostCharts() :
  frame = pd.read_csv(r'miniProject2DavidSowles2025\data\insurance.csv')

  # Show basic plot
  fig, axes = plt.subplots(nrows=1, ncols=2)
  frame.plot(ax=axes[0], kind='scatter', x='age', y='charges')
  frame[['age']].value_counts().plot(ax=axes[1], kind='bar')
  plt.show()

  highCharges = frame.loc[frame['charges'] > 10_000]
  fig,axes = plt.subplots(nrows=2, ncols=2)
  highCharges.plot(ax=axes[0,0], kind='scatter', x='age', y='charges')
  highCharges[['age']].value_counts(sort=False).plot(ax=axes[0,1], kind='bar')
  highCharges.plot(ax=axes[1,0], kind='scatter', x='bmi', y='charges')
  highCharges[['smoker']].value_counts(sort=False).plot(ax=axes[1,1], kind='bar')
  plt.show()


main()