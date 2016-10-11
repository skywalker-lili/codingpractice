
# coding: utf-8

# In[175]:


# 8.8 Permutation with Dups

# ---- Solution ----

# Turn string into a hash table
def string_toHashtable(string):
    table = {}
    for s in string:
        if s not in table:
            table[s] = 1
        else:
            table[s] += 1
    
    return table

# Recursively produce unqiue permutations based on hashtable string
def recur_perm(hash_s, prefix, length, perms):
    # base case
    if length == 0: # no string left to permutate
        perms.add("".join(prefix)) # materialize a string in the end
    
    # recursive case
    else:
        for char in hash_s.keys():
            if hash_s[char] > 0:
                hash_s[char] -= 1 # indicating this character is used
                prefix.append(char) # use the charact add to exist string
                recur_perm(hash_s, prefix, length-1, perms)
                # After recursion, need to maintain the origin hashtable string 
                # for the next for-loop at the same depth
                hash_s[char] += 1 
                prefix.pop()

# Main function
def perm_wDups(string):
    # The idea is to avoid generating duplicate string permutations and then remove them
    # Use a hashtable of charact-count pair to represent each string 
    # and at each depth, in a for-loop of removing a character as prefix + recursive call on remaining hashtable
    
    hashtable_s = string_toHashtable(string)
    
    # Produce unique permutations based on hashtable string
    perms = set([])
    recur_perm(hashtable_s, [], len(string), perms)
    
    return perms


# In[176]:

# Test
perm_wDups("aab")

