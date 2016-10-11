
# coding: utf-8

# In[104]:


# 16.6 Smallest Difference

# ---- Solution ----
def smallest_diff(a, b):
    # Sort the two arrays and have two pointers to move from both beginnings
    # According to the relative value of two pointers, move one of them each step towards end
    # Once no movement can be done, end the program
    a.sort()
    b.sort()
    pa, pb = 0, 0
    smallest_diff = abs(a[pa] - b[pb])
    smallest_diff_pair = (a[pa], b[pb])
    
    moveable = True
    while moveable:
        diff_aMinusB = a[pa] - b[pb]
        if abs(diff_aMinusB) < smallest_diff:
            smallest_diff = abs(diff_aMinusB)
            smallest_diff_pair = (a[pa], b[pb])
        if diff_aMinusB == 0: 
            return (a[pa], b[pb])
        elif diff_aMinusB < 0:
            pa += 1
        else:
            pb += 1
        
        # Check if the new pa, pb setting is possible
        if pa > len(a)-1 or pb > len(b)-1:
            moveable = False
    
    return smallest_diff_pair


# In[105]:

# Test
for (a, b) in [([1,3,15,11,2],[23,127,235,19,8])]:
    print "smallest diff pair:", smallest_diff(a, b)

