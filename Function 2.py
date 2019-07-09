#!/usr/bin/env python
# coding: utf-8

# In[11]:


#introduction to default values in functions.

def describe_pet(pet_name,animal_type='Dog'):
    '''Display Info about Pet'''
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is: {pet_name}.")
    
describe_pet('jimmmy')
describe_pet('tommy','cat')


# In[16]:


#Avoiding Argument errors:
def describe_pet(pet_name,animal_type):
    '''Display Info about Pet'''
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is: {pet_name}.")
    
describe_pet('jimmy','fish')


# In[15]:


# to return a output in a dictionary format:-
def build_person(first_name,last_name):
    '''Returns a dictionary of a person''' #DOC string....!
    person={'first':first_name,'last':last_name}
    return person

musician = build_person('AR','REHMAN')
print(musician)


# In[19]:


#Passing a For loop in a function.............!

def greet_users(names):
    '''print simple greeting to each user in a list'''
    for name in names:
        msg=f"Hello,{name.title()}"
        print(msg)
        
usernames=['selva','priya','sudhir','pankaj','geetha']

greet_users(usernames)


# In[21]:


#Passing an aritary no of arguments...!
def make_pizza(*toppings):
    '''print the list of toppings that have requested'''
    print(toppings)
    
make_pizza('mushroom','tomato','olive')


# In[ ]:




