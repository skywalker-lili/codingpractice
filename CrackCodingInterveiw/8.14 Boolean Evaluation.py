
# coding: utf-8

# In[20]:


# 8.14 Boolean Evaluation

def count_ways(s, result, memory):
    """
    Input a string of formulars, count the number of ways to add parens to let it equal to result
    """
    if len(s) == 0: return -1
    if len(s) == 1: 
        if bool(s) == result:
            return 1 # can only add a paren
        else:
            return 0
    
    if (s, result) in memory:
        return memory[(s, result)]
    
    # Recursion by splitting s into left and right on each operators
    # Depends on the operator
    ways = 0
    for i in range(1, len(s), 2):
        left = s[0:i]
        right = s[i+1:]
        operator = s[i]
        #print("{}: {} --> {}  '{}'  {}".format(result, s, left, operator, right))
        
        left_true = count_ways(left, True, memory)
        left_false = count_ways(left, False, memory)
        right_true = count_ways(right, True, memory)
        right_false = count_ways(right, False, memory)
        
        total_eval = (left_true+left_false)*(right_true+right_false) # all possible evalution situations
        
        # Depends on the operator, calculate the total amount of ways
        if operator == "&" and result == True:
            ways += (left_true * right_true)
        elif operator == "&" and result == False:
            ways += (total_eval - (left_true * right_true))
        
        elif operator == "|" and result == True:
            ways += (total_eval - (left_false*right_false))
        elif operator == "|" and result == False:
            ways += left_false * right_false
        
        elif operator == "^" and result == True:
            ways += left_true*right_false + left_false*right_true
        elif operator == "^" and result == False:
            ways += left_true*right_true + left_false*right_false
        
        else:
            raise Exception("Something weird in parsing the string, operator is {}, result is {}".format(operator, result))
    
    memory[(s, result)] = ways
    
    return ways


# In[30]:

# Test 
inputs = [("", False), ("1",True), ("1",False), ("1|1|1|1", True),("1^0|0|1",False) ,("0&0&0&1^1|0",True)]
memory = {}
for input in inputs:
    print("input is {}, result is {}".format(input, count_ways(input[0], input[1], memory)))


# In[ ]:



