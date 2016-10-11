
# coding: utf-8

# In[92]:


# 16.5 Factorial Zeros

# ---- Solution ----
def factorial_zeros(n):
    
    # Helper function use recursion and memorization to find 2s and 5s in a given number
    def count_twosAndFives(n, memory):
        if n in memory:
            return memory[n]
        else:
            twos, fives = 0, 0
            if n % 2 == 0:
                twos += 1
                twos += count_twosAndFives(n/2, memory)[0]
            if n % 5 == 0:
                fives += 1
                fives += count_twosAndFives(n/5, memory)[1]
            
            # Done recursion, save twos and fives in memeory
            memory[n] = (twos, fives)
            return (twos, fives)
    
    memory = {}
    accum_twos_fives = [0, 0]
    for i in range(n, 1, -1):
        # Find number of 2s and 5s in a given number
        # Save result in a memory for future use
        twos_fives = count_twosAndFives(i, memory)
        # Accumulate counts of 2s and 5s 
        accum_twos_fives[0] += twos_fives[0]
        accum_twos_fives[1] += twos_fives[1]
    
    return min(accum_twos_fives) # the lesser count determines the count of zeros


# In[98]:

# Test
for n in [1,2,5,10,14,15,100]:
    print "N =", n, ":", factorial_zeros(n), "trailling zeros"
    print "---"*10

