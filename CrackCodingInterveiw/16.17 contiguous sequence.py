
# coding: utf-8

# In[15]:


# 16.17 contiguous sequence

# ---- Solution ----
import sys
# Search from begining to end
def find_seq(sequence):
    # Use the knolwedge that in the final sequence, any sub sequence (longer than 1) must be larger than zero
    # Assume the sequence starts from the first positive number, end on the same number. It's now the seq has largest running sum 
    # if a seq is negative, just throw away, start seq from next number
    # if a seq has a running sum larger than previous largest running sum, set it as the seq with largest running sum
    
    class Seq():
        def __init__(self,start = 0,end = 0,sum = 0):
            self.start = start
            self.end = end
            self.sum = sum
        def copy(self,another_seq):
            self.start = another_seq.start
            self.end = another_seq.end
            self.sum = another_seq.sum
    
    # Find the first positive
    start = -1
    largest_num = -sys.maxint - 1
    for i, num in enumerate(sequence):
        if num > 0:
            start = i
            break
        if num > largest_num:
            largest_num = num
    if start == -1: # No positive number, therefore the larest seq is the largest number
        return [largest_num], largest_num
    
    # Initialize the known largest seq, which is the first positive number it self
    # Also initialize a pilot seq which will be used to explore larger sequences.
    seq = Seq(start,start,sequence[start])
    pilot = Seq(start,start,sequence[start])
    
    # Start to expand the seq by setting up a pilot seq
    while pilot.end < len(sequence) - 1: # pilot explores until the last number
        # if the pilot sum is negative and there is room to start a new seq, start a new pilot
        if pilot.sum < 0 and pilot.end + 1 <= len(sequence) - 1:
            new_pos = pilot.end + 1
            pilot = Seq(new_pos, new_pos, sequence[new_pos])
            continue # pilot is renewed, no need to do other works
        # if the pilot sum is larger than seq sum, update seq to pilot
        elif pilot.sum > seq.sum:
            seq.copy(pilot)
        # Expand the pilot end
        pilot.end += 1
        pilot.sum += sequence[pilot.end]
    
    return (sequence[seq.start:seq.end+1], seq.sum)


# In[16]:

# Test 
for seq in [[2],[-1,-2],[2,-8,3,-2,4,-10]]:
    print "seq is", seq
    print "largest subseq is", find_seq(seq)
    print "---"*10

