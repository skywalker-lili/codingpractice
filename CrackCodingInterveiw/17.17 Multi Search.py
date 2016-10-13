
# coding: utf-8

# In[59]:


# 17.17 Multi Search

class TrieNode:
    def __init__(self, word_end=False):
        self.children = {}
        self.word_end = word_end
    
    def insert(self, word):
        if len(word) == 0:
            self.word_end = True
        elif len(word) > 0:
            head = word[0]
            if head not in self.children.keys():
                self.children[head] = TrieNode()
            
            self.children[head].insert(word[1:])
    
    def gather_words(self):
        words, path = [], []
        self._recur_gather_words(path, words)
        return words
    
    def _recur_gather_words(self, path, words):
        if self.word_end == True:
            words.append("".join(path))
        
        # Keep recursion because there could be other words
        for char in self.children.keys():
            child = self.children[char]
            child._recur_gather_words(list(path)+[char], words)

# Helper fucntion to build a trie tree on all small words
def build_trie(words):
    root = TrieNode()
    for w in words:
        root.insert(w)
    
    return root

# Helper function to find small words in a substring of big string
def find_small(i, big, trie, found):
    index = i
    while index <= len(big):
        # If already reach an end, add a word into 
        if trie.word_end == True:
            found.add(big[i:index])
       
        # Haven't reached an word end, keep digging
        if index < len(big): # the last char doesn't need to check for next one
            char = big[index]    
            if char in trie.children.keys():
                trie = trie.children[char] 
            else:
                break
            index += 1 # search for next character in big
        else: # already checked last char in the big string, done
            break

# Main function to find the small words in a big words
def multi_search(big, smalls):
    # Build a trie tree of small words
    root = build_trie(smalls)
    
    # Iterate over each start at big word, search to see if small words
    # exist in this substring
    found = set([]) # use a set to avoid adding same small words multiple times
    for i in range(len(big)):
        find_small(i, big, root, found)
    
    return found


# In[60]:

# Test
big, smalls ="mississippi", ["i", "is", "hi", "isp", "sis","issi","ssipp","ssippi"]

root = build_trie(smalls)
print("Trie contains {}".format(root.gather_words()))
print(multi_search(big, smalls))

