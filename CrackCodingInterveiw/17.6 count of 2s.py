
# coding: utf-8

# In[65]:


# 17.6 count of 2s

# Main function recursion
def count_2s(num):
    digit = str(num)
    
    # Inner function to caculate the number of 2s 
    # under certain digits inclusive
    def recur_count2s(digit, memory):
        
        # If it's the last digit then
        # just check if the number is >= 2
        if len(digit) == 0:
            return 0
        elif len(digit) == 1:
            if int(digit) < 2:
                return 0
            else:
                return 1
        
        # First check if the digit is in the memory
        if digit in memory:
            return memory[digit]
        # Then use recursion to calculate and also stored in the memory
        else:
            count = 0
            
            # Assum the numer starts with k. Then for each starting digit from 0 to k-1 inclusive,
            # there's count of 2s equal to 0 to 999...9 (9 repeated by (len(digit)-1) times
            # With the addtional 2s comes from the starting 2
            for num in range(0, int(digit[0])):
                count += recur_count2s("9"*(len(digit)-1), memory)
                #print "Starting digit:{}, adding the 2 counts below {}".format(num, "9"*(len(digit)-1))
                    # if starting number is 2, then every number 
                    # between 2000...0 to 2999...9 will contribute an addtional 2
                if num == 2:
                    #print "(Starting digit-1) range includes 2: need to add addtional 10..0 counts" 
                    count += 10**(len(digit)-1)
            
            # Now deal with the addtional case, the starting digit is k,
            # We alread counted in all 2 counts in digits lower than 10**len(digit)
            # We just need to consider the rest 2 counts in digit-10**len(digit)
            # Unless, k == 2, in this case we need to also consider
            # the addtional 2s from all numbers beyond 2000...0 (0 repeated by len(digit)-1 times)
            count += recur_count2s(digit[1:], memory)
            if digit[0] == "2":
                #print "Last starting digit is 2: need to add addtional (2X...X-20...0 +1) counts"
                count += int(digit) - 2*10**(len(digit)-1) + 1
            
            # Done, calculate the count and return
            memory[digit] = count
            return count
    
    return recur_count2s(digit, {})


# In[66]:

# Test
print count_2s(25)

