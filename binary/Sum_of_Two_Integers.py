"""

371. Sum of Two Integers
Difficulty: Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Completed: 3/27/2022
"""

# exponent method
# note: breaks at numbers << 0

import numpy as np
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2(2**a * 2**b))
