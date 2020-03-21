#!/usr/bin/env python
# coding: utf-8

# In[1]:


isMLGeek


# In[2]:


isMLGeek = True
if isMLGeek:
    print 'I recommend you to read "DIY Machine Learning Systems for Kaggle Competitions with Python Programming"!'


# In[3]:


10 + 20


# In[4]:


30 - 60.6


# In[5]:


4 * 8.9


# In[6]:


5 / 4


# In[7]:


5.0 / 4


# In[8]:


5 % 4


# In[9]:


2.0 ** 3


# In[10]:


10 < 20


# In[11]:


10 > 20


# In[12]:


30 <= 30.0


# In[13]:


30.0 >= 30.0


# In[14]:


30 == 40


# In[15]:


30 != 40


# In[16]:


t = (1, 'abc', 0.4)
t[0] = 2


# In[17]:


l = [1, 'abc', 0.4]
l[0] = 2
l[0] += 1
l[0]


# In[18]:


l[0] -= 2
l[0]


# In[19]:


True and True


# In[20]:


True and False


# In[21]:


True or False


# In[22]:


False or False


# In[23]:


not True


# In[24]:


l = [1, 'abc', 0.4]
t = (1, 'abc', 0.4)
d = {1:'1', 'abc':0.1, 0.4:80}


# In[25]:


0.4 in l


# In[26]:


1 in t


# In[27]:


'abc' in d


# In[28]:


0.1 in d


# In[29]:


b = True


# In[30]:


if b:
    print "It's True!"
else:
    print "It's False!"


# In[31]:


b = False
c = True

if b:
    print "b is True!"
elif c:
    print "c is True!"
else:
    print "Both are False!"
    


# In[32]:


b = False
c = False
if b:
    print "b is True!"
elif c:
    print "c is True!"
else:
    print "Both are False!"


# In[33]:


d = {1:'1', 'abc':0.1, 0.4:80}
for k in d:
    print k, ":", d[k]


# In[34]:


def foo(x):
    return x ** 2

foo(8.0)


# In[35]:


import math
math.exp(2)


# In[36]:


from math import exp
exp(2)


# In[37]:


from math import exp as ep
ep(2)


# In[ ]:




