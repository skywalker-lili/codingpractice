
# coding: utf-8

# In[1]:

# 56. Merge Intervals
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        
        # Sort the list by start time
        intervals.sort(key = lambda x: (x.start, x.end))
        
        # Maintain the latest max from previous, check if the new adding interval can merge into it
        res = []
        start_latest = intervals[0].start
        end_latest = intervals[0].end
        for interval in intervals[1:]:
            
            # If the new interval can merge into the latest-ending interval
            # see if it can prolong the ending
            if interval.start <= end_latest:
                end_latest = max(end_latest, interval.end)
            
            # If the new interval can't merge in the latest-ending interval
            # Time to end the latest interval and start a new one
            else:
                res.append(Interval(start_latest, end_latest))
                start_latest = interval.start
                end_latest = interval.end
        
        # Don't forget to add the last interval
        res.append(Interval(start_latest, end_latest))
        
        return res
        

