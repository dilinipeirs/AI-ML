# -*- coding: utf-8 -*-
"""Copy of Visualizing the IRIS dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19KXdmm9U97chGtwLOR6dNf1HvHVOFzT7
"""

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()

"""Building a dataframe"""

df = pd.DataFrame(iris.data, columns=iris.feature_names)
#Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns)
#https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

df['target']=iris.target
print(iris.target_names)
df['species'] = df['target'].map({0:iris.target_names[0],1:iris.target_names[1],
     2:iris.target_names[2]})
df.head()

X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(1, figsize=(7, 4))

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.rainbow)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
# plt.xticks(())
# plt.yticks(())
plt.show()



X = iris.data[:, :4]  # we only take the first two features.
Y = iris.target

x_min, x_max = X[:, 2].min() - .5, X[:, 2].max() + .5
y_min, y_max = X[:, 3].min() - .5, X[:, 3].max() + .5

plt.figure(2, figsize=(7, 4))

# Plot the training points
plt.scatter(X[:, 2], X[:, 3], c=Y, cmap=plt.cm.rainbow)
plt.xlabel('Petal length')
plt.ylabel('Petal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
# plt.xticks(())
# plt.yticks(())
plt.show()


X = iris.data[:, :4]  # we only take the first two features.
Y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 3].min() - .5, X[:, 3].max() + .5

plt.figure(3, figsize=(7, 4))

# Plot the training points
plt.scatter(X[:, 0], X[:, 3], c=Y, cmap=plt.cm.rainbow)
plt.xlabel('Sepal length')
plt.ylabel('Petal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
# plt.xticks(())
# plt.yticks(())
plt.show()
