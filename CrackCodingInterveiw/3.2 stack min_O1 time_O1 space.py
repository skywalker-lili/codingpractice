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
    
    # MyStack has an internal min_stack to record the min value
    def __init__(self):
        self.min = None
        self.top = None
        # min_stack records the min_values by time order
        # the trick is it only pushes a new min when
        # the new pushed value is equal or smaller than the current min
        # so that it can only keep the pseudo-unique min values 
        # (pseudo because the same values will be repeated) 
        self.min_stack = [None]
    
    # When push, examine whethermin value  
    def push(self, d):
        new_top = MyStack.StackNode(d, below = self.top)
        self.top = new_top
        if self.min_stack[-1] is None or d <= self.min_stack[-1]:
            self.min_stack.append(d)
    
    # When pop, need to examine min value
    def pop(self):
        if self.top == None:
            print("Empty stack, dude!")
        else:
            popped = self.top
            self.top = self.top.next
            # if top is the min value, removes the last element        
            if popped.data == self.min_stack[-1]:
                self.min_stack.pop()
            return popped.data
    
    def peek(self):
        if self.top == None:
            print("Empty stack, dude!")
        else:
            return self.top.data
    
    def get_min(self):
        if self.min_stack[-1] == None:
            print("Empty stack, dude!")
        else:
            return self.min_stack[-1]
    