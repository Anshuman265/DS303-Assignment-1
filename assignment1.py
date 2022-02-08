# Importing the important libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# Loading the dataset
df = pd.read_csv("restaurent.csv")
df.head()

# Randomly selecting 50 samples from the dataset
df = df.sample(n=50)

# Plotting food vs price
plt.plot(df['food'],df['price'])
plt.xlabel('Food')
plt.ylabel('Price')
plt.show()

# Plotting decor vs price
plt.plot(df['decor'],df['price'])
plt.xlabel('Decor')
plt.ylabel('Price')
plt.show()


# Plotting service vs price
plt.plot(df['service'],df['price'])
plt.xlabel('Service')
plt.ylabel('Price')
plt.show()