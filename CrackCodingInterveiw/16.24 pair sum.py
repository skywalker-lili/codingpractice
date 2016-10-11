
# coding: utf-8

# In[1]:


# 16.24 pair with sums


# In[10]:

# ---- Solution 1 ----
# hasp map based
from collections import defaultdict
def pair_sum1(l, target):
    # Use a hashmap to store the seen value and its count
    # For a new value comes in, check if it's complement is in the seen value
    #     if true, print the pair of values and decrease the count of seen by 1
    #     if false, stores the new value as seen value
    # O(n) time and O(n) space
    
    seen = defaultdict(int)
    for i in l:
        complement = target - i
        if seen[complement] > 0:
            print(i, complement)
            seen[complement] -= 1
        else:
            seen[i] += 1


# In[18]:

# ----- Solution 2 -----
# sort and two pointers
def pair_sum2(l, target):
    # Sort the list and then use two pointers, one at start and one at end
    # The sum of tow points can be <, = , > than the target,
    #     if ==, print two numbers and move both pointers towards to middle
    #     if <, smaller pointer move towards middle (increase sum)
    #     if >, larger pointter move towards middle (decrease sum)
    l.sort()
    small = 0
    large = len(l) - 1
    while small < large:
        two_sum = l[small] + l[large]
        if two_sum == target:
            print(l[small], l[large])
            small += 1
            large -= 1
        elif two_sum < target:
            small += 1
        else:
            large -= 1
    


# In[21]:

# Test
for l_target in [([2,3,4,5,6,6,4], 8)]:
    print "Input is:", l_target[0], l_target[1]
    print "  pair_sum1 result:"
    pair_sum1(l_target[0], l_target[1])
    print "  piar_sum2 result"
    pair_sum2(l_target[0], l_target[1])
    print("---"*10)

