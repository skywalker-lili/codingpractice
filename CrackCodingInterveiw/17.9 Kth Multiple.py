
# coding: utf-8

# In[17]:


# 17.9 Kth Multiple
from collections import deque

def kth_multiple(k):
    """
    Maintain 3 candidate lists. Each time picking a number, pick the smallest form the candidates list and
    add new candidates that are spawned by the new picked number
    """
    if k<0: return -1
    val = 0
    q3, q5, q7 =  deque([1]), deque([]), deque([])
    
    for i in range(k):
        if i == 0:
            val = q3[0]
        else:
            val = min(q3[0], min(q5[0], q7[0]))
        
        if val == q3[0]:
            q3.popleft()
            q3.append(val*3)
            q5.append(val*5)
        elif val == q5[0]:
            q5.popleft()
            q5.append(val*5)
        else:
            q7.popleft()
        q7.append(val*7)
    
    return val


# In[20]:

# Test
for k in [1,2,3,4,5, 6,7]:
    print(kth_multiple(k))

