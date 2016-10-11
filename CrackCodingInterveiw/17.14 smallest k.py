
# coding: utf-8

# In[23]:

# Use a heap to find smallest K int
def topK_minHeap(array, k):
    if len(array) <= k:
        return sorted(array)
    
    # Build a min-heap
    import heapq
    # Reverse the sign of numbers so the smallest number becomes the largest
    hp = [-array[i] for i in range(k)]
    heapq.heapify(hp)
    
    for i in range(k, len(array)):
        cur_min = hp[0]
        if cur_min < -array[i]:
            heapq.heappop(hp)
            heapq.heappush(hp, -array[i])
    
    hp = [-num for num in hp]
    hp.sort()
    
    return hp


# In[41]:

# Use selection sort to find the smallest k elements

# Helper fucntion to swap two items in array
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

# Helper function to divide an array by a pivot, 
# the left side is smaller or equal to the array
# Return the index of the pivot item at last
def partition(array, start, end):
    
    while start < end:
        if array[start+1] <= array[start]:
            swap(array, start+1, start) # 保证start左边是相遇等于array[start]的
            start += 1
        else:
            swap(array, start+1, end) # 保证end右边是大于等于array[start]
            end -= 1
    
    return start

# Main function that inplace-put the smallest k elements
# in array[start:end+1] in the left of array[start:end+1]
def selectionSort_kSmallest(array, k, start, end):
    
    if k <= 0:
        print "k must be positive! Just return!"
        return
    if end-start+1 < k:
        print "sub-array length({}) is smaller than k({})! Just return!".format(end-start+1, k)
        return # array长度小于k的话返回空
    
    # 默认使用array的第0个元素作为pivot
    pivot = partition(array, start, end) # partition the array
    
    # Now we have (pivot-start+1) items on the left, including pivot itself
    
    # if left size equals k, we have found the k smallest
    if pivot-start+1 == k: 
        return
    
    # if left size less than k, still need
    # to find k-((pivot-start)+1) smallest items from the rest array
    elif pivot-start < k-1:
        selectionSort_kSmallest(array, k-(pivot-start+1), pivot+1, end)
    
    # if left size is more than k, still need
    # to find the k smallest from the left
    else:
        selectionSort_kSmallest(array, k, start, pivot)       


# In[45]:

# Test
array = [1,6,3,5,4,2]
k = 3
print "original array is", array
print "k is", k
selectionSort_kSmallest(array, k, 0, len(array)-1)
print "array after sort is",array

