
# coding: utf-8

# In[39]:

# VMware OA: interleaving strings
def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    # Assume there is a grid of s1 * s2 , we can only go to right or go down
    # Sounds like a dp right? But there is an amazing solution use DFS/BFS to reduce space requirement
    # Assume we are standing on (x,y), now we visit it and what are the neighbours we can visit?
    # Of course we can visit (x+1, y) if s1[x+1] = s3[x+y+1], and visit (x, y+1) if s2[y+1] = s3[x+y+1]
    # When to terminate? When we visited all s3's length!
    # What's the difference from dp? DFS/BFS use the same update rule but ONLY saves the frontier of visited nodes, 
    # instead of the whole past visited nodes many of which are "in-land" and useless for helping us expansion
    
    l1, l2, l3 = len(s1), len(s2), len(s3)
    
    # Special case
    if l1+l2 != l3: return False
    
    # Stack/Queue to save the frontier of visiting
    stack = []
    stack.append((0, 0)) # initially node to visit, (0, 0) means none of s1 and s2 are visited
    visited = set([]) # keep the nodes we visited
    while len(stack) > 0:
        x,y = stack.pop() # the node we are visiting
        
        # Check if the nodes we are visiting is the target
        if x + y == l3:
            return True
        visited.add((x, y))
        
        # Check what are the nodes we can visit
        # Be careful of the boundary, the last place we can still look forward is (len() - 1)th char   
        # Also the CS indexing meaning that the (x+1)th char is s[x], so be careful of the discrepency
        if x <= l1-1 and s1[x] == s3[x+y]         and (x+1, y) not in visited:
            stack.append((x+1, y))
        if y <= l2-1 and s2[y] == s3[x+y]        and (x, y+1) not in visited:
            stack.append((x, y+1))
    
    return False


# In[43]:

# Test
s1 = "ab"
s2 = "a"
s3 = "aba"
print "Testing interleaving string"
isInterleave(s1, s2, s3)


# In[44]:

# Balanced array
def is_balanced(array):
    
    # Special case when array length is 0,2,4...
    if len(array) % 2 == 0:
        return -1
    
    # Now we know the array has at least 1 element, make it as the first candidate
    # Check the candidate and if not move towards the next until passed all elements
    i = 0
    left_sum = 0
    right_sum = sum(array[i+1:])
    
    while i < len(array)-1:
        if left_sum == right_sum:
            return i
        else:
            left_sum += array[i]
            if i+1 <= len(array) - 1: 
                right_sum -= array[i+1]
            i += 1
    
    return -1


# In[45]:

# Test 
print is_balanced([])
print is_balanced([1])
print is_balanced([1,-1,1])
print is_balanced([1,2,4,-5,8])


# In[103]:

# Remove duplicated node
class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


def removeNode_singleLinked(node):
    if node == None:
        return    
    
    # Go through the linked list, re-built it by only keeping the first seen values
    
    # Initialization
    seen = set([node.value]) # has seen the first node
    last_seen = node # last_seen is also the first seen
    to_check = last_seen.next # prepare the first to be checked nodes
    
    print "initial last seen is", last_seen.value
    # while to_check is a node
    while to_check != None:
        if to_check.value not in seen: # if to_check is new
            last_seen.next = to_check # attach it into the new linked list
            seen.add(to_check.value) # see it
            last_seen = to_check # update last seen
        # always update to check
        to_check = to_check.next
        
    last_seen.next = None # last_seen's next should be None
    
    return

def removeNode_doubleLinked(node):
    if node == None:
        return
    
    seen = set([])
    # while this is a node 
    while node != None:
        if node.value not in seen:
            seen.add(node.value)
            node = node.next
        else:
            node.previous.next = node.next
            node = node.next


# In[69]:

def get_linkedList(node):
    l = []
    while node != None:
        l.append(node.value)
        node = node.next
    return l

# Test
l = [1,1,2,3,3,4,4]


# In[104]:

# Create single-linked nodes
nodes = []
for i, value in enumerate(l):
    nodes.append(Node(value))
for i in range(0, len(l)-1):
    nodes[i].next = nodes[i+1]

print "Test single linked"
print "> original nodes:", get_linkedList(nodes[0])
removeNode_singleLinked(nodes[0])
print "> after removal:", get_linkedList(nodes[0])


# In[105]:

# Create double-linked nodes
nodes = []
for i, value in enumerate(l):
    nodes.append(Node(value))
for i in range(0, len(l)-1):
    nodes[i].next = nodes[i+1]
for i in range(1, len(l)):
    nodes[i].previous = nodes[i-1]

print "Test double linked"
print "> original nodes:", get_linkedList(nodes[0])
removeNode_doubleLinked(nodes[0])
print "> ofter removal:", get_linkedList(nodes[0])


# In[ ]:




# In[ ]:




# In[ ]:



