# -*- coding: utf-8 -*-
"""Support Vector Machines.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19fqaI4S5TGjmByme06ulCJRmCXq7Iw-6
"""

import numpy as np
import cvxopt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

X, y = make_blobs(n_samples=500, centers=2,
                random_state=0, cluster_std=0.60)
#make blobs is another sample database is scikit learn

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='winter')

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33)

classifier = LinearSVC(random_state = 1)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

classifier.score(X_test, y_test)

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='winter')
plt.show()

X, y = make_blobs(n_samples=500, centers=3,
                  random_state=0, cluster_std=0.60)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='winter')

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33)

classifier = LinearSVC(random_state = 1)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

classifier.score(X_test, y_test)

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='winter')
plt.show()
