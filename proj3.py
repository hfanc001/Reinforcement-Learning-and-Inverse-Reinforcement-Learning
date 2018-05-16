
# coding: utf-8

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mdptoolbox


# In[4]:


a=numpy.zeros(shape=(10,10))
print(a)


# In[17]:


a[9,9]=10
print(a)


# In[8]:


b=numpy.zeros(shape=(10,10))
print(b)


# In[18]:


b[1,4]=b[1,5]=b[1,6]=-100
b[2,4]=b[3,4]=b[4,4]=b[5,4]=b[6,4]=-100
b[2,6]=b[3,6]=-100
b[3,7]=b[3,8]=-100
b[4,8]=b[5,8]=b[6,8]=b[7,8]=-100
b[7,7]=b[7,6]=-100
b[8,6]=-100
b[9,9]=10
print(b)


# #
# Question 1

# In[47]:



matplotlib.pyplot.pcolor(a)
plt.gca().invert_yaxis()


# In[46]:


sns.heatmap(a)


# In[44]:


matplotlib.pyplot.pcolor(b)
plt.gca().invert_yaxis()


# In[45]:


sns.heatmap(b)


# #
# Question 2

# In[61]:


#state space
ss=numpy.zeros(shape=(10,10))
#print(ss)
for i in range(0,10):
    ss[i,0]=i
    ss[i,1]=i+10
    ss[i,2]=i+20
    ss[i,3]=i+30
    ss[i,4]=i+40
    ss[i,5]=i+50
    ss[i,6]=i+60
    ss[i,7]=i+70
    ss[i,8]=i+80
    ss[i,9]=i+90
print(ss)


# In[67]:


#action set
def action(self,command):
    if command=="Move Right":
        
    elif command=="Move Left":
        
    elif command =="Move Top":
        
    elif command =="Move Down":
        
    else:
        
        


# In[62]:


#Transition Probilitiy 
w=0.1
def tp(self,state,action):
    if action ==None:
        return [0.0,state]
    else:
        return [(1-w+w/4,self.go(state,action)),
                (w/4,self.go(state,turn_left(action))),
                (w/4,self.go(state,turn_right(action))),
                (w/4,self.go(state,turn_bottom(action)))]
    

