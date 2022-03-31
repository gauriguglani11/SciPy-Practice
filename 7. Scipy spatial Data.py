#!/usr/bin/env python
# coding: utf-8

# # Scipy Spatial Data

# # Working with spatial Data

# 1. spatial data refers to data that is represented in a geometric space
# eg: we deal with spatial data problems on many tasks
# 
# 2. finding if a point is inside a boundary or not
# eg: scipy provides us with the module scipy.spatial, which has functions for working with spatial data

# # Triangulation

# 1. A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon
# 2. A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.
# 
# 3. One method to generate these triangulations through points is the Delaunay() Triangulation.

# In[2]:


import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1]
])
simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()


# Note: The simplices property creates a generalization of the triangle notation.

# # Convex Hull
# A convex hull is the smallest polygon that covers all of the given points.
# 
# Use the ConvexHull() method to create a Convex Hull.

# In[3]:


import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()


# # KD Trees
# KDTrees are a datastructure optimized for nearest neighbor queries.
# 
# E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.
# 
# The KDTree() method returns a KDTree object.
# 
# The query() method returns the distance to the nearest neighbor and the location of the neighbors.

# In[1]:


# Find the nearest neigbour to point(1,1)
from scipy.spatial import KDTree
points = [(1,-1),(2,3),(-2,3),(2,-3)]
kdtree = KDTree(points)
neighbour = kdtree.query((1,1))
print(neighbour)


# # Distance Matrix
# There are many Distance Metrics used to find various types of distances between two points in data science, Euclidean distsance, cosine distsance etc.
# 
# The distance between two vectors may not only be the length of straight line between them, it can also be the angle between them from origin, or number of unit steps required etc.
# 
# Many of the Machine Learning algorithm's performance depends greatly on distance metrices. E.g. "K Nearest Neighbors", or "K Means" etc.

# In[2]:


# EUCLIDEAN DISTEANCE
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

neighbour = euclidean(p1, p2)

print(neighbour)


# ## Cityblock Distance (Manhattan Distance)
# Is the distance computed using 4 degrees of movement.
# 
# E.g. we can only move: up, down, right, or left, not diagonally.

# In[3]:


from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)

res = cityblock(p1, p2)

print(res)


# ## Cosine Distance
# Is the value of cosine angle between the two points A and B.

# In[4]:


from scipy.spatial.distance import cosine

p1 = (1, 0)
p2 = (10, 2)

res = cosine(p1, p2)

print(res)


# # Hamming Distance
# Is the proportion of bits where two bits are difference.
# 
# It's a way to measure distance for binary sequences.
# 

# In[5]:


from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(res)

