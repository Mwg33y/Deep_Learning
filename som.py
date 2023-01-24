#Self Organizing Maps


#!pip install MiniSom

"""### Importing the libraries"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Importing the dataset"""

dataset = pd.read_csv('Credit_Card_Applications.csv')
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, -1].values

"""## Feature Scaling"""

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
X = sc.fit_transform(X)

"""##Training the SOM"""

from minisom import MiniSom
som = MiniSom(x=10, y=10, input_len= 15, sigma= 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)

"""##Visualizing the results"""
#map customers with similar characteristics together
#the outliers will  be the furthest away from the other nodes.
#The color scale will help identify which group of customers
#are break banking rules (white), and which follow the bank's rules (black)

from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar() #colorscale for rule followers/breakers


markers = ['o', 's'] #[not approved, got approval] :- credit card applications
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()

"""## Finding the frauds"""

mappings = som.win_map(X) #lists of which part of the map customers fall into

#make a list of the rule breakers who are also potential 
#fraudsters using the map
frauds = np.concatenate((mappings[(7,3)], mappings[(7,1)], mappings[(6,2)], mappings[(2,3)]), axis = 0)

frauds = sc.inverse_transform(frauds)#remove scaling from data

"""##Printing the Fraunch Clients"""

print('Fraud Customer IDs')
for i in frauds[:, 0]:
  print(int(i))