
# coding: utf-8

# In[144]:


# 8.4 Power Set

# ---- Solution 1: non-recursion ----
def power_set1(s):
    res = [set([])]
    for item in s:
        current_len = len(res)
        for i in range(current_len): # for each element in the existing result
            new_set = res[i].copy() # create a copy of existing set
            new_set.add(item) # add the item into copy
            res.append(new_set) # append the updated copy of new set
    
    return res


# In[152]:

# ---- Solution 2: recursion ----
def power_set2(s):
    s = list(s)
    
    # special case
    if len(s) == 0:
        return [set([])]
    
    # base case
    elif len(s) == 1:
        return [set([]), {s[0]}]
    
    # recursive case
    else:
        last_item = s.pop()
        previous = power_set2(s)
        temp = [existing_set.copy() for existing_set in previous] # make a copy of previous result
        # update the copy by adding the last item into it
        for existing_set in temp:
            existing_set.add(last_item)
        previous.extend(temp) # extend the previous result with updated copies

        return previous


# In[153]:

# Test
print power_set1({1,2,3})
print power_set2({1,2,3})

