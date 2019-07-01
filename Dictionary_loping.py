#!/usr/bin/env python
# coding: utf-8

# In[1]:


#looping throughthe dictionaries...!


# In[4]:


user_0={'username':'sudhirpundir1','first':'sudhir','last':'pundir',
       }

for key,values in user_0.items():
    print(f"\nKey : {key}")
    print(f"\nValues : {values}")


# In[6]:


#only keys to be printed:

for key in user_0.keys():
    print(f"\n Key: {key}")


# In[8]:


#Only values to be printed:

for values in user_0.values():
    print(f"\n value : {values}")


# In[ ]:




