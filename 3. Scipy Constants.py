#!/usr/bin/env python
# coding: utf-8

# # SciPy Constants
# 

# Constants in SciPy
# As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.
# 
# These constants can be helpful when you are working with Data Science.

# PI is an example of a scientific constant.

# In[7]:


#Print the constant value of pi
from scipy import constants
print(constants.pi)


# # Constant units
# All list of all units under the constants module can be seen using the dir() function

# In[8]:


from scipy import constants
print(dir(constants))


# # Unit Categories
# The units are placed under these categories:
# 
# Metric,
# Binary,
# Mass,
# Angle,
# Time,
# Length,
# Pressure,
# Volume,
# Speed,
# Temperature,
# Energy,
# Power,
# Force

# # Metric (SI) Prefixes:
# Return the specified unit in meter (e.g. centi returns 0.01)

# In[9]:


from scipy import constants

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21


# # Binary Prefixes:
# Return the specified unit in bytes (e.g. kibi returns 1024)

# In[13]:



print(constants.kibi)    
print(constants.mebi)    
print(constants.gibi)    
print(constants.tebi)    
print(constants.pebi)    
print(constants.exbi)    
print(constants.zebi)    
print(constants.yobi) 


# # Mass:
# Return the specified unit in kg (e.g. gram returns 0.001)

# In[12]:


from scipy import constants

print(constants.gram)        
print(constants.metric_ton)  
print(constants.grain)       
print(constants.lb)          
print(constants.pound)       
print(constants.oz)          
print(constants.ounce)       
print(constants.stone)       
print(constants.long_ton)    
print(constants.short_ton)   
print(constants.troy_ounce)  
print(constants.troy_pound)  
print(constants.carat)       
print(constants.atomic_mass) 
print(constants.m_u)         
print(constants.u)           


# # Angle:
# Return the specified unit in radians (e.g. degree returns 0.017453292519943295)

# In[14]:


from scipy import constants

print(constants.degree)     
print(constants.arcmin)     
print(constants.arcminute)  
print(constants.arcsec)     
print(constants.arcsecond) 


# # Time:
# Return the specified unit in seconds (e.g. hour returns 3600.0)

# In[16]:


from scipy import constants

print(constants.minute)      
print(constants.hour)        
print(constants.day)         
print(constants.week)        
print(constants.year)        
print(constants.Julian_year) 


# # Length:
# Return the specified unit in meters (e.g. nautical_mile returns 1852.0)

# In[17]:


from scipy import constants

print(constants.inch)              
print(constants.foot)              
print(constants.yard)              
print(constants.mile)              
print(constants.mil)               
print(constants.pt)                
print(constants.point)             
print(constants.survey_foot)       
print(constants.survey_mile)       
print(constants.nautical_mile)     
print(constants.fermi)             
print(constants.angstrom)          
print(constants.micron)            
print(constants.au)                
print(constants.astronomical_unit) 
print(constants.light_year)        
print(constants.parsec)  


# # Pressure:
# Return the specified unit in pascals (e.g. psi returns 6894.757293168361)

# In[19]:


from scipy import constants

print(constants.atm)         
print(constants.atmosphere)  
print(constants.bar)         
print(constants.torr)        
print(constants.mmHg)        
print(constants.psi)         


# # Area:
# Return the specified unit in square meters(e.g. hectare returns 10000.0)

# In[21]:


from scipy import constants

print(constants.hectare) 
print(constants.acre)    


# # Volume:
# Return the specified unit in cubic meters (e.g. liter returns 0.001)

# In[23]:


from scipy import constants
print(constants.liter)            
print(constants.litre)            
print(constants.gallon)           
print(constants.gallon_US)        
print(constants.gallon_imp)       
print(constants.fluid_ounce)      
print(constants.fluid_ounce_US)   
print(constants.fluid_ounce_imp)  
print(constants.barrel)           
print(constants.bbl)              


# # Speed:
# Return the specified unit in meters per second (e.g. speed_of_sound returns 340.5)

# In[24]:


from scipy import constants

print(constants.kmh)            #0.2777777777777778
print(constants.mph)            #0.44703999999999994
print(constants.mach)           #340.5
print(constants.speed_of_sound) #340.5
print(constants.knot)           #0.5144444444444445


# # Temperature:
# Return the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)

# In[25]:


from scipy import constants

print(constants.zero_Celsius)      
print(constants.degree_Fahrenheit) 


# # Energy:
# Return the specified unit in joules (e.g. calorie returns 4.184

# In[26]:


from scipy import constants

print(constants.eV)            
print(constants.electron_volt) 
print(constants.calorie)       
print(constants.calorie_th)    
print(constants.calorie_IT)    
print(constants.erg)           
print(constants.Btu)           
print(constants.Btu_IT)        
print(constants.Btu_th)        
print(constants.ton_TNT)       


# # Power:
# Return the specified unit in watts (e.g. horsepower returns 745.6998715822701)

# In[28]:


from scipy import constants

print(constants.hp)         
print(constants.horsepower) 


# # Force:
# Return the specified unit in newton (e.g. kilogram_force returns 9.80665)

# In[29]:


from scipy import constants

print(constants.dyn)             #1e-05
print(constants.dyne)            #1e-05
print(constants.lbf)             #4.4482216152605
print(constants.pound_force)     #4.4482216152605
print(constants.kgf)             #9.80665
print(constants.kilogram_force)  #9.80665

