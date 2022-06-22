"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 
represents the unsigned integer 43261596, so return 964176192 which its 
binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 
represents the unsigned integer 4294967293, so return 3221225471 which its 
binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32

Difficulty: Easy
Completed: 6/22/2022
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        
        b = bin(n)                      # convert to a binary number. note: leading 0s are discarded
        b = b[2:]                       # get rid of the "0b" at the beginning
        b = b[::-1]                     # reverse bits
        b += '0' * (32-len(b))          # fill in discarded bits
        return int(b,2)
        
        """
        # concise version:
        
        return int(bin(n)[:1:-1]+'0'*(34-len(bin(n))),2)
        
        """
        

"""
Explanation:

We convert the input to a binary number, format, 
reverse the bits, add leading zeros to the end, 
and convert back to decimal

Time Complexity: O(1)
Space Complexity: O(1)
"""
