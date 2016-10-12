
# coding: utf-8

# In[26]:


# 17.5 Letters and Numbers

# ---- Solution ----
def l_and_n(array):
    # First realize that the numbers and character's values doesn't matter
    # I only care about their identity
    
    # Then realize that order doesn't matter, as long as in an array, they have the same amount of counts
    
    # Third, it's natural to use (accumulated property of array until j) - (accum. property of array until i) 
    # as a substituion of (accum. property of array from i to j)
    
    # Therefore, we can create a array to record the accumulated amounts of numbers and characters until i
    # Then we can calculate the different between the two numbers at each i
    # Now, assume array[i, j+1] has the same amount of numbers and characters, the dif[i] should equal to dif[j]
    # So the question finally just becomes how to find the longest ditance between two numbers in an array
    
    def is_num(s):
        try:
            int(s)
            return True
        except:
            return False
    
    # Build the difference of accumulated number of character and of numbers
    # at each index
    acum_char = 0
    acum_num = 0
    dif = [None] * (len(array)+1)
    dif[0] = 0 # indicating when none charactera are scanned, there is no dif
    for i in xrange(1, len(array)+1): 
        if is_num(array[i-1]): # Loop over the array
            acum_num += 1
        else:
            acum_char += 1
        
        dif[i] = acum_char - acum_num
    
    # Loop over the dif, find the longest distance
    # Use a dictionary to keep the index of a dif value when it's first seen
    # Then in the later if the same value is observed, calculate the distance
    # update the maximum distance at the same time
    left = 0
    right = 0
    max_dis = right - left
    first_seen_i = {}
    for i in xrange(len(dif)):
        val = dif[i]
        if val not in first_seen_i:
            first_seen_i[val] = i
        else:
            dis = i - first_seen_i[val]
            # Update the maximum distance
            if dis > max_dis:
                max_dis = dis
                left = first_seen_i[val]
                right = i
    
    # since left and right indicate number of used characters, need to reduce by 1 to be a index
    # also left index need to add 1 because it's the subarray after made the dif unchanged
    left_i = left-1+1
    right_i = right-1
    if right_i <= left_i: # Not exist!
        return (-1, -1)
    else:
        return ((left-1)+1, (right-1))  


# In[30]:

# Test
print l_and_n("a7")
print l_and_n("a")
print l_and_n("asb56dsah1278")

