
# coding: utf-8

# In[46]:


# 16.21

# Helper function to do binary search
def b_search(l, target, start, end):
    # Binary search for target in l[start:end], 
    # remeber that l[start] is included but l[end] is not
    while start < end:
        mid = (start+end)/2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            start = mid + 1 # need to increase mid
        else:
            end = mid
    return -1 # Not found

# Main function
def sum_swap(A, B):
    # Using math,we know that if take swap a in A with b in B will allow sum(A) = sum(B)
    # b = (sum(B_orgin) - sum(A_origin))/2 - a
    # That is given A, B and an candidate for a, we know exactly value of b to search for
    # Therefore, we just sort B and do a binary search on it
    
    diff = (sum(B) - sum(A))*1.0
    B.sort()
    for a in A:
        b_index = b_search(B, diff/2 + a, 0, len(B))
        if b_index != -1:
            return {a, B[b_index]}
    return {}


# In[45]:

# Test
for (A, B) in [([4,1,2,1,1,2], [3,6,3,3])]:
    print(sum_swap(A, B))


# In[ ]:



