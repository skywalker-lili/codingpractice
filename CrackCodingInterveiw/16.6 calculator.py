
# encoding: utf-8

# In[1]:

# Helper function to parse a string to a list of ints and operators (string)
# in human reading order
def parse_string(string):    
    num_strings = {"0","1","2","3","4","5","6","7","8","9"}
    op_strings = {"+","-","*","/"}
    num_op = []
    num_buffer = ""
    for i, c in enumerate(string):
        # a specfial case when string starts with "-"
        # "-" in this case means the negative, not an operator
        if i == 0 and c == "-":
            num_buffer = "-"
            continue
        
        # When a number's character appears, add to num_buffer
        if c in num_strings:
            num_buffer = num_buffer + c
        # When it's an operator, save the current number and also the operator
        elif c in op_strings:
            num_op.append(int(num_buffer))
            num_buffer = ""
            num_op.append(c)
        
        # If this is the last character, save the number
        if i == len(string)-1:
            num_op.append(int(num_buffer))
    
    return num_op



# In[2]:

# ----------- Solution 1 ---------------------
# Use a temporary processing block to calculate */ operators

# Helper class to store the operator and number in one object
class Term():
    def __init__(self, num, op = "+"):
        self.op = op
        self.num = num
    def __str__(self):
        return self.op + str(self.num)

# Helper function to parse a list of number and operators to Term objects
def parse_numOp(num_op):
    terms = []
    for i, item in enumerate(num_op):
        if i == 0:
            term = Term(item)
            terms.append(term)
        elif isinstance(item, str):
            term = Term(op = item, num = num_op[i+1])
            terms.append(term)
    return terms 

# Helper function to save a block to current result
def save_block(res, block):
    if block.op == "+":
        return (res + block.num)
    elif block.op == "-":
        return (res - block.num)

# Helper function to modify a block based on a new term
def modify_block(block, term):
    if term.op == "*":
        block.num *= term.num
    elif term.op == "/":
        block.num /= term.num
    return block

def calculator_block(string):
    # Parse string to terms
    num_op = parse_string(string)
    terms = parse_numOp(num_op)
    
    # "+" and "-" separates the block of terms inside which that operators can be applied immediately
    # When see the "+" or "-" term, save the current block and start a new block
    # and when see the "*" or "/" term, apply the operator immediately to the current block, modify it
    # and when the term is the last one, make sure save the last block
    res = 0
    block = Term(num = 0) # assume a +0 term at the very beginning
    for i, term in enumerate(terms):
        if term.op in {"+", "-"}:
            res = save_block(res, block) # save current block
            block = term # start a new block
        elif term.op in {"*", "/"}:
            block = modify_block(block, term)
        
        if i == len(terms)-1:
            res = save_block(res, block)
    
    return res


# In[3]:

# ----------- Solution 2 ----------------

# Helper function given a number stack and a operator stack calculates the sum
def sum_stack(num_stack, op_stack):
    if len(op_stack) + 1 != len(num_stack):
        print("op stack has {} items while num stack has {}".format(len(op_stack), len(num_stack)))
        print("op stack: {}".format(op_stack))
        print("num_stack: {}".format(num_stack))
        return None
    
    base_num = num_stack.pop(0)
    while len(op_stack) > 0:
        op = op_stack.pop(0)
        if op == "+":
            base_num += num_stack.pop(0)
        else:
            base_num -= num_stack.pop(0)
    
    return base_num
            

# Use a temporary processing block to calculate * and / operators
def calculator2(string):
    # Store number and operators stacks
    # When encounters an "*" or "/" operator, pop a number and read the next number
    # apply the operator and stores the result.
    # When encoutners an "+" or "-" operator, store it
    # Finally, there will be only "+" and "-" operators left in the operator stack
    # and numbers in the number stack. Then just go through it in once
    num_op = parse_string(string)
    
    num_stack = []
    op_stack = []
    
    while len(num_op) > 0:
        item = num_op.pop(0)
        if item in {"*", "/"}:
            num1 = num_stack.pop() # first number is already in stack
            num2 = num_op.pop(0) # second number is yet to recover
            res = 0
            if item == "*":
                res += num1*num2
            else:
                res += num1/num2
            num_stack.append(res)
        elif isinstance(item, int):
            num_stack.append(item)
        else:
            op_stack.append(item)
    
    # Now just go through the two stacks sums all numbers according to operators
    return sum_stack(num_stack, op_stack)


# In[6]:

# Test
for s in ["2-3*4/2+1"]:
    print "formular is:", s
    print "calculator_block:", calculator_block(s)
    print "calculator2:", calculator2(s)
    print "---"*3

