"""

371. Sum of Two Integers
Difficulty: Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Completed:
    exponent method:                3/27/2022
    sum() and full adder method:    3/28/2022
    
"""

# exponent method
# note: breaks at numbers << 0

import numpy as np
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2(2**a * 2**b))

# sum() method

class Solution2:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])

# full adder method

import numpy as np

class Solution3:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        s = ""
        a = int(np.binary_repr(a,11),2)                             # two's complement
        b = int(np.binary_repr(b,11),2)
        
        while a or b:
            s = ''.join(('',s,str(int(a%2^b%2^carry))))             # increase sum
            carry = (a%2 & b%2) or (a%2 & carry) or (carry & b%2)   # calculate carry bit
            a = int(a/2)                                            # go to next bit
            b = int(b/2)
            
        s = ''.join(('',s,str(carry)))                              # final carry bit
        
        negative = False
        if len(s)>10:
            negative = (s[10]=="1")                                 # check if number is negative
        
        output = int(s[::-1],2) % 1024
        return output-1024 if negative else output
   
