#!/usr/bin/env python
# coding: utf-8

# In[5]:


greet = lambda name : print(f"Good Morning {name}")


# In[7]:


greet("MOK")


# In[9]:


avg = (lambda num1, num2, num3: (num1 + num2 + num3) / 3)
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))
average = avg(num1, num2, num3)
print('The average of numbers = %0.2f' % average)


# In[13]:


product = lambda x, y, z: x * y * z
result = product(2, 3, 4)
print("The product of the numbers is:", result)


# In[15]:


even  = lambda L : [x for x in L if x%2 == 0]


# In[17]:


my_list = [100,3,9,38,43,56,20]
even(my_list)


# In[19]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum /counter
    return mean


# In[21]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[23]:


product(2,4,9)


# In[ ]:




