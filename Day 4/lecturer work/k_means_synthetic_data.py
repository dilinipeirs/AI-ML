# -*- coding: utf-8 -*-
"""k-means synthetic data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1od0-EV-_0cWYh3ZZdnVPDR64P_JujbQ5
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Create 5 blobs of 2,000 random data
n_samples = 2000
random_state = 42
X, y = make_blobs(n_samples=n_samples, 
                  random_state=random_state, 
                  centers=5)

plt.scatter(X[:, 0], X[:, 1], c =y, s=3)
plt.title(f"No Clusters Assigned")

y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=5)
plt.title(f"Number of Clusters: 2")

y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=5)
plt.title(f"Number of Clusters: 3")