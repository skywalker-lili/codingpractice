
# coding: utf-8

# In[43]:

# 5. Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Try all the position substrings from longest to shortest
        # Once find a parlindrome, return immediately since it's the longest
        for L in range(len(s), 0, -1): # the length of parlindrome is L
            # Iterate all possible substrings of length L by
            # trying substrings starting at position 0, 1, ..., (len(s)-L)
            last_start_i = len(s)-L
            for i in range(0, last_start_i+1):
                substring = s[i:i+L]
                if self.is_palindrome(substring):
                    return substring
        
        return ""
    
    def is_palindrome(self, string):
        start, end = 0, len(string)-1
        while start < end:
            if string[start] != string[end]:
                return False
            start +=1
            end -= 1
        
        return True


# In[44]:

# Test
solu = Solution()
test_s = ["", "a", "aba", "abaa"]
for s in test_s:
    print("'{}': {}".format(s, solu.longestPalindrome(s)))

