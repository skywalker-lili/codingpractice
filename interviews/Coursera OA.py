
# coding: utf-8

# In[38]:

# Coursera Last substring

# Helper function to filter out invalid candidates
def filter_candidates(candidates, offset, string):
    # Find the ABSOLUTE index of character to be compared in string!!!
    absolute_indices = [candi_header_i + offset for candi_header_i in candidates]
    # Find the characters to be compared, if an index is longer than string, marked as None
    char_toCompare = []
    for index in absolute_indices:
        if index > len(string) - 1:
            char_toCompare.append(None)
        else:
            char_toCompare.append(string[index])
    
    # Go through the character to be compared and find the indices of largest ones
    remain_candidates = []
    max_char = ""
    for i, char in enumerate(char_toCompare):
        if char == None:
            continue
        else:
            if char > max_char: # find new largest char! Empty current and add the new king's index!
                remain_candidates = []
                remain_candidates.append(candidates[i])
                max_char = char
            elif char == max_char:
                remain_candidates.append(candidates[i])
    
    return remain_candidates

# Main function
def last_substring(string):
    # The last substring must end in the last character which means there can only be len(string) possible candidates
    # Therefore we can represent those candidates by their head character's index
    
    # The last substring must has the largest first letter among all initial candidates. Use this rule to 
    # Then it must have the largest second letter among left candidates that with the largest first letter
    # ...largest nth letter among left candidates with largest (n-1)th letter
    # .... Keep doing this until ...
    # Only one candidate left, which is the last substring
    
    # Ensure strings are lower case
    string = string.lower()
    
    # Initialize candidates
    candidates = [i for i in range(len(string))]
    
    # Keep filter out invalid candidates until there is only one
    relative_nth_char = 0
    while len(candidates) > 1:
        candidates = filter_candidates(candidates, relative_nth_char, string)
        relative_nth_char += 1 # increase the relative nth of char to be compared
    
    # Return results
    return string[candidates[0]:]



# In[39]:

# Test filter_candidates
s = "zbazba"
print "Testing last_substring(), input:" s
print last_substring(s)


# In[40]:

# sliding window
import sys
from collections import deque
def sliding_windows_min(array, k):
    # Notice that the rule that as long as a value comes in a window,
    # every value smaller than it won't be possible to the maximum value
    # Use this property, we can maintain a list stores values in descending order
    # so to get the largest value, just pick the first value
    # The problem is how to maintain this list. It needs to be updated every time the windows moves
    #     1. first, we need to deal with the 1st element in the list, to check if it's out of window
    #     2. 2nd, to maintain this order, we need to push the new value into correct place
    
    if k >= len(array):
        return None
    
    min_ofMax = sys.maxint # initial maximum value
    
    # A list of indices of possible largest values in descending order. 
    # Maintained during each slide
    dq = deque() 
    
    for i in xrange(len(array)):
        # If the largest is off-windows, remove it. 
        # Check len(dq) first to ensure this code doesn;t break at the start
        if len(dq) > 0 and dq[0] < i-k+1:
            dq.popleft()
        
        # Pushing the new incoming values into the right place in deque
        while len(dq) > 0 and array[dq[-1]] < array[i]:
            dq.pop()
        # Now it's safe to add the new element:
        dq.append(i)
        # if there is a complete window and the dq's maximum value is less than current maximum, reset it
        if i > k-1 and array[dq[0]] < min_ofMax:
            min_ofMax = array[dq[0]]
    
    return min_ofMax


# In[41]:

# Test sliding_windows_min
array = [4,7,1,5,8,0,11,3]
k = 3
print "Testing sliding_windows_min(), input:", array, k
print sliding_windows_min(array, k)


# In[ ]:

# Ashely Loves Numbers

# Main helper function: returns the number of non-repeating numbers in [0, n) 
def lovely_numbers(n):
    
    # First ensure that even the larest possible input 10e6 won't exceed sys.maxint
    # also that 10e6 doesn't largest lovely digit 9876543210 So we can just safely use this function
    
    
    
    # The idea is to calculate the non-repeating numbers


# In[ ]:




# In[ ]:




# In[ ]:




# In[7]:




# In[ ]:



