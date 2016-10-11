
# coding: utf-8

# In[63]:


# 16.16 sub sort

# ---- Solution ----
import sys
# Helper binary search function
# Modifed so that it can be used to find the leftmost element that's larger than a target
# or the right most element that's smaller than a target
def modified_bSearch(sequence,s,e,target,mode="leftmost&larger"):
    # Ensure that sequence[s:e] is sorted!!!
    while s < e:
        mid = (s+e)/2
        #print "checking on index:", mid, ". value:", sequence[mid]
        if mode == "leftmost&larger":
            if sequence[mid] <= target:
                s = mid + 1
            elif sequence[mid] > target:
                # check if the left element is smaller or equal to target
                if mid-1 >= s and sequence[mid-1] <= target:
                    return mid
                elif mid-1 < s: # mid is the leftmost element in search space and it's larger than target 
                    return mid
                else:
                    e = mid
        elif mode == "rightmost&smaller":
            if sequence[mid] >= target:
                e = mid
            elif sequence[mid] < target:
                # check if the right element is larger or equal to target
                if mid+1 < e and sequence[mid+1] >= target:
                    return mid
                elif mid+1 >= e: # mid is the rightmost element in search space and it's smaller than target
                    return mid
                else:
                    s = mid + 1
    
    return -1 # couldn't find return a special value
        
# Find the maximum and minimum value in a given subsequence
def max_min(sequence,s,e):
    max = -sys.maxint - 1
    min = sys.maxint
    for i in range(s, e):
        if sequence[i] >  max:
            max = sequence[i]
        if sequence[i] < min:
            min = sequence[i]
    
    return max, min
    
# Main function
def sub_sort(sequence):
    # Find the left most unsorted element and right most unsorted element
    # , call the subsequence btw them (include) s
    # Then find the smallest element in s, s_min and largest element in s, s_max
    # The only property of m and n is that elements in sequence[:m] must be less or equal to s_min
    # and elements in sequence[n+1:] must be larger or equal to s_max
    # Use this property to find the largest m and the smallest n
    
    def leftmost_unsorted(sequence):
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                return i
        return -1
    
    def rightmost_unsorted(sequence):
        for i in range(len(sequence)-1, 0, -1):
            if sequence[i] < sequence[i-1]:
                return i
        return -1
    
    
    # Find the left most and right most unsorted index
    left_unsorted = leftmost_unsorted(sequence)
    right_unsorted = rightmost_unsorted(sequence)
    
    if left_unsorted < right_unsorted:
        max, min = max_min(sequence, left_unsorted, right_unsorted+1)
        m = modified_bSearch(sequence, 0, left_unsorted, min, "leftmost&larger")
        n = modified_bSearch(sequence, right_unsorted+1, len(sequence), max, "rightmost&smaller")
        return (m, n)
    
    return (-1, -1) # special value indicating nothing need to be sorted


# In[64]:

# Test
for seq in [[1,2,4,7,10,11,7,12,6,7,16,18,19]]:
    print(sub_sort(seq))

