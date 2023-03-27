#!/usr/bin/env python
# coding: utf-8

# # SENG 207 PROJECT
# ### ELVIS FORDJOUR ADJEI - 10975102

# In[1]:


import pandas as pd
data = pd.read_csv('data.csv')
data


# In[2]:


data.info()


# In[3]:


data=data.rename(columns={'fixed acidity':'fixed_acidity','volatile acidity':'volatile_acidity','citric acid':'citric_acid','residual sugar':'residual_sugar','free sulfur dioxide':'free_sulfur_dioxide','total sulfur dioxide':'total_sulfur_dioxide'})
data


# In[4]:


data.describe()


# # FINDING THE MEAN OF THE VARIOUS PROPERTIES

# In[5]:


mean_fi=data.fixed_acidity.mean()
mean_vo=data.volatile_acidity.mean()
mean_ci=data.citric_acid.mean()
mean_re=data.residual_sugar.mean()
mean_ch=data.chlorides.mean()
mean_fr=data.free_sulfur_dioxide.mean()
mean_to=data.total_sulfur_dioxide.mean()
mean_de=data.density.mean()
mean_p=data.pH.mean()
mean_su=data.sulphates.mean()
mean_al=data.alcohol.mean()
mean_qu=data.quality.mean()

print(f'fixed_acidity: {mean_fi}')
print(f'volatile_acidity: {mean_vo}')
print(f'citric_acid: {mean_ci}')
print(f'residual_sugar: {mean_re}')
print(f'chlorides: {mean_ch}')
print(f'free_sulfur_dioxide: {mean_fr}')
print(f'total_sulfur_dioxide: {mean_to}')
print(f'density: {mean_de}')
print(f'pH: {mean_p}')
print(f'sulphates: {mean_su}')
print(f'alcohol: {mean_al}')
print(f'quality: {mean_qu}')





# # FINDING THE MODE OF THE VARIOUS PROPERTIES

# In[6]:


mode_fi=data.fixed_acidity.mode()
mode_vo=data.volatile_acidity.mode()
mode_ci=data.citric_acid.mode()
mode_re=data.residual_sugar.mode()
mode_ch=data.chlorides.mode()
mode_fr=data.free_sulfur_dioxide.mode()
mode_to=data.total_sulfur_dioxide.mode()
mode_de=data.density.mode()
mode_p=data.pH.mode()
mode_su=data.sulphates.mode()
mode_al=data.alcohol.mode()
mode_qu=data.quality.mode()

print(f'fixed_acidity: {mode_fi}')
print(f'volatile_acidity: {mode_vo}')
print(f'citric_acid: {mode_ci}')
print(f'residual_sugar: {mode_re}')
print(f'chlorides: {mode_ch}')
print(f'free_sulfur_dioxide: {mode_fr}')
print(f'total_sulfur_dioxide: {mode_to}')
print(f'density: {mode_de}')
print(f'pH: {mode_p}')
print(f'sulphates: {mode_su}')
print(f'alcohol: {mode_al}')
print(f'quality: {mode_qu}')


# # FINDING THE MEDIAN OF THE VARIOUS PROPERTIES

# In[7]:


median_fi=data.fixed_acidity.median()
median_vo=data.volatile_acidity.median()
median_ci=data.citric_acid.median()
median_re=data.residual_sugar.median()
median_ch=data.chlorides.median()
median_fr=data.free_sulfur_dioxide.median()
median_to=data.total_sulfur_dioxide.median()
median_de=data.density.median()
median_p=data.pH.median()
median_su=data.sulphates.median()
median_al=data.alcohol.median()
median_qu=data.quality.median()

print(f'fixed_acidity: {median_fi}')
print(f'volatile_acidity: {median_vo}')
print(f'citric_acid: {median_ci}')
print(f'residual_sugar: {median_re}')
print(f'chlorides: {median_ch}')
print(f'free_sulfur_dioxide: {median_fr}')
print(f'total_sulfur_dioxide: {median_to}')
print(f'density: {median_de}')
print(f'pH: {median_p}')
print(f'sulphates: {median_su}')
print(f'alcohol: {median_al}')
print(f'quality: {median_qu}')


# In[8]:


data.describe()


# In[9]:


import ydata_profiling
profile=ydata_profiling.ProfileReport(data)
profile


# In[ ]:





# In[ ]:




