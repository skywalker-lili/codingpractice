
# coding: utf-8

# In[ ]:


# 16.20 T9

# Helper function to turn a number to characters in T9
def num_toChar(num):
    return T9[num]

# Helper function to turn a character to a number in T9
def char_toNum(char):
    return T9_reverse[char]


# In[47]:

# ---- Solution 1 ----
# Use a trie tree to reduce search space everytime
# Assume dictionary is already in the trie tree

def find_word1(trie_node, sequence):
    # Go through a string seqence one character by one 
    # Only keep go on the valid route in a trie tree
    # Use a base to hold on current word-base, such as "com" for "come"
    # so that recursive find a tree can be done
    path = [] # path along the trie tree, a list of characters
    res = set([]) # result 
    
    def valid_word(trie_node, sequence, depth, path, res):
        if current_index == len(sequence): # the sequence has already been parsed
            if trie_node.is_leaf(): # the trie node also terminates, meaning a word has ended
                res.add("".join(path))
        else: # the sequence hasn't been parsed fully
            num = sequence[depth]
            characters = num_toChar(num) # can be empty
            for char in characters:
                if trie_node.contains(char): # this character is in the trie tree
                    path.append(char)
                    valid_word(trie_node.get_child(char), sequence, depth+1, path, res)
            
    valid_word(trie_node, sequence, 0, path, res)
    
    return res


# In[45]:

# ---- Solution 2 ----
# Preprocess the dictionary to represent every word as a number
# Add those numbers in a hashmap and to check a number just do a key-value retrieval

def word_toHashmap(words):
    
    # Helper function to turn a word into a number
    def word_toNumber(word):
        number = []
        for char in word:
            number.append(char_toNum(char))
        
        return "".join(number)
    
    dictionary = defaultdict(set)
    for word in words:
        number = word_toNumber(word)
        dictionary[number].add(word)
    
    return dictionary

# Run the preprocessing
dictionary = word_toHashmap(words)

def find_word2(number, dictionary):
    return dictionary[number] # returns an empty set if not found

