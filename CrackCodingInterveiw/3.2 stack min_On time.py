# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 18:00:52 2016

@author: Jingchen
"""
from __future__ import print_function, unicode_literals
import sys

# Use LinkedList to implement stack
class MyStack():
    
    # Node in a single linked list    
    class StackNode():
        def __init__(self, d, below = None):
            self.data = d
            self.next = below
    
    # MyStack uses "min" field to keep track of least value
    def __init__(self):
        self.min = None
        self.top = None
    
    # When push, need to examine min value  
    def push(self, d):
        new_top = MyStack.StackNode(d, below = self.top)
        self.top = new_top
        if self.min is None or d < self.min.data:
            self.min = new_top
    
    # When pop, need to examine min value
    def pop(self):
        if self.top == None:
            print("Empty stack, dude!")
        else:
            popped = self.top
            self.top = self.top.next
            # if top is the min, need to find a new min        
            if popped == self.min:
                self.min = self._findNewMin()
            return popped.data
        
    # A hidden function to find a new min
    # Use linear scan
    def _findNewMin(self):
        min_val = sys.maxint
        top = self.top
        min_node = None
        while top is not None:
            if top.data < min_val:
                min_node = top
            top = top.next
        
        return min_node
    
    def peek(self):
        if self.top == None:
            print("Empty stack, dude!")
        else:
            return self.top.data
    
    def get_min(self):
        if self.min == None:
            print("Empty stack, dude!")
        else:
            return self.min.data
    