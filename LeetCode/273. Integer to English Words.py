
# coding: utf-8

# In[33]:

# 273. Integer to English Words
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num < 0:
            raise ValueError("Num shouldn't be a negative number: {}".format(num))
        
        # Special case if num is zero
        # Otherwise, the 
        if num == 0:
            return "Zero"
        
        path = []
        units = [
            (1000000000, "Billion"),
            (1000000, "Million"),
            (1000, "Thousand"),
        ]
        
        path = []
        remain = num
        for unit in units:
            count_unit = remain / unit[0]
            remain = remain - count_unit * unit[0]
            if count_unit != 0:
                path.extend(self.numberToWords_lessThousand(count_unit)) # add the count of current unit
                path.extend([unit[1]]) # add the current unit
        
        # The remain is less than 1000
        path.extend(self.numberToWords_lessThousand(remain))
        
        return " ".join(path)
   
    def numberToWords_lessThousand(self, num):
        """
        Return the string version of a number that's smaller than 1000
        """
        if num > 999 or num < 0:
            raise ValueError("Number should be between 0 and 999 while it's {}".formt(num))
        
        path = []
        hundreds = num / 100
        remain = num - hundreds * 100
        if hundreds !=0:
            path.extend(self.numberToWord_lessTen(hundreds))
            path.append("Hundred")
        
        path.extend(self.numberToWords_lessHundred(remain))
        
        return path
    
    def numberToWords_lessHundred(self, num):
        """
        Return the string version of a number that's smaller than 100
        """
        if num > 99 or num < 0:
            raise ValueError("Number should be between 0 and 99 while it's {}".format(num))
        
        path = []
        tens = num / 10
        
        if tens > 1: # num is in [20,99]
            path.extend(self.tensToWord(tens)) # dealing with digit on tens
            remain = num - tens*10
            path.extend(self.numberToWord_lessTen(remain)) # dealing with the left single-digit
        
        elif tens == 1: # num is in [10, 19]
            path.extend(self.teensToWord(num))
        
        else: # the number is in [0, 9]
            path.extend(self.numberToWord_lessTen(num))
        
        return path
    
    def tensToWord(self, num):
        """
        Return the string of tens
        """
        if num not in [i for i in range(10)]:
            raise ValueError("Number should be between 0 and 9 while it's {}".formt(num))
        
        path = []
        if num == 9:
            path.append("Ninety")
        elif num == 8:
            path.append("Eighty")
        elif num == 7:
            path.append("Seventy")
        elif num == 6:
            path.append("Sixty")
        elif num == 5:
            path.append("Fifty")
        elif num == 4:
            path.append("Forty")
        elif num == 3:
            path.append("Thirty")
        elif num == 2:
            path.append("Twenty")
        
        return path
        
    def teensToWord(self, num):
        """
        Return a string for numbers between 10 and 19
        """
        if num > 19 or num < 10:
            raise ValueError("Number should be between 10 and 19 while it's {}".format(num))
        
        path = []
        if num == 19:
            path.append("Nineteen")
        elif num == 18:
            path.append("Eighteen")
        elif num == 17:
            path.append("Seventeen")
        elif num == 16:
            path.append("Sixteen")
        elif num == 15:
            path.append("Fifteen")
        elif num == 14:
            path.append("Fourteen")
        elif num == 13:
            path.append("Thirteen")
        elif num == 12:
            path.append("Twelve")
        elif num == 11:
            path.append("Eleven")
        elif num == 10:
            path.append("Ten")
    
        return path
    
    def numberToWord_lessTen(self, num):
        """
        Return the string version of a number that's smaller than 10
        """
        if num > 9 or num < 0:
            raise ValueError("Number should be between 0 and 9 while it's {}".formt(num))
            
        path = []
        if num == 9:
            path.append("Nine")
        elif num == 8:
            path.append("Eight")
        elif num == 7:
            path.append("Seven")
        elif num == 6:
            path.append("Six")
        elif num == 5:
            path.append("Five")
        elif num == 4:
            path.append("Four")
        elif num == 3:
            path.append("Three")
        elif num == 2:
            path.append("Two")
        elif num == 1:
            path.append("One")
        elif num == 0: # Don't react to zero, otherwise every number will have a zero
            pass
        
        return path    


# In[34]:

# Test
test_nums = [    0, 1, 10, 14, 40, 99, 100, 1000, 1001,     12345, 123456, 1234567, 12345678, 123456789, 2**31-1]
s = Solution()
for num in test_nums:
    print("{}: {}".format(num, s.numberToWords(num)))

