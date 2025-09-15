
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import faker
import os



print("Hello World!")

fake = faker.Faker()

'''
print(fake.state())
print(fake.pyfloat(max_value=5000, min_value=0, right_digits=2))

data1 = [
             { "first_name": fake.first_name(),
               "last_name":  fake.last_name(),
               "address": fake.address(),
               "email": fake.email(),
               "age": np.random.randint(18, 80)
             }
             for i in range(1000)
         ]

plot1 = pd.DataFrame(data = data1)
plot1.plot()

plt.show()
'''

'''

data2 = [
             { "first_name": fake.first_name(),
               "last_name":  fake.last_name(),
               "state": fake.state(),
               "email": fake.email(),
               "age": np.random.randint(18, 80),
               "traffic tickets" : np.random.randint(0,12)
             }
             for i in range(1000)
         ]

plot2 = pd.DataFrame(data = data2)

plot2["age"].plot()
plt.show()

'''



data3 = { "Name" : [] , "State" : [], "Cash" : [] }

for i in range(10) :
    data3["Name"].append(fake.name())
    data3["State"].append(fake.state())
    data3["Cash"].append(np.random.randint(0, 20000))

df = pd.DataFrame(data = data3)

print(list(df["State"]))
print(list(df["State"].keys()))

plt.plot(list(df["State"]), list(df["Cash"]))
plt.show()

print("Stuff")


'''
print(df["State"].keys())
plot3.set_xticks(df["State"].keys, df["State"].values)

plt.show()

'''

