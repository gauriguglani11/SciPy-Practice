#!/usr/bin/env python
# coding: utf-8

# # Scipy Installation guide

# If you have Python and PIP already installed on a system, then installation of SciPy is very easy.
# 
# Install it using this command:
# 
# C:\Users\Your Name>pip install scipy

# If the above command fails, you can use a python distribution that already has scipy installed like Anaconda, spyder

# # Import Scipy

# once scipy is installed, import the scipy module(s) you want to use in your applications by adding the 
# from scipyimport module statement:

# In[3]:


from scipy import constants


# Now we have imported the constants module from SciPy, and the application is ready to use it:
# 
# ## Example
# How many cubic meters are in one liter:

# In[5]:


from scipy import constants

print(constants.liter)


# constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.

# # Checking scipy version

# In[6]:


import scipy

print(scipy.__version__)


# ### two underscore characters are used in __version__.
