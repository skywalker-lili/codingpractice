
# coding: utf-8

# In[17]:


# 17.8 Circus Tower

# Helper function to find the max number of people that is compatible with using the new one
def max_compatible(max_num, heights, i, new_one):
    # Iterate back to find the latest combination that has height lower than new_one
    for j in range(i, -1, -1):
        if heights[j] < new_one[0]:
            break
    
    return max_num[j] + 1, j

def circus_tower(inputs):
    """
    Sort the inputs based on weights/heights.  Adding new inputs from lowest to highest.
    Since they are sorted, the new must be heavier/taller, we only need to worry about the other metric
    We need to make a choice: to use this new one or not:
    1. If the new one's other metric is larger, then we should use it without doubt
    2. If the new one's other metric is smaller, then we need to compare
        2.1 Don't use it: max is the old max
        2.2 Use it: go back find the latest compatible best solution with the new one
        After comparison, we decide whether or not to include the new one
    Keep adding the new ones untill all new ones are done. Then return the max 
    """
    if len(inputs) == 0:
        return 0
    
    inputs = sorted(inputs, key = lambda x: x[1]) # sort by weight, means we need to keep the height
    
    max_num = [None]*(len(inputs)+1) # store the max num each step
    heights = [None]*(len(inputs)+1) # store the height each step
    selected_ids = [[] for _ in range(len(inputs)+1)] # store the ids of people each step
    
    max_num[0], heights[0] = 0,0 # when no one is selected
    
    # Adding new people from lightest to heaviest
    for i in range(len(inputs)):
        new_one = inputs[i]
        
        # If the new one's also higher, just use it
        if new_one[0] > heights[i]:
            max_num[i+1] = max_num[i] + 1
            heights[i+1] = new_one[0]
            selected_ids[i+1] = selected_ids[i] + [i]
        # If new one is shorter, we need to compare
        else:
            max_notUse = max_num[i] # maximum number of people not using new one
            # calculate the compatible solution
            max_use, j = find_maxCompatible(max_num, heights, i, new_one)
            
            if max_use > max_notUse: # use, update max_num and heights
                max_num[i+1] = max_num[i] + 1
                heights[i+1] = new_one[0]
                selected_ids[i+1] = selected_ids[j] + [i]
            
            else: # not using, everything is the same
                max_num[i+1] = max_num[i]
                heights[i+1] = heights[i]
                selected_ids[i+1] = selected_ids[i]
    #print("max_num is {}".format(max_num))
    #print("heights is {}".format(heights))
    selected = [inputs[i] for i in selected_ids[len(inputs)]]
            
    return selected # people selected
    


# In[20]:

# Test
inputs = [(65,100), (70,150), (56,90), (75,190),(60,95), (68,100)]
print(circus_tower(inputs))

