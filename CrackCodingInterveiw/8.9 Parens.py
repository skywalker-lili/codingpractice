
# coding: utf-8

# In[30]:


# 8.9 Parens

# Helper function for generate_parens_dup
def insert_paren(paren,i):
    """
    Insert a pair of paren "()" after at the given position i of original paren
    """
    left = paren[0:i+1]
    right = paren[i+1:]
    return left+"()"+right

# Brutal forcely produce parens, using a set to avoid duplications
def generate_parens_dup(i):
    """
    Generate parens by adding new paren "()" at each possible position based on the previous parens
    """
    if i == 0:
        return set([""])
    else:
        previous_parens = generate_parens_dup(i-1) # got previous parens
        
        new_parens = set([])
        for paren in previous_parens:
            for i in range(len(paren)):
                if paren[i] == "(":
                    new_paren = insert_paren(paren, i) # insert a paren
                    new_parens.add(new_paren)
            new_parens.add(("()"+paren)) # add a "()" at the begining of paren
        
        return new_parens


# Build parens based on given allowance of left and right bracket
# Since after using each left/right bracket, the existing part of a paren is different
# there is no way to produce duplicates
def add_paren(result, left_allowance, right_allowance, paren_placeholder, i):
    """
    Recursively generate parens givent the allowance of left and right
    """
    # If left brackets are negative or more right is used than left, impossible to keep valid in the current parens
    if (left_allowance < 0) or right_allowance < left_allowance: 
        return # impossible to form valid paren. No need to recurse under this situation, 
    else:
        if left_allowance == 0 and right_allowance == 0: # used up all brackets, output a paren 
            result.add("".join(paren_placeholder))
        else:
            # New decided bracket is left
            paren_placeholder[i] = "("
            add_paren(result, left_allowance-1, right_allowance, paren_placeholder, i+1)
            
            # New decided bracket is right 
            paren_placeholder[i] = ")"
            add_paren(result, left_allowance, right_allowance-1, paren_placeholder, i+1)
        
def generate_parens(i):
    """
    Given an i, the length of final parens is known. Then at each place, decide to put an
    left or a right parent. Based this steps's decision, keep move on in this branch until finish a parens.
    When all branches are done, return all parens
    """
    result = set([])
    paren_placeholder = [None]*(2*i)
    add_paren(result, i, i, paren_placeholder, 0)
    return result


# In[29]:

# Test 
for i in range(4):
    print(generate_parens_dup(i), generate_parens(i))

