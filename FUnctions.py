#!/usr/bin/env python
# coding: utf-8

# In[1]:


def greet_user():
    print('hello...!')
    
greet_user()


# In[6]:


#INtroduction to positional arguments:-
def describe_pet(animal_type,animal_name):
    """Display info about a pet...!"""
    print(f'\n I have a animal type: {animal_type}')
    print(f"\n My {animal_type}'s name is {animal_name}")
          
describe_pet('Dog','Tommy')


# In[9]:


#Intro to Keyword arguments
def describe_pet(animal_type,animal_name):
    """Display info about a pet...!"""
    print(f'\n I have a animal type: {animal_type}')
    print(f"\n My {animal_type}'s name is {animal_name}")

describe_pet(animal_name='jimmy',animal_type='dog')


# In[12]:


#Intro to returning a value from a function:-
def get_formatted_name(first_name,last_name):
    '''Full Name, Neatly formatted'''
    full_name=f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('sudhir','pundir')
print(musician)


# In[ ]:




