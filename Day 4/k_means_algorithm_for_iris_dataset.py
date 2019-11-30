# -*- coding: utf-8 -*-
"""K Means Algorithm for iris dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TkrGkl706aJI2TFoLmYSOnwbWxha1Shj
"""

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Loading dataset
iris_df = datasets.load_iris()

#features
print(iris_df.feature_names)

#target names
print(iris_df.target_names)
#target values
print(iris_df.target)

#dataset slicing
x_axis = iris_df.data[:,0] # Sepal length
y_axis = iris_df.data[:,2] # sepal width

plt.scatter(x_axis,y_axis,c=iris_df.target,cmap=plt.cm.rainbow)

model = KMeans(n_clusters=5)

model.fit(iris_df.data)

all_predictions = model.predict(iris_df.data)

print(all_predictions)

plt.scatter(x_axis,y_axis,c=all_predictions,cmap=plt.cm.rainbow)