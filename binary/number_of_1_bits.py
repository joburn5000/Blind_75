"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32.

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            if n % 2:     # check right most bit
                ones +=1  # increment count if not divisible by 2
            n = int(n/2)  # right shift
        return ones
       
"""
Explanation:

If the number is not evenly divisible by 2, it has a 1. At every stage, check if it's divisible. 
If so, add 1 to a total, then divide the number by 2 until the number reaches 0.

Time Complexity: O(log(N))
Space Complexity: O(1)
"""
